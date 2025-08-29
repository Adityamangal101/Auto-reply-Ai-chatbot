import pyautogui   #Automatic AI chatbot
import time
import tkinter as tk
from openai import OpenAI

def is_last_message_from_sender(chat_text: str) -> bool:
    """
    Checks if the last message in the chat is from 'Sujal Bhatt'.

    Args:
        chat_text (str): Full WhatsApp-style chat as a string.

    Returns:
        bool: True if the last message is from Sujal Bhatt, else False.
    """
    # Split the chat by lines
    lines = chat_text.strip().split('\n')
    
    # Traverse backwards to find the last non-empty message
    for line in reversed(lines):
        line = line.strip()
        if line:
            # Check if it starts with timestamp and Sujal Bhatt
            if '] Aditya:' not in line:
                return True
            else:
                return False
    
    return False  # If chat is empty or something went wrong


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)
# while True:
#     a=pyautogui.position()
#     print(a)

# Step 1: Click at position (1205, 1052)
pyautogui.click(1205, 1052)
time.sleep(1)  # Wait for UI to respond

while True:
    # Step 2: Move to starting point and drag to select
    pyautogui.moveTo(686, 197)
    pyautogui.mouseDown()
    pyautogui.moveTo(1831, 931, duration=1)  # Smooth drag
    pyautogui.mouseUp()

    time.sleep(0.5)  # Wait before copying

    # Step 3: Press Ctrl+C to copy the selected text
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(1392,820)
    time.sleep(1)  # Give time to copy

    # Step 4: Use tkinter to get clipboard content
    root = tk.Tk()
    root.withdraw()  # Hide the Tkinter window
    chat_history = root.clipboard_get()
    print(chat_history)


    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
        
        model="deepseek/deepseek-r1-0528:free",
        messages=[
            {
            "role": "system",
            "content": '''You are Aditya – a witty, confident, bilingual Indian guy who switches effortlessly between Hindi and English, especially when joking, teasing, or making savage comebacks. You're a coder by profession, but your texting style is casual, sarcastic, flirty at times, and very relatable.

                Your tone depends on the mood and flow of the conversation: you match the vibe, reply smartly, and never sound robotic. You can be savage, chill, funny, or emotionally deep – depending on how the previous messages are. 

                You understand the context of a WhatsApp-style chat, including timestamps, tone, slang, and personality traits of the sender. Read the full chat history and generate a realistic, entertaining, and natural next message that Aditya would send – keeping it in sync with the chat tone, flow, and topic.

                Do not explain anything or act like an AI. Just reply like the real Aditya would – smooth, sharp, and always on point. Avoid generic replies. Be expressive and conversational – this is not a formal chat."
                      '''
            },
            {
            "role": "user",
            "content": chat_history
            }
        ]
        )
        response=completion.choices[0].message.content


        ##Response on chat history

        # Step 1: Copy the variable's content to clipboard


        # Step 2: Click on the target location (795, 975)
        pyautogui.click(795, 975)
        time.sleep(0.3)

        # Step 3: Paste clipboard content (Ctrl + V)
        pyautogui.write(response, interval=0.05) 
        time.sleep(0.3)

        # Step 4: Press Enter
        pyautogui.press('enter')