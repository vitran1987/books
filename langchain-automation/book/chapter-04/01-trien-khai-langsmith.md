# Triển khai LangSmith

Sarah Chen nghẹt thở khi đọc email từ phụ huynh. Họ phàn nàn rằng hệ thống gia sư AI mà công ty cô triển khai đã dạy sai phép nhân phân số cho con họ suốt một tuần qua. Điều kinh khủng hơn là khi Sarah kiểm tra logs, cô phát hiện ra hơn 2.300 học sinh khác cũng nhận được những lời giải toán sai tương tự trong cùng khoảng thời gian đó. Con số ấy đủ để hủy hoại uy tín mà đội ngũ cô dày công xây dựng trong suốt hai năm qua. Nhưng câu hỏi đau đớn nhất không phải là "tại sao hệ thống sai", mà là "tại sao không ai phát hiện ra sớm hơn?". Đơn giản vì không ai đang theo dõi hệ thống một cách có hệ thống.

Đó là lý do LangSmith ra đời—không phải chỉ là một công cụ debug, mà là một hệ thống observability toàn diện cho các ứng dụng AI tự động hóa. Trong kỷ nguyên mà AI agent có thể tự động xử lý hàng ngàn request mỗi ngày, việc không có visibility vào cách chúng hoạt động giống như lái xe với kính chắn gió bị che kín. Bạn có thể vẫn tiến về phía trước, nhưng tai nạn là điều không tránh khỏi.

Theo một nghiên cứu từ Gartner năm 2024, 68% các dự án AI production thất bại không phải vì model không đủ tốt, mà vì thiếu khả năng monitoring và debugging khi có vấn đề phát sinh. Đây chính xác là khoảng trống mà LangSmith lấp đầy. Công cụ này không chỉ cho phép bạn thấy AI agent của mình đang làm gì, mà còn hiểu tại sao nó lại làm như vậy, từng bước một trong chain of thought phức tạp.

## Tracing: Nhìn thấy mọi bước đi của Agent

Điểm khác biệt lớn nhất giữa traditional software và AI system nằm ở tính bất định. Với code thông thường, cùng một input luôn cho cùng một output. Nhưng với LLM, mỗi lần chạy có thể tạo ra kết quả khác nhau, thậm chí với cùng một prompt. Đây là lý do tại sao "printf debugging" truyền thống không còn hiệu quả nữa. Bạn cần một cách để capture toàn bộ execution path, từ input ban đầu đến final output, bao gồm cả mọi prompt, response, và intermediate step.

LangSmith giải quyết vấn đề này thông qua cơ chế tracing tự động. Mỗi khi một chain hoặc agent chạy, LangSmith tự động ghi lại mọi detail: thời gian bắt đầu và kết thúc mỗi step, token count, model được sử dụng, input và output của từng component, và cả error nếu có. Tất cả được visualize dưới dạng một tree structure rõ ràng, giúp developer có thể zoom in vào bất kỳ node nào để xem chi tiết.

Trong trường hợp của Sarah, nếu LangSmith đã được triển khai từ đầu, cô có thể phát hiện vấn đề ngay trong ngày đầu tiên thay vì sau một tuần. Bằng cách set up alert khi accuracy score của math tutor agent giảm xuống dưới 95%, hệ thống sẽ tự động thông báo cho team. Hơn nữa, Sarah có thể replay lại chính xác execution flow của những request bị lỗi, xem prompt nào đã được gửi đến model, response thực tế là gì, và tại sao agent lại chọn tool hoặc action cụ thể đó.

Ví dụ cụ thể, một trace điển hình của math tutor agent sẽ trông như thế này trong LangSmith:
- Root: MathTutorAgent (duration: 3.2s, tokens: 450)
  - Step 1: AnalyzeQuestion (duration: 0.8s, tokens: 120)
    - Input: "What is 2/3 × 3/4?"
    - Output: {operation: "fraction_multiplication", numerators: [2,3], denominators: [3,4]}
  - Step 2: SelectSolutionStrategy (duration: 0.6s, tokens: 95)
    - Input: {operation: "fraction_multiplication", ...}
    - Output: {strategy: "cross_multiply", steps: [...]}
  - Step 3: GenerateExplanation (duration: 1.8s, tokens: 235)
    - Input: {strategy: "cross_multiply", ...}
    - Output: "First, multiply the numerators: 2 × 3 = 6..."

Mỗi node trong tree này có thể click để xem full details, bao gồm cả prompt template được sử dụng, variables được inject, và raw response từ LLM. Khi bug xảy ra, developer không cần phải guess hoặc reproduce manually—tất cả evidence đã được capture sẵn.

## Metrics quan trọng cần theo dõi

Với hệ thống AI production, có ba nhóm metrics mà bạn phải monitor liên tục: Performance Metrics, Quality Metrics, và Cost Metrics. Mỗi nhóm phục vụ một mục đích khác nhau nhưng đều quan trọng như nhau trong việc đảm bảo hệ thống chạy healthy.

**Performance Metrics** đo lường tốc độ và khả năng responsive của hệ thống. Latency—thời gian từ khi user gửi request đến khi nhận được response đầy đủ—là metric quan trọng nhất trong nhóm này. Theo research từ Google, mỗi 100ms delay trong response time có thể giảm conversion rate xuống 7%. Với AI tutor, nếu học sinh phải đợi quá 5 giây để nhận câu trả lời, họ sẽ nhanh chóng mất kiên nhẫn và chuyển sang competitor. LangSmith tự động track latency cho từng component trong chain, giúp bạn identify bottleneck. Có thể step "GenerateExplanation" đang mất 3 giây trong khi các step khác chỉ mất vài trăm milliseconds? Đó chính là nơi cần optimize.

Throughput—số request mà hệ thống có thể xử lý trong một giây—cũng critical, đặc biệt khi scale. Một AI customer service bot có thể handle 50 concurrent conversations mà không bị chậm? Hay nó bắt đầu degrade sau 20 users? LangSmith cho phép bạn run load tests và visualize performance curve. Shopify's AI support team phát hiện rằng latency của họ tăng 300% khi vượt quá 75 concurrent users. Họ đã phải tách system ra thành multiple smaller agents, mỗi cái handle một loại request khác nhau, để distribute load evenly.

**Quality Metrics** đo lường độ chính xác và hữu ích của output. Đây là phần khó nhất vì không như latency có thể measure bằng milliseconds, quality thường subjective. Tuy nhiên, có một số cách để quantify nó. Success Rate—phần trăm requests được xử lý thành công mà không gặp error—là metric đơn giản nhất. Nhưng "không có error" không có nghĩa là "useful output". Một math tutor có thể trả lời "I don't know" cho mọi câu hỏi và có 100% success rate, nhưng hoàn toàn vô dụng.

Vì vậy, nhiều team triển khai User Feedback Score—đơn giản là thumbs up/down button sau mỗi response. Duolingo AI feature cho phép learners rate câu trả lời của AI tutor, và sau ba tháng thu thập data, họ phát hiện rằng response với feedback score thấp thường có pattern chung: quá ngắn (dưới 50 words), không có examples, hoặc sử dụng thuật ngữ quá technical mà beginner không hiểu. Team đã adjust prompt để explicitly yêu cầu AI "explain like I'm 10 years old" và bao gồm ít nhất một concrete example. Kết quả là positive feedback tăng từ 72% lên 89% chỉ sau hai tuần.

LangSmith còn hỗ trợ Custom Evaluators—cho phép bạn viết code để automatically score output. Ví dụ, với math tutor, bạn có thể viết evaluator kiểm tra xem final answer có match với expected result không. Với customer support bot, evaluator có thể check xem response có chứa required information như order number, return policy, hoặc next steps. Những evaluators này chạy automatically trên mỗi trace và aggregate thành dashboard, giúp bạn spot trends. Nếu accuracy bỗng nhiên giảm từ 95% xuống 85%, có thể đó là dấu hiệu model đã bị updated bởi provider hoặc prompt template bị modify nhầm.

**Cost Metrics** theo dõi chi phí để đảm bảo hệ thống vẫn profitable. OpenAI tính phí theo token—input tokens rẻ hơn output tokens, và GPT-4 đắt gấp 10 lần GPT-3.5. Một agent phức tạp có thể burn through hàng nghìn dollars chỉ trong vài ngày nếu không careful. LangSmith track token usage cho từng request và aggregate thành total cost. Bạn có thể set budget alert: "notify me if daily spending exceeds $100" hoặc "if average cost per request goes above $0.50".

Một case study đáng chú ý là Jasper AI—công cụ content generation với hơn 100,000 users. Ban đầu họ sử dụng GPT-4 cho tất cả requests để đảm bảo quality, nhưng monthly bill từ OpenAI lên đến $280,000. Sau khi implement LangSmith monitoring, team phát hiện rằng 60% requests là simple tasks như "fix grammar" hoặc "make this shorter"—những việc mà GPT-3.5-turbo có thể làm tốt với giá chỉ bằng 1/10. Họ implement intelligent routing: complex creative tasks dùng GPT-4, còn simple editing tasks dùng GPT-3.5. Kết quả là monthly cost giảm xuống $95,000 mà quality metrics gần như không thay đổi. Đây chính là power của observability—bạn không thể optimize cái mà bạn không measure.

## Triển khai LangSmith trong thực tế

Integrate LangSmith vào existing LangChain application cực kỳ straightforward. Về cơ bản bạn chỉ cần set hai environment variables: `LANGCHAIN_API_KEY` và `LANGCHAIN_TRACING_V2=true`. Sau đó mọi chain hoặc agent execution tự động được trace và gửi về LangSmith platform. Không cần modify code hiện tại, không cần wrap functions hay add decorators. LangChain đã built-in integration nên việc enable chỉ là flip a switch.

Tuy nhiên, để tận dụng tối đa LangSmith, bạn nên organize traces thành các "projects" và "runs". Mỗi project đại diện cho một feature hoặc environment—ví dụ "math-tutor-production", "customer-support-staging", hoặc "content-generator-dev". Trong mỗi project, các runs được group theo session hoặc user ID, giúp bạn dễ dàng filter và analyze. Nếu một user cụ thể report issue, bạn có thể search theo user_id của họ và xem toàn bộ lịch sử interaction, identify chính xác request nào gây ra problem.

Tags và metadata cũng cực kỳ hữu ích. Bạn có thể tag traces với information như "model_version: gpt-4-1106", "user_tier: premium", hoặc "feature: essay_feedback". Sau này khi cần compare performance giữa hai model versions, chỉ cần filter theo tag và compare metrics. Hoặc khi business team hỏi "premium users có experience tốt hơn free users không?", bạn có concrete data để answer thay vì guess.

Notion AI team chia sẻ setup của họ trong một blog post năm 2024. Họ có ba projects riêng: Production, Staging, và Experiments. Production project có alert setup nghiêm ngặt—bất kỳ error rate nào vượt 1% hoặc latency p95 vượt 5 giây đều trigger Slack notification ngay lập tức. Staging được dùng để test new features hoặc prompt changes trước khi deploy lên production. Experiments là playground cho research team thử nghiệm new approaches mà không sợ ảnh hưởng đến real users.

Họ cũng implement custom evaluators chạy automatically sau mỗi production deployment. Evaluators này pull random sample of 100 recent traces, run them through quality checks, và generate report comparing với baseline metrics từ previous version. Nếu bất kỳ metric nào drop more than 5%, deployment tự động rollback và alert team lead. Cơ chế này đã save họ nhiều lần khi new prompt changes tưởng chừng harmless nhưng lại cause subtle degradation in quality.

## Dashboard và Alerting

Raw traces và metrics chỉ hữu ích nếu bạn biết cách extract insights từ chúng. LangSmith cung cấp dashboard UI cho phép visualize trends over time. Bạn có thể tạo charts showing latency percentiles (p50, p90, p95, p99) by day, cost per request by hour, hoặc success rate by user cohort. Những charts này không chỉ useful cho debugging mà còn cho business decision making. Nếu thấy usage spike vào weekend, có thể cần scale infrastructure accordingly. Nếu cost per request tăng đột ngột, có thể đó là signal rằng users đang abuse system hoặc có bot traffic.

Nhưng monitoring thụ động không đủ. Bạn cần proactive alerting để catch problems trước khi chúng affect too many users. LangSmith cho phép set up rules như "if error rate exceeds 5% for more than 10 minutes, send alert to #incidents Slack channel" hoặc "if p95 latency goes above 8 seconds, page on-call engineer". Alert rules nên tuned carefully—quá sensitive sẽ tạo alert fatigue khiến team ignore notifications, quá lax thì issues chỉ được phát hiện sau khi users đã complain.

Intercom đã share metric thresholds mà họ sử dụng cho AI customer support bot: Error rate trên 3%, latency p95 trên 6 giây, hoặc daily cost tăng hơn 25% so với 7-day average đều trigger alerts. Thêm vào đó, họ có "canary alerts" monitor new deployments—nếu error rate của new version cao hơn 50% so với old version trong first 100 requests, auto-rollback immediately. Approach này đảm bảo bad deploys không bao giờ affect large portion of user base.

Một best practice khác là implement "health check endpoints" cho agents. Đây là simple test cases chạy every few minutes để verify agent vẫn functioning correctly. Ví dụ, math tutor agent có health check là solve "2+2=?". Nếu agent không trả lời "4" hoặc mất quá 10 giây để respond, alert sẽ fire ngay lập tức. Health checks này complementary với real traffic monitoring—chúng có thể catch issues ngay cả khi không có users actively using system, như lúc 3am hay trong holidays.

Datadog integration với LangSmith cũng mở ra nhiều possibilities. Bạn có thể correlate AI metrics với infrastructure metrics. Ví dụ, nếu thấy latency spike đồng thời với CPU usage tăng cao trên application servers, rõ ràng vấn đề là compute resources insufficient. Còn nếu latency tăng nhưng CPU bình thường, có thể đó là OpenAI API đang slow hoặc network issues. Context này extremely valuable khi debugging production incidents.

Cuối cùng, đừng quên về compliance và privacy khi implement observability. LangSmith traces capture full input và output của agent, bao gồm cả user data. Nếu application của bạn handle sensitive information như medical records hay financial data, cần ensure traces được encrypt at rest và comply với regulations như HIPAA hay GDPR. LangSmith có options để mask sensitive fields trước khi gửi về server—ví dụ redact credit card numbers, emails, hoặc patient names. Trade-off là bạn sẽ có less context khi debugging, nhưng đó là necessary compromise để protect user privacy.

Tóm lại, LangSmith không phải chỉ là nice-to-have debugging tool mà là essential infrastructure cho bất kỳ AI automation system nào chạy production. Nó biến "black box" AI thành "glass box", cho phép bạn understand, monitor, và optimize system một cách scientific thay vì rely on gut feeling. Trong thế giới mà một agent có thể process thousands of requests per day, việc không có observability không khác gì đánh bạc với business của mình. Sarah đã học được bài học đau đớn này—hy vọng bạn sẽ không phải lặp lại sai lầm tương tự.
