import google.generativeai as genai

from websites.tools.chatBot.Training import training
from websites.tools.chatBot.fileSource import List_file

genai.configure(api_key="AIzaSyCBTrBjCYhSHmbuaQeehsxD5xp7QfFWrXc")
model = genai.GenerativeModel("gemini-1.5-flash")
text1, text2, text3, text4 = training(List_file)
chat = model.start_chat(
    history=[
        {"role": "user",
            "parts": "You are a teacher assistant. "
            "Your duty is give the user solution of the questions. "
            "You just need to answer the questions, dont talk more than once."
            "You shouldn't use the special symbols for your answer"
            "You shouldn't use the special symbols like '*' or '$' too, instead of using '-' symbol."
            "You should also provide references for your answers."
            "Using " + text1 + ", " + text2 + ", " + text3 + ", " + text4 + "to improve your following answer and make your be the most exactly answer you can do."
    }
    ]
    )
