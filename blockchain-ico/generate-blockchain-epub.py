#!/usr/bin/env python3
"""
Blockchain ICO & Token Economics EPUB Generator
Creates EPUB from Vietnamese content about ICO, blockchain fundraising, and token economics
Comprehensive guide covering ICO revolution, token types, and practical tokenomics design
Based on successful EPUB structure with proper metadata
"""

import os
import zipfile
import shutil
import re
from pathlib import Path
from datetime import datetime
import uuid
import html

class BlockchainICOEPUBGenerator:
    def __init__(self):
        self.base_chapter_dir = Path(".")
        self.output_dir = Path("./epub-temp-blockchain-ico")
        self.epub_file = Path("./blockchain-ico-token-economics.epub")
        self.cover_image = Path("./book_cover.png")
        self.book_id = f"blockchain-ico-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.has_cover_image = False  # Track if cover image exists
        
        # Chapter and section structure for Blockchain ICO book
        self.chapters = [
            {
                "num": 1, 
                "title": "ICO - Phát Hành Đồng Tiền Lần Đầu", 
                "dir": "chapter-01",
                "sections": [
                    {"file": "01-gioi-thieu-cuoc-cach-mang-ico.md", "title": "Giới Thiệu: Cuộc Cách Mạng ICO"},
                    {"file": "02-ico-va-cac-hinh-thuc-gay-quy-truyen-thong.md", "title": "ICO và Các Hình Thức Gây Quỹ Truyền Thống"},
                    {"file": "03-quy-trinh-to-chuc-mot-ico.md", "title": "Quy Trình Tổ Chức Một ICO"},
                    {"file": "04-cau-chuyen-thanh-cong-va-bai-hoc.md", "title": "Câu Chuyện Thành Công và Bài Học"},
                    {"file": "05-that-bai-va-lua-dao.md", "title": "Thất Bại và Lừa Đảo"},
                    {"file": "06-phap-ly-va-quy-dinh.md", "title": "Pháp Lý và Quy Định"},
                    {"file": "07-su-tien-hoa.md", "title": "Sự Tiến Hóa"},
                    {"file": "08-ket-luan.md", "title": "Kết Luận"}
                ]
            },
            {
                "num": 2, 
                "title": "Token Economics - Kinh Tế Token", 
                "dir": "chapter-02",
                "sections": [
                    {"file": "01-cac-loai-token-va-chuc-nang.md", "title": "Các Loại Token và Chức Năng"},
                    {"file": "02-thiet-ke-cung-token.md", "title": "Thiết Kế Cung Token"},
                    {"file": "03-phan-phoi-token.md", "title": "Phân Phối Token"},
                    {"file": "04-tao-dong-luc.md", "title": "Tạo Động Lực"},
                    {"file": "05-tich-luy-gia-tri.md", "title": "Tích Lũy Giá Trị"},
                    {"file": "06-nghien-cuu-dien-hinh.md", "title": "Nghiên Cứu Điển Hình"},
                    {"file": "07-ket-luan-chuong.md", "title": "Kết Luận Chương"}
                ]
            },
            {
                "num": 3,
                "title": "Sự Tiến Hóa Của Gây Quỹ Blockchain - Từ ICO Đến IEO",
                "dir": "chapter-03",
                "sections": [
                    {"file": "01-ieo-initial-exchange-offering.md", "title": "IEO - Initial Exchange Offering"},
                    {"file": "02-ido-initial-dex-offering.md", "title": "IDO - Initial DEX Offering"},
                    {"file": "03-launchpads-and-airdrops.md", "title": "Launchpads và Airdrops"}
                ]
            },
            {
                "num": 4,
                "title": "Pháp Lý Và Quy Định - Bài Học Từ SEC",
                "dir": "chapter-04",
                "sections": [
                    {"file": "01-howey-test-and-sec.md", "title": "Howey Test và SEC"},
                    {"file": "02-global-regulatory-landscape.md", "title": "Bối Cảnh Pháp Lý Toàn Cầu"},
                    {"file": "03-compliance-strategies.md", "title": "Chiến Lược Tuân Thủ"}
                ]
            },
            {
                "num": 5,
                "title": "DeFi - Tài Chính Phi Tập Trung",
                "dir": "chapter-05",
                "sections": [
                    {"file": "01-defi-protocol-fundamentals.md", "title": "Nguyên Lý Cơ Bản DeFi Protocol"},
                    {"file": "02-yield-farming-and-liquidity-mining.md", "title": "Yield Farming và Liquidity Mining"},
                    {"file": "03-defi-risks-and-security.md", "title": "Rủi Ro DeFi và Bảo Mật"}
                ]
            },
            {
                "num": 6,
                "title": "DAO - Tổ Chức Tự Trị Phi Tập Trung",
                "dir": "chapter-06",
                "sections": [
                    {"file": "01-dao-governance-fundamentals.md", "title": "Nguyên Lý Quản Trị DAO"},
                    {"file": "02-dao-case-studies-and-lessons.md", "title": "Nghiên Cứu Điển Hình DAO và Bài Học"}
                ]
            },
            {
                "num": 7,
                "title": "NFT và Metaverse - Kinh Tế Sở Hữu Kỹ Thuật Số",
                "dir": "chapter-07",
                "sections": [
                    {"file": "01-nft-fundamentals-and-mechanics.md", "title": "Nguyên Lý Cơ Bản và Cơ Chế NFT"},
                    {"file": "02-nft-boom-bust-and-lessons.md", "title": "Chu Kỳ Bùng Nổ - Sụp Đổ NFT và Bài Học"}
                ]
            },
            {
                "num": 8,
                "title": "Stablecoins - Đồng Tiền Ổn Định",
                "dir": "chapter-08",
                "sections": [
                    {"file": "01-stablecoins-and-terra-case-study.md", "title": "Stablecoins và Nghiên Cứu Điển Hình Terra"}
                ]
            },
            {
                "num": 9,
                "title": "RWA - Token Hóa Thế Giới Thực",
                "dir": "chapter-09",
                "sections": [
                    {"file": "01-rwa-tokenization.md", "title": "Token Hóa Tài Sản Thế Giới Thực"}
                ]
            },
            {
                "num": 10,
                "title": "Tương Lai - Từ Miễn Phí Đến Vô Hạn",
                "dir": "chapter-10",
                "sections": [
                    {"file": "01-tuong-lai-va-ket-luan.md", "title": "Tương Lai và Kết Luận"}
                ]
            },
            {
                "num": 11,
                "title": "Token Tự Trị Và Khung Pháp Lý",
                "dir": "chapter-11",
                "sections": [
                    {"file": "01-autonomous-tokens-and-legal-framework.md", "title": "Token Tự Trị và Khung Pháp Lý"}
                ]
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
        """Copy cover image"""
        print("Copying cover image...")
        if self.cover_image.exists():
            shutil.copy2(self.cover_image, self.output_dir / "OEBPS" / "images" / "cover.png")
            print("✅ Cover image copied")
            return True
        else:
            print("⚠️ Cover image not found - EPUB will be generated without cover image")
            return False

    def clean_text(self, text):
        """Clean and escape text for XHTML"""
        if not text:
            return ""
        
        # Remove any null bytes or control characters
        text = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', text)
        
        # Escape HTML entities
        text = html.escape(text, quote=False)
        
        return text

    def convert_bold_text(self, text):
        """Convert **bold** markdown syntax to <strong> HTML tags"""
        # Handle bold text with **text** syntax
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
            elif line.startswith('### '):
                header_content = self.convert_bold_text(line[4:].strip())
                html_paragraphs.append(f'<h4>{header_content}</h4>')
            elif line.startswith('#### '):
                header_content = self.convert_bold_text(line[5:].strip())
                html_paragraphs.append(f'<h5>{header_content}</h5>')
            elif line.startswith('- ') or line.startswith('* '):
                list_content = self.convert_bold_text(line[2:].strip())
                html_paragraphs.append(f'<p>• {list_content}</p>')
            elif line.startswith('1. ') or re.match(r'^\d+\. ', line):
                content = re.sub(r'^\d+\. ', '', line)
                list_content = self.convert_bold_text(content.strip())
                html_paragraphs.append(f'<p>1. {list_content}</p>')
            else:
                if line:
                    # Convert bold text in regular paragraphs
                    paragraph_content = self.convert_bold_text(line)
                    html_paragraphs.append(f'<p>{paragraph_content}</p>')

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

    def convert_chapters(self):
        """Convert all chapters with their sections to XHTML"""
        print("Converting chapters to XHTML...")

        section_counter = 0  # Global counter for all sections across chapters

        for chapter_info in self.chapters:
            chapter_num = chapter_info["num"]
            chapter_title = chapter_info["title"]
            chapter_dir = chapter_info["dir"]
            sections = chapter_info.get("sections", [])

            print(f"\n� Processing Chapter {chapter_num}: {chapter_title}...")

            # Process each section in the chapter
            for section_info in sections:
                section_counter += 1
                section_file = section_info["file"]
                section_title = section_info["title"]

                print(f"  📄 Processing Section {section_counter}: {section_title}...")

                # Build path to section file
                section_path = self.base_chapter_dir / chapter_dir / section_file

                # Read content
                content = ""
                if section_path.exists():
                    print(f"    Reading {section_file}...")
                    try:
                        with open(section_path, "r", encoding="utf-8") as f:
                            content = f.read()
                    except Exception as e:
                        print(f"    ❌ Error reading {section_file}: {str(e)}")
                        content = f"<p>Lỗi đọc file: {str(e)}</p>"
                else:
                    print(f"    ⚠️ Section file not found: {section_path}")
                    content = f"<p>Nội dung cho phần {section_title} đang được cập nhật.</p>"

                # Convert to HTML
                full_title = f"Chương {chapter_num}.{sections.index(section_info) + 1}: {section_title}"
                html_content = self.markdown_to_html(content, full_title)
                xhtml_content = self.create_xhtml_template(full_title, html_content)

                # Save XHTML file
                output_file = self.output_dir / "OEBPS" / "content" / f"section-{section_counter:03d}.xhtml"
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(xhtml_content)

                print(f"    ✅ section-{section_counter:03d}.xhtml created")

        print(f"\n✅ Total sections processed: {section_counter}")

    def create_front_matter(self):
        """Create front matter files"""
        print("Creating front matter...")

        # Cover page - only if cover image exists
        if self.has_cover_image:
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
        <img src="../images/cover.png" alt="Blockchain, ICO và Token Economics - Book Cover"/>
    </div>
</body>
</html>'''

            with open(self.output_dir / "OEBPS" / "content" / "cover.xhtml", "w", encoding="utf-8") as f:
                f.write(cover_html)
            print("  ✅ Cover page created")
        else:
            print("  ⚠️ Skipping cover page (no cover image)")

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
    <h1>Blockchain, ICO và Token Economics</h1>
    <p class="subtitle">Hướng Dẫn Toàn Diện Về Phát Hành Đồng Tiền Lần Đầu và Thiết Kế Kinh Tế Token</p>
    <div class="publication-info">
        <p><strong>Chủ đề:</strong> Blockchain, Cryptocurrency, ICO, Token Economics, DeFi, DAO, NFT</p>
        <p><strong>Năm xuất bản:</strong> 2025</p>
        <p><strong>Ngôn ngữ:</strong> Tiếng Việt</p>
        <p><strong>Số chương:</strong> 11 chương toàn diện</p>
        <p><strong>Phạm vi:</strong> Từ lịch sử ICO đến token hóa tài sản thực, tương lai blockchain và token tự trị</p>
        <p><strong>Nội dung:</strong> ICO, Token Economics, IEO/IDO, Pháp lý, DeFi, DAO, NFT, Stablecoins, RWA, Future, Autonomous Tokens</p>
    </div>
</body>
</html>'''

        with open(self.output_dir / "OEBPS" / "content" / "title-page.xhtml", "w", encoding="utf-8") as f:
            f.write(title_html)

        print("✅ Front matter created")

    def copy_css(self):
        """Copy CSS file"""
        print("Copying CSS file...")

        css_content = '''/* Blockchain ICO & Token Economics EPUB CSS Styles */
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

h1 { font-size: 2em; }
h2 { font-size: 1.5em; }
h3 { font-size: 1.3em; }
h4 { font-size: 1.1em; }

p {
    margin: 1em 0;
    text-align: justify;
}

/* Bold text styling */
strong {
    font-weight: bold;
    color: #1a365d;
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
    color: #1a365d;
    margin-bottom: 0.5em;
}

.subtitle {
    font-size: 1.2em;
    color: #2d3748;
    font-style: italic;
    margin-bottom: 2em;
}

.publication-info {
    text-align: left;
    max-width: 600px;
    margin: 0 auto;
}

.chapter-title {
    border-bottom: 2px solid #f7931a;
    padding-bottom: 0.5em;
    margin-bottom: 1em;
}

.chapter-content {
    max-width: 800px;
    margin: 0 auto;
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
    color: #1a365d;
}

nav a:hover {
    color: #f7931a;
}'''

        with open(self.output_dir / "OEBPS" / "styles" / "main.css", "w", encoding="utf-8") as f:
            f.write(css_content)

        print("✅ CSS file copied")

    def create_navigation_document(self):
        """Create navigation document"""
        print("Creating navigation document...")

        nav_links = []
        section_counter = 0

        for chapter_info in self.chapters:
            chapter_num = chapter_info["num"]
            chapter_title = chapter_info["title"]
            sections = chapter_info.get("sections", [])

            # Add all sections with flat structure (no nested ol)
            for idx, section_info in enumerate(sections):
                section_counter += 1
                section_title = section_info["title"]
                full_title = f"Chương {chapter_num}.{idx + 1}: {self.clean_text(section_title)}"
                nav_links.append(f'            <li><a href="section-{section_counter:03d}.xhtml">{full_title}</a></li>')

        nav_html = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
    <title>Mục lục</title>
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
        """Create content.opf file"""
        print("Creating content.opf...")

        # Create manifest items
        manifest_items = [
            '<item id="nav" href="content/nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
            '<item id="title-page" href="content/title-page.xhtml" media-type="application/xhtml+xml"/>',
        ]

        spine_items = [
            '<itemref idref="title-page"/>',
            '<itemref idref="nav"/>',
        ]

        # Add cover only if it exists
        if self.has_cover_image:
            manifest_items.insert(0, '<item id="cover" href="content/cover.xhtml" media-type="application/xhtml+xml"/>')
            spine_items.insert(0, '<itemref idref="cover"/>')

        # Add all sections
        section_counter = 0
        for chapter_info in self.chapters:
            sections = chapter_info.get("sections", [])
            for _ in sections:
                section_counter += 1
                section_id = f"section-{section_counter:03d}"
                manifest_items.append(f'<item id="{section_id}" href="content/section-{section_counter:03d}.xhtml" media-type="application/xhtml+xml"/>')
                spine_items.append(f'<itemref idref="{section_id}"/>')

        # Add resources - cover image only if it exists
        if self.has_cover_image:
            manifest_items.append('<item id="cover-image" href="images/cover.png" media-type="image/png" properties="cover-image"/>')
        manifest_items.append('<item id="css" href="styles/main.css" media-type="text/css"/>')

        # Metadata
        title = "Blockchain, ICO và Token Economics"
        description = "Hướng dẫn toàn diện về Initial Coin Offering (ICO), Token Economics, và toàn bộ hệ sinh thái blockchain fundraising. Bao gồm 11 chương: ICO, Token Economics, IEO/IDO, Pháp lý, DeFi, DAO, NFT, Stablecoins, RWA Tokenization, Tương lai blockchain, và Token tự trị. Từ lịch sử, quy trình, bài học thành công/thất bại đến thiết kế kinh tế token, quản trị phi tập trung, và ứng dụng thực tế."

        # Build cover meta tag only if cover exists
        cover_meta = ''
        if self.has_cover_image:
            cover_meta = '\n        <meta name="cover" content="cover-image"/>'

        # Build guide section
        guide_cover = ''
        if self.has_cover_image:
            guide_cover = '\n        <reference type="cover" title="Cover" href="content/cover.xhtml"/>'

        content_opf = f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="bookid" version="3.0">
    <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
        <dc:identifier id="bookid">{self.book_id}</dc:identifier>
        <dc:title>{title}</dc:title>
        <dc:creator>Blockchain Expert Team</dc:creator>
        <dc:language>vi</dc:language>
        <dc:date>{datetime.now().strftime('%Y-%m-%d')}</dc:date>
        <dc:publisher>Blockchain Publishing</dc:publisher>
        <dc:subject>Blockchain</dc:subject>
        <dc:subject>ICO</dc:subject>
        <dc:subject>Token Economics</dc:subject>
        <dc:subject>Cryptocurrency</dc:subject>
        <dc:subject>Smart Contracts</dc:subject>
        <dc:description>{description}</dc:description>
        <dc:rights>© 2025 Blockchain Expert Team</dc:rights>
        <meta property="dcterms:modified">{datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')}</meta>{cover_meta}
    </metadata>

    <manifest>
{chr(10).join("        " + item for item in manifest_items)}
    </manifest>

    <spine>
{chr(10).join("        " + item for item in spine_items)}
    </spine>

    <guide>{guide_cover}
        <reference type="title-page" title="Title Page" href="content/title-page.xhtml"/>
        <reference type="toc" title="Table of Contents" href="content/nav.xhtml"/>
        <reference type="text" title="Start of Content" href="content/section-001.xhtml"/>
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
        print("🚀 Starting Blockchain ICO & Token Economics EPUB generation...")
        print("📊 Target: 11 chapters with comprehensive sections")
        print("📚 Topics: ICO, Token Economics, IEO/IDO, Regulations, DeFi, DAO, NFT, Stablecoins, RWA, Future, Autonomous Tokens")
        print("=" * 70)

        try:
            self.setup_directories()
            self.create_mimetype()
            self.create_container_xml()
            self.has_cover_image = self.copy_cover_image()  # Store the result
            self.convert_chapters()
            self.create_front_matter()
            self.copy_css()
            self.create_navigation_document()
            self.create_content_opf()
            self.create_epub_zip()
            self.cleanup()

            print("=" * 70)
            print("🎉 Blockchain ICO & Token Economics EPUB generation completed!")
            print(f"📚 Output file: {self.epub_file}")
            print("📊 Structure: 11 chapters covering full blockchain fundraising ecosystem")
            print("🔗 Content: ICO, Token Economics, IEO/IDO, Legal, DeFi, DAO, NFT, Stablecoins, RWA, Future, Autonomous Tokens")
            print("✅ Optimized for reading experience")
            if not self.has_cover_image:
                print("⚠️  Note: Generated without cover image (add book_cover.png for cover)")
            print("🔄 Ready for distribution")

        except Exception as e:
            print(f"❌ Error during EPUB generation: {e}")
            raise

def main():
    generator = BlockchainICOEPUBGenerator()
    generator.generate()

if __name__ == "__main__":
    main()
