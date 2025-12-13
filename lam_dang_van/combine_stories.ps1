# Script để kết hợp tất cả câu chuyện từ 1-16 thành file HTML
$storyDir = "Sach_101_Cau_Chuyen_Lam_Van/04_Cau_Chuyen/Phan_1_Cau_Chuyen_01_20"
$outputFile = "Cau_Chuyen_01_16_Combined.html"

# Tạo header HTML
$htmlContent = @"
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>101 Câu Chuyện Làm Văn - Phần 1 (Câu chuyện 1-16)</title>
    <style>
        body {
            font-family: 'Times New Roman', serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f9f9f9;
        }
        .story {
            background-color: white;
            margin: 30px 0;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .story h1 {
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        .story p {
            text-align: justify;
            margin-bottom: 15px;
            text-indent: 30px;
        }
        .toc {
            background-color: #ecf0f1;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
        }
        .toc h2 {
            color: #2c3e50;
            margin-bottom: 15px;
        }
        .toc ul {
            list-style-type: none;
            padding-left: 0;
        }
        .toc li {
            margin: 8px 0;
            padding: 5px;
            background-color: white;
            border-radius: 5px;
        }
        .toc a {
            text-decoration: none;
            color: #3498db;
            font-weight: bold;
        }
        .toc a:hover {
            color: #2980b9;
        }
    </style>
</head>
<body>
    <div class="toc">
        <h2>📚 MỤC LỤC - 101 CÂU CHUYỆN LÀM VĂN (PHẦN 1)</h2>
        <ul>
"@

# Lấy danh sách tất cả file câu chuyện và sắp xếp theo thứ tự
$storyFiles = Get-ChildItem -Path $storyDir -Filter "*.md" | Sort-Object Name

# Tạo mục lục
foreach ($file in $storyFiles) {
    $storyNumber = ($file.Name -split "_")[2]
    $storyTitle = ($file.Name -replace "Cau_Chuyen_\d+_", "" -replace "\.md$", "") -replace "_", " "
    $storyTitle = $storyTitle.ToUpper()
    $htmlContent += "            <li><a href=`"#story$storyNumber`">CÂU CHUYỆN $storyNumber`: $storyTitle</a></li>`n"
}

$htmlContent += @"
        </ul>
    </div>

"@

# Đọc và thêm nội dung từng câu chuyện
foreach ($file in $storyFiles) {
    Write-Host "Đang xử lý: $($file.Name)"
    
    $storyNumber = ($file.Name -split "_")[2]
    $content = Get-Content -Path $file.FullName -Encoding UTF8 -Raw
    
    # Chuyển đổi Markdown sang HTML
    $htmlStory = $content -replace "^# (.+)$", "<h1 id=`"story$storyNumber`">`$1</h1>" -replace "`n`n", "</p>`n<p>" -replace "^(?!<h1|<p>)", "<p>" -replace "$", "</p>"
    $htmlStory = $htmlStory -replace "<p></p>", ""
    
    $htmlContent += @"
    <div class="story">
        $htmlStory
    </div>

"@
}

# Kết thúc HTML
$htmlContent += @"
</body>
</html>
"@

# Ghi file HTML
$htmlContent | Out-File -FilePath $outputFile -Encoding UTF8
Write-Host "Đã tạo file: $outputFile"
