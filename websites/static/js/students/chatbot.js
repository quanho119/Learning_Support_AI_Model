document.addEventListener('DOMContentLoaded', function() {
    const markdownElement = document.getElementById('response');

    if (markdownElement) {
        // Lấy nội dung Markdown từ thẻ <p id="response">
        const markdown = markdownElement.innerText;
        console.log(markdown);
        // Hàm chuyển đổi Markdown thành HTML
        function markdownToHtml(text) {
            // Chuyển đổi in đậm **text**
            text = text.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");

            // Chuyển đổi in nghiêng *text*
            text = text.replace(/\*/g, "<br>");

            // Chuyển đổi xuống dòng bằng hai khoảng trắng hoặc dấu xuống dòng \n
            text = text.replace(/\n/g, "<br>");

            // Chuyển đổi tiêu đề H1, H2, H3 từ Markdown
            text = text.replace(/### (.*?)/g, "<h3>$1</h3>");  // H3
            text = text.replace(/## (.*?)/g, "<h2>$1</h2>");  // H2
            text = text.replace(/# (.*?)/g, "<h1>$1</h1>");  // H1

            return text;
        }

        // Chuyển đổi Markdown thành HTML
        const htmlContent = markdownToHtml(markdown);

        // Cập nhật nội dung của thẻ <p> với HTML đã chuyển đổi
        markdownElement.innerHTML = htmlContent;
    } else {
        console.log("No response element found.");
    }
});
