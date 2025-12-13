#!/usr/bin/env python3
"""
AI-Era Education EPUB Generator
Creates EPUB from Vietnamese content about reimagining education for the AI age
Comprehensive guide covering traditional education crisis, AI learning revolution, and practical implementation
Based on successful EPUB structure with proper metadata and Google Play Books compatibility
"""

import os
import zipfile
import shutil
import re
from pathlib import Path
from datetime import datetime
import uuid
import html

class AIEducationEPUBGenerator:
    def __init__(self):
        self.base_book_dir = Path("./book")
        self.output_dir = Path("./epub-temp-ai-education")
        self.epub_file = Path("./ai-education-reimagined.epub")
        self.cover_image = Path("./book-cover.png")
        self.book_id = f"ai-education-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.has_cover_image = False  # Track if cover image exists
        
        # Chapter and section structure for AI-Era Education book
        # 5 Parts with 15 Chapters
        self.chapters = [
            # PART I: THE EDUCATION EMERGENCY - Understanding What's Broken (Chapters 1-3)
            {
                "part": 1,
                "part_title": "Phần I: Khủng Hoảng Giáo Dục - Hiểu Rõ Vấn Đề",
                "num": 1, 
                "title": "Thực Trạng Giáo Dục - Khi Nhà Trường Xa Rời Cuộc Sống", 
                "dir": "part-1/chapter-01",
                "sections": [
                    {"file": "01-diploma-paradox.md", "title": "Nghịch Lý Bằng Cấp"},
                    {"file": "02-employer-wants-vs-school-teaches.md", "title": "Những Gì Nhà Tuyển Dụng Muốn vs. Những Gì Trường Học Dạy"},
                    {"file": "03-student-debt-crisis.md", "title": "Khủng Hoảng Nợ Sinh Viên"},
                    {"file": "04-vietnam-case-study.md", "title": "Nghiên Cứu Điển Hình Việt Nam"},
                    {"file": "05-skills-half-life.md", "title": "Chu Kỳ Sống Của Kiến Thức"},
                    {"file": "06-forgotten-majority.md", "title": "Đa Số Bị Lãng Quên"},
                    {"file": "07-measuring-the-cost.md", "title": "Đo Lường Chi Phí"}
                ]
            },
            {
                "part": 1,
                "part_title": "Phần I: Khủng Hoảng Giáo Dục - Hiểu Rõ Vấn Đề",
                "num": 2, 
                "title": "Cách Mạng Tri Thức AI - Khi Máy Móc Thông Minh Hơn Sách Giáo Khoa", 
                "dir": "part-1/chapter-02",
                "sections": [
                    {"file": "01-race-to-train-god.md", "title": "Cuộc Đua Huấn Luyện AI"},
                    {"file": "02-100-billion-training.md", "title": "100 Tỷ Đô La Cho Đào Tạo AI"},
                    {"file": "03-ai-models-capabilities.md", "title": "Khả Năng Của Các Mô Hình AI"},
                    {"file": "04-patient-teacher.md", "title": "Giáo Viên Kiên Nhẫn Không Bao Giờ Ngủ"},
                    {"file": "05-case-studies-kids-learning.md", "title": "Nghiên Cứu Điển Hình: Trẻ Em Học Với AI"},
                    {"file": "06-neuroscience-ai-learning.md", "title": "Khoa Học Thần Kinh Về Học Tập Với AI"},
                    {"file": "07-what-ai-cannot-replace.md", "title": "Những Gì AI Không Thể Thay Thế"}
                ]
            },
            {
                "part": 1,
                "part_title": "Phần I: Khủng Hoảng Giáo Dục - Hiểu Rõ Vấn Đề",
                "num": 3,
                "title": "Khủng Hoảng Chương Trình Học - Những Gì Chúng Ta Ép Trẻ Học",
                "dir": "part-1/chapter-03",
                "sections": [
                    {"file": "01-honest-survey.md", "title": "Khảo Sát Thành Thật"},
                    {"file": "02-artist-calculus.md", "title": "Nghệ Sĩ Và Giải Tích Cao Cấp"},
                    {"file": "03-engineer-biology.md", "title": "Kỹ Sư Và Sách Sinh Học"},
                    {"file": "04-cognitive-load.md", "title": "Lý Thuyết Tải Nhận Thức"},
                    {"file": "05-passion-killer.md", "title": "Kẻ Giết Chết Đam Mê"},
                    {"file": "06-finland-lesson.md", "title": "Bài Học Từ Phần Lan"},
                    {"file": "07-opportunity-cost.md", "title": "Phân Tích Chi Phí Cơ Hội"}
                ]
            },
            
            # PART II: THE GLOBAL LABORATORY - What Actually Works (Chapters 4-5)
            {
                "part": 2,
                "part_title": "Phần II: Phòng Thí Nghiệm Toàn Cầu - Những Gì Thực Sự Hiệu Quả",
                "num": 4,
                "title": "Những Người Nổi Loạn Thành Công - Mô Hình Giáo Dục Thay Thế Hiệu Quả",
                "dir": "part-2/chapter-04",
                "sections": [
                    {"file": "01-finland-revolution.md", "title": "Cách Mạng Phần Lan"},
                    {"file": "02-montessori-method.md", "title": "Phương Pháp Montessori"},
                    {"file": "03-singapore-streaming.md", "title": "Hệ Thống Phân Luồng Singapore"},
                    {"file": "04-homeschooling-renaissance.md", "title": "Phục Hưng Giáo Dục Tại Nhà"},
                    {"file": "05-democratic-schools.md", "title": "Trường Học Dân Chủ"},
                    {"file": "06-microschools-pods.md", "title": "Vi Trường Học và Learning Pods"},
                    {"file": "07-meta-analysis-what-works.md", "title": "Phân Tích Tổng Hợp: Những Gì Hiệu Quả"}
                ]
            },
            {
                "part": 2,
                "part_title": "Phần II: Phòng Thí Nghiệm Toàn Cầu - Những Gì Thực Sự Hiệu Quả",
                "num": 5,
                "title": "Khoa Học Thần Kinh Về Học Tập - Cách Bộ Não Thực Sự Học",
                "dir": "part-2/chapter-05",
                "sections": [
                    {"file": "01-forgetting-curve.md", "title": "Đường Cong Quên Lãng"},
                    {"file": "02-spaced-repetition.md", "title": "Lặp Lại Ngắt Quãng"},
                    {"file": "03-talent-code-myelin.md", "title": "Mã Tài Năng và Myelin"},
                    {"file": "04-growth-fixed-mindset.md", "title": "Tư Duy Phát Triển và Cố Định"},
                    {"file": "05-neuroscience-motivation.md", "title": "Khoa Học Thần Kinh Về Động Lực"},
                    {"file": "06-critical-sensitive-periods.md", "title": "Giai Đoạn Nhạy Cảm và Quan Trọng"},
                    {"file": "07-personalized-learning-brain.md", "title": "Học Tập Cá Nhân Hóa và Não Bộ"}
                ]
            },
            
            # PART III: THE NEW FRAMEWORK - Building Personalized Learning Paths (Chapters 6-8)
            {
                "part": 3,
                "part_title": "Phần III: Khung Giáo Dục Mới - Xây Dựng Con Đường Học Tập Cá Nhân Hóa",
                "num": 6,
                "title": "Khung Học Tập Thích Ứng - Vượt Qua Mô Hình 5-5-4-2",
                "dir": "part-3/chapter-06",
                "sections": [
                    {"file": "01-5-5-4-2-starting-point.md", "title": "Điểm Khởi Đầu 5-5-4-2"},
                    {"file": "02-personalization-principle.md", "title": "Nguyên Tắc Cá Nhân Hóa"},
                    {"file": "03-core-competencies-matrix.md", "title": "Ma Trận Năng Lực Cốt Lõi"},
                    {"file": "04-early-specialization-research.md", "title": "Nghiên Cứu Về Chuyên Môn Hóa Sớm"},
                    {"file": "05-multi-potentiality-design.md", "title": "Thiết Kế Cho Đa Tài Năng"},
                    {"file": "06-late-bloomers-path-switchers.md", "title": "Người Nở Muộn và Chuyển Đổi Con Đường"},
                    {"file": "07-assessment-beyond-testing.md", "title": "Đánh Giá Vượt Ra Khỏi Thi Cử"}
                ]
            },
            {
                "part": 3,
                "part_title": "Phần III: Khung Giáo Dục Mới - Xây Dựng Con Đường Học Tập Cá Nhân Hóa",
                "num": 7,
                "title": "AI Làm Đối Tác Học Tập - Triển Khai Thực Tế Cho Trẻ Em",
                "dir": "part-3/chapter-07",
                "sections": [
                    {"file": "01-ai-literacy-curriculum.md", "title": "Chương Trình Giáo Dục AI"},
                    {"file": "02-starting-simple-ages-8-12.md", "title": "Bắt Đầu Đơn Giản: 8-12 Tuổi"},
                    {"file": "03-critical-thinking-ai-era.md", "title": "Tư Duy Phê Phán Thời Đại AI"},
                    {"file": "04-prompt-engineering-skill.md", "title": "Kỹ Năng Prompt Engineering"},
                    {"file": "05-ai-assisted-project-learning.md", "title": "Học Tập Dự Án Với Hỗ Trợ AI"},
                    {"file": "06-common-pitfalls-avoidance.md", "title": "Những Cạm Bẫy Thường Gặp"},
                    {"file": "07-measuring-progress-metrics.md", "title": "Đo Lường Tiến Bộ"}
                ]
            },
            {
                "part": 3,
                "part_title": "Phần III: Khung Giáo Dục Mới - Xây Dựng Con Đường Học Tập Cá Nhân Hóa",
                "num": 8,
                "title": "Khung An Toàn & Đạo Đức - Bảo Vệ Trẻ Em Trong Khi Cho Phép Phát Triển",
                "dir": "part-3/chapter-08",
                "sections": [
                    {"file": "01-real-risks-assessment.md", "title": "Đánh Giá Rủi Ro Thực Tế"},
                    {"file": "02-age-appropriate-boundaries.md", "title": "Ranh Giới Phù Hợp Theo Độ Tuổi"},
                    {"file": "03-technical-safeguards.md", "title": "Biện Pháp Bảo Vệ Kỹ Thuật"},
                    {"file": "04-teaching-verification.md", "title": "Dạy Kỹ Năng Xác Minh"},
                    {"file": "05-ethical-use-of-ai.md", "title": "Sử Dụng AI Có Đạo Đức"},
                    {"file": "06-parental-involvement-spectrum.md", "title": "Phổ Tham Gia Của Cha Mẹ"},
                    {"file": "07-when-to-intervene-red-flags.md", "title": "Khi Nào Can Thiệp: Cờ Đỏ"}
                ]
            },
            
            # PART IV: SPECIALIZED PATHWAYS - Practical Applications by Domain (Chapters 9-11)
            {
                "part": 4,
                "part_title": "Phần IV: Con Đường Chuyên Môn Hóa - Ứng Dụng Thực Tế Theo Lĩnh Vực",
                "num": 9,
                "title": "Con Đường Sáng Tạo - Nghệ Thuật, Âm Nhạc, Thiết Kế Với AI",
                "dir": "part-4/chapter-09",
                "sections": [
                    {"file": "01-visual-arts-with-ai.md", "title": "Nghệ Thuật Thị Giác Với AI"},
                    {"file": "02-music-and-audio-creation.md", "title": "Sáng Tạo Âm Nhạc và Âm Thanh"},
                    {"file": "03-video-and-animation.md", "title": "Video và Hoạt Hình"},
                    {"file": "04-design-and-user-experience.md", "title": "Thiết Kế và Trải Nghiệm Người Dùng"},
                    {"file": "05-writing-and-storytelling.md", "title": "Viết Lách và Kể Chuyện"},
                    {"file": "06-building-creative-portfolio.md", "title": "Xây Dựng Portfolio Sáng Tạo"},
                    {"file": "07-from-hobby-to-income.md", "title": "Từ Sở Thích Đến Thu Nhập"}
                ]
            },
            {
                "part": 4,
                "part_title": "Phần IV: Con Đường Chuyên Môn Hóa - Ứng Dụng Thực Tế Theo Lĩnh Vực",
                "num": 10,
                "title": "Con Đường Kỹ Thuật - Lập Trình, Kỹ Thuật, Khoa Học Dữ Liệu Với AI",
                "dir": "part-4/chapter-10",
                "sections": [
                    {"file": "01-programming-fundamentals.md", "title": "Nguyên Lý Lập Trình Cơ Bản"},
                    {"file": "02-ai-assisted-development.md", "title": "Phát Triển Với Hỗ Trợ AI"},
                    {"file": "03-web-development-fast-track.md", "title": "Phát Triển Web Nhanh"},
                    {"file": "04-mobile-app-development.md", "title": "Phát Triển Ứng Dụng Di Động"},
                    {"file": "05-data-science-analytics.md", "title": "Khoa Học Dữ Liệu và Phân Tích"},
                    {"file": "06-building-ai-applications.md", "title": "Xây Dựng Ứng Dụng AI"},
                    {"file": "07-technical-portfolio.md", "title": "Portfolio Kỹ Thuật"},
                    {"file": "08-from-code-to-career.md", "title": "Từ Code Đến Sự Nghiệp"}
                ]
            },
            {
                "part": 4,
                "part_title": "Phần IV: Con Đường Chuyên Môn Hóa - Ứng Dụng Thực Tế Theo Lĩnh Vực",
                "num": 11,
                "title": "Con Đường Kinh Doanh & Lãnh Đạo - Khởi Nghiệp và Kỹ Năng Con Người",
                "dir": "part-4/chapter-11",
                "sections": [
                    {"file": "01-entrepreneurial-mindset.md", "title": "Tư Duy Khởi Nghiệp"},
                    {"file": "02-starting-first-business.md", "title": "Bắt Đầu Doanh Nghiệp Đầu Tiên"},
                    {"file": "03-ai-powered-marketing-sales.md", "title": "Marketing và Bán Hàng Với AI"},
                    {"file": "04-operations-automation.md", "title": "Vận Hành và Tự Động Hóa"},
                    {"file": "05-leadership-team-building.md", "title": "Lãnh Đạo và Xây Dựng Đội Nhóm"},
                    {"file": "06-strategic-thinking.md", "title": "Tư Duy Chiến Lược"},
                    {"file": "07-scaling-next-level.md", "title": "Mở Rộng Quy Mô"}
                ]
            },
            
            # PART V: IMPLEMENTATION - Making It Real (Chapters 12-15)
            {
                "part": 5,
                "part_title": "Phần V: Triển Khai - Biến Thành Hiện Thực",
                "num": 12,
                "title": "Kế Hoạch Chuyển Đổi - Từ Trường Học Truyền Thống Sang Học Tập Với AI",
                "dir": "part-5/chapter-12",
                "sections": [
                    {"file": "01-assessing-current-situation.md", "title": "Đánh Giá Tình Hình Hiện Tại"},
                    {"file": "02-building-transition-timeline.md", "title": "Xây Dựng Lộ Trình Chuyển Đổi"},
                    {"file": "03-starting-small-experiments.md", "title": "Bắt Đầu Với Thí Nghiệm Nhỏ"},
                    {"file": "04-managing-family-resistance.md", "title": "Quản Lý Sự Phản Đối Trong Gia Đình"},
                    {"file": "05-working-with-schools.md", "title": "Làm Việc Với Nhà Trường"},
                    {"file": "06-budget-and-resources.md", "title": "Ngân Sách và Nguồn Lực"},
                    {"file": "07-measuring-progress-adjusting.md", "title": "Đo Lường Tiến Bộ và Điều Chỉnh"}
                ]
            },
            {
                "part": 5,
                "part_title": "Phần V: Triển Khai - Biến Thành Hiện Thực",
                "num": 13,
                "title": "Lộ Trình 10 Năm - Kế Hoạch Cụ Thể Cho Độ Tuổi 10-20",
                "dir": "part-5/chapter-13",
                "sections": [
                    {"file": "01-ages-10-11-foundation.md", "title": "Tuổi 10-11: Nền Tảng"},
                    {"file": "02-ages-12-13-skill-building.md", "title": "Tuổi 12-13: Xây Dựng Kỹ Năng"},
                    {"file": "03-ages-14-15-exploration.md", "title": "Tuổi 14-15: Khám Phá"},
                    {"file": "04-ages-16-17-focused-development.md", "title": "Tuổi 16-17: Phát Triển Tập Trung"},
                    {"file": "05-ages-18-20-launch-phase.md", "title": "Tuổi 18-20: Giai Đoạn Khởi Đầu"},
                    {"file": "06-handling-different-paces.md", "title": "Xử Lý Tốc Độ Khác Nhau"},
                    {"file": "07-year-by-year-metrics.md", "title": "Chỉ Số Theo Từng Năm"},
                    {"file": "08-complete-10-year-checklist.md", "title": "Danh Sách Kiểm Tra 10 Năm Hoàn Chỉnh"}
                ]
            },
            {
                "part": 5,
                "part_title": "Phần V: Triển Khai - Biến Thành Hiện Thực",
                "num": 14,
                "title": "Hướng Dẫn Sống Sót Cho Cha Mẹ - Quản Lý Hành Trình",
                "dir": "part-5/chapter-14",
                "sections": [
                    {"file": "01-your-role-as-ai-era-parent.md", "title": "Vai Trò Của Bạn Là Cha Mẹ Thời AI"},
                    {"file": "02-managing-learning-curve.md", "title": "Quản Lý Đường Cong Học Tập"},
                    {"file": "03-time-energy-management.md", "title": "Quản Lý Thời Gian và Năng Lượng"},
                    {"file": "04-handling-external-pressure.md", "title": "Xử Lý Áp Lực Bên Ngoài"},
                    {"file": "05-supporting-without-hovering.md", "title": "Hỗ Trợ Mà Không Áp Đặt"},
                    {"file": "06-parent-self-care-boundaries.md", "title": "Tự Chăm Sóc và Ranh Giới"},
                    {"file": "07-troubleshooting-common-problems.md", "title": "Xử Lý Sự Cố Thường Gặp"}
                ]
            },
            {
                "part": 5,
                "part_title": "Phần V: Triển Khai - Biến Thành Hiện Thực",
                "num": 15,
                "title": "Tương Lai Giáo Dục - Thế Hệ Đầu Tiên Bản Địa AI",
                "dir": "part-5/chapter-15",
                "sections": [
                    {"file": "01-education-in-2030.md", "title": "Giáo Dục Năm 2030"},
                    {"file": "02-workplace-of-2035.md", "title": "Môi Trường Làm Việc 2035"},
                    {"file": "03-society-culture-shifts.md", "title": "Thay Đổi Xã Hội và Văn Hóa"},
                    {"file": "04-first-ai-native-generation.md", "title": "Thế Hệ Đầu Tiên Bản Địa AI"},
                    {"file": "05-risks-challenges-ahead.md", "title": "Rủi Ro và Thách Thức Phía Trước"},
                    {"file": "06-opportunities-for-vietnamese.md", "title": "Cơ Hội Cho Người Việt Nam"},
                    {"file": "07-your-childs-legacy.md", "title": "Di Sản Của Con Bạn"}
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

    def clean_text_for_title(self, text):
        """Clean and escape text for titles (no markdown)"""
        if not text:
            return ""
        
        # Remove any null bytes or control characters
        text = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', text)
        
        # Escape HTML entities
        text = html.escape(text, quote=False)
        
        return text

    def convert_bold_text(self, text):
        """Convert **bold** markdown syntax to <strong> HTML tags after escaping content"""
        # First escape HTML special characters in the text
        text = html.escape(text, quote=False)
        # Then convert markdown bold to HTML bold (after escaping, ** is still **)
        text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
        return text

    def markdown_to_html(self, markdown_content, title):
        """Convert markdown to HTML with proper bold text handling"""
        if not markdown_content or not markdown_content.strip():
            return f"<h2>{self.clean_text_for_title(title)}</h2><p>Nội dung đang được cập nhật.</p>"

        # Remove null bytes and control characters, but DON'T escape yet
        markdown_content = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', markdown_content)

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
            return f"<h2>{self.clean_text_for_title(title)}</h2><p>Nội dung đang được cập nhật.</p>"

        return '\n'.join(html_paragraphs)

    def create_xhtml_template(self, title, content):
        """Create XHTML template"""
        clean_title = self.clean_text_for_title(title)
        
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
            part_num = chapter_info.get("part", "")
            part_title = chapter_info.get("part_title", "")

            print(f"\n📖 Processing {part_title}")
            print(f"   Chapter {chapter_num}: {chapter_title}...")

            # Process each section in the chapter
            for section_info in sections:
                section_counter += 1
                section_file = section_info["file"]
                section_title = section_info["title"]

                print(f"  📄 Section {section_counter}: {section_title}...")

                # Build path to section file
                section_path = self.base_book_dir / chapter_dir / section_file

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
        <img src="../images/cover.png" alt="Giáo Dục Thời Đại AI - Book Cover"/>
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
    <h1>Giáo Dục Thời Đại AI</h1>
    <p class="subtitle">Con Đường Học Tập Mới Cho Thế Hệ Không Bị Bỏ Lại Phía Sau</p>
    <p class="author">Tác giả: Bạn Giỏi Research Lab</p>
    <div class="publication-info">
        <p><strong>Chủ đề:</strong> Giáo Dục, AI, Học Tập Cá Nhân Hóa, Tương Lai Giáo Dục</p>
        <p><strong>Năm xuất bản:</strong> 2025</p>
        <p><strong>Ngôn ngữ:</strong> Tiếng Việt</p>
        <p><strong>Cấu trúc:</strong> 5 phần, 15 chương toàn diện</p>
        <p><strong>Phạm vi:</strong> Từ khủng hoảng giáo dục truyền thống đến mô hình học tập cá nhân hóa với AI</p>
        <p><strong>Nội dung:</strong> Khủng hoảng giáo dục, Cách mạng AI, Khoa học thần kinh, Mô hình thay thế, Khung học tập mới, Con đường chuyên môn, Triển khai thực tế</p>
    </div>
</body>
</html>'''

        with open(self.output_dir / "OEBPS" / "content" / "title-page.xhtml", "w", encoding="utf-8") as f:
            f.write(title_html)

        print("✅ Front matter created")

    def copy_css(self):
        """Copy CSS file"""
        print("Copying CSS file...")

        css_content = '''/* AI-Era Education EPUB CSS Styles */
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
                full_title = f"Chương {chapter_num}.{idx + 1}: {self.clean_text_for_title(section_title)}"
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
        title = "Giáo Dục Thời Đại AI: Con Đường Học Tập Mới Cho Thế Hệ Không Bị Bỏ Lại Phía Sau"
        description = "Hướng dẫn toàn diện về việc tái tưởng tượng giáo dục trong thời đại trí tuệ nhân tạo. Từ khủng hoảng giáo dục truyền thống đến mô hình học tập cá nhân hóa với AI. Bao gồm 5 phần, 15 chương: Khủng hoảng giáo dục (ch 1-3), Mô hình thay thế toàn cầu &amp; khoa học thần kinh (ch 4-5), Khung học tập mới với AI (ch 6-8), Con đường chuyên môn hóa: Sáng tạo, Kỹ thuật, Kinh doanh (ch 9-11), Triển khai thực tế cho gia đình (ch 12-15). Dựa trên nghiên cứu khoa học, case studies thực tế, và lộ trình triển khai chi tiết."

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
        <dc:subject>Giáo dục</dc:subject>
        <dc:subject>Trí tuệ nhân tạo</dc:subject>
        <dc:subject>Học tập cá nhân hóa</dc:subject>
        <dc:subject>AI trong giáo dục</dc:subject>
        <dc:subject>Tương lai giáo dục</dc:subject>
        <dc:subject>Giáo dục thay thế</dc:subject>
        <dc:subject>Khoa học thần kinh</dc:subject>
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
        print("🚀 Starting AI-Era Education EPUB generation...")
        print("📊 Target: 5 parts, 15 chapters with comprehensive sections")
        print("📚 Topics: Education Crisis, AI Revolution, Neuroscience, Alternative Models, New Learning Framework, Specialized Pathways, Practical Implementation")
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
            print("🎉 AI-Era Education EPUB generation completed!")
            print(f"📚 Output file: {self.epub_file}")
            print("📊 Structure: 5 parts, 15 chapters covering complete education transformation")
            print("🔗 Content: Traditional Crisis → AI Learning → Neuroscience → New Framework → Implementation")
            print("✅ Optimized for reading experience and Google Play Books compatibility")
            if not self.has_cover_image:
                print("⚠️  Note: Generated without cover image (add book_cover.png for cover)")
            print("🔄 Ready for distribution")

        except Exception as e:
            print(f"❌ Error during EPUB generation: {e}")
            raise

def main():
    generator = AIEducationEPUBGenerator()
    generator.generate()

if __name__ == "__main__":
    main()
