#!/usr/bin/env python3
"""
Marketing & Advertising for EdTech EPUB Generator
Creates EPUB from Vietnamese content about advertising and monetization for educational platforms
Comprehensive guide covering Google Adsense, Facebook Ads, AI agents, and creative monetization
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

class MarketingEdTechEPUBGenerator:
    def __init__(self):
        self.base_chapter_dir = Path("book")
        self.output_dir = Path("./epub-temp-marketing")
        self.epub_file = Path("./marketing-edtech-guide.epub")
        self.cover_image = Path("./book-cover.png")
        self.book_id = f"marketing-edtech-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.has_cover_image = False  # Track if cover image exists
        
        # Chapter and section structure for Marketing EdTech book
        self.chapters = [
            {
                "num": 1,
                "title": "Hiểu Rõ Bản Chất Quảng Cáo Cho Nền Tảng Giáo Dục",
                "dir": "chapter-01",
                "sections": [
                    {"file": "1.1-ban-chat-quang-cao-giao-duc.md", "title": "Đặc Thù Quảng Cáo Giáo Dục"},
                    {"file": "1.2-tam-ly-nguoi-dung.md", "title": "Phân Tích Tâm Lý Người Dùng"},
                    {"file": "1.3-dao-duc-phap-ly.md", "title": "Khung Pháp Lý và Đạo Đức"},
                    {"file": "1.4-can-bang-doanh-thu-trai-nghiem.md", "title": "Chiến Lược Cân Bằng"},
                    {"file": "1.5-case-study-khan-academy.md", "title": "Khan Academy Approach"},
                    {"file": "1.6-case-study-duolingo.md", "title": "Duolingo's Freemium + Ads Model"},
                    {"file": "1.7-bai-hoc-ung-dung.md", "title": "Bài Học Cho Bạn Giỏi"}
                ]
            },
            {
                "num": 2,
                "title": "Hiểu Thị Trường Việt Nam - Người Dùng Việt 'Ưa Miễn Phí'",
                "dir": "chapter-02",
                "sections": [
                    {"file": "2.1-thi-truong-giao-duc-viet.md", "title": "Bức Tranh Tổng Quan"},
                    {"file": "2.2-tam-ly-mien-phi.md", "title": "Tâm Lý Người Việt với 'Miễn Phí'"},
                    {"file": "2.3-kha-nang-chi-tra.md", "title": "Thu Nhập và Chi Tiêu Giáo Dục"},
                    {"file": "2.4-case-study-hocmai.md", "title": "Hocmai.vn: Mô Hình Hybrid"},
                    {"file": "2.5-case-study-vndoc.md", "title": "Vndoc.com: Quảng Cáo Thuần Túy"},
                    {"file": "2.6-that-bai-tra-phi.md", "title": "Các Startup Thất Bại"},
                    {"file": "2.7-co-hoi-freemium-ads.md", "title": "Chiến Lược Cho Bạn Giỏi"}
                ]
            },
            {
                "num": 3,
                "title": "Google Adsense - Cơ Chế, Chiến Lược và Phương Pháp Tối Ưu",
                "dir": "chapter-03",
                "sections": [
                    {"file": "3.1-co-che-adsense.md", "title": "Cơ Chế Hoạt Động và Auction System"},
                    {"file": "3.2-chinh-sach-2024-2025.md", "title": "Update Chính Sách Mới Nhất"},
                    {"file": "3.3-phuong-phap-tich-hop.md", "title": "So Sánh Integration Approaches"},
                    {"file": "3.4-cac-loai-quang-cao.md", "title": "Các Định Dạng và Use Cases"},
                    {"file": "3.5-chien-luoc-vi-tri.md", "title": "Placement Strategies Cho EdTech"},
                    {"file": "3.6-performance-balance.md", "title": "Cân Bằng Revenue vs Page Speed"},
                    {"file": "3.7-ai-ml-adsense.md", "title": "ML Trong Adsense và Cách Tận Dụng"},
                    {"file": "3.8-thuc-hanh-ban-gioi.md", "title": "Strategy Cho Bạn Giỏi"}
                ]
            },
            {
                "num": 4,
                "title": "Tối Ưu Hóa Thu Nhập Google Adsense - Phương Pháp và Chiến Lược",
                "dir": "chapter-04",
                "sections": [
                    {"file": "4.1-seo-content-strategy.md", "title": "SEO Approach Cho High-Value Traffic"},
                    {"file": "4.2-content-optimization.md", "title": "Content Strategy Tăng CTR/CPC"},
                    {"file": "4.3-experimentation-method.md", "title": "A/B Testing Methodology"},
                    {"file": "4.4-engagement-strategies.md", "title": "Strategies Tăng Pageviews"},
                    {"file": "4.5-mobile-first-approach.md", "title": "Mobile Optimization Approach"},
                    {"file": "4.6-header-bidding.md", "title": "Header Bidding Concept and When to Use"},
                    {"file": "4.7-ad-refresh-method.md", "title": "Safe Refresh Strategies"},
                    {"file": "4.8-traffic-quality.md", "title": "Quality Assurance Methods"},
                    {"file": "4.9-case-study-revenue.md", "title": "Analysis Các Website Thành Công"},
                    {"file": "4.10-ke-hoach-ban-gioi.md", "title": "Roadmap Cho Bạn Giỏi"}
                ]
            },
            {
                "num": 5,
                "title": "Vượt Qua Thách Thức 3 Tuần Đầu - Chẩn Đoán và Phương Pháp Giải Quyết",
                "dir": "chapter-05",
                "sections": [
                    {"file": "5.1-normal-learning-period.md", "title": "Hiểu Giai Đoạn Đầu"},
                    {"file": "5.2-diagnostic-methods.md", "title": "Phương Pháp Chẩn Đoán"},
                    {"file": "5.3-analytics-approach.md", "title": "Data Analysis Methods"},
                    {"file": "5.4-30-day-methodology.md", "title": "Optimization Roadmap"},
                    {"file": "5.5-revenue-benchmarks.md", "title": "Realistic Expectations"},
                    {"file": "5.6-scaling-strategy.md", "title": "Lộ Trình Scale Revenue"},
                    {"file": "5.7-infrastructure.md", "title": "Khi Nào Cần Infrastructure Upgrades"},
                    {"file": "5.8-common-mistakes.md", "title": "Pitfalls và Solutions"},
                    {"file": "5.9-action-plan.md", "title": "Action Plan for Bạn Giỏi"}
                ]
            },
            {
                "num": 6,
                "title": "Facebook Audience Network - Chiến Lược và Phương Pháp Tích Hợp",
                "dir": "chapter-06",
                "sections": [
                    {"file": "6.1-fan-overview.md", "title": "FAN Ecosystem và Comparison"},
                    {"file": "6.2-integration-approach.md", "title": "Integration Methods và Considerations"},
                    {"file": "6.3-requirements.md", "title": "Điều Kiện và Preparation"},
                    {"file": "6.4-mediation-strategy.md", "title": "When and Why Mediation"},
                    {"file": "6.5-waterfall-vs-bidding.md", "title": "Comparing Approaches"},
                    {"file": "6.6-optimization-strategy.md", "title": "FAN Optimization Methods"},
                    {"file": "6.7-performance-analysis.md", "title": "Performance Comparison"},
                    {"file": "6.8-case-studies.md", "title": "FAN Success Stories"},
                    {"file": "6.9-decision-framework.md", "title": "Phù Hợp Với Bạn Giỏi?"}
                ]
            },
            {
                "num": 7,
                "title": "Khảo Sát Các Nền Tảng Quảng Cáo Thay Thế - So Sánh và Lựa Chọn",
                "dir": "chapter-07",
                "sections": [
                    {"file": "7.1-platform-comparison.md", "title": "Feature Comparison Major Platforms"},
                    {"file": "7.2-ezoic-ai-approach.md", "title": "Ezoic's AI Methodology"},
                    {"file": "7.3-premium-networks.md", "title": "Mediavine/AdThrive Analysis"},
                    {"file": "7.4-affiliate-strategy.md", "title": "Affiliate Approach Cho EdTech"},
                    {"file": "7.5-native-advertising.md", "title": "Native Ad Strategy"},
                    {"file": "7.6-emerging-tech.md", "title": "Blockchain & Privacy-First Ads"},
                    {"file": "7.7-revenue-comparison.md", "title": "Platform Revenue Analysis"},
                    {"file": "7.8-diversification-strategy.md", "title": "Diversification Methodology"},
                    {"file": "7.9-selection-framework.md", "title": "Decision Framework Choosing Platforms"}
                ]
            },
            {
                "num": 8,
                "title": "Quảng Cáo Tích Hợp Trong Bài Học - Gamified Advertising Strategy",
                "dir": "chapter-08",
                "sections": [
                    {"file": "8.1-innovation-need.md", "title": "Tại Sao Cần Đổi Mới"},
                    {"file": "8.2-rewarded-video-strategy.md", "title": "Rewarded Ads Methodology"},
                    {"file": "8.3-interstitial-strategy.md", "title": "Optimal Timing Approach"},
                    {"file": "8.4-unlock-mechanics.md", "title": "Ads-for-Content Methodology"},
                    {"file": "8.5-reward-integration.md", "title": "Point System Integration"},
                    {"file": "8.6-ai-personalization.md", "title": "Personalization Approach"},
                    {"file": "8.7-balance-framework.md", "title": "Engagement/Monetization Balance"},
                    {"file": "8.8-duolingo-analysis.md", "title": "Duolingo's Strategy Breakdown"},
                    {"file": "8.9-validation-methods.md", "title": "User Testing Approach"},
                    {"file": "8.10-implementation-plan.md", "title": "Plan for Bạn Giỏi"}
                ]
            },
            {
                "num": 9,
                "title": "Survey Monetization - Phương Pháp và Chiến Lược",
                "dir": "chapter-09",
                "sections": [
                    {"file": "9.1-platform-comparison.md", "title": "Survey Platform Analysis"},
                    {"file": "9.2-integration-strategy.md", "title": "Integration Methodology"},
                    {"file": "9.3-data-monetization.md", "title": "Legal Monetization Approaches"},
                    {"file": "9.4-reward-mechanics.md", "title": "Reward Strategy"},
                    {"file": "9.5-privacy-strategy.md", "title": "Privacy-Compliant Methods"},
                    {"file": "9.6-value-creation.md", "title": "Creating Valuable Insights"},
                    {"file": "9.7-ai-enhancement.md", "title": "AI for Survey Improvement"},
                    {"file": "9.8-analysis-methods.md", "title": "Data Analysis Approaches"},
                    {"file": "9.9-case-studies.md", "title": "Survey Success Stories"},
                    {"file": "9.10-bangioi-plan.md", "title": "Survey Strategy for Bạn Giỏi"}
                ]
            },
            {
                "num": 10,
                "title": "Sponsored Content và Partnership Strategy",
                "dir": "chapter-10",
                "sections": [
                    {"file": "10.1-sponsored-strategy.md", "title": "Sponsored Content Approach"},
                    {"file": "10.2-partnership-framework.md", "title": "Finding Partners Methodology"},
                    {"file": "10.3-affiliate-approach.md", "title": "Affiliate Strategy"},
                    {"file": "10.4-branded-content.md", "title": "Branded Content Methodology"},
                    {"file": "10.5-b2b-strategy.md", "title": "B2B Partnership Approach"},
                    {"file": "10.6-white-label-licensing.md", "title": "White-Label Strategy"},
                    {"file": "10.7-revenue-models.md", "title": "Revenue Sharing Comparison"},
                    {"file": "10.8-integration-methods.md", "title": "Seamless Integration"},
                    {"file": "10.9-partnership-case-studies.md", "title": "Partnership Success Stories"},
                    {"file": "10.10-ban-gioi-partnerships.md", "title": "Partnership Plan for Bạn Giỏi"}
                ]
            },
            {
                "num": 11,
                "title": "AI Agents Trong Advertising - Chiến Lược và Phương Pháp",
                "dir": "chapter-11",
                "sections": [
                    {"file": "11.1-ai-agent-landscape.md", "title": "AI Agent Frameworks Comparison"},
                    {"file": "11.2-use-cases.md", "title": "Where AI Agents Add Value"},
                    {"file": "11.3-autonomous-optimization.md", "title": "Self-Optimization Concept"},
                    {"file": "11.4-content-generation.md", "title": "AI for Creative Strategy"},
                    {"file": "11.5-monitoring-strategy.md", "title": "AI Monitoring Approach"},
                    {"file": "11.6-experimentation-automation.md", "title": "Automated Testing Methodology"},
                    {"file": "11.7-multi-agent-concept.md", "title": "Agent Orchestration Strategy"},
                    {"file": "11.8-cost-benefit.md", "title": "ROI Analysis Framework"},
                    {"file": "11.9-adoption-roadmap.md", "title": "Phased Implementation Plan"},
                    {"file": "11.10-case-studies.md", "title": "AI Agent Success Stories"},
                    {"file": "11.11-bangioi-ai-strategy.md", "title": "AI Agent Plan for Bạn Giỏi"}
                ]
            },
            {
                "num": 13,
                "title": "Đo Lường, Phân Tích và Tối Ưu Hóa Liên Tục",
                "dir": "chapter-13",
                "sections": [
                    {"file": "13.1-analytics-strategy.md", "title": "What to Measure và Why"},
                    {"file": "13.2-metrics-framework.md", "title": "Interpreting Key Metrics"},
                    {"file": "13.3-ux-metrics.md", "title": "Balancing Revenue vs UX"},
                    {"file": "13.4-testing-methodology.md", "title": "Statistical Approach"},
                    {"file": "13.5-feedback-systems.md", "title": "User Feedback Strategy"},
                    {"file": "13.6-optimization-process.md", "title": "Regular Review Methodology"},
                    {"file": "13.7-reporting-strategy.md", "title": "Stakeholder Communication"},
                    {"file": "13.8-automation-approach.md", "title": "What to Automate"},
                    {"file": "13.9-ai-insights.md", "title": "AI for Predictions"},
                    {"file": "13.10-continuous-improvement.md", "title": "Building Optimization Culture"},
                    {"file": "13.11-web3-prep.md", "title": "Token Integration Strategy"},
                    {"file": "13.12-long-term-vision.md", "title": "Future Roadmap"}
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
    <h1>Kiếm Tiền Từ Quảng Cáo Cho Nền Tảng Giáo Dục</h1>
    <p class="subtitle">Hướng Dẫn Toàn Diện Về Google Adsense, Facebook Ads, AI Agents và Chiến Lược Monetization Sáng Tạo</p>
    <p class="author">Tác giả: Bạn Giỏi Research Lab</p>
    <div class="publication-info">
        <p><strong>Chủ đề:</strong> Digital Advertising, EdTech Monetization, Google Adsense, AI Agents, Marketing Strategy</p>
        <p><strong>Năm xuất bản:</strong> 2025</p>
        <p><strong>Ngôn ngữ:</strong> Tiếng Việt</p>
        <p><strong>Số chương:</strong> 11 chương toàn diện</p>
        <p><strong>Phạm vi:</strong> Từ bản chất quảng cáo giáo dục đến AI agents, tối ưu hóa liên tục và chiến lược Web3</p>
        <p><strong>Nội dung:</strong> Adsense, Facebook Ads, Alternative Platforms, Gamified Ads, Surveys, Partnerships, AI Agents, Analytics</p>
    </div>
</body>
</html>'''

        with open(self.output_dir / "OEBPS" / "content" / "title-page.xhtml", "w", encoding="utf-8") as f:
            f.write(title_html)

        print("✅ Front matter created")

    def copy_css(self):
        """Copy CSS file"""
        print("Copying CSS file...")

        css_content = '''/* Marketing EdTech EPUB CSS Styles */
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
    margin-bottom: 1em;
}

.author {
    font-size: 1.1em;
    color: #1a365d;
    font-weight: bold;
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
        title = "Kiếm Tiền Từ Quảng Cáo Cho Nền Tảng Giáo Dục"
        description = html.escape("Hướng dẫn toàn diện về kiếm tiền từ quảng cáo cho nền tảng giáo dục trực tuyến. Bao gồm 11 chương: Bản chất quảng cáo giáo dục, Thị trường Việt Nam, Google Adsense deep dive, Facebook Audience Network, Alternative platforms, Gamified advertising, Survey monetization, Sponsored content, AI agents strategies, và Analytics & optimization. Từ chiến lược cơ bản đến phương pháp kỹ thuật tiên tiến, AI automation, và lộ trình triển khai thực tế cho startup EdTech.", quote=False)

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
        <dc:creator>Bạn Giỏi Research Lab</dc:creator>
        <dc:language>vi</dc:language>
        <dc:date>{datetime.now().strftime('%Y-%m-%d')}</dc:date>
        <dc:publisher>Bạn Giỏi Research Lab</dc:publisher>
        <dc:subject>Digital Advertising</dc:subject>
        <dc:subject>EdTech Monetization</dc:subject>
        <dc:subject>Google Adsense</dc:subject>
        <dc:subject>Facebook Ads</dc:subject>
        <dc:subject>AI Agents</dc:subject>
        <dc:subject>Marketing Strategy</dc:subject>
        <dc:description>{description}</dc:description>
        <dc:rights>© 2025 Bạn Giỏi Research Lab</dc:rights>
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
        print("🚀 Starting Marketing EdTech EPUB generation...")
        print("📊 Target: 11 chapters with comprehensive sections (chapters 1-11, 13)")
        print("📚 Topics: Adsense, Facebook Ads, Alternative Platforms, Gamified Ads, Surveys, Partnerships, AI Agents, Analytics")
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
            print("🎉 Marketing EdTech EPUB generation completed!")
            print(f"📚 Output file: {self.epub_file}")
            print("📊 Structure: 11 chapters covering advertising and monetization for EdTech platforms")
            print("🔗 Content: Adsense, Facebook Ads, Alternatives, Gamified Ads, Surveys, Partnerships, AI Agents, Analytics")
            print("✅ Optimized for reading experience")
            if not self.has_cover_image:
                print("⚠️  Note: Generated without cover image (add book_cover.png for cover)")
            print("🔄 Ready for distribution")

        except Exception as e:
            print(f"❌ Error during EPUB generation: {e}")
            raise

def main():
    generator = MarketingEdTechEPUBGenerator()
    generator.generate()

if __name__ == "__main__":
    main()
