#!/usr/bin/env python3
"""Create a simple placeholder PNG image"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder_cover():
    """Create a simple text-based cover image"""
    # Create image
    width, height = 800, 1200
    img = Image.new('RGB', (width, height), color='#1a365d')
    draw = ImageDraw.Draw(img)
    
    # Add text
    try:
        font_title = ImageFont.truetype("arial.ttf", 60)
        font_subtitle = ImageFont.truetype("arial.ttf", 30)
    except:
        font_title = ImageFont.load_default()
        font_subtitle = ImageFont.load_default()
    
    # Title
    title = "BG Internal Book"
    subtitle = "Governance & Token Economics"
    
    # Get text size and center it
    bbox1 = draw.textbbox((0, 0), title, font=font_title)
    text_width1 = bbox1[2] - bbox1[0]
    text_height1 = bbox1[3] - bbox1[1]
    
    bbox2 = draw.textbbox((0, 0), subtitle, font=font_subtitle)
    text_width2 = bbox2[2] - bbox2[0]
    text_height2 = bbox2[3] - bbox2[1]
    
    # Draw text
    draw.text(((width - text_width1) // 2, height // 2 - 100), title, fill='white', font=font_title)
    draw.text(((width - text_width2) // 2, height // 2 + 50), subtitle, fill='#f7931a', font=font_subtitle)
    
    # Save
    img.save("book_cover.png")
    print("✅ Placeholder cover created: book_cover.png")

if __name__ == "__main__":
    try:
        create_placeholder_cover()
    except ImportError:
        print("⚠️  PIL/Pillow not available")
        print("Creating a minimal valid PNG file instead...")
        
        # Create minimal valid PNG (1x1 pixel transparent)
        png_data = bytes.fromhex(
            '89504e470d0a1a0a'  # PNG signature
            '0000000d49484452'  # IHDR chunk header
            '0000000100000001'  # width=1, height=1
            '08060000001f15c4'  # bit depth, color type, etc.
            '89'                # IHDR CRC
            '0000000a49444154'  # IDAT chunk header
            '78da6200010000'   # compressed data
            '00050001'
            '0d0a2db4'          # IDAT CRC
            '0000000049454e44'  # IEND chunk header
            'ae426082'          # IEND CRC
        )
        
        with open('book_cover.png', 'wb') as f:
            f.write(png_data)
        
        print("✅ Minimal PNG cover created: book_cover.png")
