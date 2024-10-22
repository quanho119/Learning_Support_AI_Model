document.addEventListener("DOMContentLoaded", function () {
    // Lấy nút Explain và form
    const explainButton = document.getElementById("explainButton");
    const answerForm = document.getElementById("answerForm");

    // Kiểm tra xem nút và form có tồn tại không
    if (explainButton && answerForm) {
        explainButton.onclick = function () {
            answerForm.style.display = "none"; // Ẩn form khi nhấn nút
        };
    }
});