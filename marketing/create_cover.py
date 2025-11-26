from PIL import Image, ImageDraw, ImageFont
import textwrap

# Create a simple cover image (800x1200)
width, height = 800, 1200
img = Image.new('RGB', (width, height), color='#1a365d')  # Dark blue background

draw = ImageDraw.Draw(img)

# Try to use a default font
try:
    title_font = ImageFont.truetype("arial.ttf", 60)
    subtitle_font = ImageFont.truetype("arial.ttf", 30)
except:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()

# Add title
title = "KIẾM TIỀN TỪ QUẢNG CÁO"
title2 = "CHO NỀN TẢNG GIÁO DỤC"

# Center the text
title_bbox = draw.textbbox((0, 0), title, font=title_font)
title_width = title_bbox[2] - title_bbox[0]
title_x = (width - title_width) // 2

title2_bbox = draw.textbbox((0, 0), title2, font=title_font)
title2_width = title2_bbox[2] - title2_bbox[0]
title2_x = (width - title2_width) // 2

draw.text((title_x, 200), title, fill='white', font=title_font)
draw.text((title2_x, 280), title2, fill='white', font=title_font)

# Add subtitle
subtitle = "Google Adsense • Facebook Ads"
subtitle2 = "AI Agents • Analytics"

subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
subtitle_x = (width - subtitle_width) // 2

subtitle2_bbox = draw.textbbox((0, 0), subtitle2, font=subtitle_font)
subtitle2_width = subtitle2_bbox[2] - subtitle2_bbox[0]
subtitle2_x = (width - subtitle2_width) // 2

draw.text((subtitle_x, 500), subtitle, fill='#4299e1', font=subtitle_font)
draw.text((subtitle2_x, 550), subtitle2, fill='#4299e1', font=subtitle_font)

# Add year
year = "2025"
year_bbox = draw.textbbox((0, 0), year, font=subtitle_font)
year_width = year_bbox[2] - year_bbox[0]
year_x = (width - year_width) // 2
draw.text((year_x, 1050), year, fill='white', font=subtitle_font)

# Save
img.save('book_cover.png')
print("✅ Cover image created: book_cover.png")
