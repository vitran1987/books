# TÓM TẮT CHƯƠNG 8: STABLECOIN - ĐỒNG TIỀN ỔN ĐỊNH VÀ BÀI HỌC TỪ SỰ SUY SỤP TERRA/LUNA

## Tổng Quan Chương

Chương 8 khám phá sâu về stablecoin - một trong những đổi mới quan trọng nhất trong hệ sinh thái cryptocurrency, được thiết kế để giải quyết vấn đề biến động giá. Từ các mô hình được thế chấp bằng fiat (USDT, USDC), stablecoin phi tập trung được thế chấp bằng crypto (DAI), đến stablecoin thuật toán (Terra/Luna), chương này cung cấp cái nhìn toàn diện về cách các loại stablecoin hoạt động, những rủi ro của chúng, và bài học đau đớn từ một trong những thảm họa tài chính lớn nhất trong lịch sử crypto - sự sụp đổ Terra/Luna xóa sạch hơn 40 tỷ đô la chỉ trong một tuần tháng 5/2022.

---

## 1. SỰ RA ĐỜI CỦA STABLECOIN: GIẢI PHÁP CHO BÀI TOÁN BIẾN ĐỘNG

### Vấn Đề Cơ Bản

**Biến Động Giá Cực Cao:**
- Bitcoin và hầu hết cryptocurrency có thể tăng/giảm 10-20% trong một ngày
- Khiến việc sử dụng làm phương tiện thanh toán hàng ngày không thực tế
- Người dùng và doanh nghiệp không muốn rủi ro giá trị tiền tệ khi mua hàng hóa/dịch vụ

**Ví Dụ Minh Họa:**
- Quán cà phê chấp nhận Bitcoin: Ly cà phê $5
- Sáng: Khách trả 0.0001 BTC (Bitcoin = $50,000)
- Chiều: Bitcoin giảm xuống $45,000 → 0.0001 BTC chỉ còn trị giá $4.50 (-10%)
- Hoặc Bitcoin tăng lên $55,000 → 0.0001 BTC = $5.50 (khách cảm thấy trả quá nhiều)

### Giải Pháp Stablecoin

**Định Nghĩa:**
- Cryptocurrency được thiết kế để duy trì giá trị ổn định
- Gắn kết với tài sản dự trữ (thường là tiền fiat như USD, EUR)
- Kết hợp ưu điểm của crypto + sự ổn định của tiền truyền thống

**Lợi Ích:**
- Giao dịch xuyên biên giới nhanh chóng, phí thấp
- Lưu trữ giá trị mà không lo biến động
- Sử dụng cơ sở hạ tầng blockchain (minh bạch, bảo mật)
- "Bến đỗ an toàn" trong cơn bão thị trường crypto

**Quy Mô Thị Trường (2025):**
- Tổng vốn hóa: >$150 tỷ
- Từ vài tỷ (2019) → đỉnh ~$180 tỷ (2022) → phục hồi $150 tỷ+ (2025)
- Khối lượng giao dịch hàng ngày thường >$100 tỷ (vượt cả Bitcoin)

### Ứng Dụng Chính

1. **Giao dịch:** Di chuyển giá trị giữa các sàn giao dịch và blockchain
2. **DeFi:** Phương tiện chính trong cho vay, thanh khoản, yield farming
3. **Thanh toán xuyên biên giới:** Nhanh hơn, rẻ hơn SWIFT truyền thống
4. **Bảo toàn giá trị:** Tránh biến động trong thị trường crypto

---

## 2. STABLECOIN ĐƯỢC THẾ CHẤP BẰNG FIAT: MÔ HÌNH TRUYỀN THỐNG NHƯNG HIỆU QUẢ

### Tether (USDT) - Stablecoin Lớn Nhất

**Thông Tin Cơ Bản:**
- Ra mắt: 2014 bởi Tether Limited
- Vốn hóa (2025): $83 tỷ (>50% thị trường stablecoin)
- Khối lượng giao dịch hàng ngày: Thường >$50 tỷ (nhiều hơn Bitcoin)

**Cơ Chế Hoạt Động:**
- Mỗi USDT được phát hành → Tether Limited giữ $1 USD trong dự trữ
- Người dùng có thể đổi 1 USDT lấy $1 thật
- Tạo "neo giá" tự nhiên: Nếu USDT < $1 → Mua rẻ, đổi lấy $1 (kiếm lời)
- Nếu USDT > $1 → Gửi $1 lấy USDT mới, bán với giá cao hơn (kiếm lời)

**Tranh Cãi và Vấn Đề Minh Bạch:**
- Nhiều năm từ chối công bố kiểm toán đầy đủ
- 2017: Tách khỏi ngân hàng chính, câu hỏi về dự trữ
- **2019:** Tổng chưởng lý New York kiện Tether/Bitfinex
  - Cáo buộc: Che giấu mất $850 triệu từ dự trữ
  - Sử dụng dự trữ Tether để che đập khoản lỗ
- **2021:** Nộp phạt $18.5 triệu, cam kết minh bạch hơn

**Báo Cáo Dự Trữ (5/2021) - Gây Tranh Cãi:**
- Chỉ 3.87% dự trữ là tiền mặt thực sự
- Phần lớn còn lại: Commercial paper (giấy tờ thương mại), khoản vay được bảo đảm
- Commercial paper: Nợ ngắn hạn do công ty phát hành, có rủi ro tín dụng
- Nếu các công ty này gặp khó khăn → Giá trị dự trữ giảm

**Cải Thiện (2023-2025):**
- Giảm đáng kể commercial paper
- Tăng tiền mặt, tín phiếu kho bạc Mỹ (US Treasury bills)
- Đến 2025: >85% dự trữ là tiền mặt + tín phiếu kho bạc
- Báo cáo chứng thực hàng quý từ BDO (công ty kiểm toán quốc tế)

### USDC (USD Coin) - Minh Bạch và Tuân Thủ

**Thông Tin Cơ Bản:**
- Ra mắt: 7/2018 bởi Circle (hỗ trợ bởi Goldman Sachs)
- Vốn hóa đỉnh: $55 tỷ (2021)
- Vị trí: Stablecoin lớn thứ hai sau Tether

**Chiến Lược Khác Biệt:**
- **Minh bạch:** Kiểm toán hàng tháng bởi Grant Thornton từ đầu
- **Dự trữ chất lượng cao:** 100% tiền mặt + tín phiếu kho bạc Mỹ ngắn hạn
- **Tuân thủ quy định:** Quan hệ với ngân hàng uy tín

**Thành Công:**
- Tăng trưởng từ ~$0 (2018) → $55 tỷ (2021)
- Stablecoin được nhà đầu tư tổ chức và doanh nghiệp ưa chuộng nhất
- **Quan hệ đối tác:**
  - Visa, Mastercard: Hỗ trợ thanh toán USDC
  - BlackRock ($10+ nghìn tỷ tài sản): Quỹ thanh khoản cho dự trữ USDC

### Khủng Hoảng Silicon Valley Bank (3/2023)

**Sự Kiện:**
- Silicon Valley Bank (SVB) bị đóng cửa đột ngột
- Circle có $3.3 tỷ (≈8% tổng dự trữ) bị kẹt tại SVB
- USDC mất neo giá, giảm xuống $0.88

**Phản Ứng:**
- Hoảng loạn trong thị trường crypto
- Circle công bố: Phần còn lại dự trữ ($37 tỷ+) vẫn an toàn
- Chính phủ Mỹ: Bảo vệ đầy đủ người gửi tiền tại SVB
- USDC phục hồi về $1 trong vài ngày

**Bài Học:**
- Ngay cả stablecoin được quản lý tốt vẫn phụ thuộc hệ thống ngân hàng truyền thống
- Có thể bị ảnh hưởng bởi rủi ro hệ thống

### Mô Hình Kinh Doanh Stablecoin Fiat

**Nguồn Lợi Nhuận:**
- Không tính phí giao dịch cho người dùng
- Kiếm lãi suất từ dự trữ (tín phiếu kho bạc, tiền gửi ngân hàng)

**Ví Dụ Lợi Nhuận (2023-2024):**
- Lãi suất Federal Reserve: 5-5.5%
- **USDC ($55 tỷ dự trữ):** Kiếm ~$2.75 tỷ/năm chỉ từ lãi suất
- **Tether ($83 tỷ dự trữ):** Kiếm >$4 tỷ/năm
- **Tether báo cáo (2023):** Lợi nhuận ròng >$4.5 tỷ trong năm

**Đặc Điểm:**
- Kinh doanh cực kỳ sinh lời trong môi trường lãi suất cao
- Lợi nhuận giảm trong môi trường lãi suất thấp

---

## 3. DAI VÀ STABLECOIN ĐƯỢC THẾ CHẤP BẰNG CRYPTO: PHI TẬP TRUNG THỰC SỰ

### MakerDAO và DAI

**Khái Niệm:**
- Stablecoin phi tập trung thực sự
- Không cần công ty giữ dự trữ fiat, không cần ngân hàng
- Được hỗ trợ bởi cryptocurrency (ETH, WBTC, USDC,...)
- Vốn hóa (2025): ~$5 tỷ (stablecoin phi tập trung lớn nhất)

### Cơ Chế Thế Chấp Quá Mức (Over-Collateralization)

**Cách Hoạt Động:**
- Muốn tạo 1,000 DAI → Phải gửi ít nhất $1,500 giá trị ETH (tỷ lệ 150%)
- Gửi tài sản vào "Vault" (smart contract)
- Tạo ra DAI (thực chất là vay DAI với ETH làm tài sản thế chấp)
- Phải trả "phí ổn định" (stability fee) - lãi suất vay

**Tỷ Lệ Thế Chấp:**
- ETH: Thường 150%
- Tài sản biến động hơn: 175-200%

**Ví Dụ Cụ Thể:**
- Alice gửi 1 ETH ($3,000) vào Vault
- Tạo ra 2,000 DAI
- Tỷ lệ thế chấp: 150% (3,000/2,000 = 1.5)
- **Nếu ETH tăng lên $4,000:** Tỷ lệ cải thiện lên 200% (an toàn hơn)
- **Nếu ETH giảm xuống $2,000:** Tỷ lệ giảm xuống 100% (< 150% ngưỡng thanh lý) → Vault bị thanh lý

### Cơ Chế Thanh Lý

**Khi Tỷ Lệ < 150%:**
- Vault tự động bị thanh lý
- ETH thế chấp được bán đấu giá để thu hồi DAI
- Phạt thanh lý: Thường 13%
- Đảm bảo luôn có đủ tài sản thế chấp hỗ trợ DAI lưu hành

### Duy Trì Neo Giá $1

**Cơ Chế Thị Trường:**
- **DAI > $1 (ví dụ $1.05):**
  - Arbitrageur tạo DAI mới (chi phí $1), bán thị trường ($1.05), kiếm lời $0.05
  - → Tăng cung DAI → Giá giảm về $1
  
- **DAI < $1 (ví dụ $0.95):**
  - Arbitrageur mua DAI rẻ ($0.95), dùng để trả nợ vault (giá trị $1), kiếm lời $0.05
  - → Giảm cung DAI → Giá tăng về $1

**Công Cụ Quản Trị:**
- Điều chỉnh "phí ổn định" để ảnh hưởng cung cầu
- Người nắm giữ MKR token bỏ phiếu về các thay đổi tham số
- Phí ổn định tăng → Đắt hơn để tạo DAI → Giảm cung
- Phí ổn định giảm → Rẻ hơn để tạo DAI → Tăng cung

### Black Thursday - Bài Kiểm Tra Thực Chiến (12/3/2020)

**Sự Kiện:**
- ETH giảm >50% trong vài giờ (từ ~$200 xuống <$100)
- Hàng nghìn Vault bị thanh lý đồng loạt
- Tắc nghẽn mạng Ethereum (phí gas hàng trăm đô la/giao dịch)

**Vấn Đề:**
- Một số đấu giá thanh lý kết thúc với giá $0
- Keepers mua ETH thế chấp mà không phải trả DAI
- Tạo ra khoản nợ xấu $5.7 triệu (DAI không được hỗ trợ đầy đủ)

**Phản Ứng:**
- Tổ chức đấu giá nợ (debt auction)
- Bán MKR mới để thu về DAI lấp đầy khoản thiếu hụt
- Thành công, hệ thống ổn định trở lại

**Cải Thiện Sau Đó:**
- Cơ chế đấu giá thanh lý mới hiệu quả hơn
- Đa dạng hóa tài sản thế chấp (WBTC, USDC, UNI, COMP,...)
- **Peg Stability Module (PSM):** Hoán đổi trực tiếp DAI ↔ USDC (1:1) để duy trì neo giá tốt hơn

### Tranh Cãi Về Phi Tập Trung (2025)

**Vấn Đề:**
- Phần đáng kể tài sản thế chấp của MakerDAO là USDC và Real-World Assets (RWA)
- USDC là stablecoin tập trung, có thể bị Circle đóng băng/kiểm duyệt
- Câu hỏi: DAI còn thực sự "phi tập trung" hay không?

**Cân Bằng:**
- Thêm USDC/RWA giúp mở rộng quy mô, cải thiện tính ổn định
- Nhưng giảm mức độ phi tập trung
- Một số chấp nhận vì lợi ích thực tế, một số phản đối vì nguyên tắc

---

## 4. TERRA/LUNA: GIẤC MƠ STABLECOIN THUẬT TOÁN VÀ CƠN ÁC MỘNG

### Tổng Quan Terra Ecosystem

**Vào Mùa Xuân 2022:**
- Do Kwon (doanh nhân Hàn Quốc): Nhân vật quyền lực nhất crypto
- **Tổng vốn hóa:** >$60 tỷ (UST + LUNA)
- **UST:** Stablecoin lớn thứ 3 thế giới (sau USDT, USDC)
- **Anchor Protocol:** Cung cấp lợi suất 20%/năm cho người gửi UST
  - Hàng tỷ đô la chảy vào Anchor
  - So với lãi suất ngân hàng ~0% hoặc DeFi khác 4-5%

**Tuyên Bố Của Do Kwon:**
- Terra đang xây dựng tương lai của tiền tệ
- Stablecoin fiat như USDC "lỗi thời" và "không thể mở rộng"

### Cơ Chế Stablecoin Thuật Toán

**Không Có Tài Sản Thế Chấp Bên Ngoài:**
- Khác USDC (dự trữ đô la thật) và DAI (tài sản crypto vượt mức)
- Dựa vào cơ chế thuật toán và mối quan hệ cộng sinh UST ↔ LUNA

**Cơ Chế Burn-and-Mint:**
- Luôn có thể đốt 1 UST → Tạo ra $1 giá trị LUNA
- Luôn có thể đốt $1 giá trị LUNA → Tạo ra 1 UST

**Lý Thuyết Neo Giá:**
- **UST = $1.05 (cao hơn mục tiêu):**
  - Đốt $1 LUNA → Tạo 1 UST (chi phí $1)
  - Bán UST với giá $1.05 → Kiếm lời $0.05
  - → Tăng cung UST → Giá giảm về $1
  
- **UST = $0.95 (thấp hơn mục tiêu):**
  - Mua UST với giá $0.95
  - Đốt UST → Nhận $1 giá trị LUNA → Kiếm lời $0.05
  - → Giảm cung UST → Giá tăng về $1

**Trên lý thuyết:** Tự điều chỉnh, không cần dự trữ fiat, không cần thế chấp quá mức

### Điểm Yếu Cơ Bản - Vòng Xoáy Tử Thần (Death Spiral)

**Giả Định Nguy Hiểm:**
- Toàn bộ hệ thống phụ thuộc vào giả định: LUNA luôn có giá trị và luôn có người sẵn sàng mua

**Kịch Bản Sụp Đổ:**
1. Làn sóng bán tháo UST lớn (vì hoảng loạn/mất niềm tin)
2. Giá UST giảm < $1
3. Người ta mua UST rẻ, đốt để nhận LUNA
4. Hệ thống phải tạo ra (mint) LUNA mới
5. **Càng nhiều UST bị đốt → Càng nhiều LUNA mới được tạo ra**
6. **Cung LUNA tăng → Giá LUNA giảm**
7. **Giá LUNA giảm → Niềm tin vào hệ thống giảm**
8. **Nhiều người bán UST hơn → Vòng lặp lại từ bước 3**
9. **→ Vòng xoáy tử thần: Không thể dừng lại khi đã bắt đầu**

**Cảnh Báo Sớm Bị Bỏ Qua:**
- Các nhà phê bình so sánh Terra với mô hình Ponzi/kim tự tháp
- Giá trị duy trì chỉ khi có dòng tiền mới liên tục chảy vào
- Khi niềm tin lung lay và vốn đảo chiều → Toàn bộ sụp đổ
- Do Kwon bác bỏ lời chỉ trích, công kích người hoài nghi

### Anchor Protocol - Quả Bom Hẹn Giờ

**Hứa Hẹn:**
- "Tiết kiệm blockchain"
- Gửi UST, nhận lợi suất 20%/năm
- Đầu 2022: Thu hút >$14 tỷ UST

**Câu Hỏi Quan Trọng:** 20% lợi suất đến từ đâu?

**Thực Tế:**
- Anchor cho vay UST với lãi suất cao hơn
- Người vay gửi tài sản thế chấp (chủ yếu bLUNA - LUNA được staked)
- Lợi nhuận từ hoạt động cho vay + staking rewards

**Vấn Đề:**
- Lợi nhuận thực tế từ hoạt động này: Chỉ 3-5%/năm
- Khoảng cách (20% - 5% = 15%) được lấp đầy bằng "quỹ dự trữ" do Terra Foundation trợ cấp
- **Terra Foundation đang trợ cấp lợi suất 20% để thu hút người dùng**

**Mô Hình Không Bền Vững:**
- Quỹ dự trữ Anchor cạn dần:
  - 2/2022: >70 triệu UST
  - 4/2022: <30 triệu UST
- Với tốc độ tiêu hao này: Cạn kiệt trong vài tháng
- Khi cạn kiệt → Phải cắt lợi suất xuống 3-5%
- → Người gửi tiền rút tiền hàng loạt
- → Áp lực bán lớn lên UST
- → Có thể kích hoạt vòng xoáy tử thần

**Tranh Luận Nội Bộ:**
- Cộng đồng nhận thức vấn đề
- Thảo luận về giảm lợi suất xuống mức bền vững
- Do Kwon phản đối: Giảm lợi suất = Mất lợi thế cạnh tranh, có thể kích hoạt chạy ngân hàng

### Luna Foundation Guard (LFG)

**Lưới An Toàn:**
- Tổ chức phi lợi nhuận thiết lập để bảo vệ UST
- Mua và giữ dự trữ Bitcoin lớn
- Cuối cùng đạt: ~$3.5 tỷ Bitcoin
- Mục đích: Hỗ trợ UST trong trường hợp khủng hoảng

**Như sau này chứng minh:** Không đủ để ngăn chặn cuộc tấn công/mất niềm tin quy mô lớn

---

## 5. SỰ SỤP ĐỔ THÁNG 5 NĂM 2022: THẢM HỌA NHANH NHẤT LỊCH SỬ CRYPTO

### Ngày 7 Tháng 5, 2022 - Những Dấu Hiệu Đầu Tiên

**Sự Kiện:**
- UST mất neo giá bí ẩn: Giảm xuống $0.98
- Rút tiền lớn từ Anchor: ~$2 tỷ UST trong vài giờ
- Tạo áp lực bán lớn lên UST

**Đồn Đoán:**
- Cuộc tấn công có phối hợp từ quỹ hedge/đối thủ?
- Hoặc nhà đầu tư lớn mất niềm tin, quyết định thoát?

**Can Thiệp LFG:**
- Sử dụng Bitcoin dự trữ mua UST trên thị trường
- UST phục hồi lên $0.99 trong vài giờ
- Do Kwon tweet: "Deploying more capital - steady lads"
- Nhưng LFG đã tiêu tốn lượng Bitcoin đáng kể

### Ngày 8 Tháng 5, 2022 - Áp Lực Tăng Lên

**Tình Hình Xấu Đi:**
- UST giảm xuống $0.95 vào sáng sớm
- Phục hồi khó khăn hơn
- LFG tiếp tục bơm Bitcoin, nhưng hiệu quả giảm

**Hiệu Ứng Phụ:**
- LFG bán Bitcoin để mua UST
- → Áp lực bán lên Bitcoin
- → Giá Bitcoin giảm
- → Giá trị dự trữ LFG giảm

**LUNA Bắt Đầu Sụp Đổ:**
- Từ ~$80 xuống $60 trong một ngày (-25%)
- Thị trường lo ngại hệ thống phải mint nhiều LUNA hơn

**Hoảng Loạn Lan Rộng:**
- Nhiều người rút UST khỏi Anchor và DeFi
- Hiệu ứng domino: Càng bán nhiều → Giá càng giảm → Càng nhiều người hoảng sợ
- **Cuối ngày:** UST = $0.91, LUNA mất >40% giá trị
- TVL hệ sinh thái Terra bắt đầu giảm mạnh

### Ngày 9 Tháng 5, 2022 - Vòng Xoáy Tử Thần Bắt Đầu

**Thảm Họa Thực Sự:**
- **UST:** $0.70 (sáng) → $0.60 (chiều)
- Cơ chế arbitrage hoạt động như thiết kế: Mua UST rẻ, đốt để nhận LUNA

**Bùng Nổ Cung LUNA:**
- Hệ thống phải tạo ra lượng LUNA khổng lồ
- Trong 24 giờ: Cung LUNA tăng từ ~350 triệu lên >1 tỷ token
- **Tăng gần gấp 3 lần trong một ngày**

**Giá LUNA Sụp Đổ:**
- $60 → $30 → $20 → $10 (tất cả trong một ngày)

**Vòng Xoáy Tự Củng Cố:**
1. UST giảm
2. Đốt UST → Nhận LUNA
3. Hệ thống tạo nhiều LUNA
4. Giá LUNA giảm
5. Niềm tin giảm
6. Nhiều người bán UST hơn
7. Vòng lặp lại

**Can Thiệp Thất Bại:**
- Tạm dừng blockchain Terra để ngăn việc tạo LUNA mới
- Kêu gọi sàn giao dịch hỗ trợ
- LFG công bố đã sử dụng hầu hết dự trữ Bitcoin (~$3 tỷ)
- Thông tin mơ hồ, chậm trễ → Xói mòn thêm niềm tin

### Ngày 10 Tháng 5, 2022 - Sụp Đổ Hoàn Toàn

**Con Số Thảm Khốc:**
- **UST:** Giảm xuống <$0.30
- **LUNA:** Giảm xuống <$1 (từ $80 vài ngày trước)
- **Cung LUNA:** Bùng nổ lên >6 tỷ token

**Tình Trạng Hỗn Loạn:**
- Giá LUNA: Vài cent → Vài phần nghìn đô la
- Nhiều sàn đình chỉ giao dịch LUNA/UST do biến động quá mức
- Hệ thống quá tải

**Nhà Đầu Tư Mất Tất Cả:**
- Tài sản bay hơi trước mắt
- Tiết kiệm cả đời, tiền học phí con cái, tiền vay ngân hàng → Mất gần như tất cả

**Câu Chuyện Đau Lòng:**
- Người dùng mất $2 triệu (tiết kiệm 20 năm làm việc)
- Người vay tiền ngân hàng mua LUNA, giờ nợ ngân hàng với không còn gì trả
- Báo cáo trầm cảm, ý định tự tử → Cộng đồng đăng đường dây nóng sức khỏe tâm thần

### Ngày 11-13 Tháng 5, 2022 - Hậu Quả và Lây Lan

**LUNA Tiếp Tục Sụp Đổ:**
- Giá giảm gần như $0
- Cung token bùng nổ: Hàng trăm tỷ → Hàng nghìn tỷ token (con số phi thực tế)
- Cơ chế mint hoàn toàn mất kiểm soát

**UST Không Bao Giờ Phục Hồi:**
- Dao động $0.10-$0.20

**Blockchain Terra Dừng Hoạt Động:**
- 13/5: Dừng hoàn toàn để ngăn việc tạo thêm LUNA

**Thiệt Hại Tổng Thể:**
- Vốn hóa LUNA + UST: Từ >$60 tỷ xuống <$1 tỷ
- **Xóa sạch >$40 tỷ trong một tuần**
- >200,000 người nắm giữ LUNA mất phần lớn/toàn bộ đầu tư
- Hàng chục nghìn người có UST trong Anchor

### Hiệu Ứng Lây Lan (Contagion)

**Three Arrows Capital (3AC):**
- Quỹ hedge crypto lớn nhất với hàng tỷ đô la
- Exposure lớn đến LUNA
- Không đáp ứng margin calls
- **Phá sản 6/2022:** Nợ >$3 tỷ

**Celsius Network:**
- Nền tảng cho vay crypto lớn, hàng triệu người dùng
- Bị ảnh hưởng nặng bởi Terra + khoản lỗ từ 3AC
- **6/2022:** Đóng băng tất cả rút tiền
- **7/2022:** Nộp đơn phá sản với $4.7 tỷ nợ người gửi tiền

**Voyager Digital:**
- Nền tảng giao dịch crypto
- Cho 3AC vay $650 triệu, không thu hồi được
- **Phá sản**

**BlockFi:**
- Công ty cho vay crypto
- Nhận cứu trợ khẩn cấp từ FTX
- (FTX sau đó cũng sụp đổ 11/2022 trong vụ bê bối riêng)

**Tổng Thiệt Hại:**
- Terra + hiệu ứng lây lan: **>$60 tỷ**
- Một trong những thảm họa tài chính lớn nhất lịch sử crypto
- So sánh: Mt. Gox (2014): 850,000 BTC; The DAO (2016)
- **Điểm khác biệt:** Tốc độ - Terra sụp đổ hoàn toàn chỉ trong **một tuần**

---

## 6. BÀI HỌC ĐAU ĐỚN VÀ TƯƠNG LAI STABLECOIN

### Bài Học 1: Stablecoin Thuật Toán Không Có Tài Sản Thế Chấp Là Cực Kỳ Dễ Bị Tổn Thương

**Vấn Đề Cơ Bản:**
- Không thể tạo ra giá trị từ hư không chỉ bằng thuật toán
- Khi niềm tin mất → Toàn bộ sụp đổ vì không có gì hỗ trợ bên dưới
- Cơ chế burn-and-mint UST ↔ LUNA là trò chơi tổng bằng không
- Khi cần tạo quá nhiều LUNA → Pha loãng cung → LUNA mất giá trị → Cơ chế không còn hoạt động

**So Sánh với DAI:**
- DAI yêu cầu 150% tài sản thế chấp thực (ETH, WBTC,...)
- Nếu giá trị tài sản giảm quá thấp → Vault thanh lý, tài sản bán để đảm bảo DAI được hỗ trợ
- **Có tài sản thực sự hữu hình hỗ trợ mỗi DAI**
- UST chỉ "hỗ trợ" bởi LUNA - không có giá trị nội tại, chỉ dựa vào nhu cầu thị trường và niềm tin

### Bài Học 2: Lợi Suất Bền Vững

**Nguyên Tắc Tài Chính Cơ Bản:**
- "Không có bữa trưa miễn phí" (No free lunch)
- Lợi nhuận cao luôn đi kèm rủi ro cao
- Lợi nhuận "không rủi ro" 20% là không thể tồn tại trong điều kiện thị trường bình thường

**Câu Hỏi Quan Trọng:**
- Nếu dự án hứa lợi suất vượt xa thị trường tổng thể → Tiền đến từ đâu?
- **Anchor:** Từ trợ cấp quỹ dự trữ = Mô hình Ponzi
  - Người gửi sớm được trả bằng tiền người gửi sau + bán LUNA
  - Chỉ kéo dài khi có dòng vốn mới liên tục
  - Khi vốn ngừng/đảo chiều → Sụp đổ

**Cảnh Báo Cho Nhà Đầu Tư:**
- Nếu không hiểu cách sản phẩm tài chính tạo lợi nhuận → Đừng đầu tư
- FOMO (fear of missing out) nguy hiểm: "Mọi người đều kiếm tiền" hoặc "Tôi có thể thoát trước khi sụp đổ"
- Nhiều người nghe cảnh báo nhưng bỏ qua → Mất toàn bộ tài sản

### Bài Học 3: Rủi Ro Hệ Thống và Hiệu Ứng Lây Lan

**Hệ Sinh Thái Kết Nối Cao:**
- Một thất bại lớn có thể lan rộng xa hơn nhiều so với dự án ban đầu
- 3AC, Celsius, Voyager, BlockFi: Tất cả bị ảnh hưởng qua khoản vay, đầu tư, quan hệ đối tác

**Tầm Quan Trọng Quản Lý Rủi Ro:**
- Không đặt quá nhiều vốn vào một dự án/hệ sinh thái duy nhất
- Đa dạng hóa là then chốt

**So Sánh Tài Chính Truyền Thống:**
- Có nhiều công cụ quản lý rủi ro hệ thống:
  - Yêu cầu vốn tối thiểu
  - Kiểm tra stress test
  - Giới hạn concentration risk
  - Bảo hiểm tiền gửi
  
**Trong Crypto:**
- Phần lớn biện pháp bảo vệ không tồn tại/rất yếu
- Celsius, 3AC vận hành với đòn bẩy cực cao, concentration risk lớn, không giám sát bên ngoài
- Khi thị trường quay đầu → Không có bộ đệm → Sụp đổ nhanh

### Bài Học 4: Văn Hóa Kiêu Ngạo và Bỏ Qua Cảnh Báo

**Do Kwon và Terra:**
- Kiêu ngạo đáng kể
- Bác bỏ người chỉ trích
- Tuyên bố Terra đã "giải quyết" vấn đề stablecoin
- Công kích đối thủ và người hoài nghi trên mạng xã hội
- Tạo văn hóa: Câu hỏi về rủi ro = FUD (fear, uncertainty, doubt) không đáng chú ý

**Hậu Quả:**
- Nhiều người trong cộng đồng Terra không nhận ra dấu hiệu cảnh báo
- Không chuẩn bị cho kịch bản xấu nhất

**Văn Hóa Khỏe Mạnh Hơn:**
- Khuyến khích câu hỏi khó
- Thảo luận trung thực về rủi ro
- Thừa nhận hạn chế công nghệ và mô hình kinh doanh

---

## 7. PHẢN ỨNG CƠ QUAN QUẢN LÝ VÀ QUY ĐỊNH MỚI

### Hoa Kỳ

**SEC (Ủy ban Chứng khoán và Giao dịch):**
- Mở cuộc điều tra Terraform Labs và Do Kwon ngay sau sự sụp đổ
- **2/2023:** Buộc tội gian lận chứng khoán
  - Cáo buộc: Đánh lừa nhà đầu tư về tính ổn định UST và khả năng bền vững lợi suất Anchor
  
**Do Kwon - Người Bị Truy Nã:**
- Rời Hàn Quốc trước khi sụp đổ
- Trở thành người bị truy nã quốc tế
- **3/2023:** Bị bắt tại Montenegro khi dùng hộ chiếu giả
- **Đến 2025:** Thủ tục pháp lý và dẫn độ tiếp diễn (Hoa Kỳ + Hàn Quốc yêu cầu dẫn độ)

**Dự Luật Stablecoin:**
- Nhiều dự luật đề xuất:
  - Yêu cầu nhà phát hành đăng ký
  - Giữ dự trữ 100% bằng tài sản thanh khoản cao
  - Kiểm toán thường xuyên
  - Một số đề xuất **cấm hoàn toàn** stablecoin thuật toán không có tài sản thế chấp

### Liên Minh Châu Âu

**MiCA (Markets in Crypto-Assets Regulation) - 2023:**
- Khuôn khổ toàn diện về quy định crypto
- **Yêu cầu cho stablecoin:**
  - Dự trữ phải được phân tách khỏi tài sản công ty
  - Phải được cấp phép
  - Công bố thông tin chi tiết về dự trữ
  - Stablecoin thuật toán: Yêu cầu đặc biệt cao hơn hoặc có thể bị cấm

### Singapore

**MAS (Cơ quan Tiền tệ Singapore):**
- Hướng dẫn mới:
  - Nhà phát hành phải giữ dự trữ 100% trong tài sản chất lượng cao
  - Cơ chế đổi 1:1 rõ ràng

### Nhật Bản

**Luật Stablecoin (2023):**
- Chỉ ngân hàng, công ty chuyển tiền được cấp phép, hoặc công ty tin thác được phép phát hành stablecoin

### Hàn Quốc

- Đặc biệt quyết liệt trong đẩy mạnh quy định crypto sau thảm họa Terra (quê hương Do Kwon)

---

## 8. PHẢN ỨNG TỪ NGÀNH CÔNG NGHIỆP CRYPTO

### Stablecoin Thuật Toán Khác

**Mất Niềm Tin:**
- Nhiều dự án stablecoin thuật toán khác đối mặt giám sát kỹ lưỡng
- Một số tự nguyện thay đổi mô hình hoặc tăng tài sản thế chấp

**FRAX (Fractional-Algorithmic Stablecoin):**
- Tăng tỷ lệ thế chấp lên gần 100% để đáp ứng nhu cầu an toàn hơn

**Dự Án Mới:**
- Tránh xa mô hình thuật toán thuần túy
- Tập trung vào thiết kế được thế chấp đầy đủ hoặc vượt mức

### Stablecoin Fiat Được Hưởng Lợi

**Chuyển Dịch Vốn:**
- Sau sự kiện: Hàng tỷ đô la chuyển từ UST và stablecoin rủi ro sang USDC/USDT
- Được coi "an toàn hơn" do có dự trữ fiat thực

**Thị Phần USDC:**
- Tăng đáng kể
- Nhà đầu tư tổ chức và doanh nghiệp tìm stablecoin đáng tin cậy
- Củng cố vị thế stablecoin fiat là lựa chọn chủ đạo

---

## 9. TƯƠNG LAI CỦA STABLECOIN

### Stablecoin Fiat (USDC, USDT)

**Vị Thế:**
- Tiếp tục chiếm thị phần lớn nhất
- Đặc biệt trong thanh toán, giao dịch, ứng dụng doanh nghiệp
- Tính ổn định và tuân thủ quy định là ưu tiên

**Xu Hướng Mới:**
- Tăng "stablecoin được quy định"
- Phát hành bởi ngân hàng và tổ chức tài chính truyền thống
- Đáp ứng tiêu chuẩn quy định nghiêm ngặt
- Có thể được bảo hiểm

**CBDC (Central Bank Digital Currency):**
- Một số ngân hàng trung ương phát triển tiền kỹ thuật số
- Có thể cạnh tranh trực tiếp với stablecoin tư nhân

### Stablecoin Crypto (DAI)

**Thị Trường Ngách:**
- Phục vụ những người coi trọng phi tập trung
- Không muốn phụ thuộc hệ thống ngân hàng truyền thống

**Thách Thức:**
- Cân bằng giữa phi tập trung và hiệu quả vốn để cạnh tranh

### Stablecoin Thuật Toán

**Khó Phục Hồi Niềm Tin:**
- Đặc biệt loại không có tài sản thế chấp như Terra

**Điều Kiện Thành Công Trong Tương Lai:**
- Nếu có dự án mới: Cần chứng minh cơ chế hoàn toàn mới
- Vượt qua điểm yếu đã lộ rõ của mô hình Terra

### Bài Học Tổng Thể

**Đổi Mới Đi Kèm Rủi Ro:**
- Thất bại (dù đau đớn) là phần cần thiết của quá trình học hỏi
- Ngành blockchain đã trải qua nhiều thất bại lớn trước đây:
  - Mt. Gox (2014)
  - The DAO (2016)
  - BitConnect
  - Giờ là Terra (2022)
- Mỗi lần, học được bài học quan trọng và trở nên mạnh mẽ hơn

**Tiềm Năng Stablecoin:**
- Vẫn là đổi mới quan trọng với tiềm năng to lớn
- Cải thiện hệ thống tài chính toàn cầu:
  - Thanh toán xuyên biên giới
  - Tài chính vi mô
  - Dịch vụ tài chính cho người không có tài khoản ngân hàng

**Yêu Cầu:**
- Học hỏi từ sai lầm Terra
- Xây dựng hệ thống an toàn và bền vững hơn
- Đặt sự bảo vệ người dùng lên hàng đầu (thay vì chỉ tăng trưởng với mọi giá)

---

## CÁC CON SỐ VÀ SỰ KIỆN QUAN TRỌNG CẦN NHỚ

### Thị Trường Stablecoin Tổng Thể

- **Vốn hóa (2025):** >$150 tỷ
- **Lộ trình:** Vài tỷ (2019) → đỉnh ~$180 tỷ (2022) → $150 tỷ+ (2025)
- **Khối lượng giao dịch hàng ngày:** Thường >$100 tỷ (vượt Bitcoin)

### Tether (USDT)

- **Ra mắt:** 2014
- **Vốn hóa (2025):** $83 tỷ (>50% thị trường stablecoin)
- **Khối lượng giao dịch hàng ngày:** >$50 tỷ
- **Tranh cãi:** 2019 - Kiện bởi Tổng chưởng lý NY (mất $850M)
- **Phạt (2021):** $18.5 triệu
- **Dự trữ (5/2021):** Chỉ 3.87% tiền mặt, phần lớn commercial paper
- **Cải thiện (2025):** >85% dự trữ là tiền mặt + tín phiếu kho bạc Mỹ
- **Lợi nhuận (2023):** >$4.5 tỷ chỉ trong một năm

### USDC

- **Ra mắt:** 7/2018 (Circle, hỗ trợ bởi Goldman Sachs)
- **Vốn hóa đỉnh:** $55 tỷ (2021)
- **Dự trữ:** 100% tiền mặt + tín phiếu kho bạc Mỹ ngắn hạn
- **Kiểm toán:** Hàng tháng bởi Grant Thornton
- **Khủng hoảng SVB (3/2023):** $3.3 tỷ (8% dự trữ) kẹt tại SVB, USDC giảm xuống $0.88, phục hồi về $1 trong vài ngày

### MakerDAO và DAI

- **Ra mắt:** 2017
- **Vốn hóa (2025):** ~$5 tỷ (stablecoin phi tập trung lớn nhất)
- **Tỷ lệ thế chấp:** ETH 150%, tài sản khác 175-200%
- **Black Thursday (12/3/2020):** ETH giảm >50% trong vài giờ, tạo nợ xấu $5.7M, đấu giá nợ thành công
- **Phạt thanh lý:** Thường 13%
- **Cải thiện:** PSM (Peg Stability Module), đa dạng hóa tài sản thế chấp (WBTC, USDC, UNI, COMP, RWA)

### Terra/Luna - Sự Sụp Đổ

**Trước Sụp Đổ (Mùa Xuân 2022):**
- **Tổng vốn hóa:** >$60 tỷ (UST + LUNA)
- **UST:** Stablecoin lớn thứ 3 thế giới
- **Anchor Protocol:** Lợi suất 20%/năm, thu hút >$14 tỷ UST
- **LFG dự trữ Bitcoin:** ~$3.5 tỷ
- **Lợi nhuận thực Anchor:** Chỉ 3-5%/năm (được trợ cấp để đạt 20%)
- **Quỹ dự trữ Anchor:** Từ >70M UST (2/2022) xuống <30M UST (4/2022)

**Tuần Sụp Đổ (7-13/5/2022):**

| Ngày | UST | LUNA | Cung LUNA | Sự Kiện Chính |
|------|-----|------|-----------|---------------|
| 7/5 | $0.98 | ~$80 | ~350M | Rút $2B từ Anchor, LFG can thiệp |
| 8/5 | $0.91 | $60 (-25%) | - | Phục hồi khó khăn hơn |
| 9/5 | $0.60 | $10 (-87%) | >1B (+3x) | Vòng xoáy tử thần bắt đầu |
| 10/5 | <$0.30 | <$1 (-99%) | >6B (+6x) | Sụp đổ hoàn toàn |
| 11-13/5 | $0.10-$0.20 | ~$0 | Hàng nghìn tỷ | Blockchain dừng (13/5) |

**Thiệt Hại:**
- **Xóa sạch:** >$40 tỷ giá trị (LUNA + UST) trong một tuần
- **Số người bị ảnh hưởng:** >200,000 người nắm giữ LUNA + hàng chục nghìn người gửi UST

**Hiệu Ứng Lây Lan:**
- **Three Arrows Capital (3AC):** Phá sản 6/2022, nợ >$3 tỷ
- **Celsius Network:** Đóng băng rút tiền 6/2022, phá sản 7/2022, nợ $4.7 tỷ
- **Voyager Digital:** Phá sản (cho 3AC vay $650M)
- **BlockFi:** Nhận cứu trợ FTX (FTX sau đó cũng sụp đổ 11/2022)
- **Tổng thiệt hại (Terra + lây lan):** >$60 tỷ

**Hậu Quả Pháp Lý:**
- **SEC buộc tội (2/2023):** Gian lận chứng khoán
- **Do Kwon bị bắt (3/2023):** Tại Montenegro với hộ chiếu giả
- **Tình trạng (2025):** Thủ tục dẫn độ tiếp diễn (Hoa Kỳ + Hàn Quốc yêu cầu)

### So Sánh Tốc Độ Sụp Đổ

- **Terra/Luna:** Một tuần (nhanh nhất)
- **Mt. Gox (2014):** Nhiều tuần/tháng
- **The DAO (2016):** Nhiều tuần/tháng
