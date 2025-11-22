# TASK PHASE 7: EPUB GENERATION & QUALITY CHECK

**Ngày tạo:** 22/11/2025
**Thời gian:** 1 week
**Ưu tiên:** High

---

## MỤC TIÊU

Convert finalized manuscript to EPUB format and perform comprehensive quality assurance.

---

## EPUB GENERATION

### Day 1-2: Script Preparation

**Review existing script:**
- `blockchain-ico/ban-gioi/internal-book-v2/generate-epub.py` (if exists)
- Or create new based on: `ai_startup/generate-ai-entrepreneur-epub.py`

**Script must handle:**
- Markdown to HTML conversion
- Proper heading hierarchy (H1 → h1, H2 → h2, etc.)
- Image embedding (charts, diagrams)
- Table formatting
- Code blocks (for formulas, examples)
- Footnotes/endnotes
- Table of contents auto-generation
- Metadata (title, author, language, date)

**Metadata to set:**
```python
title = "Bạn Giỏi Token Economics - Hướng Dẫn Toàn Diện"
author = "Bạn Giỏi Team"
language = "vi"  # Vietnamese
publisher = "Bạn Giỏi Foundation"
date = "2025-11-XX"
description = "Hướng dẫn chi tiết về tokenomics của nền tảng Bạn Giỏi, bao gồm thiết kế token, use cases, và hướng dẫn thuế Việt Nam."
```

### Day 3: Generate EPUB

**Steps:**
1. Consolidate all chapter markdown files
2. Add front matter and back matter
3. Run generation script
4. Output: `ban-gioi-token-economics-v2.epub`

**Folder structure during generation:**
```
temp_epub_ban_gioi_v2/
  mimetype
  META-INF/
    container.xml
  OEBPS/
    content.opf
    toc.ncx
    stylesheet.css
    nav.xhtml
    chapter-01.xhtml
    chapter-02.xhtml
    ...
    chapter-09.xhtml
    images/
      (diagrams, charts)
```

---

## QUALITY ASSURANCE TESTING

### Day 4-5: Multi-Reader Testing

**Test on multiple EPUB readers:**
- [ ] **Calibre** (Desktop - Windows/Mac/Linux)
  - TOC navigation works
  - Chapters display correctly
  - Images render properly
  - Tables formatted well
  
- [ ] **Apple Books** (macOS/iOS)
  - Font rendering
  - Image quality
  - Hyperlinks functional
  
- [ ] **Google Play Books** (Android/Web)
  - Mobile responsiveness
  - Page flow
  - Search functionality
  
- [ ] **Adobe Digital Editions**
  - Standards compliance
  - Metadata correct

**Check on different screen sizes:**
- [ ] Desktop (large screen)
- [ ] Tablet (iPad, Android tablet)
- [ ] Phone (iOS, Android)
- [ ] E-reader (Kindle Paperwhite via conversion)

### Day 6: Content Validation

**Table of Contents:**
- [ ] All 9 chapters listed
- [ ] Subsections nested properly
- [ ] Page/location links work
- [ ] Hierarchy correct (Ch → Section → Subsection)

**Images:**
- [ ] All diagrams embedded
- [ ] Charts visible and clear
- [ ] Alt text for accessibility
- [ ] No broken image links

**Formatting:**
- [ ] Headings styled correctly (H1 largest, H2 medium, H3 smaller)
- [ ] Paragraphs have proper spacing
- [ ] Lists formatted (if any)
- [ ] Code blocks/formulas readable
- [ ] Tables don't overflow

**Metadata:**
- [ ] Title correct
- [ ] Author name
- [ ] Language set to Vietnamese
- [ ] Publication date
- [ ] Cover image (if created)
- [ ] Description/summary

**Hyperlinks:**
- [ ] Internal links work (cross-references)
- [ ] External links functional (sources, websites)
- [ ] Footnote links bidirectional

### Day 7: Validation & Final Fixes

**EPUB Validator:**
- [ ] Run through epubcheck (https://www.w3.org/publishing/epubcheck/)
- [ ] Fix any errors (critical)
- [ ] Fix warnings (if feasible)
- [ ] Validate accessibility (WCAG standards)

**Final checks:**
- [ ] File size reasonable (<50MB ideally)
- [ ] No malformed XML
- [ ] Character encoding correct (UTF-8)
- [ ] Vietnamese diacritics display properly

**Comparison with V1:**
- [ ] V2 file larger (more content)
- [ ] All V2 changes reflected
- [ ] No V1 content accidentally left (e.g., BGS mentions)

---

## DELIVERABLES

### 1. EPUB File
**Filename:** `ban-gioi-token-economics-v2.epub`
**Location:** `blockchain-ico/ban-gioi/`
**Size:** ~10-30 MB (depending on images)

### 2. Quality Report
**Document:** `blockchain-ico/ban-gioi/epub-quality-report-v2.md`

**Contents:**
- Validation results (epubcheck)
- Reader compatibility matrix
- Known issues (if any)
- Recommended readers
- Installation instructions

### 3. Generation Script
**File:** `blockchain-ico/ban-gioi/generate-ban-gioi-v2-epub.py`
**Documented:** Comments explaining each step
**Reusable:** Can regenerate if changes needed

### 4. Source Files Archive
**Backup of:**
- All markdown chapter files
- Images/diagrams used
- CSS stylesheet
- Metadata file
**For future updates/corrections**

---

## KNOWN ISSUES TO AVOID

Based on `EPUB-KNOWN-ISSUES.md` (if exists):

### Common EPUB Problems:
- **TOC not generating:** Ensure proper heading hierarchy
- **Images not showing:** Check file paths, embedding method
- **Vietnamese characters broken:** UTF-8 encoding mandatory
- **Tables overflow:** Use responsive CSS, limit table width
- **Links broken:** Validate all href attributes
- **Metadata missing:** Fill all Dublin Core fields

### Solutions Applied:
- Use `lang="vi"` attribute
- Encode all files as UTF-8 with BOM
- Test images in base64 vs external files
- Responsive table CSS
- Validate all links before generation

---

## SUCCESS CRITERIA

✅ EPUB passes epubcheck with 0 errors
✅ TOC navigation works in all tested readers
✅ All images display correctly
✅ Vietnamese text renders properly (no � characters)
✅ File size <50MB
✅ Metadata complete and accurate
✅ Readable on mobile, tablet, desktop
✅ All 9 chapters present and formatted
✅ No V1 content remaining

---

## POST-GENERATION

### Distribution Preparation:
- [ ] Upload to Google Drive/Dropbox for team review
- [ ] Create sample excerpts (Chapter 1 + Chapter 9)
- [ ] Generate PDF version (via Calibre) for print option
- [ ] Create cover image (if not yet done)

### Marketing Assets:
- [ ] Book description (Vietnamese & English)
- [ ] Key features bullet points
- [ ] Author bio
- [ ] Sample screenshots from EPUB

---

**Priority:** HIGH - Final deliverable
**Team:** Primary writer + Technical specialist
**Output:** Publication-ready EPUB file