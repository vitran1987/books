#!/usr/bin/env python3
"""
Solo-Preneur with AI Agents EPUB Generator
Creates EPUB from Vietnamese content about building an EdTech startup with AI agents
Comprehensive guide covering AI orchestration, automation, development, and scaling strategies
Based on successful EPUB structure with proper metadata and EPUB-KNOWN-ISSUES.md compliance
"""

import os
import zipfile
import shutil
import re
from pathlib import Path
from datetime import datetime
import uuid
import html

class SoloPreneur_EPUBGenerator:
    def __init__(self):
        self.base_chapter_dir = Path("book")
        self.output_dir = Path("./epub-temp-solo-preneur")
        self.epub_file = Path("./solo-preneur-ai-agents-guide.epub")
        self.cover_image = Path("./book_cover.png")
        self.book_id = f"solo-preneur-ai-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.has_cover_image = False  # Track if cover image exists
        
        # Chapter and section structure for Solo-Preneur with AI Agents book
        self.chapters = [
            {
                "num": 1,
                "title": "Thời Đại Của Agentic AI và Solo-Preneur",
                "dir": "chapter-01",
                "sections": [
                    {"file": "1.1-the-shift-to-agentic.md", "title": "Thay Đổi Lớn: Từ Copilot Sang Agentic AI"},
                    {"file": "1.2-one-person-unicorn.md", "title": "One-Person Unicorn: Hiện Thực Hay Ảo Tưởng?"},
                    {"file": "1.3-map-vs-mvp.md", "title": "MAP vs MVP: Chiến Lược Mới Cho Startup"},
                    {"file": "1.4-mindset-orchestrator.md", "title": "Mindset Mới: Từ Builder Sang Orchestrator"},
                    {"file": "1.5-tech-landscape-2025.md", "title": "Technology Landscape 2025"},
                    {"file": "1.6-november-2025-breakthrough.md", "title": "November 2025: Bước Ngoặt Lớn"},
                    {"file": "1.7-vietnamese-edtech-opportunity.md", "title": "Cơ Hội EdTech Việt Nam"}
                ]
            },
            {
                "num": 2,
                "title": "Xây Dựng Đội Nhóm AI: Organizational Design",
                "dir": "chapter-02",
                "sections": [
                    {"file": "2.1-ai-org-chart.md", "title": "Sơ Đồ Tổ Chức AI"},
                    {"file": "2.2-defining-roles.md", "title": "Định Nghĩa Vai Trò Cho Từng Agent"},
                    {"file": "2.3-communication-protocol.md", "title": "Giao Thức Giao Tiếp Giữa Agents"},
                    {"file": "2.4-chatops-infrastructure.md", "title": "ChatOps Infrastructure"},
                    {"file": "2.5-human-in-the-loop.md", "title": "Human-in-the-Loop Strategy"},
                    {"file": "2.6-agent-delegation-strategy.md", "title": "Chiến Lược Ủy Quyền"},
                    {"file": "2.7-cost-optimization.md", "title": "Tối Ưu Hóa Chi Phí"}
                ]
            },
            {
                "num": 3,
                "title": "Chọn Và Sử Dụng AI Models",
                "dir": "chapter-03",
                "sections": [
                    {"file": "3.1-gpt51-codex.md", "title": "GPT-5.1 và Codex Mới Nhất"},
                    {"file": "3.2-gemini3-pro.md", "title": "Gemini 3 Pro"},
                    {"file": "3.3-claude-opus-45.md", "title": "Claude Opus 4.5"},
                    {"file": "3.4-raptor-mini.md", "title": "Raptor Mini và Các Models Nhỏ"},
                    {"file": "3.5-model-comparison.md", "title": "So Sánh Models"},
                    {"file": "3.6-integration-strategies.md", "title": "Chiến Lược Tích Hợp"}
                ]
            },
            {
                "num": 4,
                "title": "Agent Frameworks và Automation Platforms",
                "dir": "chapter-04",
                "sections": [
                    {"file": "4.1-n8n-overview.md", "title": "n8n: Low-Code Automation"},
                    {"file": "4.2-first-agent-tutorial.md", "title": "Tutorial: Agent Đầu Tiên"},
                    {"file": "4.3-langchain-langgraph.md", "title": "LangChain và LangGraph"},
                    {"file": "4.4-github-copilot-workspace.md", "title": "GitHub Copilot Workspace"},
                    {"file": "4.5-google-antigravity.md", "title": "Google Antigravity Platform"},
                    {"file": "4.6-model-context-protocol.md", "title": "Model Context Protocol (MCP)"},
                    {"file": "4.7-platform-selection.md", "title": "Lựa Chọn Platform Phù Hợp"},
                    {"file": "4.8-advanced-workflows.md", "title": "Advanced Workflows"}
                ]
            },
            {
                "num": 5,
                "title": "Development: Xây Dựng MVP Với AI Agents",
                "dir": "chapter-05",
                "sections": [
                    {"file": "5.1-ai-product-manager.md", "title": "AI Product Manager"},
                    {"file": "5.2-frontend-development.md", "title": "Frontend Development"},
                    {"file": "5.3-backend-development.md", "title": "Backend Development"},
                    {"file": "5.4-ai-tutor-implementation.md", "title": "Xây Dựng AI Tutor"},
                    {"file": "5.5-testing-qa.md", "title": "Testing và QA"},
                    {"file": "5.6-devops-ai.md", "title": "DevOps với AI"},
                    {"file": "5.7-development-best-practices.md", "title": "Best Practices"}
                ]
            },
            {
                "num": 6,
                "title": "Quality Assurance và Compliance",
                "dir": "chapter-06",
                "sections": [
                    {"file": "6.1-automated-testing.md", "title": "Automated Testing"},
                    {"file": "6.2-security-best-practices.md", "title": "Security Best Practices"},
                    {"file": "6.3-ai-output-qa.md", "title": "AI Output Quality Assurance"},
                    {"file": "6.4-compliance-legal.md", "title": "Compliance và Legal"}
                ]
            },
            {
                "num": 7,
                "title": "EdTech-Specific: Xây Dựng Hệ Thống Giáo Dục",
                "dir": "chapter-07",
                "sections": [
                    {"file": "7.1-curriculum-expert.md", "title": "AI Curriculum Expert"},
                    {"file": "7.2-tutor-personality.md", "title": "Tutor Personality Design"},
                    {"file": "7.3-multimodal-content.md", "title": "Multimodal Content Creation"},
                    {"file": "7.4-adaptive-learning.md", "title": "Adaptive Learning Engine"},
                    {"file": "7.5-vietnamese-language.md", "title": "Vietnamese Language Processing"},
                    {"file": "7.6-assessment-grading.md", "title": "Assessment và Grading"},
                    {"file": "7.7-teacher-tools.md", "title": "Teacher Tools"}
                ]
            },
            {
                "num": 8,
                "title": "Marketing và Growth với AI Agents",
                "dir": "chapter-08",
                "sections": [
                    {"file": "8.1-content-marketing.md", "title": "Content Marketing"},
                    {"file": "8.2-social-media.md", "title": "Social Media Automation"},
                    {"file": "8.3-performance-marketing.md", "title": "Performance Marketing"},
                    {"file": "8.4-growth-hacking.md", "title": "Growth Hacking"}
                ]
            },
            {
                "num": 9,
                "title": "Back-Office Operations: Tự Động Hóa Hoàn Toàn",
                "dir": "chapter-09",
                "sections": [
                    {"file": "9.1-financial-management.md", "title": "Financial Management"},
                    {"file": "9.2-legal-compliance.md", "title": "Legal và Compliance"},
                    {"file": "9.3-customer-support.md", "title": "Customer Support"},
                    {"file": "9.4-hr-admin.md", "title": "HR và Admin"}
                ]
            },
            {
                "num": 10,
                "title": "Scaling: Từ Local Đến Global",
                "dir": "chapter-10",
                "sections": [
                    {"file": "10.1-multi-language.md", "title": "Multi-Language Expansion"},
                    {"file": "10.2-scaling-infrastructure.md", "title": "Scaling Infrastructure"},
                    {"file": "10.3-business-models.md", "title": "Business Models"}
                ]
            },
            {
                "num": 11,
                "title": "Tương Lai: 2027-2030",
                "dir": "chapter-11",
                "sections": [
                    {"file": "11.1-ai-evolution.md", "title": "AI Evolution Roadmap"},
                    {"file": "11.2-mega-scale-solo.md", "title": "Mega-Scale Solo Operations"},
                    {"file": "11.3-future-preparation.md", "title": "Future Preparation"}
                ]
            },
            {
                "num": 12,
                "title": "Implementation Roadmap: 12 Tháng Đầu",
                "dir": "chapter-12",
                "sections": [
                    {"file": "12.1-months-0-3-foundation.md", "title": "Tháng 0-3: Foundation"},
                    {"file": "12.2-months-4-6-growth.md", "title": "Tháng 4-6: Growth"},
                    {"file": "12.3-months-7-12-scale.md", "title": "Tháng 7-12: Scale"},
                    {"file": "12.4-vision-2027.md", "title": "Vision 2027"}
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
        <img src="../images/cover.png" alt="Kiếm Tiền Từ Quảng Cáo Cho Nền Tảng Giáo Dục - Book Cover"/>
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
    <h1>Solo-Preneur với AI Agents: Xây Dựng Startup EdTech Một Mình</h1>
    <p class="subtitle">Hướng Dẫn Toàn Diện Về AI Orchestration, Automation, Development và Scaling Strategies</p>
    <div class="publication-info">
        <p><strong>Chủ đề:</strong> AI Agents, Solo-Preneur, EdTech Startup, Automation, Agentic AI</p>
        <p><strong>Năm xuất bản:</strong> 2025</p>
        <p><strong>Ngôn ngữ:</strong> Tiếng Việt</p>
        <p><strong>Số chương:</strong> 12 chương toàn diện</p>
        <p><strong>Phạm vi:</strong> Từ Agentic AI mindset đến xây dựng MVP, scaling và vision 2027-2030</p>
        <p><strong>Nội dung:</strong> AI Models, Agent Frameworks, Development, QA, EdTech Implementation, Marketing, Operations, Global Scaling</p>
    </div>
</body>
</html>'''

        with open(self.output_dir / "OEBPS" / "content" / "title-page.xhtml", "w", encoding="utf-8") as f:
            f.write(title_html)

        print("✅ Front matter created")

    def copy_css(self):
        """Copy CSS file"""
        print("Copying CSS file...")

        css_content = '''/* Solo-Preneur AI Agents EPUB CSS Styles */
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
    border-bottom: 2px solid #4299e1;
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
    color: #4299e1;
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
        title = "Solo-Preneur với AI Agents: Xây Dựng Startup EdTech Một Mình"
        description = html.escape("Hướng dẫn toàn diện về xây dựng startup EdTech với AI agents. Bao gồm 12 chương: Thời đại Agentic AI, Xây dựng đội nhóm AI, Chọn AI models, Agent frameworks, Development với AI, Quality assurance, EdTech-specific implementation, Marketing automation, Back-office operations, Global scaling, Tương lai 2027-2030, và Implementation roadmap 12 tháng. Từ mindset orchestrator đến phương pháp kỹ thuật tiên tiến, AI automation, và lộ trình triển khai thực tế cho solo-preneur.", quote=False)

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
        <dc:creator>AI-Powered Solo-Preneur Expert Team</dc:creator>
        <dc:language>vi</dc:language>
        <dc:date>{datetime.now().strftime('%Y-%m-%d')}</dc:date>
        <dc:publisher>Solo-Preneur Publishing</dc:publisher>
        <dc:subject>AI Agents</dc:subject>
        <dc:subject>Solo-Preneur</dc:subject>
        <dc:subject>EdTech Startup</dc:subject>
        <dc:subject>Agentic AI</dc:subject>
        <dc:subject>Automation</dc:subject>
        <dc:subject>AI Models</dc:subject>
        <dc:description>{description}</dc:description>
        <dc:rights>© 2025 AI-Powered Solo-Preneur Expert Team</dc:rights>
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
        print("🚀 Starting Solo-Preneur AI Agents EPUB generation...")
        print("📊 Target: 12 chapters with comprehensive sections")
        print("📚 Topics: AI Orchestration, Models, Frameworks, Development, QA, EdTech, Marketing, Operations, Scaling")
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
            print("🎉 Solo-Preneur AI Agents EPUB generation completed!")
            print(f"📚 Output file: {self.epub_file}")
            print("📊 Structure: 12 chapters covering AI agents for solo-preneur EdTech startup")
            print("🔗 Content: Agentic AI, Organizational Design, Models, Frameworks, Development, QA, EdTech, Marketing, Operations, Scaling, Future Vision")
            print("✅ Optimized for reading experience")
            if not self.has_cover_image:
                print("⚠️  Note: Generated without cover image (add book_cover.png for cover)")
            print("🔄 Ready for distribution")

        except Exception as e:
            print(f"❌ Error during EPUB generation: {e}")
            raise

def main():
    generator = SoloPreneur_EPUBGenerator()
    generator.generate()

if __name__ == "__main__":
    main()
