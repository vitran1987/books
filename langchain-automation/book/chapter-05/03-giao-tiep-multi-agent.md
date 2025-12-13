# Giao tiếp Multi-Agent

## Khi một Agent không đủ

Tuấn Anh, sinh viên năm hai ngành Công nghệ Thông tin, đang chuẩn bị cho buổi phỏng vấn thực tập đầu tiên của mình tại một công ty công nghệ lớn. Anh biết rằng mình cần luyện tập kỹ năng phỏng vấn, nhưng không có ai để giúp đỡ—bạn bè đều bận rộn, và việc thuê một career coach chuyên nghiệp vượt quá ngân sách của một sinh viên. Tuấn Anh quyết định thử một nền tảng AI coaching mới, nơi hai Agent riêng biệt đóng vai: một Agent là "Interviewer" (người phỏng vấn), còn Agent kia là "Coach" (huấn luyện viên).

Cuộc phỏng vấn mô phỏng bắt đầu. Interviewer Agent hỏi: "Hãy kể về một dự án khó khăn mà bạn đã hoàn thành." Tuấn Anh trả lời, giải thích về một dự án nhóm xây dựng ứng dụng mobile. Khi câu trả lời kết thúc, Coach Agent can thiệp: "Bạn đã mô tả dự án khá tốt, nhưng chưa làm nổi bật vai trò cụ thể của bạn. Trong lần trả lời tiếp theo, hãy nhấn mạnh rằng bạn đã là người thiết kế kiến trúc backend và giải quyết vấn đề performance." Sau đó, Interviewer Agent đặt câu hỏi follow-up: "Bạn đã đối mặt với những thách thức kỹ thuật gì trong dự án đó?" Tuấn Anh trả lời lần nữa, lần này áp dụng lời khuyên của Coach. Sau 30 phút luyện tập, Tuấn Anh cảm thấy tự tin hơn nhiều—không chỉ vì đã thực hành trả lời câu hỏi, mà vì đã nhận được feedback chi tiết và có cơ hội điều chỉnh ngay lập tức.

Đây là sức mạnh của multi-agent communication—thay vì một Agent đơn lẻ cố gắng làm mọi thứ, nhiều Agent với vai trò và chuyên môn khác nhau cộng tác với nhau để tạo ra trải nghiệm học tập phong phú và hiệu quả hơn. Mô hình này không chỉ đơn thuần là chia nhỏ công việc, mà còn tạo ra một dynamic interaction (tương tác động) giống như các tình huống thực tế ngoài đời—nơi con người học tập tốt nhất không phải từ một nguồn thông tin duy nhất, mà từ cuộc đối thoại, tranh luận, và trao đổi với nhiều người khác nhau.

## Roleplaying Agents: Học qua tương tác

Một trong những ứng dụng phổ biến nhất của multi-agent communication là "roleplaying" (đóng vai). Trong giáo dục ngôn ngữ, ví dụ, thay vì chỉ có một AI tutor đơn thuần hỏi đáp, các nền tảng tiên tiến đang triển khai hệ thống với nhiều Agent đóng vai các nhân vật khác nhau trong các tình huống giao tiếp thực tế.

Duolingo Max, phiên bản nâng cao của Duolingo ra mắt vào đầu năm 2024, đã tích hợp tính năng "Scenario Practice" với multi-agent system. Khi học tiếng Pháp, người học có thể tham gia vào tình huống "Đặt phòng khách sạn ở Paris". Trong tình huống này, một Agent đóng vai nhân viên lễ tân khách sạn—hỏi về ngày check-in, loại phòng, phương thức thanh toán—trong khi Agent khác đóng vai "Language Coach" (huấn luyện viên ngôn ngữ) đứng bên cạnh, gợi ý từ vựng và ngữ pháp khi người học gặp khó khăn. Nếu người học nói "Je veux une chambre pour deux nuits" (Tôi muốn một phòng cho hai đêm), nhân viên lễ tân sẽ phản hồi một cách tự nhiên và tiếp tục cuộc hội thoại. Nhưng nếu người học nói "Je avoir chambre deux nuits" (sai ngữ pháp), Language Coach sẽ nhẹ nhàng can thiệp: "Bạn có thể thử dùng 'veux' (muốn) sau 'Je' không? Đó là dạng chia động từ 'vouloir' (muốn) ở ngôi thứ nhất số ít."

Điều thú vị là hai Agent này không hoạt động độc lập, mà liên tục trao đổi thông tin với nhau thông qua một shared state (trạng thái chia sẻ). Language Coach biết chính xác người học đã nói gì với nhân viên lễ tân, có thể đánh giá mức độ chính xác ngữ pháp và tự nhiên của câu nói, sau đó quyết định có cần can thiệp hay không. Nhân viên lễ tân cũng nhận biết được khi Language Coach đưa ra gợi ý, sẽ tạm dừng để người học có thời gian điều chỉnh câu trả lời trước khi tiếp tục cuộc hội thoại.

Dữ liệu từ Duolingo cho thấy người dùng tham gia Scenario Practice với multi-agent system dành trung bình 3.5 lần thời gian nhiều hơn so với bài tập truyền thống, và tỷ lệ retention (giữ chân người dùng) tăng 31% sau 3 tháng. Quan trọng hơn, trong các bài test speaking thực tế, học viên qua Scenario Practice đạt điểm fluency (lưu loát) cao hơn 28% so với nhóm chỉ học qua bài tập nghe-đọc truyền thống.

## Debate Agents: Học qua tranh luận

Một pattern khác cực kỳ hữu ích trong giáo dục là "debate" (tranh luận)—hai hoặc nhiều Agent đại diện cho các quan điểm khác nhau về một chủ đề gây tranh cãi, tranh luận với nhau để người học có thể quan sát và hình thành quan điểm riêng. Phương pháp này đặc biệt hiệu quả trong các môn xã hội, triết học, hoặc bất kỳ lĩnh vực nào không có một câu trả lời duy nhất đúng.

Coursera, trong khóa học "Critical Thinking and Ethics" ra mắt vào tháng 6/2024, đã triển khai một tính năng gọi là "AI Debate Theater". Khi học đến chủ đề "Liệu AI có nên được sử dụng trong quyết định tuyển dụng?", học viên không chỉ đọc tài liệu lý thuyết mà còn xem một cuộc tranh luận trực tiếp giữa hai Agent: "ProAI Agent" và "CautiousAI Agent".

ProAI Agent lập luận: "AI loại bỏ bias tiềm thức của con người trong tuyển dụng. Nghiên cứu từ Harvard Business Review cho thấy 75% nhà tuyển dụng thừa nhận họ đã bị ảnh hưởng bởi những yếu tố không liên quan như ngoại hình hoặc trường đại học của ứng viên. AI chỉ đánh giá dựa trên kỹ năng và kinh nghiệm thực tế, công bằng hơn nhiều."

CautiousAI Agent phản biện: "Nhưng AI được huấn luyện từ dữ liệu của con người, và dữ liệu đó chứa đựng bias. Amazon đã phải hủy bỏ công cụ tuyển dụng AI của họ vào năm 2018 vì nó phân biệt đối xử với ứng viên nữ. AI không phải là trung lập—nó phản ánh và thậm chí khuếch đại bias có sẵn trong dữ liệu huấn luyện."

ProAI Agent đáp lại: "Đúng, nhưng đó là vấn đề về cách xây dựng AI, không phải về bản chất của AI. Nếu chúng ta cẩn thận kiểm tra và cân bằng dữ liệu huấn luyện, AI có thể công bằng hơn nhiều so với con người. Còn con người thì không thể 'debug' bias của chính mình."

Cuộc tranh luận tiếp diễn với nhiều lượt qua lại, mỗi Agent đưa ra bằng chứng, phản biện lập luận của đối phương, và dần dần làm rõ các sắc thái phức tạp của vấn đề. Sau khi xem xong, học viên được yêu cầu viết một bài essay ngắn trình bày quan điểm của riêng mình, có thể đồng ý với một bên, hoặc đưa ra quan điểm thứ ba kết hợp các yếu tố từ cả hai.

Kết quả đánh giá từ 12,000 học viên tham gia khóa học cho thấy nhóm xem AI Debate Theater viết bài essay với độ sâu phân tích cao hơn 42% và đưa ra nhiều luận điểm đa chiều hơn 35% so với nhóm chỉ đọc tài liệu tĩnh. Quan trọng hơn, 87% học viên cho biết cuộc tranh luận giữa các Agent giúp họ hiểu rõ hơn về sự phức tạp của vấn đề, thay vì chỉ tìm kiếm một câu trả lời đơn giản đúng/sai.

## LangGraph: Điều phối Agent như một state machine

Để xây dựng các hệ thống multi-agent phức tạp, các nhà phát triển cần một framework mạnh mẽ để quản lý luồng giao tiếp, quyết định Agent nào nói khi nào, và đảm bảo các Agent hoạt động nhịp nhàng với nhau. LangGraph, một thư viện được phát triển bởi LangChain ra mắt vào đầu năm 2024, chính là công cụ được thiết kế cho mục đích này.

LangGraph mô hình hóa hệ thống multi-agent như một state machine (máy trạng thái)—một graph trong đó mỗi node đại diện cho một Agent hoặc một trạng thái cụ thể, và mỗi edge (cạnh) đại diện cho điều kiện chuyển từ trạng thái này sang trạng thái khác. Ví dụ: trong hệ thống roleplaying của Duolingo mô tả ở trên, graph có thể có các node như:

- **Student Input**: Node nhận input từ học sinh
- **Language Coach Analysis**: Node phân tích câu trả lời của học sinh
- **Coach Intervention**: Node quyết định có cần can thiệp hay không
- **Hotel Receptionist Response**: Node sinh phản hồi từ nhân viên lễ tân
- **End of Conversation**: Node kết thúc khi cuộc hội thoại hoàn tất

Các edge giữa các node có các điều kiện cụ thể. Ví dụ: từ "Language Coach Analysis" có thể có hai edge: một edge đến "Coach Intervention" nếu phát hiện lỗi nghiêm trọng, và một edge khác đến "Hotel Receptionist Response" nếu câu trả lời của học sinh đủ tốt để tiếp tục cuộc hội thoại không cần điều chỉnh.

Một tính năng mạnh mẽ của LangGraph là khả năng xử lý "parallel execution" (thực thi song song). Trong một số tình huống, nhiều Agent có thể hoạt động đồng thời. Ví dụ: trong hệ thống debate về AI ethics, có thể có một "Moderator Agent" (người điều phối) đồng thời theo dõi cả hai Agent tranh luận, đánh giá xem cuộc tranh luận có đi chệch hướng hay không, và quyết định khi nào nên kết thúc hoặc chuyển sang chủ đề con tiếp theo.

## Ứng dụng thực tế: Team of Experts

Một mô hình multi-agent đang ngày càng phổ biến trong giáo dục là "Team of Experts"—một nhóm Agent với chuyên môn khác nhau cộng tác để giải quyết một vấn đề phức tạp. Thay vì một Agent đa năng cố gắng biết tất cả mọi thứ (và thường sẽ sai trong nhiều lĩnh vực), hệ thống này tạo ra các Agent chuyên sâu, mỗi Agent xuất sắc trong một lĩnh vực cụ thể.

Khan Academy đã thử nghiệm một hệ thống như vậy cho môn STEM (Science, Technology, Engineering, Mathematics) vào tháng 9/2024. Khi học sinh hỏi một câu hỏi như "Làm thế nào để thiết kế một cây cầu vững chắc?", hệ thống không để một Agent duy nhất trả lời, mà kích hoạt một nhóm gồm:

**Physics Agent**: Giải thích các nguyên lý vật lý liên quan—trọng lực, lực kéo, lực nén, moment xoắn.

**Materials Agent**: Thảo luận về các vật liệu xây dựng phù hợp—thép, beton, gỗ—ưu nhược điểm của từng loại.

**Math Agent**: Hướng dẫn các phép tính cần thiết để xác định kích thước dầm, trụ, và tải trọng tối đa.

**History Agent**: Đưa ra các ví dụ lịch sử về những cây cầu nổi tiếng và bài học từ các thất bại (như cầu Tacoma Narrows sụp đổ vào năm 1940 do cộng hưởng).

**Design Agent**: Tổng hợp tất cả thông tin từ các Agent khác và đề xuất một quy trình thiết kế bước-by-bước.

Các Agent này không chỉ đơn thuần lần lượt nói, mà thực sự tương tác với nhau. Physics Agent có thể nói: "Để cầu không bị sập, lực nén trên các trụ không được vượt quá ngưỡng chịu tải của vật liệu." Materials Agent nghe thấy điều này và bổ sung: "Với thép grade A36, ngưỡng đó là khoảng 36,000 psi. Nếu dùng beton, con số sẽ thấp hơn nhiều, khoảng 3,000-5,000 psi." Math Agent lập tức đưa ra công thức: "Vậy chúng ta cần tính stress = Force / Area, và đảm bảo stress < yield strength của vật liệu."

Sau khoảng 5-7 phút trao đổi giữa các Agent, Design Agent tổng hợp và trình bày một kế hoạch thiết kế rõ ràng, từng bước một, kèm theo các tính toán cụ thể và giải thích tại sao mỗi quyết định được đưa ra. Học sinh không chỉ nhận được câu trả lời, mà còn được chứng kiến toàn bộ quá trình tư duy của một đội ngũ chuyên gia đa lĩnh vực.

Đánh giá ban đầu từ 3,000 học sinh thử nghiệm cho thấy Team of Experts giúp học sinh hiểu sâu hơn về tính liên ngành của các vấn đề thực tế—89% học sinh cho biết họ nhận ra rằng giải quyết vấn đề phức tạp cần kiến thức từ nhiều lĩnh vực, không chỉ một môn học đơn lẻ. Điểm số trung bình trong các bài test STEM tổng hợp tăng 19% sau 2 tháng sử dụng hệ thống.

## Thách thức và best practices

Mặc dù multi-agent systems mang lại nhiều lợi ích, việc triển khai chúng không phải không có thách thức. Một vấn đề lớn là "coordination overhead" (chi phí điều phối)—khi có nhiều Agent, việc quyết định Agent nào nên nói khi nào, làm thế nào để tránh các Agent nói chồng lên nhau hoặc mâu thuẫn với nhau, và đảm bảo cuộc hội thoại không bị lạc hướng trở nên phức tạp.

Một best practice quan trọng là thiết lập rõ ràng "roles and responsibilities" (vai trò và trách nhiệm). Mỗi Agent cần biết chính xác nhiệm vụ của mình là gì, khi nào nên can thiệp, và khi nào nên im lặng để Agent khác nói. Trong hệ thống Team of Experts của Khan Academy, mỗi Agent được định nghĩa một "persona" cụ thể trong system prompt, ví dụ: "You are the Physics Expert Agent. Your role is to explain physical principles relevant to the problem. Speak only when your expertise is needed. Be concise and cite scientific principles clearly."

Một best practice khác là sử dụng một "Orchestrator Agent" (Agent điều phối)—một Agent đặc biệt có nhiệm vụ quản lý luồng hội thoại, quyết định Agent nào nên được kích hoạt tiếp theo dựa trên ngữ cảnh. Trong hệ thống debate của Coursera, Orchestrator Agent theo dõi số lượng lượt tranh luận, đảm bảo cả hai bên đều có đủ cơ hội phát biểu, và quyết định khi nào nên kết thúc tranh luận để tránh lặp lại.

Cuối cùng, vấn đề "consistency" (tính nhất quán) cũng rất quan trọng. Khi nhiều Agent tương tác, có thể xuất hiện những mâu thuẫn không mong muốn—Agent A nói một điều, Agent B phủ nhận điều đó một cách không cố ý. Để phòng tránh, các hệ thống production thường duy trì một "shared knowledge base" (cơ sở tri thức chung) mà tất cả Agent đều truy cập, đảm bảo thông tin thực tế (như ngày Napoleon qua đời) được thống nhất. Đối với các vấn đề chủ quan hoặc gây tranh cãi, sự mâu thuẫn có thể được chấp nhận—thậm chí khuyến khích—miễn là nó được frame như một "healthy debate" (tranh luận lành mạnh) thay vì confusion (sự lộn xộn).

## Tương lai của collaborative AI

Xu hướng hiện tại đang đi xa hơn roleplaying và debate—hướng tới các hệ thống nơi AI Agents không chỉ nói chuyện với nhau, mà còn cộng tác thực hiện các nhiệm vụ phức tạp, giống như một team làm việc thực sự. Microsoft đang phát triển "Copilot Studio", một nền tảng cho phép tạo ra các nhóm Agent với vai trò khác nhau—một Agent viết code, Agent khác review code, Agent thứ ba viết documentation, Agent thứ tư kiểm tra bugs. OpenAI cũng đã công bố "GPT Teams" vào hội nghị DevDay 2024, với tầm nhìn về các Agent có thể tự tổ chức và phân chia công việc mà không cần con người điều khiển chi tiết từng bước.

Trong giáo dục, điều này có thể dẫn đến các "AI Study Groups" (nhóm học tập AI)—nơi một nhóm Agent đóng vai các sinh viên khác nhau với phong cách học và quan điểm khác nhau, cùng nhau thảo luận và giải quyết bài tập, trong khi người học thực có thể quan sát, tham gia, hoặc học hỏi từ dynamic interaction giữa các Agent. Tưởng tượng một sinh viên cô đơn học một mình lúc nửa đêm, nhưng vẫn có thể "ngồi trong" một study group ảo với nhiều "bạn học AI", mỗi người đưa ra ý kiến và góc nhìn khác nhau về bài toán—trải nghiệm đó có thể thay đổi hoàn toàn cách chúng ta nghĩ về học tập cá nhân và học tập xã hội.

