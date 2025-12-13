#!/usr/bin/env python3
"""
EPUB Quality Verification Script
Verifies that bold text conversion and other quality standards are met
"""

import zipfile
import re
import os
from pathlib import Path

def verify_epub_bold_conversion(epub_path):
    """Verify that bold text conversion is working correctly in EPUB"""
    
    print(f"\n🔍 Verifying EPUB: {epub_path}")
    print("=" * 60)
    
    if not os.path.exists(epub_path):
        print(f"❌ EPUB file not found: {epub_path}")
        return False
    
    try:
        with zipfile.ZipFile(epub_path, 'r') as epub:
            # Get all XHTML content files
            content_files = [f for f in epub.namelist() if f.endswith('.xhtml') and 'content/' in f]
            
            total_files = len(content_files)
            files_with_bold = 0
            total_strong_tags = 0
            files_with_remaining_markdown = 0
            
            print(f"📄 Found {total_files} content files to check")
            
            for content_file in content_files:
                try:
                    content = epub.read(content_file).decode('utf-8')
                    
                    # Check for remaining ** markdown syntax
                    remaining_bold_markdown = re.findall(r'\*\*.*?\*\*', content)
                    
                    # Check for <strong> tags
                    strong_tags = re.findall(r'<strong>.*?</strong>', content)
                    
                    if remaining_bold_markdown:
                        files_with_remaining_markdown += 1
                        print(f"❌ {content_file}: Found {len(remaining_bold_markdown)} remaining ** syntax")
                        for example in remaining_bold_markdown[:3]:
                            print(f"   Example: {example}")
                    
                    if strong_tags:
                        files_with_bold += 1
                        total_strong_tags += len(strong_tags)
                        print(f"✅ {content_file}: {len(strong_tags)} <strong> tags")
                    
                except Exception as e:
                    print(f"❌ Error reading {content_file}: {e}")
            
            # Check CSS for strong styling
            css_files = [f for f in epub.namelist() if f.endswith('.css')]
            css_has_strong_styling = False
            
            for css_file in css_files:
                try:
                    css_content = epub.read(css_file).decode('utf-8')
                    if 'strong' in css_content and 'font-weight' in css_content:
                        css_has_strong_styling = True
                        print(f"✅ CSS file {css_file} includes strong element styling")
                        break
                except Exception as e:
                    print(f"❌ Error reading CSS {css_file}: {e}")
            
            # Summary
            print("\n📊 VERIFICATION SUMMARY")
            print("-" * 40)
            print(f"Total content files: {total_files}")
            print(f"Files with <strong> tags: {files_with_bold}")
            print(f"Total <strong> tags found: {total_strong_tags}")
            print(f"Files with remaining ** syntax: {files_with_remaining_markdown}")
            print(f"CSS includes strong styling: {'✅ Yes' if css_has_strong_styling else '❌ No'}")
            
            # Overall assessment
            success = (files_with_remaining_markdown == 0 and css_has_strong_styling)
            
            if success:
                print("\n🎉 EPUB QUALITY VERIFICATION: PASSED")
                print("✅ All bold text properly converted to <strong> tags")
                print("✅ No remaining ** markdown syntax found")
                print("✅ CSS includes proper strong element styling")
            else:
                print("\n❌ EPUB QUALITY VERIFICATION: FAILED")
                if files_with_remaining_markdown > 0:
                    print(f"❌ {files_with_remaining_markdown} files still contain ** markdown syntax")
                if not css_has_strong_styling:
                    print("❌ CSS does not include strong element styling")
            
            return success
            
    except Exception as e:
        print(f"❌ Error opening EPUB file: {e}")
        return False

def verify_epub_structure(epub_path):
    """Verify basic EPUB structure requirements"""
    
    print(f"\n📁 Verifying EPUB structure: {epub_path}")
    print("=" * 60)
    
    required_files = [
        'mimetype',
        'META-INF/container.xml',
        'OEBPS/content.opf'
    ]
    
    try:
        with zipfile.ZipFile(epub_path, 'r') as epub:
            file_list = epub.namelist()
            
            missing_files = []
            for required_file in required_files:
                if required_file not in file_list:
                    missing_files.append(required_file)
                else:
                    print(f"✅ {required_file}")
            
            # Check for navigation file
            nav_files = [f for f in file_list if 'nav.xhtml' in f]
            if nav_files:
                print(f"✅ Navigation file: {nav_files[0]}")
            else:
                missing_files.append("Navigation file (nav.xhtml)")
            
            # Check for CSS files
            css_files = [f for f in file_list if f.endswith('.css')]
            if css_files:
                print(f"✅ CSS files: {len(css_files)} found")
            else:
                missing_files.append("CSS files")
            
            if missing_files:
                print(f"\n❌ Missing required files:")
                for missing in missing_files:
                    print(f"   - {missing}")
                return False
            else:
                print(f"\n✅ EPUB structure verification: PASSED")
                return True
                
    except Exception as e:
        print(f"❌ Error verifying EPUB structure: {e}")
        return False

def main():
    """Main verification process"""
    
    print("🧪 EPUB Quality Verification Tool")
    print("=" * 60)
    print("Checking generated EPUB files for:")
    print("- Bold text conversion (** → <strong>)")
    print("- CSS styling for bold text")
    print("- Basic EPUB structure compliance")
    
    # List of EPUB files to verify
    epub_files = [
        "ai-entrepreneur-guide-vietnamese.epub"
    ]
    
    results = {}
    
    for epub_file in epub_files:
        if os.path.exists(epub_file):
            bold_conversion_ok = verify_epub_bold_conversion(epub_file)
            structure_ok = verify_epub_structure(epub_file)
            results[epub_file] = bold_conversion_ok and structure_ok
        else:
            print(f"\n⚠️ EPUB file not found: {epub_file}")
            results[epub_file] = False
    
    # Final summary
    print("\n" + "=" * 60)
    print("🏁 FINAL VERIFICATION RESULTS")
    print("=" * 60)
    
    all_passed = True
    for epub_file, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{epub_file}: {status}")
        if not passed:
            all_passed = False
    
    if all_passed:
        print("\n🎉 ALL EPUB FILES PASSED QUALITY VERIFICATION!")
        print("✅ Bold text conversion working correctly")
        print("✅ EPUB structure compliant")
        print("✅ Ready for distribution")
    else:
        print("\n❌ SOME EPUB FILES FAILED VERIFICATION")
        print("Please review the issues above and regenerate EPUBs if needed")
    
    return all_passed

if __name__ == "__main__":
    main()
