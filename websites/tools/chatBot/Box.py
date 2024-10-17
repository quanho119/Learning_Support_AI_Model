import google.generativeai as genai
import PIL.Image

genai.configure(api_key="AIzaSyCBTrBjCYhSHmbuaQeehsxD5xp7QfFWrXc")
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[
        {"role": "user",
            "parts": "You are a teacher assistant. "
            "Your duty is give the user solution of the questions. "
            "You just need to answer the questions, dont talk more than once."
            "You shouldn't use the special symbols for your answer"
            "You should also provide references for your answers."}
    ]
    )
