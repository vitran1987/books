# Known Issues and Solutions for EPUB Generation

## Document Purpose
This document catalogs all issues encountered during EPUB generation for Google Play Books and other platforms, along with their solutions. Use this as a troubleshooting guide when EPUBs fail validation or upload.

---

## Critical Issues (Will Cause Rejection)

### 1. XML Special Characters Not Escaped

**Issue:** Unescaped special characters in XHTML content cause XML parsing errors.

**Symptoms:**
- Google Play Books rejects upload with "invalid XML" error
- XML parsers report "not well-formed (invalid token)"
- Error message includes line and column number

**Root Cause:**
XML/XHTML reserves certain characters that must be escaped:
- `&` must be `&amp;`
- `<` must be `&lt;`
- `>` must be `&gt;`
- `"` must be `&quot;` (in attributes)
- `'` must be `&apos;` (in attributes)

**Example Problem:**
```html
<!-- WRONG - Will fail validation -->
<p>Governance & Strategic Decision</p>
<p>Click here to learn more >> </p>
<p>Price < $100</p>
```

**Correct Solution:**
```html
<!-- CORRECT - Valid XML -->
<p>Governance &amp; Strategic Decision</p>
<p>Click here to learn more &gt;&gt; </p>
<p>Price &lt; $100</p>
```

**Where to Fix:**
- **Hardcoded templates:** Search for `&`, `<`, `>` in HTML template strings
- **Dynamic content:** Use Python's `html.escape()` function
- **Generated content:** Ensure `clean_text()` method is applied to all user content

**How to Detect:**
```python
# Run this validator
python validate_epub.py

# Look for errors like:
# ❌ OEBPS/content/title-page.xhtml: not well-formed (invalid token): line 18, column 50
```

**Prevention:**
```python
import html

# For dynamic content
content = html.escape(user_text, quote=False)

# For quote characters in attributes
attr_value = html.escape(user_text, quote=True)
```

---

### 2. Missing Navigation Document

**Issue:** EPUB 3.0 requires a navigation document with `properties="nav"`.

**Symptoms:**
- Validator reports "Missing navigation document"
- Table of contents doesn't work
- Some readers can't navigate between chapters

**Root Cause:**
EPUB 3.0 specification requires a navigation document (nav.xhtml) that:
- Has `epub:type="toc"` attribute on the `<nav>` element
- Is listed in manifest with `properties="nav"`
- Contains proper `<ol>` list structure

**Solution:**
Ensure content.opf has:
```xml
<item id="nav" href="content/nav.xhtml" 
      media-type="application/xhtml+xml" 
      properties="nav"/>
```

And nav.xhtml contains:
```html
<nav epub:type="toc" id="toc">
    <h1>Mục lục</h1>
    <ol>
        <li><a href="section-001.xhtml">Chapter Title</a></li>
    </ol>
</nav>
```

---

### 3. Incorrect Navigation Links

**Issue:** Navigation hrefs use wrong paths (absolute instead of relative or vice versa).

**Symptoms:**
- Table of contents links don't work
- Clicking chapters leads to 404 or blank pages
- Google Play Books may reject or display navigation incorrectly

**Root Cause:**
Path resolution in EPUB is relative to the current file's location.

**Example:**
If `nav.xhtml` is at `OEBPS/content/nav.xhtml` and section is at `OEBPS/content/section-001.xhtml`, the link should be:

```html
<!-- CORRECT - Both files in same folder -->
<a href="section-001.xhtml">Chapter 1</a>

<!-- WRONG - Tries to find OEBPS/content/content/section-001.xhtml -->
<a href="content/section-001.xhtml">Chapter 1</a>
```

**How to Fix:**
- Links in `nav.xhtml` to other files in `content/` folder: use `section-XXX.xhtml`
- Links in `nav.xhtml` to `styles/main.css`: use `../styles/main.css`
- Links in content.opf (which is in OEBPS/): use `content/section-XXX.xhtml`

**Rule of Thumb:**
Paths are always relative to the **current file's location**, not the EPUB root.

---

### 4. Missing or Invalid Mimetype

**Issue:** Mimetype file is missing, compressed, or not first in ZIP.

**Symptoms:**
- EPUB readers don't recognize file as EPUB
- "File is corrupted" or "Not a valid EPUB" errors
- Google Play Books immediate rejection

**Requirements:**
1. **Must be named:** `mimetype` (lowercase, no extension)
2. **Must contain:** `application/epub+zip` (exactly 20 bytes, no newline)
3. **Must be first file** in ZIP archive
4. **Must be uncompressed** (ZIP_STORED, not ZIP_DEFLATED)

**How to Check:**
```python
import zipfile
z = zipfile.ZipFile('book.epub', 'r')
print("First file:", z.namelist()[0])  # Should be 'mimetype'
print("Compress type:", z.getinfo('mimetype').compress_type)  # Should be 0
print("Content:", z.read('mimetype'))  # Should be b'application/epub+zip'
```

**How to Fix in Python:**
```python
# When creating ZIP, add mimetype FIRST and UNCOMPRESSED
with zipfile.ZipFile(epub_file, 'w') as epub_zip:
    # Add mimetype first (uncompressed)
    epub_zip.write(
        output_dir / "mimetype", 
        "mimetype", 
        compress_type=zipfile.ZIP_STORED  # CRITICAL!
    )
    
    # Then add everything else with compression
    # ...rest of files...
```

---

### 5. Missing Cover Image or Images Folder

**Issue:** EPUB has no cover or images folder doesn't exist in ZIP.

**Symptoms:**
- Google Play Books may reject (depends on policy)
- No cover shown in library/catalog
- Unprofessional appearance
- Content.opf references non-existent cover image

**Root Cause:**
- ZIP files don't store empty directories
- If images/ folder is created but no image is copied, folder doesn't exist in final ZIP
- Google Play Books often requires cover for publication

**Solution:**
Always include at least a placeholder cover:

```python
# Create minimal valid PNG (1x1 transparent pixel)
png_data = bytes.fromhex(
    '89504e470d0a1a0a0000000d49484452000000010000000108060000001f15c4'
    '890000000a4944415478da620001000000050001 0d0a2db40000000049454e44ae426082'
)
with open('book_cover.png', 'wb') as f:
    f.write(png_data)
```

Or use PIL/Pillow to create a proper cover with text.

**Recommended Cover Specs:**
- Format: PNG or JPEG
- Dimensions: 800x1200 pixels (2:3 ratio) minimum
- Size: Under 2MB
- Resolution: 72 DPI minimum

---

## Warning Issues (May Cause Problems)

### 6. Missing dcterms:modified Timestamp

**Issue:** EPUB 3.0 recommends dcterms:modified in metadata.

**Symptoms:**
- Some validators show warning
- May affect update detection on platforms
- Not critical but unprofessional

**Solution:**
Add to content.opf metadata:
```xml
<meta property="dcterms:modified">2025-11-18T21:33:09Z</meta>
```

**How to Generate in Python:**
```python
from datetime import datetime
timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
```

---

### 7. Missing DOCTYPE Declaration

**Issue:** XHTML files without DOCTYPE declaration.

**Symptoms:**
- Some validators issue warnings
- Rendering may vary across readers
- Not XHTML5 compliant

**Solution:**
All XHTML files should start with:
```html
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
```

---

### 8. Inconsistent Metadata

**Issue:** Missing or incomplete required metadata fields.

**Required in content.opf:**
- `dc:title` - Book title
- `dc:language` - Language code (e.g., "vi", "en")
- `dc:identifier` - Unique book identifier
- `dc:creator` - Author/creator name (optional but recommended)
- `dc:date` - Publication date (recommended)

**Recommended:**
- `dc:publisher`
- `dc:subject` (keywords, can have multiple)
- `dc:description`
- `dc:rights` (copyright)

---

## Platform-Specific Issues

### Google Play Books

**Additional Requirements:**
1. **Cover image mandatory** for publication
2. **Strict XML validation** - no tolerance for errors
3. **Minimum content** - very short books may be rejected
4. **Language declaration** - must match actual content language

**Known Rejections:**
- Invalid XML (most common)
- Missing cover image
- Broken internal links
- Copyright/rights issues
- Adult content without proper flagging

---

### Apple Books

**Known Issues:**
- Requires specific metadata for iBooks features
- Font embedding has strict requirements
- Fixed layout EPUBs need special declarations

---

## Validation Tools

### Built-in Validator (validate_epub.py)

```bash
cd path/to/epub/folder
python validate_epub.py
```

**Checks:**
- Mimetype correctness
- XML well-formedness
- Required metadata
- File existence
- Navigation structure
- Content.opf validity

---

### EPUBCheck (Industry Standard)

Download from: https://github.com/w3c/epubcheck

```bash
java -jar epubcheck.jar book.epub
```

Most authoritative EPUB validator.

---

### Online Validators

- **EPUB Validator:** http://validator.idpf.org/
- **Pagina EPUB Checker:** https://www.pagina.gmbh/produkte/epub-checker/

---

## Common Error Messages

### "not well-formed (invalid token)"
**Cause:** Unescaped special character in XML
**Fix:** Escape `&`, `<`, `>`, `"`, `'` characters

### "Missing navigation document"
**Cause:** No file with `properties="nav"` in manifest
**Fix:** Add nav.xhtml with proper properties

### "File not found in manifest"
**Cause:** Manifest lists file that doesn't exist in ZIP
**Fix:** Verify all manifest hrefs exist as actual files

### "Mimetype not found"
**Cause:** Mimetype isn't first file or is compressed
**Fix:** Recreate ZIP with mimetype first and uncompressed

### "Invalid file sequence"
**Cause:** Files in wrong order in ZIP
**Fix:** Ensure: mimetype (first) → META-INF → OEBPS

---

## Debugging Checklist

When EPUB fails validation:

- [ ] Extract EPUB (it's a ZIP) and examine structure
- [ ] Run validate_epub.py for detailed report
- [ ] Check mimetype file (first, uncompressed, exact content)
- [ ] Verify all XHTML files are valid XML (no unescaped `&`, `<`, `>`)
- [ ] Confirm navigation links use correct relative paths
- [ ] Ensure all files in manifest actually exist in ZIP
- [ ] Check content.opf has all required metadata
- [ ] Verify cover image exists if referenced
- [ ] Test navigation by clicking links in an EPUB reader

---

## Quick Fix Commands

### Extract EPUB for inspection
```powershell
Expand-Archive -Path book.epub -DestinationPath epub-temp -Force
```

### Check ZIP structure
```python
import zipfile
z = zipfile.ZipFile('book.epub', 'r')
for name in z.namelist()[:10]:
    print(name)
```

### Validate XML files
```python
import xml.etree.ElementTree as ET
ET.parse('path/to/file.xhtml')  # Will raise exception if invalid
```

### Find unescaped ampersands
```powershell
Get-Content file.xhtml | Select-String -Pattern '&(?!amp;|lt;|gt;|quot;|apos;)'
```

---

## Best Practices

### Template Safety
```python
# BAD - Hardcoded strings may have unescaped characters
html = '''<p>Company & Partners</p>'''

# GOOD - Use html.escape for all text content
import html
company_name = "Company & Partners"
html = f'<p>{html.escape(company_name)}</p>'
```

### Path Construction
```python
# For files in same directory
href = "section-001.xhtml"

# For files in parent's sibling directory
href = "../styles/main.css"

# In content.opf (which is in OEBPS/)
href = "content/section-001.xhtml"
```

### Metadata Completeness
Always include at minimum:
- Title, Language, Identifier
- Modified timestamp for EPUB 3
- Creator (author)
- Publisher (even if self-published)

---

## Testing Strategy

1. **Generate EPUB**
2. **Run validate_epub.py** - Fix all errors
3. **Test in Calibre** (free EPUB reader) - Verify navigation works
4. **Run EPUBCheck** (if available) - Industry standard validation
5. **Test upload to Google Play Books** - Final verification
6. **Check on actual device** - Real-world testing

---

## Support Resources

### Official Specifications
- EPUB 3.3: https://www.w3.org/TR/epub-33/
- EPUB Accessibility: https://www.w3.org/TR/epub-a11y-11/

### Validation Tools
- EPUBCheck: https://github.com/w3c/epubcheck
- EPUB Validator: http://validator.idpf.org/

### Communities
- MobileRead Forums: https://www.mobileread.com/forums/
- EPUB Stack Exchange: https://ebooks.stackexchange.com/

---

## Version History

- **v1.0** (2025-11-18): Initial documentation
  - XML escaping issues
  - Navigation path problems
  - Cover image requirements
  - Mimetype specifications

---

## Contact

For issues with this specific EPUB generation script, refer to:
- `generate-bg-epub.py` - Main generation script
- `validate_epub.py` - Validation tool
- `compare_epubs.py` - Comparison tool
- This document for troubleshooting
