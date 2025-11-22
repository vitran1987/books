# TASK 12: EPUB GENERATION & QUALITY ASSURANCE

**Duration:** 1 week  
**Priority:** CRITICAL (Final delivery)  
**Dependencies:** Task 11 (Reviewed manuscript)  
**Team:** Technical Publisher + QA Tester

---

## OBJECTIVE

Convert the final Series 2 manuscript into a high-quality EPUB file, validate across multiple e-readers, fix all technical issues, and deliver the final product ready for distribution.

---

## PREREQUISITES

Before starting Task 12, ensure:

**✅ From Task 11:**
- [ ] All 9 chapters reviewed and finalized
- [ ] All diagrams in high-resolution format (PNG/SVG, 300 DPI)
- [ ] All tables properly formatted
- [ ] Editor sign-off obtained
- [ ] Review report completed

**✅ Assets Ready:**
- [ ] Cover image (1600×2400 px minimum, JPG/PNG)
- [ ] Author bio and photo
- [ ] Copyright page content
- [ ] Dedication/acknowledgments (if any)
- [ ] ISBN (if publishing commercially)

**✅ Metadata:**
- [ ] Title: "Blockchain, ICO & Token Economics - Series 2: Cải Tiến & Tối Ưu"
- [ ] Subtitle: "9 Nâng Cấp Thiết Yếu Từ Series 1 Đến Mô Hình Hoàn Thiện"
- [ ] Author: [Your Name]
- [ ] Language: Vietnamese (vi)
- [ ] Publication date
- [ ] Keywords: blockchain, ICO, token economics, governance, Vietnam, cryptocurrency, DeFi

---

## PHASE 1: EPUB GENERATION (2 days)

### 1.1 Prepare Source Files

**Directory structure:**
```
blockchain-ico/ban-gioi/internal-book-v2/epub-source/
├── chapters/
│   ├── chuong-01-governance-model.md
│   ├── chuong-02-single-token-model.md
│   ├── ...
│   └── chuong-09-thue-ke-toan-vietnam.md
├── images/
│   ├── cover.jpg
│   ├── diagram-governance-flowchart.png
│   ├── diagram-token-flow.png
│   ├── ...
├── metadata.yaml
└── styles.css
```

**metadata.yaml example:**
```yaml
---
title: "Blockchain, ICO & Token Economics - Series 2"
subtitle: "Cải Tiến & Tối Ưu"
author: [Your Name]
language: vi
date: 2025-01-15
rights: © 2025 [Your Name]. All rights reserved.
publisher: [Publisher Name]
identifier:
  - scheme: ISBN
    text: [ISBN if available]
cover-image: images/cover.jpg
stylesheet: styles.css
---
```

**styles.css:**
```css
/* Typography */
body {
  font-family: "Noto Serif", Georgia, serif;
  font-size: 1em;
  line-height: 1.6;
  margin: 0 5%;
}

h1 {
  font-size: 1.8em;
  font-weight: bold;
  margin-top: 2em;
  margin-bottom: 1em;
  page-break-before: always;
}

h2 {
  font-size: 1.4em;
  font-weight: bold;
  margin-top: 1.5em;
  margin-bottom: 0.8em;
}

h3 {
  font-size: 1.2em;
  font-weight: bold;
  margin-top: 1.2em;
  margin-bottom: 0.6em;
}

/* Tables */
table {
  border-collapse: collapse;
  width: 100%;
  margin: 1em 0;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
  font-weight: bold;
}

/* Code blocks */
pre {
  background-color: #f5f5f5;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 1em;
  overflow-x: auto;
}

code {
  font-family: "Courier New", monospace;
  font-size: 0.9em;
}

/* Images */
img {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 1em auto;
}

/* Lists */
ul, ol {
  margin: 1em 0;
  padding-left: 2em;
}

li {
  margin: 0.5em 0;
}

/* Blockquotes */
blockquote {
  margin: 1em 0;
  padding-left: 1em;
  border-left: 4px solid #ddd;
  font-style: italic;
}
```

### 1.2 Run EPUB Generation Script

**Use existing script as template:**
`blockchain-ico/generate-blockchain-epub.py`

**Update for Series 2:**

```python
#!/usr/bin/env python3
"""
Generate EPUB for Blockchain ICO Token Economics - Series 2
Based on existing generate-blockchain-epub.py with Series 2 specific updates
"""

import os
import shutil
from ebooklib import epub
import markdown

# Configuration
BOOK_TITLE = "Blockchain, ICO & Token Economics - Series 2"
BOOK_SUBTITLE = "Cải Tiến & Tối Ưu"
BOOK_AUTHOR = "[Your Name]"
BOOK_LANGUAGE = "vi"
BOOK_IDENTIFIER = "series-2-blockchain-ico-improvements"

# Paths
SOURCE_DIR = "internal-book-v2/epub-source/chapters"
IMAGE_DIR = "internal-book-v2/epub-source/images"
OUTPUT_FILE = "blockchain-ico-series-2.epub"

# Chapter mapping
CHAPTERS = [
    ("chuong-01-governance-model.md", "Chương 1: Mô Hình Quản Trị Cải Tiến"),
    ("chuong-02-single-token-model.md", "Chương 2: Mô Hình Token Đơn Giản"),
    ("chuong-03-flexible-supply.md", "Chương 3: Nguồn Cung Linh Hoạt"),
    ("chuong-04-market-driven-rewards.md", "Chương 4: Phần Thưởng Theo Thị Trường"),
    ("chuong-05-realistic-projections.md", "Chương 5: Dự Báo Thực Tế"),
    ("chuong-06-platform-token-holdings.md", "Chương 6: Nền Tảng Không Giữ Token"),
    ("chuong-07-dynamic-burn.md", "Chương 7: Đốt Token Động"),
    ("chuong-08-anti-whale.md", "Chương 8: Chống Cá Voi"),
    ("chuong-09-thue-ke-toan-vietnam.md", "Chương 9: Thuế & Kế Toán Việt Nam"),
]

def create_epub():
    """Main EPUB creation function"""
    
    # Create book
    book = epub.EpubBook()
    
    # Set metadata
    book.set_identifier(BOOK_IDENTIFIER)
    book.set_title(BOOK_TITLE)
    book.add_author(BOOK_AUTHOR)
    book.set_language(BOOK_LANGUAGE)
    
    # Add cover
    cover_path = os.path.join(IMAGE_DIR, "cover.jpg")
    if os.path.exists(cover_path):
        with open(cover_path, 'rb') as cover_file:
            book.set_cover("cover.jpg", cover_file.read())
    
    # Add CSS
    style = '''
    @namespace epub "http://www.idpf.org/2007/ops";
    
    body {
        font-family: "Noto Serif", Georgia, serif;
        line-height: 1.6;
        margin: 0 5%;
    }
    
    h1 {
        font-size: 1.8em;
        margin-top: 2em;
        page-break-before: always;
    }
    
    h2 { font-size: 1.4em; margin-top: 1.5em; }
    h3 { font-size: 1.2em; margin-top: 1.2em; }
    
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 1em 0;
    }
    
    th, td {
        border: 1px solid #ddd;
        padding: 8px;
    }
    
    pre {
        background-color: #f5f5f5;
        border: 1px solid #ddd;
        padding: 1em;
        overflow-x: auto;
    }
    
    img {
        max-width: 100%;
        height: auto;
        display: block;
        margin: 1em auto;
    }
    '''
    
    nav_css = epub.EpubItem(
        uid="style_nav",
        file_name="style/nav.css",
        media_type="text/css",
        content=style
    )
    book.add_item(nav_css)
    
    # Process chapters
    chapters_epub = []
    toc = []
    spine = ['nav']
    
    for idx, (filename, title) in enumerate(CHAPTERS, 1):
        filepath = os.path.join(SOURCE_DIR, filename)
        
        if not os.path.exists(filepath):
            print(f"Warning: {filepath} not found, skipping")
            continue
        
        # Read markdown
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Convert to HTML
        html_content = markdown.markdown(
            content,
            extensions=['tables', 'fenced_code', 'nl2br']
        )
        
        # Create chapter
        chapter = epub.EpubHtml(
            title=title,
            file_name=f'chap_{idx:02d}.xhtml',
            lang=BOOK_LANGUAGE
        )
        
        chapter.content = f'<h1>{title}</h1>\n{html_content}'
        chapter.add_item(nav_css)
        
        book.add_item(chapter)
        chapters_epub.append(chapter)
        toc.append(chapter)
        spine.append(chapter)
    
    # Add images
    for img_file in os.listdir(IMAGE_DIR):
        if img_file.lower().endswith(('.png', '.jpg', '.jpeg', '.svg')):
            img_path = os.path.join(IMAGE_DIR, img_file)
            
            with open(img_path, 'rb') as img:
                img_content = img.read()
            
            # Determine media type
            if img_file.lower().endswith('.png'):
                media_type = 'image/png'
            elif img_file.lower().endswith('.svg'):
                media_type = 'image/svg+xml'
            else:
                media_type = 'image/jpeg'
            
            img_item = epub.EpubItem(
                uid=f"img_{img_file}",
                file_name=f"images/{img_file}",
                media_type=media_type,
                content=img_content
            )
            
            book.add_item(img_item)
    
    # Set TOC
    book.toc = toc
    
    # Add navigation files
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    
    # Set spine
    book.spine = spine
    
    # Write EPUB
    epub.write_epub(OUTPUT_FILE, book, {})
    
    print(f"✓ EPUB generated: {OUTPUT_FILE}")
    print(f"  Chapters: {len(chapters_epub)}")
    print(f"  Size: {os.path.getsize(OUTPUT_FILE) / 1024:.1f} KB")

if __name__ == "__main__":
    create_epub()
```

**Run generation:**
```powershell
cd e:\Books\blockchain-ico
python generate-series-2-epub.py
```

**Expected output:**
- `blockchain-ico-series-2.epub` file created
- ~2-5 MB file size (depending on images)
- No errors or warnings

### 1.3 Validate EPUB Structure

**Use EPUBCheck validator:**
```powershell
# Download EPUBCheck if not already: https://github.com/w3c/epubcheck/releases
java -jar epubcheck.jar blockchain-ico-series-2.epub
```

**Expected result:**
- No errors
- Warnings acceptable if minor (font embedding, etc.)

**Common issues from KNOWN-ISSUES.md to avoid:**
- ❌ XML escaping in content (& → &amp;, < → &lt;)
- ❌ Mimetype not first file or compressed
- ❌ Invalid XHTML structure
- ❌ Missing navigation elements

**Fix if found:**
- Review script's HTML generation
- Ensure markdown conversion escapes properly
- Check mimetype file creation
- Validate TOC and spine

---

## PHASE 2: QUALITY ASSURANCE TESTING (3 days)

### 2.1 Multi-Platform Testing

**Test on all major e-readers:**

**Desktop:**
- [ ] **Calibre** (Windows/Mac/Linux)
  - Open EPUB
  - Check TOC navigation
  - Check all chapters load
  - Check images display correctly
  - Check tables render properly
  - Check formatting (fonts, spacing)
  
- [ ] **Adobe Digital Editions**
  - Same checks as Calibre
  - Test page turning smoothness
  - Test search functionality

**Mobile:**
- [ ] **Apple Books** (iOS/macOS)
  - Transfer EPUB via AirDrop or email
  - Check rendering on iPhone and iPad
  - Test night mode
  - Test font size adjustments
  
- [ ] **Google Play Books** (Android/Web)
  - Upload to Google Play Books library
  - Check rendering on phone and tablet
  - Test annotations and highlights

**E-Ink Readers:**
- [ ] **Kindle** (via conversion)
  - Convert EPUB to MOBI using Calibre
  - Transfer to Kindle
  - Test on actual Kindle device (if available)
  - Note: Some formatting may degrade (acceptable)

- [ ] **Kobo** (if available)
  - Direct EPUB support
  - Check rendering

### 2.2 Content Verification

**For each chapter, verify:**

**Text Rendering:**
- [ ] Vietnamese characters display correctly (no encoding issues)
- [ ] No broken formatting (unexpected line breaks, missing italics/bold)
- [ ] Code blocks readable and properly formatted
- [ ] Quotation marks correct (not curly quotes in code)

**Images:**
- [ ] All diagrams visible
- [ ] Images not pixelated (high resolution maintained)
- [ ] Images not too large (don't overflow page)
- [ ] Captions display correctly

**Tables:**
- [ ] All tables render (not broken)
- [ ] Columns align properly
- [ ] Headers bold and distinct
- [ ] Data readable (not cut off)

**Navigation:**
- [ ] TOC includes all 9 chapters
- [ ] Clicking TOC entries jumps to correct chapter
- [ ] Chapter headings match TOC
- [ ] Logical reading order maintained

**Links:**
- [ ] External links work (if any)
- [ ] Internal cross-references work (if any)
- [ ] Footnotes/endnotes navigate correctly (if any)

### 2.3 Functional Testing

**Reader Features:**
- [ ] **Bookmarks:** Can set and return to bookmarks
- [ ] **Highlights:** Can highlight text
- [ ] **Notes:** Can add annotations
- [ ] **Search:** Can search for text (finds results)
- [ ] **Font adjustment:** Changing font size works correctly
- [ ] **Night mode:** Dark mode renders text visible

**Performance:**
- [ ] Book opens quickly (<5 seconds)
- [ ] Page turns smooth (no lag)
- [ ] Searching is responsive
- [ ] No crashes or freezes

### 2.4 Issue Tracking

**Use checklist to document issues:**

| Issue # | Severity | Platform | Description | Status | Fix |
|---------|----------|----------|-------------|--------|-----|
| 1       | Critical | All      | Chapter 3 missing images | Open | Re-export images |
| 2       | Minor    | Calibre  | Table border too thin | Open | Adjust CSS |
| ...     | ...      | ...      | ...         | ...    | ... |

**Severity levels:**
- **Critical:** Blocks reading or missing content → Must fix before release
- **High:** Significant formatting issue or broken feature → Should fix
- **Medium:** Minor visual inconsistency → Nice to fix
- **Low:** Cosmetic issue → Can defer

**Fix priority:**
- Address all Critical and High issues
- Fix Medium if time allows
- Document Low issues for future revision

---

## PHASE 3: FIXES & ITERATIONS (1 day)

### 3.1 Content Fixes

**If content issues found:**

**Missing/broken content:**
- Identify source file causing issue
- Fix in markdown source
- Regenerate EPUB
- Re-test affected sections

**Formatting issues:**
- Adjust CSS styles
- Regenerate EPUB
- Verify fix across all platforms

**Image issues:**
- Re-export images at correct resolution
- Update image references if needed
- Regenerate EPUB
- Check image quality

### 3.2 Metadata Fixes

**If metadata incorrect:**

**Update metadata.yaml:**
- Title, author, date, etc.
- Keywords for discoverability
- ISBN if applicable

**Update cover:**
- Ensure correct file path
- Correct dimensions (1600×2400 minimum)
- High quality (300 DPI)

**Regenerate EPUB after any metadata changes**

### 3.3 Regression Testing

**After each fix:**
- Re-run EPUBCheck validator
- Re-test on at least 2 platforms (Calibre + mobile)
- Confirm fix worked
- Ensure no new issues introduced

**Iteration cycle:**
1. Test → Find issues
2. Fix → Regenerate EPUB
3. Re-test → Verify fixes
4. Repeat until no critical/high issues remain

---

## PHASE 4: FINAL DELIVERY (1 day)

### 4.1 Final Validation

**Before declaring EPUB complete:**

**Technical checklist:**
- [ ] EPUBCheck passes with no errors
- [ ] All chapters present (9 chapters)
- [ ] All images included and displaying
- [ ] TOC complete and functional
- [ ] Metadata accurate
- [ ] File size reasonable (<10 MB)

**Quality checklist:**
- [ ] Tested on ≥3 platforms (desktop, mobile, web)
- [ ] No critical or high severity issues
- [ ] Vietnamese text renders correctly
- [ ] Professional appearance (formatting consistent)

**Content checklist:**
- [ ] All 9 chapters from reviewed manuscript
- [ ] No placeholder or draft text
- [ ] Copyright page included
- [ ] Author bio included (if desired)

### 4.2 Package Deliverables

**Create final package:**

```
blockchain-ico-series-2-final/
├── blockchain-ico-series-2.epub          # Main EPUB file
├── blockchain-ico-series-2.mobi          # Kindle version (optional)
├── cover.jpg                             # Cover image standalone
├── README.txt                            # Installation instructions
├── qa-report.md                          # QA test results
└── metadata.json                         # Book metadata for distribution
```

**README.txt example:**
```
BLOCKCHAIN, ICO & TOKEN ECONOMICS - SERIES 2
Cải Tiến & Tối Ưu

INSTALLATION:
1. Download blockchain-ico-series-2.epub
2. Open with your e-reader app:
   - iOS/Mac: Apple Books
   - Android: Google Play Books
   - Desktop: Calibre or Adobe Digital Editions
   - Kindle: Convert .mobi version

TROUBLESHOOTING:
- If images don't display: Ensure e-reader supports PNG/JPG
- If Vietnamese text shows ��: Check e-reader language support
- For best experience: Use latest version of e-reader app

SUPPORT:
Contact: [Your Email]
Website: [Your Website]

© 2025 [Your Name]. All rights reserved.
```

**qa-report.md:**
- Summary of testing performed
- Platforms tested
- Issues found and fixed
- Final validation results
- Sign-off from QA tester

**metadata.json:**
```json
{
  "title": "Blockchain, ICO & Token Economics - Series 2",
  "subtitle": "Cải Tiến & Tối Ưu",
  "author": "[Your Name]",
  "language": "vi",
  "isbn": "[ISBN if available]",
  "publication_date": "2025-01-15",
  "pages": "[Estimated page count]",
  "word_count": 50000,
  "chapters": 9,
  "price": {
    "vnd": 299000,
    "usd": 12.99
  },
  "keywords": [
    "blockchain",
    "ICO",
    "token economics",
    "cryptocurrency",
    "governance",
    "DeFi",
    "Vietnam",
    "crypto taxation"
  ],
  "description": "Series 2 tập trung vào 9 cải tiến thiết yếu từ Series 1, bao gồm mô hình quản trị cải tiến, token đơn giản hóa, nguồn cung linh hoạt, phần thưởng theo thị trường, dự báo thực tế, nền tảng không giữ token, đốt token động, chống cá voi, và hướng dẫn thuế Việt Nam chi tiết.",
  "series": {
    "name": "Blockchain, ICO & Token Economics",
    "number": 2,
    "total": 2
  }
}
```

### 4.3 Distribution Preparation

**If publishing commercially:**

**Upload to distributors:**
- [ ] Amazon Kindle Direct Publishing (KDP) - .mobi version
- [ ] Apple Books - .epub
- [ ] Google Play Books - .epub
- [ ] Kobo Writing Life - .epub
- [ ] Vietnam book platforms (Fahasa, Tiki, etc.) - .epub

**Set pricing:**
- Consider Series 1 price for consistency
- Suggested: 299,000 VND (~$12.99 USD)
- Or bundle both series at discount

**Marketing materials:**
- Book description (Vietnamese + English)
- Author bio
- Sample chapters (first 2 chapters as PDF)
- Cover images for social media

**If distributing freely or to limited audience:**
- [ ] Upload to Google Drive / Dropbox
- [ ] Share link with readers
- [ ] Or email directly

### 4.4 Archive & Backup

**Preserve all source materials:**

**Archive structure:**
```
blockchain-ico-series-2-archive-[date]/
├── source-markdown/          # All chapter .md files
├── images-high-res/          # Original high-res images
├── research-data/            # Research database from Task 01
├── drafts/                   # Draft versions (for reference)
├── reviews/                  # Review reports from Task 11
├── epub-final/               # Final EPUB + deliverables
├── scripts/                  # EPUB generation scripts
└── README-archive.md         # Documentation of archive
```

**Backup locations:**
- [ ] Local external drive
- [ ] Cloud storage (Google Drive, OneDrive, etc.)
- [ ] Git repository (if appropriate) - vitran1987/books

**Version control:**
- Tag final version: `series-2-v1.0-final`
- Document any post-release updates as v1.1, v1.2, etc.

---

## QUALITY CHECKLIST

**EPUB Generation:**
- [ ] Script runs without errors
- [ ] All chapters included in correct order
- [ ] All images embedded correctly
- [ ] CSS applied properly
- [ ] Metadata complete and accurate
- [ ] EPUBCheck validation passes

**Multi-Platform Testing:**
- [ ] Tested on Calibre (desktop)
- [ ] Tested on Apple Books (mobile/desktop)
- [ ] Tested on Google Play Books (mobile/web)
- [ ] Tested on e-ink reader or Kindle (optional)
- [ ] All platforms render content correctly

**Content Verification:**
- [ ] Vietnamese text displays correctly (no encoding issues)
- [ ] All images visible and high quality
- [ ] All tables render properly
- [ ] Navigation (TOC) works perfectly
- [ ] No broken formatting or missing content

**Functional Testing:**
- [ ] Bookmarks, highlights, notes work
- [ ] Search functionality works
- [ ] Font adjustment works
- [ ] Night mode works
- [ ] Performance acceptable (no lag)

**Issue Resolution:**
- [ ] All critical issues fixed
- [ ] All high priority issues fixed
- [ ] Medium issues addressed (if time allows)
- [ ] Low issues documented for future

**Final Delivery:**
- [ ] Final EPUB file ready
- [ ] QA report completed
- [ ] README and metadata prepared
- [ ] All deliverables packaged
- [ ] Archive created and backed up

---

## SUCCESS CRITERIA

**Task 12 is complete when:**
- ✅ EPUB file generated successfully
- ✅ EPUBCheck validation passes
- ✅ Tested on minimum 3 platforms (all working)
- ✅ All critical and high priority issues resolved
- ✅ Vietnamese text renders correctly everywhere
- ✅ Professional quality presentation
- ✅ QA report completed and signed off
- ✅ Final deliverables packaged
- ✅ Source materials archived and backed up
- ✅ Ready for distribution or publication

---

**Task Owner:** Technical Publisher (Lead) + QA Tester  
**Input:** Reviewed manuscript from Task 11 + Assets  
**Output:** Final EPUB file + Deliverables package  
**Timeline:** Week 18  
**Status:** ⏳ Waiting for Task 11 completion

---

## POST-RELEASE PLAN

**After EPUB release:**

**Version 1.0 Release:**
- Distribute to target audience
- Collect reader feedback
- Monitor for reported issues

**Maintenance:**
- If minor errors found → Create errata document
- If major errors found → Plan v1.1 update
- Update EPUB and redistribute

**Future Editions:**
- Series 3 (if needed in future)
- Translated editions (English version?)
- Updated editions as crypto landscape evolves

**Analytics (if commercial):**
- Track sales/downloads
- Monitor reviews and ratings
- Gather reader feedback for improvements
