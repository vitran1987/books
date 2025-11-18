# TÓM TẮT CHƯƠNG 7: NFT - CƠ CHẾ TOKEN HÓA TÀI SẢN SỐ

## I. KHÁI NIỆM CỐT LÕI NFT

### NFT (Non-Fungible Token - Token Không Thể Thay Thế)
- **Định nghĩa**: Token kỹ thuật số duy nhất được ghi lại trên blockchain với mã định danh riêng biệt
- **Khác biệt với Fungible Token**: 
  - Bitcoin/ETH: Có thể thay thế lẫn nhau (1 BTC = 1 BTC)
  - NFT: Mỗi token độc nhất, không thể thay thế (NFT #1 ≠ NFT #2)
- **Giải quyết vấn đề**: Sao chép vô hạn của tài sản kỹ thuật số → Tạo ra khan hiếm và chứng minh quyền sở hữu

### Sự Kiện Lịch Sử
- **Beeple "Everydays: The First 5000 Days"**: Bán với giá **69.3 triệu USD** tại Christie's (tháng 3/2021)
- Một trong những tác phẩm nghệ thuật đắt nhất từ nghệ sĩ còn sống
- Đánh dấu NFT được công nhận bởi giới nghệ thuật truyền thống

## II. CƠ CHẾ KỸ THUẬT NFT

### Tiêu Chuẩn ERC-721 (2017)
- Được giới thiệu bởi Dieter Shirley và Dapper Labs (CryptoKitties)
- **Chức năng cơ bản**:
  1. **Theo dõi quyền sở hữu**: Mỗi token có "owner" rõ ràng trên blockchain
  2. **Chuyển nhượng**: Chủ sở hữu có thể chuyển NFT an toàn qua giao dịch blockchain
  3. **Metadata**: Lưu trữ thông tin mô tả (tên, mô tả, URI đến file kỹ thuật số)
- **Hạn chế**: Mỗi NFT cần một smart contract riêng → Không hiệu quả khi quản lý nhiều token

### IPFS (InterPlanetary File System)
- **Vai trò**: Lưu trữ file kỹ thuật số phi tập trung
- **Content Hash**: Mã định danh duy nhất dựa trên nội dung file
  - Nếu nội dung thay đổi 1 bit → Hash thay đổi hoàn toàn
  - Xác minh tính xác thực của tác phẩm
- **Lợi ích**: Không phụ thuộc vào một công ty/dịch vụ cụ thể, tồn tại miễn là có node lưu trữ

### Tiêu Chuẩn ERC-1155 (2018)
- Được giới thiệu bởi Enjin
- **Multi-Token Standard**: Một smart contract quản lý nhiều loại token (fungible + non-fungible)
- **Ứng dụng chính**: Gaming blockchain
  - Thanh kiếm độc nhất (NFT) + Bình máu phổ biến (fungible token) trong cùng contract
- **Lợi ích**:
  - Giảm chi phí gas đáng kể
  - Hỗ trợ "batch transfers": Chuyển nhiều loại token trong 1 giao dịch
  - Đơn giản hóa phát triển và bảo trì

## III. NFT NGHỆ THUẬT KỸ THUẬT SỐ

### Quy Mô Thị Trường
- **2020**: ~100 triệu USD tổng giá trị giao dịch
- **2021 (đỉnh cao)**: Hơn **25 tỷ USD** (tăng 250 lần trong 1 năm)
- Duy trì hàng tỷ USD/năm sau khi hạ nhiệt

### Royalty Tự Động
- **Cơ chế**: Smart contract tự động trích % mỗi giao dịch bán lại → Ví nghệ sĩ
- **Tỷ lệ tiêu chuẩn**: 5-10%
- **Ý nghĩa**: Nghệ sĩ hưởng lợi mọi lần tác phẩm tăng giá, không chỉ lần bán đầu
- **Ví dụ**: NFT bán ban đầu 1 ETH, bán lại 10 ETH → Nghệ sĩ nhận 0.5-1 ETH royalty

### Provenance và Authenticity
- **Blockchain = Hồ sơ nguồn gốc minh bạch, bất biến**
- Xem toàn bộ lịch sử: Ai tạo, khi nào, ai sở hữu, giá từng lần chuyển nhượng
- Loại bỏ hoàn toàn rủi ro tác phẩm giả

### Các Nghệ Sĩ NFT Nổi Bật

#### Pak (Ẩn danh)
- **"Merge" (12/2021)**: 
  - 28,000 collectors
  - 312,686 "masses" (đơn vị NFT)
  - Tổng giá trị: **91.8 triệu USD**
  - Kỷ lục NFT đắt nhất từ nghệ sĩ còn sống (vượt Beeple)
- **Đặc điểm**: Masses có thể merge → Tác phẩm nghệ thuật động, tương tác

### Dân Chủ Hóa Thị Trường
- **Gallery truyền thống**: 
  - Hoa hồng 50%
  - Cần đại diện, mối quan hệ, triển lãm
  - Chỉ số ít nghệ sĩ được lựa chọn
- **NFT Marketplaces**:
  - Phí nền tảng 2.5% (OpenSea)
  - Không cần gatekeeper
  - Bán trực tiếp đến công chúng toàn cầu

## IV. NFT TRONG GAMING

### Axie Infinity - Case Study Play-to-Earn

#### Thành Tích Đỉnh Cao (2021)
- **2.7 triệu người chơi hoạt động hàng ngày** (tháng 8/2021)
- Tổng doanh thu NFT: Hơn **4 tỷ USD**
- Thu nhập người chơi: **200-500 USD/tháng** (đáng kể tại Philippines)
- Một số Axie hiếm: Hơn **300,000 USD**
- Định giá công ty: **3 tỷ USD** (10/2021, vốn hóa 152 triệu USD từ Andreessen Horowitz)

#### Sụp Đổ (2022-2023)
- **Ronin Bridge bị hack (3/2022)**: Hơn **625 triệu USD** bị đánh cắp (một trong những vụ hack lớn nhất lịch sử crypto)
- Người chơi hoạt động giảm **80%**: Từ 2.7 triệu xuống ~500,000
- Giá SLP giảm **97.5%**: Từ 0.40 USD (7/2021) xuống <0.01 USD (2023)
- Kiếm tiền từ game gần như không khả thi

#### Bài Học
- **Mô hình play-to-earn thuần túy không bền vững**
- Động lực chính là kiếm tiền (không phải giải trí) → Vòng lặp giống Ponzi
- Cần người chơi mới liên tục → Khi giảm, hệ thống sụp đổ
- **Tương lai**: Gameplay thú vị TRƯỚC, NFT/rewards CHỈ LÀ phần bổ sung

### Quyền Sở Hữu Thực Sự
- **Truyền thống**: Công ty game sở hữu tất cả tài sản trong game, người chơi chỉ "thuê"
- **NFT**: Người chơi sở hữu NFT trong ví blockchain riêng
- Có thể mua, bán, tặng, cho thuê MÀ KHÔNG CẦN sự cho phép từ công ty game

## V. NFT MEMBERSHIP - BORED APE YACHT CLUB (BAYC)

### Ra Mắt và Tăng Trưởng
- **Ngày ra mắt**: 30/4/2021 (Yuga Labs)
- **Giá mint**: 0.08 ETH (~200 USD)
- **Bán hết**: 10,000 NFTs trong vài giờ
- **Giá sàn đỉnh cao**: Hơn **150 ETH** (~450,000 USD, tháng 4/2022)
- Tăng **500 lần** trong 4 tháng đầu

### Đặc Quyền Membership
1. **Quyền thương mại đầy đủ**: Tạo merchandise, dự án kinh doanh với hình ảnh Ape
2. **Sự kiện độc quyền**: ApeFest (NYC, Miami) - festival âm nhạc và nghệ thuật
3. **Airdrops**: Mutant Apes, Bored Ape Kennel Club
4. **Cộng đồng toàn cầu**: Discord networking với creators, doanh nhân, nghệ sĩ, influencers
5. **Metaverse**: Otherside - trải nghiệm game và xã hội

### Chủ Sở Hữu Nổi Tiếng
- Justin Bieber, Snoop Dogg, Madonna, Jimmy Fallon
- Visa: Mua CryptoPunk 150,000 USD (8/2021)

### Thành Tựu Kinh Doanh
- **Vốn hóa Series A (3/2022)**: **450 triệu USD**, định giá **4 tỷ USD**
- Mua lại CryptoPunks và Meebits
- Hợp tác: Adidas (20 triệu USD vài giờ), Gucci, Rolling Stone

### Sụt Giảm Bear Market (2022-2023)
- Giá sàn giảm **80% (tính bằng ETH)**: Từ 150 ETH xuống ~30 ETH
- Giảm **90% (tính bằng USD)**: Do giá ETH cũng giảm
- Nhưng vẫn duy trì cộng đồng mạnh, tiếp tục xây dựng

## VI. UTILITY NFTs

### NFT Tickets (Vé Sự Kiện)
**Nền tảng**: GET Protocol, Ticketmaster

**Lợi ích so với vé truyền thống**:
1. **Chống giả**: Mã định danh duy nhất trên blockchain, gần như bất khả thi làm giả
2. **Kiểm soát bán lại**: Royalty tích hợp → Người tổ chức nhận phần từ mỗi lần bán lại (thay vì scalpers lấy hết)
3. **Kỷ vật kỹ thuật số**: Sau sự kiện, vé trở thành collectible, có thể cập nhật ảnh/video/nội dung độc quyền

**Ứng dụng thực tế**:
- **Kings of Leon (2023)**: Ban nhạc rock đầu tiên phát hành album dưới dạng NFT + NFT tickets cho concert
- **Coachella**: NFT lifetime passes (tham dự festival miễn phí suốt đời + trải nghiệm VIP)

### Real World Assets (RWA) Tokenization

#### Propy - Bất Động Sản
- **Giao dịch lịch sử (2/2022)**: Nhà Tampa, Florida - **653,000 USD** thông qua NFT
- Người mua nhận NFT đại diện quyền sở hữu pháp lý (ghi nhận trên blockchain + hồ sơ công chứng)

**Lợi ích**:
1. **Đơn giản hóa giao dịch**: Giảm từ tuần/tháng giấy tờ xuống nhanh hơn nhiều qua smart contract
2. **Tăng thanh khoản**: Dễ bán/thế chấp NFT hơn tài sản vật lý
3. **Fractional ownership**: Chia nhà thành nhiều NFT nhỏ → Nhiều người cùng đầu tư

#### Các RWA Khác
- **Rally**: Xe hơi collectible
- **WiV**: Rượu vang
- **Đồng hồ sang trọng, nghệ thuật vật lý, hàng xa xỉ**

### Access Control (Kiểm Soát Truy Cập)
- **Thay thế username/password**: Yêu cầu sở hữu NFT cụ thể để truy cập nội dung/dịch vụ
- **Ví dụ**:
  - NFT certificates cho khóa học → Mở khóa khóa nâng cao/cộng đồng alumni
  - NFT subscriptions → Có thể bán lại (không thể với Netflix/Spotify)

## VII. KINH TẾ NHÀ SÁNG TẠO

### Royalties - Tranh Cãi Lớn

#### Cơ Chế Ban Đầu
- Smart contract tự động chuyển % giao dịch bán lại về ví nghệ sĩ
- **Tỷ lệ**: 5-10%
- Nguồn thu nhập thụ động đáng kể (Beeple: Hàng triệu USD từ royalties)

#### Blur Marketplace Phá Vỡ (2022-2023)
- **Biến royalties thành TÙY CHỌN** thay vì bắt buộc
- Người mua có thể chọn: Trả đầy đủ, một phần, hoặc không trả
- Tạo áp lực cạnh tranh → OpenSea cũng phải làm royalties optional
- **Tác động**: Tổng royalty giảm **70%** từ đỉnh 2021 (không chỉ do thị trường giảm, còn do nhiều người chọn không trả)

#### Vấn Đề
- Royalties KHÔNG được enforce ở cấp blockchain
- Chỉ là quy ước của marketplaces qua smart contracts
- Một lợi ích lớn nhất của NFT biến mất nếu không được đảm bảo

### Marketplaces và Phí

#### OpenSea (lớn nhất)
- Phí: **2.5%** mỗi giao dịch (thấp hơn 50% của gallery truyền thống)
- Thị phần: Hơn **90%** vào đỉnh cao 2021
- Khối lượng đỉnh cao: **5 tỷ USD/tháng** (8/2021)

#### Foundation
- Phí lần bán đầu: **15%**
- Phí bán lại: **2.5%**
- Cộng đồng nghệ thuật chất lượng cao

#### Manifold và Zora
- Công cụ cho nghệ sĩ tự mint và bán trực tiếp
- Không cần marketplace trung gian
- Chỉ trả phí gas blockchain

### Direct-to-Fan Models

#### 3LAU (Nhạc sĩ, 2/2021)
- Bộ sưu tập 33 NFTs
- Tổng giá trị: **11.6 triệu USD**
- Bao gồm: Album, demo độc quyền, trải nghiệm gặp nghệ sĩ
- Kiếm nhiều hơn đáng kể so với Spotify (chỉ phần nhỏ của một cent/stream)

#### Các Nhạc Sĩ Khác
- RAC, Grimes
- Bỏ qua hãng thu âm và nền tảng streaming
- Người hâm mộ nhận: Quyền sở hữu độc quyền, trải nghiệm độc đáo, kết nối trực tiếp với nghệ sĩ

## VIII. CƠN SỐT NFT 2021 - BOOM

### Quý 1/2021

#### CryptoPunks
- **Bộ sưu tập**: 10,000 pixel art characters (Larva Labs, 2017)
- Ban đầu phân phối miễn phí
- **Giao dịch lớn (2/2021)**: 4,200 ETH (~7.5 triệu USD)
- **Giá sàn tăng**: Từ ~15 ETH đầu năm lên >100 ETH trong vài tháng

#### Beeple Christie's (3/2021)
- **69.3 triệu USD** cho "Everydays: The First 5000 Days"
- Lần đầu Christie's bán tác phẩm kỹ thuật số thuần túy
- Xuất hiện trang nhất NYT, WSJ, BBC
- **Google Trends**: Tìm kiếm "NFT" tăng **1,000%** trong tháng 3

### Quý 2/2021 - BAYC Ra Mắt
- Giá mint 0.08 ETH → Giá sàn 40 ETH sau 4 tháng (**500 lần**)
- Câu chuyện triệu phú nhờ đầu tư 800 USD → FOMO lan rộng

### Quý 3 & 4/2021 - Ngôi Sao và Thương Hiệu Tham Gia
- **Visa (8/2021)**: Mua CryptoPunk 150,000 USD
- **Snoop Dogg (9/2021)**: Tiết lộ là @CozomoMedici (collector NFT triệu USD)
- **Adidas (10/2021)**: Hợp tác BAYC, bán NFT kiếm >20 triệu USD vài giờ
- **Grimes (11/2021)**: Bộ sưu tập NFT 6 triệu USD
- **Nike (12/2021)**: Mua RTFKT Studios >100 triệu USD

### Số Liệu Giao Dịch Đỉnh Cao
- **OpenSea**: 
  - Tháng 1/2021: 21 triệu USD
  - Tháng 8/2021: **5 tỷ USD** (tăng ~250 lần trong 7 tháng)
  - Ngày cao điểm: >100,000 giao dịch, >200 triệu USD/ngày
- **Số ví duy nhất**: Từ ~50,000 đầu năm → >1 triệu cuối năm (**20 lần**)

## IX. ĐỘNG LỰC ĐẰNG SAU CƠN SỐT

### 1. Thanh Khoản Khổng Lồ (COVID-19)
- **Fed Mỹ**: Bơm >4 nghìn tỷ USD vào nền kinh tế
- **Chính phủ Mỹ**: Phát hành >5 nghìn tỷ USD kích thích
- Lãi suất gần 0% → Nhà đầu tư tìm tài sản sinh lời cao

### 2. Lockdown Thay Đổi Hành Vi
- Không thể du lịch, ăn nhà hàng, sự kiện trực tiếp
- Thời gian rảnh + Tiền tiết kiệm tăng
- Chuyển sang hoạt động kỹ thuật số: Gaming, Discord, Twitter, đầu tư
- **Morning Consult**: 44% người Mỹ 18-34 tuổi tăng hoạt động đầu tư trong đại dịch

### 3. Đầu Cơ và FOMO
- Câu chuyện lợi nhuận khổng lồ lan truyền nhanh trên mạng xã hội
- Vòng phản hồi tích cực: Giá tăng → Chia sẻ → Nhiều người tham gia → Giá tăng thêm
- **Blockchain minh bạch**: Mọi người xem chính xác giao dịch trên Etherscan → Xác thực legitimacy
- **Chainalysis**: Hơn **60%** người mua NFT 2021 bán lại trong **30 ngày** (đầu cơ ngắn hạn)

### 4. Địa Vị Xã Hội (Social Status Signaling)
- Thế giới ngày càng kỹ thuật số → Địa vị xã hội cũng chuyển sang kỹ thuật số
- CryptoPunk/BAYC làm avatar = Tín hiệu:
  - Thuộc cộng đồng crypto tinh hoa
  - Giàu có (chi hàng trăm nghìn USD cho tài sản kỹ thuật số)
  - "Early adopter" của phong trào văn hóa mới
- **Twitter NFT profile pictures (1/2022)**: Hình lục giác xác minh on-chain quyền sở hữu NFT thực

## X. SỰ SỤP ĐỔ 2022-2023 - BUST

### Yếu Tố Vĩ Mô
- **Fed tăng lãi suất (đầu 2022)**: Chống lạm phát → Kết thúc kỷ nguyên tiền rẻ
- Nhà đầu tư rút khỏi tài sản rủi ro cao (crypto, NFT) → Tài sản an toàn

### Sụt Giảm Giá Crypto
- **Bitcoin**: Từ ~69,000 USD (11/2021) xuống <20,000 USD (giữa 2022) - **Giảm ~70%**
- **Ethereum**: Từ 4,800 USD xuống <1,000 USD - **Giảm ~80%**

### Sụt Giảm NFT

#### Bored Ape Yacht Club
- Giá sàn: Từ >150 ETH (4/2022) xuống ~30 ETH (đầu 2023)
- **Giảm 80% (ETH), >90% (USD)**

#### Bộ Sưu Tập Nhỏ Hơn
- Hàng nghìn dự án giá gần = 0
- **Chainalysis**: Khoảng **45%** bộ sưu tập NFT 2021-2022 có giá sàn = 0 ETH vào 2023
- Hàng triệu NFT trong ví không ai muốn mua

### Sụt Giảm Khối Lượng Giao Dịch
- **OpenSea**: Từ 5 tỷ USD/tháng xuống <500 triệu USD cuối 2022 - **Giảm 90%**
- **Người dùng hoạt động**: Từ >1 triệu ví/tháng xuống ~100,000-200,000 ví
- Nhiều marketplace nhỏ đóng cửa hoặc sa thải đại trà
- Coinbase, FTX thu hẹp/đóng mảng NFT

### Câu Chuyện Bi Thảm
- Người vay tiền/thế chấp nhà mua NFT → Mắc nợ với tài sản mất giá trị
- Nghệ sĩ bỏ việc ổn định cho NFT toàn thời gian → Không bán được gì
- Collectors chi hàng trăm nghìn USD → Bộ sưu tập chỉ còn vài nghìn USD

## XI. DỰ ÁN SỐNG SÓT - BLUE-CHIPS

### CryptoPunks
- **Vị thế**: "Digital artifact" có giá trị lịch sử
- Giá sàn giảm: Từ >100 ETH xuống ~40-50 ETH
- Vẫn duy trì thanh khoản và sự quan tâm từ collectors nghiêm túc
- Một số Punks hiếm vẫn bán hàng trăm ETH

### Bored Ape Yacht Club
- Cộng đồng mạnh mẽ duy trì
- Yuga Labs tiếp tục đầu tư: Otherside metaverse, Mutant Apes
- Tổ chức ApeFest 2022, 2023 với hàng nghìn người tham dự
- Hợp đồng với Adidas, Gucci, Rolling Stone
- Xây dựng brand và IP dài hạn

### ENS (Ethereum Name Service)
- **Utility thực tế**: Tên miền blockchain thay địa chỉ ví dài
- Tăng trưởng ngay cả trong bear market
- **Tên miền .eth**: Từ 1 triệu (đầu 2022) → >2.5 triệu (cuối 2023)
- Identity on-chain dễ nhớ có giá trị thực tế

### POAP (Proof of Attendance Protocol)
- NFT attendance badges cho sự kiện
- Hàng triệu NFT được phát hành (conferences, concerts, v.v.)
- Tiếp tục phát triển do utility rõ ràng

### Gaming Tiếp Tục Xây Dựng

#### Gods Unchained
- Trading card game blockchain
- Cộng đồng trung thành nhờ gameplay chất lượng cao (tương tự Hearthstone)
- Tập trung vào trải nghiệm game TRƯỚC, NFT SAU

#### Sorare
- Fantasy football game sử dụng NFT cards cầu thủ thực
- Hợp đồng licensing: Premier League, La Liga, NBA
- **Vốn hóa**: 152 triệu USD từ Softbank, định giá **4.3 tỷ USD**

## XII. BÀI HỌC ĐẮT GIÁ

### Điều Gì Hoạt Động

#### 1. Cộng Đồng Mạnh Mẽ và Cam Kết
- NFT không chỉ là tài sản đầu tư mà là phần của identity và văn hóa
- Tham gia Discord, meetups, collaborate, ủng hộ brand ngay cả khi giá giảm
- Cộng đồng = "Moat" bảo vệ giá trị
- **Ví dụ**: BAYC, CryptoPunks

#### 2. Utility Thực Tế Vượt Ra Ngoài Speculation
- Không chỉ hứa hẹn mà thực sự GIAO utility
- **BAYC**: Sự kiện thực tế, airdrop NFTs, IP rights
- **ENS**: Dịch vụ thực tế dùng hàng ngày
- **Sorare**: Game thực sự thú vị
- Value proposition rõ ràng ngoài đầu tư đầu cơ

#### 3. Minh Bạch và Giao Tiếp Liên Tục
- Minh bạch về roadmap, tiến độ, cách sử dụng funds
- Giao tiếp thường xuyên qua Twitter, Discord
- Giải thích quyết định khó khăn, lắng nghe feedback
- Đối mặt trực tiếp với vấn đề thay vì im lặng
- Xây dựng niềm tin và loyalty

### Điều Gì Thất Bại

#### 1. Đầu Cơ Thuần Túy Không Foundation
- Hàng nghìn dự án tạo ra CHỈ để kiếm tiền nhanh từ hype
- Không có tầm nhìn dài hạn, team năng lực, kế hoạch tạo giá trị
- Roadmap mơ hồ đầy buzzwords ("metaverse", "P2E", "utility") không chi tiết
- Mint hết → Im lặng/biến mất → NFT vô giá trị

#### 2. Celebrity Cash-Grabs
- Nghệ sĩ/influencers/brands nhảy vào KHÔNG hiểu/tin công nghệ
- Chỉ thấy cơ hội kiếm tiền nhanh từ fanbase
- Mint, promote mạnh, bán hết → Không tương tác/không giao utility
- **Logan Paul - CryptoZoo**: Hứa game P2E phức tạp, huy động hàng triệu USD, game không bao giờ hoàn thành, bị kiện gian lận

#### 3. Over-Promising và Under-Delivering
- Roadmap cực kỳ tham vọng: Metaverse, game AAA, DAO, merchandise, festival...
- Team không có kinh nghiệm, nguồn lực, năng lực thực hiện
- Sau mint → Nhận ra không thể thực hiện → Im lặng/trì hoãn/abandon dự án
- Tạo môi trường cynicism (hoài nghi) sâu sắc trong cộng đồng

## XIII. TƯƠNG LAI NFT - INFRASTRUCTURE THAY VÌ HYPE

### 1. Gaming và Metaverse
- **Chuyển đổi**: Từ game xây dựng chỉ xung quanh kiếm tiền → Trải nghiệm gaming chất lượng cao TRƯỚC, NFT tích hợp TỰ NHIÊN
- **Game studios lớn**: Ubisoft, Square Enix, Epic Games kế hoạch tích hợp NFT
- **Yêu cầu**: Quyền sở hữu thực sự, giao dịch tự do, KHÔNG ảnh hưởng gameplay/không pay-to-win
- **Immutable X**: Layer 2 cho NFT gaming
  - Hợp tác >200 game studios
  - Hàng triệu giao dịch, phí gần = 0
  - Infrastructure quy mô lớn đang được xây

### 2. Fractionalization và Financialization

#### Fractional Ownership
- **Nền tảng**: Fractional.art, Tessera
- **Cơ chế**: Chia NFT đắt tiền thành nhiều phần nhỏ
- **Ví dụ**: CryptoPunk 1 triệu USD → 1 triệu tokens → Mỗi token 1 USD (0.0001% quyền sở hữu)
- **Lợi ích**: Dân chủ hóa tiếp cận NFT blue-chip, tăng thanh khoản

#### NFT as Collateral (DeFi)
- **Nền tảng**: NFTfi, Arcade
- **Cơ chế**: Thế chấp NFT để vay tiền
- **Ví dụ**: Bored Ape 100,000 USD → Vay 50,000-70,000 USD → Trả lãi → Nhận lại NFT khi trả nợ
- Thị trường lending mới

### 3. Real World Assets (RWA) Tokenization
- **Công ty**: Propy (bất động sản), Rally (xe hơi collectible), WiV (rượu vang)
- **Tiềm năng**: Thị trường hàng nghìn tỷ USD
- Mọi thứ có thể được tokenized: Nhà đất, xe hơi, nghệ thuật vật lý, hàng xa xỉ
- Giao dịch trên blockchain nhanh hơn, chi phí thấp hơn phương thức truyền thống
- **Thách thức**: Pháp lý và kỹ thuật cần giải quyết

### 4. Identity và Credential
- **Trường đại học**: Bằng tốt nghiệp dưới dạng NFT (không giả mạo, xác minh ngay lập tức)
- **Chứng chỉ chuyên môn, licenses, memberships** được tokenized
- **Tương lai**: Ví blockchain chứa tất cả NFT credentials, chia sẻ và xác minh ngay lập tức không cần bên thứ ba

## XIV. SỐ LIỆU QUAN TRỌNG CẦN NHỚ

### Thị Trường NFT
- 2020: **~100 triệu USD**
- 2021 đỉnh cao: **>25 tỷ USD** (tăng 250 lần)
- OpenSea đỉnh: **5 tỷ USD/tháng** (8/2021)
- OpenSea sụt: **<500 triệu USD/tháng** (cuối 2022, giảm 90%)

### Giao Dịch Lịch Sử
- Beeple "Everydays": **69.3 triệu USD** (3/2021)
- Pak "Merge": **91.8 triệu USD** (12/2021, kỷ lục nghệ sĩ còn sống)
- CryptoPunk: **7.5 triệu USD** (2/2021)
- 3LAU NFT collection: **11.6 triệu USD** (2/2021)
- Propy BĐS Tampa: **653,000 USD** (2/2022)

### NFT Projects
- **CryptoPunks**: 10,000 NFTs (Larva Labs, 2017)
- **BAYC**: 10,000 NFTs (Yuga Labs, 4/2021)
  - Giá mint: 0.08 ETH
  - Giá sàn đỉnh: >150 ETH (~450,000 USD)
  - Giá sàn bear: ~30 ETH (~50,000 USD)
  - Vốn hóa Yuga Labs: **4 tỷ USD** (3/2022)

### Gaming
- **Axie Infinity đỉnh (8/2021)**:
  - 2.7 triệu người chơi/ngày
  - >4 tỷ USD tổng doanh thu NFT
  - Định giá: **3 tỷ USD**
- **Axie Infinity sụt**:
  - Ronin hack: **625 triệu USD** (3/2022)
  - Người chơi giảm 80%: ~500,000
  - SLP giảm 97.5%: 0.40 USD → <0.01 USD
- **Sorare**: Định giá **4.3 tỷ USD** (vốn hóa 680 triệu USD từ Softbank)

### Người Dùng
- Ví duy nhất giao dịch NFT:
  - Đầu 2021: ~50,000
  - Cuối 2021: >1 triệu (tăng 20 lần)
  - Cuối 2022: ~100,000-200,000 (giảm 80-90%)

### ENS
- Tên miền .eth: Từ 1 triệu (đầu 2022) → >2.5 triệu (cuối 2023)

### Thống Kê Thị Trường
- **Chainalysis**: 
  - >60% người mua NFT 2021 bán lại trong 30 ngày (đầu cơ)
  - ~45% bộ sưu tập NFT 2021-2022 có giá sàn = 0 ETH vào 2023
- **Morning Consult**: 44% người Mỹ 18-34 tuổi tăng hoạt động đầu tư trong COVID

### Kích Thích COVID
- Fed Mỹ bơm: **>4 nghìn tỷ USD**
- Chính phủ Mỹ kích thích: **>5 nghìn tỷ USD**

## XV. KẾT LUẬN - ĐIỂM THEN CHỐT

### 1. NFT Giải Quyết Vấn Đề Căn Bản
- **Sao chép vô hạn** của tài sản kỹ thuật số → **Khan hiếm và chứng minh quyền sở hữu**
- Tạo ra thị trường mới cho nghệ thuật kỹ thuật số (trước đây gần như không có)

### 2. Tiêu Chuẩn Kỹ Thuật
- **ERC-721**: Nền tảng cho NFT nghệ thuật, collectibles
- **ERC-1155**: Multi-token standard cho gaming
- **IPFS**: Lưu trữ phi tập trung, content hash đảm bảo tính xác thực

### 3. Royalty Tự Động
- Cách mạng cho nghệ sĩ: Thu nhập thụ động mọi lần tác phẩm bán lại
- **Nhưng**: Không enforce ở cấp blockchain → Tranh cãi khi marketplaces làm optional

### 4. Chu Kỳ Boom-Bust
- **Boom 2021**: Thanh khoản COVID, lockdown, FOMO, địa vị xã hội
- **Bust 2022-2023**: Tăng lãi suất, crypto sụt, đầu cơ không bền vững
- **Bài học**: Cộng đồng mạnh + Utility thực tế = Sống sót; Đầu cơ thuần túy + Over-promise = Thất bại

### 5. Blue-Chips Sống Sót
- **CryptoPunks**, **BAYC**: Giảm giá nhưng duy trì cộng đồng, tiếp tục xây dựng
- **ENS**, **POAP**: Utility thực tế tăng trưởng ngay cả bear market
- **Gods Unchained**, **Sorare**: Gaming tập trung gameplay chất lượng

### 6. Tương Lai = Infrastructure
- Không còn chỉ speculation, chuyển sang ứng dụng thực tế
- **Gaming**: Trải nghiệm tốt TRƯỚC, NFT tích hợp tự nhiên
- **Fractionalization**: Dân chủ hóa tiếp cận NFT đắt tiền
- **DeFi**: NFT làm collateral, thị trường lending mới
- **RWA**: Tokenize bất động sản, xe, nghệ thuật vật lý (thị trường nghìn tỷ USD)
- **Identity**: Bằng cấp, chứng chỉ, credentials trên blockchain

### 7. NFT Không Phải Con Đường Tắt Giàu Qua Đêm
- **Thực tế**: Công nghệ mạnh mẽ biến đổi cách sở hữu, giao dịch, tương tác với tài sản kỹ thuật số
- **Yêu cầu**: Sử dụng có trách nhiệm, tập trung giá trị dài hạn
- **Tương lai**: Phần không thể thiếu của nền kinh tế kỹ thuật số, không phải trend tạm thời
