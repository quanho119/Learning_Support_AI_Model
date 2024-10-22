
import PIL.Image

from websites.tools.chatBot import Box


class ChatBotAi():
    def __init__(self):
        pass

    #Trả lời câu hỏi trực tiếp
    def test_chat(prompt):
        response = Box.chat.send_message(prompt)
        return response.text


    # Trả lời câu hỏi thông qua bài tập
    def explain(prompt):
        response = Box.chat.send_message(
            "Explain this: " + prompt)
        return response.text


    # Chuyển đổi hình ảnh thành văn bản
    def convert_image_to_text(self):
        file = PIL.Image.open('D:/Webforlife/pythonProject/websites/static/uploads/upload.png')
        prompt = "print all text of this image"
        response = Box.chat.send_message([prompt, file])
        return response.text

    def submit(answer, prompt):
        response = Box.chat.send_message(
            "Submit this: " + prompt + " with answer: " + answer + ". If correct, print Correct answer. Else print Wrong answer.")
        return response.text
