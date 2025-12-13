# EPUB Generation Standards and Process Documentation

**Version**: 2.0  
**Date**: August 2, 2025  
**Status**: Updated with Bold Text Handling Requirements  

---

## 📋 Overview

This document establishes standardized requirements and processes for generating EPUB files from markdown content, ensuring consistent quality, proper formatting, and professional presentation across all book projects.

## 🎯 Core Requirements

### 1. Markdown to HTML Conversion Standards

#### Bold Text Handling (CRITICAL)
- **Requirement**: All `**bold text**` markdown syntax MUST be converted to `<strong>` HTML tags
- **Implementation**: Use regex pattern `r'\*\*(.*?)\*\*'` to replace with `<strong>\1</strong>`
- **Scope**: Apply to all content types (headers, paragraphs, lists, etc.)
- **Validation**: No `**` characters should remain in final EPUB content

#### Header Conversion
- `# Header` → `<h2>Header</h2>`
- `## Header` → `<h3>Header</h3>`
- `### Header` → `<h4>Header</h4>`
- `#### Header` → `<h5>Header</h5>`

#### List Conversion
- `- Item` → `<p>• Item</p>`
- `* Item` → `<p>• Item</p>`
- `1. Item` → `<p>1. Item</p>`

### 2. CSS Styling Requirements

#### Bold Text Styling
```css
strong {
    font-weight: bold;
    color: #1a365d; /* or appropriate theme color */
}
```

#### Base Typography
```css
body {
    font-family: "Times New Roman", serif;
    line-height: 1.6;
    margin: 0;
    padding: 1em;
    color: #333;
}

h1, h2, h3, h4, h5, h6 {
    color: #1a365d;
    margin-top: 1.5em;
    margin-bottom: 0.5em;
    line-height: 1.2;
}

p {
    margin: 1em 0;
    text-align: justify;
}
```

### 3. EPUB Structure Standards

#### Required Files
- `mimetype` - EPUB format identifier
- `META-INF/container.xml` - Container specification
- `OEBPS/content.opf` - Package document with metadata
- `OEBPS/content/nav.xhtml` - Navigation document
- `OEBPS/content/cover.xhtml` - Cover page
- `OEBPS/content/title-page.xhtml` - Title page
- `OEBPS/content/chapter-XX.xhtml` - Chapter files
- `OEBPS/styles/main.css` - Styling
- `OEBPS/images/cover.png` - Cover image

#### XHTML Template Structure
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
    <title>Chapter Title</title>
    <link rel="stylesheet" type="text/css" href="../styles/main.css"/>
    <meta charset="UTF-8"/>
</head>
<body>
    <section epub:type="chapter" class="chapter">
        <h1 class="chapter-title">Chapter Title</h1>
        <div class="chapter-content">
            <!-- Content with proper bold formatting -->
        </div>
    </section>
</body>
</html>
```

## 🔧 Implementation Guidelines

### 1. Markdown Processing Function

All EPUB generation scripts MUST implement this function:

```python
def convert_bold_text(self, text):
    """Convert **bold** markdown syntax to <strong> HTML tags"""
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    return text

def markdown_to_html(self, markdown_content, title):
    """Convert markdown to HTML with proper bold text handling"""
    if not markdown_content or not markdown_content.strip():
        return f"<h2>{self.clean_text(title)}</h2><p>Nội dung đang được cập nhật.</p>"
    
    # Clean the content first
    markdown_content = self.clean_text(markdown_content)
    
    lines = markdown_content.split('\n')
    html_paragraphs = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Convert headers (apply bold conversion to header content too)
        if line.startswith('# '):
            header_content = self.convert_bold_text(line[2:].strip())
            html_paragraphs.append(f'<h2>{header_content}</h2>')
        elif line.startswith('## '):
            header_content = self.convert_bold_text(line[3:].strip())
            html_paragraphs.append(f'<h3>{header_content}</h3>')
        # ... continue for other header levels and content types
        else:
            if line:
                # Convert bold text in regular paragraphs
                paragraph_content = self.convert_bold_text(line)
                html_paragraphs.append(f'<p>{paragraph_content}</p>')
    
    return '\n'.join(html_paragraphs)
```

### 2. Quality Assurance Checklist

#### Pre-Generation Validation
- [ ] All source markdown files contain proper `**bold**` syntax
- [ ] Vietnamese characters are properly encoded (UTF-8)
- [ ] Chapter structure follows heading hierarchy
- [ ] Cover image exists and is properly sized

#### Post-Generation Validation
- [ ] No `**` characters remain in generated XHTML files
- [ ] All bold text is wrapped in `<strong>` tags
- [ ] CSS includes proper `strong` element styling
- [ ] EPUB passes epubcheck validation
- [ ] Navigation works correctly
- [ ] Content displays properly in EPUB readers

### 3. Testing Requirements

#### Bold Text Conversion Testing
Create test cases covering:
- Simple bold text: `**Text**` → `<strong>Text</strong>`
- Multiple bold sections in one line
- Bold text in headers
- Bold text with Vietnamese characters
- Mixed content with bold and regular text

#### EPUB Reader Testing
Test generated EPUB files in:
- Adobe Digital Editions
- Calibre
- Google Play Books
- Apple Books
- Amazon Kindle (if converting to MOBI)

## 📁 File Organization

### Script Location
- `generate-ai-entrepreneur-epub.py` - Main EPUB generation script for the AI Entrepreneur Guide (29 chapters)

### Documentation Files
- `EPUB-GENERATION-STANDARDS.md` - This document
- `08-publication/PUBLICATION-PROCESS.md` - Overall publication process
- `test-bold-conversion.py` - Bold conversion testing script

## 🚀 Usage Instructions

### 1. Generate EPUB with Bold Text Support
```bash
# Generate AI Entrepreneur Guide EPUB (29 chapters)
python generate-ai-entrepreneur-epub.py
```

### 2. Validate Bold Text Conversion
```bash
# Run bold conversion tests
python test-bold-conversion.py

# Run comprehensive EPUB quality verification
python verify-epub-quality.py
```

### 3. EPUB Validation
```bash
# Validate generated EPUB (requires epubcheck installation)
epubcheck ai-entrepreneur-guide-vietnamese.epub
```

## 📊 Quality Standards

### Content Quality
- **Bold Text**: 100% conversion rate from markdown to HTML
- **Vietnamese Support**: Full UTF-8 character support
- **Navigation**: Complete table of contents with all chapters
- **Metadata**: Complete publication information

### Technical Quality
- **EPUB 3.0 Compliance**: Full specification compliance
- **File Size**: Optimized for distribution
- **Compatibility**: Works across major EPUB readers
- **Accessibility**: Screen reader compatible

## 🔄 Version History

### Version 2.0 (August 2, 2025)
- Added comprehensive bold text handling requirements
- Updated markdown_to_html function specifications
- Added CSS styling requirements for bold text
- Included testing and validation procedures
- Added quality assurance checklist

### Version 1.0 (Previous)
- Initial EPUB generation process documentation
- Basic structure and metadata requirements

---

**Document Maintained By**: AI Development Team  
**Next Review Date**: September 2, 2025  
**Contact**: Update this document when EPUB generation processes change
