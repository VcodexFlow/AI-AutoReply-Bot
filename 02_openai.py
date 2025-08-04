# pip install google-generativeai
import google.generativeai as genai

# ✅ Step 1: Configure your Gemini API key
genai.configure(api_key="")  # Replace with your real API key

# ✅ Step 2: Create Gemini model (use "gemini-pro" for text chat)
model = genai.GenerativeModel("gemini-1.5-flash")
  # more advanced than "gemini-pro"

# ✅ Step 3: Define your conversation history (chat input)
chat_history = "Varun: Hello, how can I help?\nUser: Tell me a joke."

response = model.generate_content([
    "You are Varun, a friendly coder from India who speaks Hindi and English.",
    chat_history
])  


# ✅ Step 4: Generate response
response = model.generate_content([
    "You are a person named Varun who speaks Hindi as well as English. "
    "He is from India and is a coder. Analyze the chat history and respond like Varun in a friendly tone.",
    chat_history
])

# ✅ Step 5: Print the generated reply
print("🤖 Varun says:", response.text)
