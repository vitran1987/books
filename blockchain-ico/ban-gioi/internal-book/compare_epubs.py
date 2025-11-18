#!/usr/bin/env python3
"""Compare two EPUB files to find differences"""

import zipfile
import os
from pathlib import Path

def compare_epub_structure(epub1_path, epub2_path):
    """Compare the structure and content of two EPUB files"""
    
    print(f"Comparing EPUBs:")
    print(f"  Working: {epub1_path}")
    print(f"  Testing: {epub2_path}")
    print("=" * 70)
    
    with zipfile.ZipFile(epub1_path, 'r') as z1, zipfile.ZipFile(epub2_path, 'r') as z2:
        files1 = set(z1.namelist())
        files2 = set(z2.namelist())
        
        print(f"\nFile count:")
        print(f"  Working EPUB: {len(files1)} files")
        print(f"  Testing EPUB: {len(files2)} files")
        
        only_in_1 = files1 - files2
        only_in_2 = files2 - files1
        common = files1 & files2
        
        if only_in_1:
            print(f"\n❌ Files ONLY in working EPUB:")
            for f in sorted(only_in_1):
                print(f"    - {f}")
        
        if only_in_2:
            print(f"\n⚠️  Files ONLY in testing EPUB:")
            for f in sorted(only_in_2):
                print(f"    - {f}")
        
        print(f"\n✅ Common files: {len(common)}")
        
        # Check mimetype specifics
        print("\nMimetype details:")
        mime1_info = z1.getinfo('mimetype')
        mime2_info = z2.getinfo('mimetype')
        print(f"  Working - Compress type: {mime1_info.compress_type}, Size: {mime1_info.file_size}")
        print(f"  Testing - Compress type: {mime2_info.compress_type}, Size: {mime2_info.file_size}")
        
        # Compare file order
        print("\nFile order (first 10):")
        print("  Working EPUB:")
        for i, name in enumerate(z1.namelist()[:10]):
            print(f"    {i+1}. {name}")
        print("  Testing EPUB:")
        for i, name in enumerate(z2.namelist()[:10]):
            print(f"    {i+1}. {name}")
        
        # Compare content.opf
        if 'OEBPS/content.opf' in common:
            print("\nComparing content.opf:")
            opf1 = z1.read('OEBPS/content.opf').decode('utf-8')
            opf2 = z2.read('OEBPS/content.opf').decode('utf-8')
            if opf1 == opf2:
                print("  ✅ content.opf files are identical")
            else:
                print("  ❌ content.opf files differ")
                print(f"     Working length: {len(opf1)}")
                print(f"     Testing length: {len(opf2)}")
        
        # Compare nav.xhtml
        nav_paths = ['OEBPS/content/nav.xhtml', 'OEBPS/nav.xhtml']
        for nav_path in nav_paths:
            if nav_path in common:
                print(f"\nComparing {nav_path}:")
                nav1 = z1.read(nav_path).decode('utf-8')
                nav2 = z2.read(nav_path).decode('utf-8')
                if nav1 == nav2:
                    print(f"  ✅ {nav_path} files are identical")
                else:
                    print(f"  ❌ {nav_path} files differ")
                    # Show first difference
                    lines1 = nav1.split('\n')
                    lines2 = nav2.split('\n')
                    for i, (line1, line2) in enumerate(zip(lines1, lines2)):
                        if line1 != line2:
                            print(f"     First diff at line {i+1}:")
                            print(f"       Working: {line1[:80]}")
                            print(f"       Testing: {line2[:80]}")
                            break

if __name__ == "__main__":
    working_epub = Path(r"e:\Books\blockchain-ico\blockchain-ico-token-economics.epub")
    testing_epub = Path(r"e:\Books\blockchain-ico\ban-gioi\internal-book\bg-internal-book.epub")
    
    if working_epub.exists() and testing_epub.exists():
        compare_epub_structure(str(working_epub), str(testing_epub))
    else:
        print("Error: One or both EPUB files not found")
        print(f"  Working: {working_epub} - {'EXISTS' if working_epub.exists() else 'NOT FOUND'}")
        print(f"  Testing: {testing_epub} - {'EXISTS' if testing_epub.exists() else 'NOT FOUND'}")
