import google.generativeai as genai

API_KEY = "AIzaSyA6HP2yuMpSEpcRGRSihZgKuQ64D8kUewE"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

print("Chat with Gemini! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chat.send_message(user_input)
    print("Gemini:" , response.text)