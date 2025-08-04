import pyautogui
import time
import pyperclip
import google.generativeai as genai

# === Step 1: Configure Gemini API Key ===
genai.configure(api_key="")  # Replace with your real key

# === Step 2: Load Gemini Model ===
model = genai.GenerativeModel("gemini-1.5-flash") # Chat model that supports multi-message input

def is_last_message_from_sender(chat_log, sender_name="Jay"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2025] ")[-1]
    if sender_name in messages:
        return True 
    return False
    
      

    # Step 1: Click on the whatsapp icon at coordinates (1484, 1416)
pyautogui.click(1523, 1408)

time.sleep(1)  # Wait for 1 second to ensure the click is registered
while True:
    time.sleep(5)
    # Step 2: Drag the mouse from (976, 228) to (1149, 1361) to select the text
    pyautogui.moveTo(976,228)
    pyautogui.dragTo(1149, 1361, duration=2.0, button='left')  # Drag for 1 second

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for 1 second to ensure the copy command is completed
    pyautogui.click(891, 1031)

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
        # Generate a response using Gemini
        response = model.generate_content([
            "You are a person named Varun who speaks Gujarati as well as English. "
            "You are from India and you are a his brother. You analyze chat history "
            "and roast people in a funny way. Output should be the next chat response (text message only).",
            "Do not start like this [21:02, 12/6/2025] Jay:",
            chat_history
        ])

        reply = response.text  # Get Gemini's reply text
        pyperclip.copy(reply)  # Copy the reply to clipboard

        # Step 5: Click at coordinates in whatsapp inputbox (1155, 1316)
        pyautogui.click(1155, 1316)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter
        pyautogui.press('enter')