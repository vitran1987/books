#!/usr/bin/env python3
"""
Comprehensive EPUB Validator
Checks for common issues that cause Google Play Books rejection
"""

import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
import re

def validate_epub(epub_path):
    errors = []
    warnings = []
    
    print(f"Validating {epub_path}...")
    print("=" * 70)
    
    # Check 1: File exists
    if not Path(epub_path).exists():
        errors.append(f"❌ File not found: {epub_path}")
        return errors, warnings
    
    with zipfile.ZipFile(epub_path, 'r') as z:
        names = z.namelist()
        
        # Check 2: Mimetype
        print("\n📋 Checking mimetype...")
        if 'mimetype' not in names:
            errors.append("❌ Missing mimetype file")
        else:
            if names[0] != 'mimetype':
                errors.append(f"❌ Mimetype not first file (found: {names[0]})")
            
            mimetype_info = z.getinfo('mimetype')
            if mimetype_info.compress_type != 0:
                errors.append(f"❌ Mimetype is compressed (type={mimetype_info.compress_type})")
            
            mimetype_content = z.read('mimetype')
            if mimetype_content != b'application/epub+zip':
                errors.append(f"❌ Invalid mimetype content: {mimetype_content}")
            else:
                print("  ✅ Mimetype correct")
        
        # Check 3: Container.xml
        print("\n📋 Checking container.xml...")
        if 'META-INF/container.xml' not in names:
            errors.append("❌ Missing META-INF/container.xml")
        else:
            try:
                container_xml = z.read('META-INF/container.xml')
                ET.fromstring(container_xml)
                print("  ✅ container.xml valid")
            except ET.ParseError as e:
                errors.append(f"❌ container.xml parse error: {e}")
        
        # Check 4: Content.opf
        print("\n📋 Checking content.opf...")
        opf_files = [n for n in names if n.endswith('content.opf')]
        if not opf_files:
            errors.append("❌ Missing content.opf")
        else:
            try:
                opf_content = z.read(opf_files[0])
                opf_root = ET.fromstring(opf_content)
                
                # Check metadata
                ns = {'opf': 'http://www.idpf.org/2007/opf', 'dc': 'http://purl.org/dc/elements/1.1/'}
                
                title = opf_root.find('.//dc:title', ns)
                if title is None:
                    errors.append("❌ Missing dc:title")
                else:
                    print(f"  ✅ Title: {title.text}")
                
                lang = opf_root.find('.//dc:language', ns)
                if lang is None:
                    errors.append("❌ Missing dc:language")
                else:
                    print(f"  ✅ Language: {lang.text}")
                
                identifier = opf_root.find('.//dc:identifier', ns)
                if identifier is None:
                    errors.append("❌ Missing dc:identifier")
                else:
                    print(f"  ✅ Identifier: {identifier.text}")
                
                # Check for nav
                manifest = opf_root.find('.//opf:manifest', ns)
                nav_item = None
                for item in manifest.findall('.//opf:item', ns):
                    props = item.get('properties', '')
                    if 'nav' in props:
                        nav_item = item
                        break
                
                if nav_item is None:
                    errors.append("❌ No navigation document with properties='nav'")
                else:
                    print(f"  ✅ Nav document: {nav_item.get('href')}")
                
                # Check for cover-image
                cover_item = None
                for item in manifest.findall('.//opf:item', ns):
                    props = item.get('properties', '')
                    if 'cover-image' in props:
                        cover_item = item
                        break
                
                if cover_item is None:
                    warnings.append("⚠️  No cover-image in manifest")
                else:
                    print(f"  ✅ Cover image: {cover_item.get('href')}")
                
            except ET.ParseError as e:
                errors.append(f"❌ content.opf parse error: {e}")
        
        # Check 5: XHTML files
        print("\n📋 Checking XHTML files...")
        xhtml_files = [n for n in names if n.endswith('.xhtml')]
        xhtml_errors = 0
        for xhtml_file in xhtml_files[:10]:  # Check first 10
            try:
                content = z.read(xhtml_file)
                ET.fromstring(content)
            except ET.ParseError as e:
                errors.append(f"❌ {xhtml_file}: {e}")
                xhtml_errors += 1
        
        if xhtml_errors == 0:
            print(f"  ✅ All checked XHTML files valid ({len(xhtml_files)} total)")
        else:
            print(f"  ❌ {xhtml_errors} XHTML files have errors")
        
        # Check 6: Look for common encoding issues
        print("\n📋 Checking for encoding issues...")
        for xhtml_file in xhtml_files[:5]:
            content = z.read(xhtml_file).decode('utf-8')
            # Check for unescaped & (not followed by valid entity)
            unescaped_amp = re.findall(r'&(?![a-zA-Z]+;|#\d+;|#x[0-9a-fA-F]+;)', content)
            if unescaped_amp:
                errors.append(f"❌ {xhtml_file}: Found unescaped ampersands: {unescaped_amp[:3]}")
            
            # Check for < and > outside tags
            outside_tags = re.findall(r'>[^<]*<(?!/|[a-zA-Z])', content)
            if outside_tags:
                warnings.append(f"⚠️  {xhtml_file}: Potential unescaped < or >")
        
        print(f"  ✅ Encoding checks complete")
    
    print("\n" + "=" * 70)
    print(f"\n📊 VALIDATION SUMMARY")
    print(f"Total Errors: {len(errors)}")
    print(f"Total Warnings: {len(warnings)}")
    
    if errors:
        print("\n❌ ERRORS:")
        for error in errors:
            print(f"  {error}")
    
    if warnings:
        print("\n⚠️  WARNINGS:")
        for warning in warnings:
            print(f"  {warning}")
    
    if not errors and not warnings:
        print("\n✅ EPUB passed all checks!")
    
    return errors, warnings

if __name__ == "__main__":
    import sys
    epub_file = sys.argv[1] if len(sys.argv) > 1 else "marketing-edtech-guide.epub"
    validate_epub(epub_file)
