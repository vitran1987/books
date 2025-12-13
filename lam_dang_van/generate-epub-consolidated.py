#!/usr/bin/env python3
"""
EPUB Generator - Consolidated Version
Creates EPUB with consolidated chapters to match working EPUB structure (9 chapters max)
Based on successful ai-code-assistance-tools-vietnamese.epub structure
"""

import os
import zipfile
import shutil
import re
from pathlib import Path
from datetime import datetime
import uuid
import html

class EPUBGeneratorConsolidated:
    def __init__(self):
        self.base_story_dir = Path("Sach_101_Cau_Chuyen_Lam_Van/04_Cau_Chuyen")
        self.output_dir = Path("./epub-temp-consolidated")
        self.epub_file = Path("./101-cau-chuyen-lam-van.epub")
        self.cover_image = Path("./lam_dang_van_book_cover.png")
        self.book_id = f"101-cau-chuyen-lam-van-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        # Consolidated chapter structure for 101 Câu Chuyện Lam Vân
        self.consolidated_chapters = [
            {
                "file": "chapter-01.xhtml",
                "title": "Phần 1: Những Ngày Đầu (Câu chuyện 1-20)",
                "sections": [
                    ("Phan_1_Cau_Chuyen_01_20", "*.md"),
                ]
            },
            {
                "file": "chapter-02.xhtml",
                "title": "Phần 2: Học Cách Hiểu Biết (Câu chuyện 21-40)",
                "sections": [
                    ("Phan_2_Cau_Chuyen_21_40", "*.md"),
                ]
            },
            {
                "file": "chapter-03.xhtml",
                "title": "Phần 3: Chia Sẻ và Quan Tâm (Câu chuyện 41-60)",
                "sections": [
                    ("Phan_3_Cau_Chuyen_41_60", "*.md"),
                ]
            },
            {
                "file": "chapter-04.xhtml",
                "title": "Phần 4: Yêu Thương và Bảo Vệ (Câu chuyện 61-80)",
                "sections": [
                    ("Phan_4_Cau_Chuyen_61_80", "*.md"),
                ]
            },
            {
                "file": "chapter-05.xhtml",
                "title": "Phần 5: Trưởng Thành và Hoàn Thiện (Câu chuyện 81-101)",
                "sections": [
                    ("Phan_5_Cau_Chuyen_81_101", "*.md"),
                ]
            }
        ]

        # Add appendix for story collection
        self.appendix = {
            "file": "appendix-a.xhtml",
            "title": "Phụ lục A: Hướng dẫn Đọc và Thông điệp",
            "sections": [
                # Will contain reading guide and key messages
            ]
        }

    def setup_directories(self):
        """Set up EPUB directory structure"""
        print("Setting up EPUB directory structure...")
        
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        
        self.output_dir.mkdir()
        (self.output_dir / "META-INF").mkdir()
        (self.output_dir / "OEBPS").mkdir()
        (self.output_dir / "OEBPS" / "content").mkdir()
        (self.output_dir / "OEBPS" / "styles").mkdir()
        (self.output_dir / "OEBPS" / "images").mkdir()
        
        print("✅ Directory structure created")

    def create_mimetype(self):
        """Create mimetype file"""
        print("Creating mimetype file...")
        with open(self.output_dir / "mimetype", "w", encoding="utf-8", newline='') as f:
            f.write("application/epub+zip")
        print("✅ mimetype created")

    def create_container_xml(self):
        """Create container.xml"""
        print("Creating container.xml...")
        
        container_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
    <rootfiles>
        <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
    </rootfiles>
</container>'''
        
        with open(self.output_dir / "META-INF" / "container.xml", "w", encoding="utf-8") as f:
            f.write(container_xml)
        
        # Create display options
        display_options = '''<?xml version="1.0" encoding="UTF-8"?>
<display_options>
    <platform name="*">
        <option name="specified-fonts">true</option>
        <option name="interactive">false</option>
        <option name="fixed-layout">false</option>
        <option name="open-to-spread">false</option>
        <option name="orientation-lock">none</option>
    </platform>
</display_options>'''
        
        with open(self.output_dir / "META-INF" / "com.apple.ibooks.display-options.xml", "w", encoding="utf-8") as f:
            f.write(display_options)
        
        print("✅ container.xml and display options created")

    def copy_cover_image(self):
        """Copy cover image"""
        print("Copying cover image...")
        if self.cover_image.exists():
            shutil.copy2(self.cover_image, self.output_dir / "OEBPS" / "images" / "cover.png")
            print("✅ Cover image copied")
        else:
            print("⚠️ Cover image not found")

    def clean_text(self, text):
        """Clean and escape text for XHTML"""
        if not text:
            return ""
        
        # Remove any null bytes or control characters
        text = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', text)
        
        # Escape HTML entities
        text = html.escape(text, quote=False)
        
        # Fix common encoding issues
        text = text.replace('â€™', "'")
        text = text.replace('â€œ', '"')
        text = text.replace('â€', '"')
        text = text.replace('â€"', '–')
        text = text.replace('â€"', '—')
        
        return text

    def markdown_to_html(self, markdown_content, title):
        """Convert markdown to HTML"""
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
                
            # Convert headers
            if line.startswith('# '):
                html_paragraphs.append(f'<h2>{line[2:].strip()}</h2>')
            elif line.startswith('## '):
                html_paragraphs.append(f'<h3>{line[3:].strip()}</h3>')
            elif line.startswith('### '):
                html_paragraphs.append(f'<h4>{line[4:].strip()}</h4>')
            elif line.startswith('#### '):
                html_paragraphs.append(f'<h5>{line[5:].strip()}</h5>')
            elif line.startswith('- ') or line.startswith('* '):
                html_paragraphs.append(f'<p>• {line[2:].strip()}</p>')
            elif line.startswith('1. ') or re.match(r'^\d+\. ', line):
                content = re.sub(r'^\d+\. ', '', line)
                html_paragraphs.append(f'<p>1. {content.strip()}</p>')
            else:
                if line:
                    html_paragraphs.append(f'<p>{line}</p>')
        
        if not html_paragraphs:
            return f"<h2>{self.clean_text(title)}</h2><p>Nội dung đang được cập nhật.</p>"
        
        return '\n'.join(html_paragraphs)

    def create_xhtml_template(self, title, content):
        """Create XHTML template"""
        clean_title = self.clean_text(title)
        
        return f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
    <title>{clean_title}</title>
    <link rel="stylesheet" type="text/css" href="../styles/main.css"/>
    <meta charset="UTF-8"/>
</head>
<body>
    <section epub:type="chapter" class="chapter">
        <h1 class="chapter-title">{clean_title}</h1>
        <div class="chapter-content">
            {content}
        </div>
    </section>
</body>
</html>'''

    def convert_consolidated_chapters(self):
        """Convert consolidated chapters to XHTML"""
        print("Converting consolidated chapters to XHTML...")
        
        for chapter_info in self.consolidated_chapters:
            chapter_file = chapter_info["file"]
            chapter_title = chapter_info["title"]
            sections = chapter_info["sections"]
            
            print(f"\n📚 Processing {chapter_title}...")
            
            # Combine all sections into one chapter
            combined_content = []
            
            for section_key, md_pattern in sections:
                section_dir = self.base_story_dir / section_key

                if section_dir.exists():
                    # Get all markdown files in the section directory
                    md_files = sorted(section_dir.glob("*.md"))

                    for source_file in md_files:
                        print(f"  Adding {source_file.name}...")
                        try:
                            with open(source_file, "r", encoding="utf-8") as f:
                                markdown_content = f.read()

                            # Extract story title from markdown content
                            lines = markdown_content.split('\n')
                            story_title = "Câu chuyện"
                            for line in lines:
                                if line.startswith('# '):
                                    story_title = line[2:].strip()
                                    break

                            combined_content.append(f"<hr/><h2>{story_title}</h2>")
                            combined_content.append(self.markdown_to_html(markdown_content, story_title))

                        except Exception as e:
                            print(f"  ❌ Error processing {source_file.name}: {str(e)}")
                            combined_content.append(f"<p>Error loading {source_file.name}: {str(e)}</p>")
                else:
                    print(f"  ⚠️ Section directory {section_key} not found")
            
            # Create default content if no sections found
            if not combined_content:
                combined_content = [
                    "<h2>Nội dung đang được cập nhật</h2>",
                    "<p>Phần này sẽ chứa các câu chuyện thuộc giai đoạn tương ứng.</p>"
                ]
            
            # Create XHTML file
            html_content = '\n'.join(combined_content) if combined_content else f"<p>Nội dung đang được cập nhật.</p>"
            xhtml_content = self.create_xhtml_template(chapter_title, html_content)
            
            output_file = self.output_dir / "OEBPS" / "content" / chapter_file
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(xhtml_content)
            
            print(f"  ✅ {chapter_file} created")

    def convert_appendix(self):
        """Convert appendix for story collection"""
        print("\n📚 Processing Appendix...")

        # Create reading guide content
        appendix_content = [
            "<h2>Hướng dẫn Đọc</h2>",
            "<p>Cuốn sách '101 Câu Chuyện Lam Vân' được chia thành 5 phần, mỗi phần thể hiện một giai đoạn phát triển của nhân vật chính:</p>",
            "<ul>",
            "<li><strong>Phần 1 (Câu chuyện 1-20):</strong> Những ngày đầu - Giai đoạn ganh ghét và chối bỏ</li>",
            "<li><strong>Phần 2 (Câu chuyện 21-40):</strong> Học cách hiểu biết - Giai đoạn nghi ngờ và xây dựng</li>",
            "<li><strong>Phần 3 (Câu chuyện 41-60):</strong> Chia sẻ và quan tâm - Giai đoạn hiểu biết và thay đổi</li>",
            "<li><strong>Phần 4 (Câu chuyện 61-80):</strong> Yêu thương và bảo vệ - Giai đoạn yêu thương và bảo vệ</li>",
            "<li><strong>Phần 5 (Câu chuyện 81-101):</strong> Trưởng thành và hoàn thiện - Giai đoạn trưởng thành và hoàn thiện</li>",
            "</ul>",
            "<h2>Thông điệp Chính</h2>",
            "<p>Tình yêu thương gia đình là giá trị cốt lõi nhất trong cuộc sống. Qua hành trình của Lam, chúng ta học được rằng:</p>",
            "<ul>",
            "<li>Mỗi người đều có thể thay đổi và trở nên tốt hơn</li>",
            "<li>Tình yêu thương cần được thể hiện qua hành động cụ thể</li>",
            "<li>Chia sẻ và quan tâm làm cho tình yêu thương trở nên sâu sắc hơn</li>",
            "<li>Bảo vệ và chăm sóc người thân là trách nhiệm của mỗi người</li>",
            "<li>Hoàn thiện bản thân để có thể yêu thương và giúp đỡ người khác tốt hơn</li>",
            "</ul>"
        ]

        # Create appendix XHTML file
        html_content = '\n'.join(appendix_content)
        xhtml_content = self.create_xhtml_template(self.appendix["title"], html_content)

        output_file = self.output_dir / "OEBPS" / "content" / self.appendix["file"]
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(xhtml_content)

        print(f"  ✅ {self.appendix['file']} created")

    def create_front_matter(self):
        """Create front matter files"""
        print("Creating front matter...")

        # Cover page
        cover_html = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
    <title>Cover</title>
    <link rel="stylesheet" type="text/css" href="../styles/main.css"/>
    <meta charset="UTF-8"/>
</head>
<body class="cover">
    <div class="cover-image">
        <img src="../images/cover.png" alt="AI và Tương Lai Lập Trình - Book Cover"/>
    </div>
</body>
</html>'''

        with open(self.output_dir / "OEBPS" / "content" / "cover.xhtml", "w", encoding="utf-8") as f:
            f.write(cover_html)

        # Title page
        title_html = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
    <title>Title Page</title>
    <link rel="stylesheet" type="text/css" href="../styles/main.css"/>
    <meta charset="UTF-8"/>
</head>
<body class="title-page">
    <h1>101 Câu Chuyện Lam Vân</h1>
    <p class="subtitle">Tuyển tập câu chuyện về tình yêu thương gia đình</p>
    <p class="author">Tác giả: Bạn Giỏi Research Lab</p>
    <div class="publication-info">
        <p><strong>Tác giả:</strong> Robot của Ba Vi</p>
        <p><strong>Năm xuất bản:</strong> 2025</p>
        <p><strong>Ngôn ngữ:</strong> Tiếng Việt</p>
    </div>
</body>
</html>'''

        with open(self.output_dir / "OEBPS" / "content" / "title-page.xhtml", "w", encoding="utf-8") as f:
            f.write(title_html)

        print("✅ Front matter created")

    def copy_css(self):
        """Copy CSS file"""
        print("Copying CSS file...")

        css_content = '''/* EPUB CSS Styles */
body {
    font-family: "Times New Roman", serif;
    line-height: 1.6;
    margin: 0;
    padding: 1em;
    color: #333;
}

h1, h2, h3, h4, h5, h6 {
    color: #2c3e50;
    margin-top: 1.5em;
    margin-bottom: 0.5em;
    line-height: 1.2;
}

h1 { font-size: 2em; }
h2 { font-size: 1.5em; }
h3 { font-size: 1.3em; }
h4 { font-size: 1.1em; }

p {
    margin: 1em 0;
    text-align: justify;
}

.cover {
    text-align: center;
    padding: 0;
}

.cover-image img {
    max-width: 100%;
    height: auto;
}

.title-page {
    text-align: center;
    padding: 2em 1em;
}

.title-page h1 {
    font-size: 2.5em;
    color: #2c3e50;
    margin-bottom: 0.5em;
}

.subtitle {
    font-size: 1.2em;
    color: #7f8c8d;
    font-style: italic;    margin-bottom: 1em;
}

.author {
    font-size: 1.1em;
    color: #1a365d;
    font-weight: bold;    margin-bottom: 2em;
}

.publication-info {
    text-align: left;
    max-width: 600px;
    margin: 0 auto;
}

.chapter-title {
    border-bottom: 2px solid #3498db;
    padding-bottom: 0.5em;
    margin-bottom: 1em;
}

.chapter-content {
    max-width: 800px;
    margin: 0 auto;
}

hr {
    border: none;
    border-top: 2px solid #ecf0f1;
    margin: 2em 0;
}

/* Navigation styles */
nav ol, nav ul {
    list-style-type: none;
    padding-left: 0;
}

nav li {
    margin: 0.5em 0;
}

nav a {
    text-decoration: none;
    color: #2c3e50;
}

nav a:hover {
    color: #3498db;
}'''

        with open(self.output_dir / "OEBPS" / "styles" / "main.css", "w", encoding="utf-8") as f:
            f.write(css_content)

        print("✅ CSS file copied")

    def create_navigation_document(self):
        """Create navigation document - flat structure like working EPUB"""
        print("Creating navigation document...")

        nav_links = []
        for chapter_info in self.consolidated_chapters:
            chapter_file = chapter_info["file"]
            chapter_title = chapter_info["title"]
            nav_links.append(f'            <li><a href="{chapter_file}">{self.clean_text(chapter_title)}</a></li>')

        # Add appendix
        nav_links.append(f'            <li><a href="{self.appendix["file"]}">{self.clean_text(self.appendix["title"])}</a></li>')

        nav_html = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
    <title>Navigation</title>
    <link rel="stylesheet" type="text/css" href="../styles/main.css"/>
    <meta charset="UTF-8"/>
</head>
<body>
    <nav epub:type="toc" id="toc">
        <h1>Mục lục</h1>
        <ol>
{chr(10).join(nav_links)}
        </ol>
    </nav>
</body>
</html>'''

        with open(self.output_dir / "OEBPS" / "content" / "nav.xhtml", "w", encoding="utf-8") as f:
            f.write(nav_html)

        print("✅ Navigation document created")

    def create_content_opf(self):
        """Create content.opf file - matches working EPUB structure exactly"""
        print("Creating content.opf...")

        # Create manifest items in simple order like working EPUB
        manifest_items = [
            '<item id="nav" href="content/nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
            '<item id="cover" href="content/cover.xhtml" media-type="application/xhtml+xml"/>',
            '<item id="title-page" href="content/title-page.xhtml" media-type="application/xhtml+xml"/>',
        ]

        spine_items = [
            '<itemref idref="cover"/>',
            '<itemref idref="title-page"/>',
            '<itemref idref="nav"/>',
        ]

        # Add chapters in sequential order
        for i, chapter_info in enumerate(self.consolidated_chapters, 1):
            chapter_file = chapter_info["file"]
            chapter_id = f"chapter-{i:02d}"
            manifest_items.append(f'<item id="{chapter_id}" href="content/{chapter_file}" media-type="application/xhtml+xml"/>')
            spine_items.append(f'<itemref idref="{chapter_id}"/>')

        # Add appendix
        manifest_items.append(f'<item id="appendix-a" href="content/{self.appendix["file"]}" media-type="application/xhtml+xml"/>')
        spine_items.append('<itemref idref="appendix-a"/>')

        # Add resources
        manifest_items.extend([
            '<item id="cover-image" href="images/cover.png" media-type="image/png" properties="cover-image"/>',
            '<item id="css" href="styles/main.css" media-type="text/css"/>',
        ])

        # Metadata matching working EPUB
        title = "101 Câu Chuyện Lam Vân"
        description = "Tuyển tập 101 câu chuyện về tình yêu thương gia đình qua hành trình phát triển của nhân vật Lam từ ganh ghét đến yêu thương hoàn thiện"

        content_opf = f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="bookid" version="3.0">
    <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
        <dc:identifier id="bookid">{self.book_id}</dc:identifier>
        <dc:title>{title}</dc:title>
        <dc:creator>Bạn Giỏi Research Lab</dc:creator>
        <dc:language>vi</dc:language>
        <dc:date>{datetime.now().strftime('%Y-%m-%d')}</dc:date>
        <dc:publisher>Bạn Giỏi Research Lab</dc:publisher>
        <dc:subject>Văn học thiếu nhi</dc:subject>
        <dc:subject>Tình yêu thương gia đình</dc:subject>
        <dc:description>{description}</dc:description>
        <dc:rights>© 2025 Bạn Giỏi Research Lab</dc:rights>
        <meta property="dcterms:modified">{datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')}</meta>
        <meta name="cover" content="cover-image"/>
    </metadata>

    <manifest>
        {chr(10).join("        " + item for item in manifest_items)}
    </manifest>

    <spine>
        {chr(10).join("        " + item for item in spine_items)}
    </spine>

    <guide>
        <reference type="cover" title="Cover" href="content/cover.xhtml"/>
        <reference type="title-page" title="Title Page" href="content/title-page.xhtml"/>
        <reference type="toc" title="Table of Contents" href="content/nav.xhtml"/>
        <reference type="text" title="Start of Content" href="content/chapter-01.xhtml"/>
    </guide>
</package>'''

        with open(self.output_dir / "OEBPS" / "content.opf", "w", encoding="utf-8") as f:
            f.write(content_opf)

        print("✅ content.opf created")

    def create_epub_zip(self):
        """Create final EPUB ZIP file"""
        print("Creating EPUB ZIP file...")

        with zipfile.ZipFile(self.epub_file, 'w', zipfile.ZIP_DEFLATED) as epub_zip:
            # Add mimetype first (uncompressed)
            epub_zip.write(self.output_dir / "mimetype", "mimetype", compress_type=zipfile.ZIP_STORED)

            # Add META-INF files
            meta_inf_dir = self.output_dir / "META-INF"
            if meta_inf_dir.exists():
                for file_path in meta_inf_dir.rglob("*"):
                    if file_path.is_file():
                        arc_path = file_path.relative_to(self.output_dir)
                        epub_zip.write(file_path, arc_path, compress_type=zipfile.ZIP_DEFLATED)

            # Add OEBPS files
            oebps_dir = self.output_dir / "OEBPS"
            if oebps_dir.exists():
                # Add content.opf first
                content_opf_path = oebps_dir / "content.opf"
                if content_opf_path.exists():
                    epub_zip.write(content_opf_path, "OEBPS/content.opf", compress_type=zipfile.ZIP_DEFLATED)

                # Add all other OEBPS files
                for root, dirs, files in os.walk(oebps_dir):
                    for file in sorted(files):
                        if file != "content.opf":
                            file_path = Path(root) / file
                            arc_path = file_path.relative_to(self.output_dir)
                            epub_zip.write(file_path, arc_path, compress_type=zipfile.ZIP_DEFLATED)

        print("✅ EPUB ZIP file created")

    def cleanup(self):
        """Clean up temporary directory"""
        print("Cleaning up temporary files...")
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        print("✅ Cleanup completed")

    def generate(self):
        """Main generation process"""
        print("🚀 Starting 101 Câu Chuyện Lam Vân EPUB generation...")
        print("📊 Target: 5 chapters (5 phases of character development)")
        print("=" * 70)

        try:
            self.setup_directories()
            self.create_mimetype()
            self.create_container_xml()
            self.copy_cover_image()
            self.convert_consolidated_chapters()
            self.convert_appendix()
            self.create_front_matter()
            self.copy_css()
            self.create_navigation_document()
            self.create_content_opf()
            self.create_epub_zip()
            self.cleanup()

            print("=" * 70)
            print("🎉 101 Câu Chuyện Lam Vân EPUB generation completed!")
            print(f"📚 Output file: {self.epub_file}")
            print("📊 Structure: 5 chapters (5 phases of character development)")
            print("✅ Optimized for reading experience")
            print("🔄 Ready for distribution")

        except Exception as e:
            print(f"❌ Error during EPUB generation: {e}")
            raise

def main():
    generator = EPUBGeneratorConsolidated()
    generator.generate()

if __name__ == "__main__":
    main()
