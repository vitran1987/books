#!/usr/bin/env python3
"""
EPUB Generator for "CẨM NANG DOANH NHÂN - HBR Handbook"
Converts Vietnamese text file to EPUB format
Based on the consolidated EPUB generator script
"""

import os
import zipfile
import shutil
import re
from pathlib import Path
from datetime import datetime
import uuid
import html

class HarvardHandbookEPUBGenerator:
    def __init__(self):
        self.source_file = Path("HBR Handbook - Cảm nang quản trị toàn tập từ Harvard - Cẩm nang doanh nhân.txt")
        self.output_dir = Path("./epub-temp-harvard-handbook")
        self.epub_file = Path("./cam-nang-quan-tri-harvard.epub")
        self.cover_image = Path("./harvard_handbook_cover.png")  # Optional cover image
        self.book_id = f"harvard-handbook-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        # Chapter structure for the book
        self.chapters = [
            {
                "title": "Lời giới thiệu",
                "keywords": ["Lời giới thiệu", "Để khởi nghiệp thành công và bền vững hơn"]
            },
            {
                "title": "Phần I: Chuẩn bị hành trang",
                "keywords": ["PHẦN I: CHUẨN BỊ HÀNH TRANG", "CHUẨN BỊ HÀNH TRANG"]
            },
            {
                "title": "01 Liệu bạn có phù hợp với khởi sự kinh doanh?",
                "keywords": ["01   Liệu bạn có phù hợp với khởi sự kinh doanh?", "Liệu bạn có phù hợp với khởi sự kinh doanh?"]
            },
            {
                "title": "Phần II: Xác định hình hài doanh nghiệp",
                "keywords": ["PHẦN II: XÁC ĐỊNH HÌNH HÀI DOANH NGHIỆP", "XÁC ĐỊNH HÌNH HÀI DOANH NGHIỆP"]
            },
            {
                "title": "02 Tạo dựng cơ hội",
                "keywords": ["02 Tạo dựng cơ hội", "Tạo dựng cơ hội"]
            },
            {
                "title": "03 Xây dựng mô hình và chiến lược kinh doanh",
                "keywords": ["03   Xây dựng mô hình và chiến lược kinh doanh", "Xây dựng mô hình và chiến lược kinh doanh"]
            },
            {
                "title": "04 Tổ chức công ty của bạn",
                "keywords": ["04 Tổ chức công ty của bạn", "Tổ chức công ty của bạn"]
            },
            {
                "title": "05 Viết bản kế hoạch kinh doanh",
                "keywords": ["05 Viết bản kế hoạch kinh doanh", "Viết bản kế hoạch kinh doanh"]
            },
            {
                "title": "Phần III: Tài chính doanh nghiệp",
                "keywords": ["PHẦN III: TÀI CHÍNH DOANH NGHIỆP", "TÀI CHÍNH DOANH NGHIỆP"]
            },
            {
                "title": "06 Gọi vốn giai đoạn khởi nghiệp",
                "keywords": ["06 Gọi vốn giai đoạn khởi nghiệp", "Gọi vốn giai đoạn khởi nghiệp"]
            },
            {
                "title": "07 Gọi vốn giai đoạn tăng trưởng",
                "keywords": ["07 Gọi vốn giai đoạn tăng trưởng", "Gọi vốn giai đoạn tăng trưởng"]
            },
            {
                "title": "08 Đầu tư thiên thần và đầu tư mạo hiểm",
                "keywords": ["08 Đầu tư thiên thần và đầu tư mạo hiểm", "Đầu tư thiên thần và đầu tư mạo hiểm"]
            },
            {
                "title": "09 Trở thành công ty đại chúng",
                "keywords": ["09 Trở thành công ty đại chúng", "Trở thành công ty đại chúng"]
            },
            {
                "title": "Phần IV: Mở rộng quy mô",
                "keywords": ["PHẦN IV: MỞ RỘNG QUY MÔ", "MỞ RỘNG QUY MÔ"]
            },
            {
                "title": "10 Duy trì tăng trưởng doanh nghiệp",
                "keywords": ["10 Duy trì tăng trưởng doanh nghiệp", "Duy trì tăng trưởng doanh nghiệp"]
            },
            {
                "title": "11 Lãnh đạo một doanh nghiệp đang phát triển",
                "keywords": ["11 Lãnh đạo một doanh nghiệp đang phát triển", "Lãnh đạo một doanh nghiệp đang phát triển"]
            },
            {
                "title": "12 Giữ vững tinh thần khởi nghiệp",
                "keywords": ["12 Giữ vững tinh thần khởi nghiệp", "Giữ vững tinh thần khởi nghiệp"]
            },
            {
                "title": "Phần V: Hướng đến tương lai",
                "keywords": ["PHẦN V: HƯỚNG ĐẾN TƯƠNG LAI", "HƯỚNG ĐẾN TƯƠNG LAI"]
            },
            {
                "title": "13 Thời gian gặt hái thành quả",
                "keywords": ["13 Thời gian gặt hái thành quả", "Thời gian gặt hái thành quả"]
            },
            {
                "title": "Phụ lục A: Hiểu báo cáo tài chính",
                "keywords": ["Phụ lục A: Hiểu báo cáo tài chính", "Hiểu báo cáo tài chính"]
            },
            {
                "title": "Phụ lục B: Báo cáo hòa vốn",
                "keywords": ["Phụ lục B: Báo cáo hòa vốn", "Báo cáo hòa vốn"]
            },
            {
                "title": "Phụ lục C: Định giá: Doanh nghiệp của bạn thực sự có giá trị bao nhiêu?",
                "keywords": ["Phụ lục C: Định giá: Doanh nghiệp của bạn thực sự có giá trị bao nhiêu?", "Định giá: Doanh nghiệp của bạn thực sự có giá trị bao nhiêu?"]
            },
            {
                "title": "Phụ lục D: Bán các cổ phiếu hạn chế và kiểm soát: Quy định 144 của SEC",
                "keywords": ["Phụ lục D: Bán các cổ phiếu hạn chế và kiểm soát: Quy định 144 của SEC", "Bán các cổ phiếu hạn chế và kiểm soát: Quy định 144 của SEC"]
            },
            {
                "title": "Thuật ngữ",
                "keywords": ["Thuật ngữ", "Lời giới thiệu W"]
            }
        ]

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

    def read_source_file(self):
        """Read and return the content of the source text file"""
        try:
            with open(self.source_file, "r", encoding="utf-8") as f:
                content = f.read()
            print(f"✅ Source file read successfully ({len(content)} characters)")
            return content
        except Exception as e:
            print(f"❌ Error reading source file: {e}")
            return None

    def split_into_chapters(self, content):
        """Split the content into chapters based on keywords"""
        chapters_content = []
        
        # Add introduction with book title
        intro_chapter = {
            "title": "Trang bìa và thông tin sách",
            "content": f"""<h1>CẨM NANG DOANH NHÂN</h1>
<h2>HBR Handbook - Cảm nang quản trị toàn tập từ Harvard</h2>
<h3>Tác giả: HARVARD BUSINESS REVIEW</h3>
<p><em>Cẩm nang dành cho doanh nhân khởi nghiệp</em></p>
<hr/>
<p>Cuốn sách này là cẩm nang toàn tập về khởi nghiệp từ Harvard Business Review, cung cấp kiến thức và công cụ cần thiết để thành lập và phát triển doanh nghiệp thành công.</p>"""
        }
        chapters_content.append(intro_chapter)
        
        # Split content by chapters
        for i, chapter in enumerate(self.chapters):
            chapter_content = self.extract_chapter_content(content, i, chapter)
            if chapter_content:
                chapters_content.append({
                    "title": chapter["title"],
                    "content": chapter_content
                })
        
        return chapters_content

    def extract_chapter_content(self, content, chapter_index, chapter_info):
        """Extract content for a specific chapter"""
        try:
            # Find the start of current chapter
            start_pos = -1
            for keyword in chapter_info["keywords"]:
                pos = content.find(keyword)
                if pos != -1:
                    start_pos = pos
                    break
            
            if start_pos == -1:
                print(f"⚠️ Chapter '{chapter_info['title']}' not found")
                return None
            
            # Find the start of next chapter
            end_pos = len(content)
            if chapter_index + 1 < len(self.chapters):
                next_chapter = self.chapters[chapter_index + 1]
                for keyword in next_chapter["keywords"]:
                    pos = content.find(keyword, start_pos + 100)
                    if pos != -1:
                        end_pos = pos
                        break
            
            chapter_text = content[start_pos:end_pos].strip()
            return self.text_to_html(chapter_text)
            
        except Exception as e:
            print(f"❌ Error extracting chapter '{chapter_info['title']}': {e}")
            return None

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

    def text_to_html(self, text):
        """Convert plain text to HTML with basic formatting"""
        if not text or not text.strip():
            return "<p>Nội dung đang được cập nhật.</p>"
        
        # Clean the text first
        text = self.clean_text(text)
        
        # Split into paragraphs
        paragraphs = text.split('\n\n')
        html_content = []
        
        for paragraph in paragraphs:
            paragraph = paragraph.strip()
            if not paragraph:
                continue
            
            # Check if it's a title (all caps, shorter than 100 chars)
            if (paragraph.isupper() and len(paragraph) < 100 and 
                not any(char.isdigit() for char in paragraph[:20])):
                html_content.append(f'<h2>{paragraph}</h2>')
            # Check if it's a subtitle or section header
            elif paragraph.startswith(('Chương', 'Phần', 'CHƯƠNG', 'PHẦN')) or len(paragraph) < 80:
                # Split by sentences for better readability
                sentences = re.split(r'(?<=[.!?])\s+', paragraph)
                if len(sentences) == 1 and len(paragraph) < 80:
                    html_content.append(f'<h3>{paragraph}</h3>')
                else:
                    html_content.append(f'<p>{paragraph}</p>')
            else:
                # Regular paragraph - split long paragraphs for better readability
                if len(paragraph) > 1000:
                    sentences = re.split(r'(?<=[.!?])\s+', paragraph)
                    current_para = ""
                    for sentence in sentences:
                        if len(current_para + sentence) > 500 and current_para:
                            html_content.append(f'<p>{current_para.strip()}</p>')
                            current_para = sentence + " "
                        else:
                            current_para += sentence + " "
                    if current_para.strip():
                        html_content.append(f'<p>{current_para.strip()}</p>')
                else:
                    html_content.append(f'<p>{paragraph}</p>')
        
        return '\n'.join(html_content) if html_content else "<p>Nội dung đang được cập nhật.</p>"

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
        
        print("✅ container.xml created")

    def copy_cover_image(self):
        """Copy cover image if it exists"""
        print("Checking for cover image...")
        if self.cover_image.exists():
            shutil.copy2(self.cover_image, self.output_dir / "OEBPS" / "images" / "cover.png")
            print("✅ Cover image copied")
            return True
        else:
            print("⚠️ Cover image not found, creating placeholder")
            return False

    def create_front_matter(self, has_cover=False):
        """Create front matter files"""
        print("Creating front matter...")

        # Cover page
        if has_cover:
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
        <img src="../images/cover.png" alt="Miễn Phí - Book Cover"/>
    </div>
</body>
</html>'''
        else:
            cover_html = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
    <title>Cover</title>
    <link rel="stylesheet" type="text/css" href="../styles/main.css"/>
    <meta charset="UTF-8"/>
</head>
<body class="cover">
    <div class="cover-text">
        <h1>CẨM NANG DOANH NHÂN</h1>
        <h2>HBR Handbook - Cảm nang quản trị toàn tập từ Harvard</h2>
        <h3>HARVARD BUSINESS REVIEW</h3>
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
    <h1>CẨM NANG DOANH NHÂN</h1>
    <p class="subtitle">HBR Handbook - Cảm nang quản trị toàn tập từ Harvard</p>
    <div class="publication-info">
        <p><strong>Tác giả:</strong> Harvard Business Review</p>
        <p><strong>Năm xuất bản:</strong> 2025</p>
        <p><strong>Ngôn ngữ:</strong> Tiếng Việt</p>
        <p><strong>Thể loại:</strong> Kinh tế - Kinh doanh - Khởi nghiệp</p>
    </div>
</body>
</html>'''

        with open(self.output_dir / "OEBPS" / "content" / "title-page.xhtml", "w", encoding="utf-8") as f:
            f.write(title_html)

        print("✅ Front matter created")

    def copy_css(self):
        """Copy CSS file"""
        print("Creating CSS file...")

        css_content = '''/* EPUB CSS Styles for Miễn Phí Book */
body {
    font-family: "Times New Roman", serif;
    line-height: 1.6;
    margin: 0;
    padding: 1em;
    color: #333;
    text-align: justify;
}

h1, h2, h3, h4, h5, h6 {
    color: #2c3e50;
    margin-top: 1.5em;
    margin-bottom: 0.5em;
    line-height: 1.2;
    text-align: left;
}

h1 { 
    font-size: 2em; 
    border-bottom: 3px solid #3498db;
    padding-bottom: 0.3em;
}
h2 { 
    font-size: 1.5em;
    border-bottom: 1px solid #bdc3c7;
    padding-bottom: 0.2em;
}
h3 { font-size: 1.3em; }
h4 { font-size: 1.1em; }

p {
    margin: 1em 0;
    text-indent: 1.5em;
}

p:first-child {
    text-indent: 0;
}

.cover {
    text-align: center;
    padding: 2em 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    min-height: 80vh;
}

.cover-image img {
    max-width: 100%;
    height: auto;
}

.cover-text h1 {
    font-size: 3em;
    color: #e74c3c;
    margin-bottom: 0.5em;
    border: none;
}

.cover-text h2 {
    font-size: 1.8em;
    color: #34495e;
    margin-bottom: 1em;
    border: none;
}

.cover-text h3 {
    font-size: 1.5em;
    color: #7f8c8d;
    font-style: italic;
}

.title-page {
    text-align: center;
    padding: 2em 1em;
}

.title-page h1 {
    font-size: 2.5em;
    color: #e74c3c;
    margin-bottom: 0.5em;
    border: none;
}

.subtitle {
    font-size: 1.2em;
    color: #7f8c8d;
    font-style: italic;
    margin-bottom: 2em;
    text-indent: 0;
}

.publication-info {
    text-align: left;
    max-width: 600px;
    margin: 2em auto 0;
    background-color: #f8f9fa;
    padding: 1.5em;
    border-radius: 8px;
}

.publication-info p {
    margin: 0.5em 0;
    text-indent: 0;
}

.chapter-title {
    border-bottom: 2px solid #3498db;
    padding-bottom: 0.5em;
    margin-bottom: 1em;
    color: #2c3e50;
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

em {
    font-style: italic;
    color: #7f8c8d;
}

strong {
    font-weight: bold;
    color: #2c3e50;
}

/* Navigation styles */
nav ol, nav ul {
    list-style-type: none;
    padding-left: 0;
}

nav li {
    margin: 0.8em 0;
    padding: 0.5em;
    background-color: #f8f9fa;
    border-left: 4px solid #3498db;
}

nav a {
    text-decoration: none;
    color: #2c3e50;
    font-weight: 500;
}

nav a:hover {
    color: #3498db;
}

.toc-title {
    text-align: center;
    margin-bottom: 2em;
    color: #2c3e50;
}

/* Responsive design */
@media screen and (max-width: 600px) {
    body {
        padding: 0.5em;
    }
    
    .cover-text h1 {
        font-size: 2em;
    }
    
    .cover-text h2 {
        font-size: 1.3em;
    }
}'''

        with open(self.output_dir / "OEBPS" / "styles" / "main.css", "w", encoding="utf-8") as f:
            f.write(css_content)

        print("✅ CSS file created")

    def create_navigation_document(self, chapters_content):
        """Create navigation document"""
        print("Creating navigation document...")

        nav_links = []
        
        # Add front matter links
        nav_links.append('            <li><a href="cover.xhtml">Bìa sách</a></li>')
        nav_links.append('            <li><a href="title-page.xhtml">Trang tiêu đề</a></li>')
        
        # Add chapter links
        for i, chapter in enumerate(chapters_content):
            chapter_file = f"chapter-{i+1:02d}.xhtml"
            nav_links.append(f'            <li><a href="{chapter_file}">{self.clean_text(chapter["title"])}</a></li>')

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
        <h1 class="toc-title">Mục lục - Cẩm nang doanh nhân</h1>
        <ol>
{chr(10).join(nav_links)}
        </ol>
    </nav>
</body>
</html>'''

        with open(self.output_dir / "OEBPS" / "content" / "nav.xhtml", "w", encoding="utf-8") as f:
            f.write(nav_html)

        print("✅ Navigation document created")

    def create_chapters(self, chapters_content):
        """Create XHTML files for each chapter"""
        print("Creating chapter files...")
        
        for i, chapter in enumerate(chapters_content):
            chapter_file = f"chapter-{i+1:02d}.xhtml"
            xhtml_content = self.create_xhtml_template(chapter["title"], chapter["content"])
            
            output_file = self.output_dir / "OEBPS" / "content" / chapter_file
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(xhtml_content)
            
            print(f"  ✅ Created {chapter_file}: {chapter['title']}")

    def create_content_opf(self, chapters_content, has_cover=False):
        """Create content.opf file"""
        print("Creating content.opf...")

        # Create manifest items
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

        # Add chapters
        for i, chapter in enumerate(chapters_content):
            chapter_id = f"chapter-{i+1:02d}"
            chapter_file = f"chapter-{i+1:02d}.xhtml"
            manifest_items.append(f'<item id="{chapter_id}" href="content/{chapter_file}" media-type="application/xhtml+xml"/>')
            spine_items.append(f'<itemref idref="{chapter_id}"/>')

        # Add resources
        if has_cover:
            manifest_items.append('<item id="cover-image" href="images/cover.png" media-type="image/png" properties="cover-image"/>')
        manifest_items.append('<item id="css" href="styles/main.css" media-type="text/css"/>')

        # Metadata
        title = "Cẩm nang doanh nhân - HBR Handbook - Cảm nang quản trị toàn tập từ Harvard"
        description = "Cuốn sách cẩm nang toàn tập về khởi nghiệp từ Harvard Business Review, cung cấp kiến thức và công cụ cần thiết để thành lập và phát triển doanh nghiệp thành công."

        content_opf = f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="bookid" version="3.0">
    <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
        <dc:identifier id="bookid">{self.book_id}</dc:identifier>
        <dc:title>{title}</dc:title>
        <dc:creator>Harvard Business Review</dc:creator>
        <dc:language>vi</dc:language>
        <dc:date>{datetime.now().strftime('%Y-%m-%d')}</dc:date>
        <dc:publisher>AI Book Converter</dc:publisher>
        <dc:subject>Khởi nghiệp</dc:subject>
        <dc:subject>Kinh doanh</dc:subject>
        <dc:subject>Quản trị</dc:subject>
        <dc:description>{description}</dc:description>
        <dc:rights>© Harvard Business Review</dc:rights>
        <meta property="dcterms:modified">{datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')}</meta>
        {f'<meta name="cover" content="cover-image"/>' if has_cover else ''}
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
        print("🚀 Starting EPUB generation for 'Cẩm nang doanh nhân' book...")
        print("📖 Source: Vietnamese text file")
        print("=" * 70)

        try:
            # Read source file
            content = self.read_source_file()
            if not content:
                raise Exception("Failed to read source file")

            # Setup directories
            self.setup_directories()
            
            # Create basic files
            self.create_mimetype()
            self.create_container_xml()
            
            # Check for cover image
            has_cover = self.copy_cover_image()
            
            # Split content into chapters
            chapters_content = self.split_into_chapters(content)
            print(f"📚 Created {len(chapters_content)} chapters")
            
            # Create all files
            self.create_front_matter(has_cover)
            self.copy_css()
            self.create_chapters(chapters_content)
            self.create_navigation_document(chapters_content)
            self.create_content_opf(chapters_content, has_cover)
            
            # Generate final EPUB
            self.create_epub_zip()
            self.cleanup()

            print("=" * 70)
            print("🎉 EPUB generation completed successfully!")
            print(f"📚 Output file: {self.epub_file}")
            print(f"📊 Chapters: {len(chapters_content)}")
            print("✅ Ready for reading")

        except Exception as e:
            print(f"❌ Error during EPUB generation: {e}")
            raise

def main():
    generator = HarvardHandbookEPUBGenerator()
    generator.generate()

if __name__ == "__main__":
    main()