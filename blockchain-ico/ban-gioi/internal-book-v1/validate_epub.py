# Detailed EPUB Analysis and Fix Script
# This will check for common Google Play Books rejection reasons

import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
import re

def analyze_epub(epub_path):
    """Comprehensive EPUB analysis"""
    issues = []
    warnings = []
    
    print("=" * 70)
    print(f"ANALYZING: {epub_path}")
    print("=" * 70)
    
    with zipfile.ZipFile(epub_path, 'r') as zf:
        # 1. Check mimetype
        print("\n[1] MIMETYPE CHECK")
        try:
            first_file = zf.namelist()[0]
            if first_file != 'mimetype':
                issues.append(f"❌ First file must be 'mimetype', found '{first_file}'")
            else:
                print("✅ Mimetype is first file")
            
            mime_info = zf.getinfo('mimetype')
            if mime_info.compress_type != 0:
                issues.append(f"❌ Mimetype must be uncompressed (ZIP_STORED), found type {mime_info.compress_type}")
            else:
                print("✅ Mimetype is uncompressed")
            
            mime_content = zf.read('mimetype').decode('utf-8')
            if mime_content != 'application/epub+zip':
                issues.append(f"❌ Mimetype content incorrect: '{mime_content}'")
            else:
                print("✅ Mimetype content correct")
        except Exception as e:
            issues.append(f"❌ Mimetype error: {e}")
        
        # 2. Check container.xml
        print("\n[2] CONTAINER.XML CHECK")
        try:
            container = zf.read('META-INF/container.xml').decode('utf-8')
            if 'OEBPS/content.opf' not in container:
                issues.append("❌ Container.xml doesn't reference OEBPS/content.opf")
            else:
                print("✅ Container.xml references content.opf correctly")
        except Exception as e:
            issues.append(f"❌ Container.xml error: {e}")
        
        # 3. Parse and validate content.opf
        print("\n[3] CONTENT.OPF CHECK")
        try:
            opf_content = zf.read('OEBPS/content.opf').decode('utf-8')
            
            # Register namespaces
            ET.register_namespace('', 'http://www.idpf.org/2007/opf')
            ET.register_namespace('dc', 'http://purl.org/dc/elements/1.1/')
            
            root = ET.fromstring(opf_content)
            
            # Check version
            version = root.get('version')
            print(f"📖 EPUB version: {version}")
            
            # Check unique-identifier
            unique_id = root.get('unique-identifier')
            if not unique_id:
                issues.append("❌ Missing unique-identifier attribute in package")
            else:
                print(f"✅ Unique identifier: {unique_id}")
            
            # Check metadata
            ns = {'opf': 'http://www.idpf.org/2007/opf',
                  'dc': 'http://purl.org/dc/elements/1.1/'}
            
            metadata = root.find('opf:metadata', ns)
            if metadata is None:
                metadata = root.find('metadata')
            
            if metadata is not None:
                # Required metadata
                title = metadata.find('dc:title', ns)
                if title is None:
                    issues.append("❌ Missing dc:title")
                else:
                    print(f"✅ Title: {title.text}")
                
                lang = metadata.find('dc:language', ns)
                if lang is None:
                    issues.append("❌ Missing dc:language")
                else:
                    print(f"✅ Language: {lang.text}")
                
                identifier = metadata.find('dc:identifier', ns)
                if identifier is None:
                    issues.append("❌ Missing dc:identifier")
                else:
                    print(f"✅ Identifier: {identifier.text}")
                
                # Check for modified date (required for EPUB 3)
                modified = metadata.find("*[@property='dcterms:modified']")
                if modified is None and version == '3.0':
                    warnings.append("⚠️  Missing dcterms:modified (recommended for EPUB 3)")
                else:
                    print(f"✅ Modified date: {modified.text if modified is not None else 'N/A'}")
            
            # Check manifest
            manifest = root.find('opf:manifest', ns)
            if manifest is None:
                manifest = root.find('manifest')
            
            if manifest is not None:
                items = manifest.findall('opf:item', ns)
                if not items:
                    items = manifest.findall('item')
                
                print(f"✅ Manifest has {len(items)} items")
                
                # Check for nav document (required for EPUB 3)
                nav_item = None
                for item in items:
                    props = item.get('properties', '')
                    if 'nav' in props:
                        nav_item = item
                        break
                
                if nav_item is None and version == '3.0':
                    issues.append("❌ Missing navigation document (properties='nav') in manifest")
                else:
                    print(f"✅ Navigation document: {nav_item.get('href') if nav_item else 'N/A'}")
                
                # Verify all manifest items exist in ZIP
                print("\n[4] FILE EXISTENCE CHECK")
                missing_files = []
                for item in items:
                    href = item.get('href')
                    if href:
                        full_path = f"OEBPS/{href}"
                        if full_path not in zf.namelist():
                            missing_files.append(full_path)
                
                if missing_files:
                    issues.append(f"❌ Files in manifest but not in ZIP: {missing_files}")
                else:
                    print("✅ All manifest items exist in ZIP")
            
            # Check spine
            spine = root.find('opf:spine', ns)
            if spine is None:
                spine = root.find('spine')
            
            if spine is not None:
                itemrefs = spine.findall('opf:itemref', ns)
                if not itemrefs:
                    itemrefs = spine.findall('itemref')
                
                print(f"✅ Spine has {len(itemrefs)} items")
                
                if len(itemrefs) == 0:
                    issues.append("❌ Spine is empty")
            else:
                issues.append("❌ Missing spine element")
            
        except ET.ParseError as e:
            issues.append(f"❌ content.opf XML parse error: {e}")
        except Exception as e:
            issues.append(f"❌ content.opf error: {e}")
        
        # 4. Check navigation document
        print("\n[5] NAVIGATION DOCUMENT CHECK")
        nav_files = [f for f in zf.namelist() if 'nav.xhtml' in f]
        if nav_files:
            try:
                nav_content = zf.read(nav_files[0]).decode('utf-8')
                
                # Check for nav element with epub:type="toc"
                if 'epub:type="toc"' not in nav_content:
                    warnings.append("⚠️  Navigation document missing epub:type='toc'")
                else:
                    print("✅ Navigation has epub:type='toc'")
                
                # Check for proper XHTML structure
                if '<!DOCTYPE html>' not in nav_content:
                    warnings.append("⚠️  Navigation missing DOCTYPE declaration")
                else:
                    print("✅ Navigation has DOCTYPE")
                
                # Validate as XML
                try:
                    ET.fromstring(nav_content)
                    print("✅ Navigation is valid XML")
                except:
                    issues.append("❌ Navigation is not valid XML")
            except Exception as e:
                issues.append(f"❌ Navigation error: {e}")
        else:
            issues.append("❌ No navigation document found")
        
        # 5. Check content files
        print("\n[6] CONTENT FILES CHECK")
        xhtml_files = [f for f in zf.namelist() if f.endswith('.xhtml') or f.endswith('.html')]
        print(f"Found {len(xhtml_files)} XHTML/HTML files")
        
        invalid_files = []
        for xhtml_file in xhtml_files:
            try:
                content = zf.read(xhtml_file).decode('utf-8')
                ET.fromstring(content)
            except Exception as e:
                invalid_files.append((xhtml_file, str(e)))
        
        if invalid_files:
            issues.append(f"❌ Invalid XHTML files: {[f[0] for f in invalid_files]}")
            for file, error in invalid_files:
                print(f"  ❌ {file}: {error[:100]}")
        else:
            print("✅ All XHTML files are valid XML")
    
    # Summary
    print("\n" + "=" * 70)
    print("ANALYSIS SUMMARY")
    print("=" * 70)
    
    if issues:
        print(f"\n❌ CRITICAL ISSUES ({len(issues)}):")
        for issue in issues:
            print(f"  {issue}")
    else:
        print("\n✅ NO CRITICAL ISSUES FOUND")
    
    if warnings:
        print(f"\n⚠️  WARNINGS ({len(warnings)}):")
        for warning in warnings:
            print(f"  {warning}")
    
    if not issues and not warnings:
        print("\n🎉 EPUB APPEARS TO BE VALID!")
    
    return len(issues) == 0

if __name__ == "__main__":
    epub_file = Path("bg-internal-book.epub")
    if epub_file.exists():
        is_valid = analyze_epub(str(epub_file))
        print(f"\nFinal result: {'✅ VALID' if is_valid else '❌ HAS ISSUES'}")
    else:
        print(f"Error: {epub_file} not found")
