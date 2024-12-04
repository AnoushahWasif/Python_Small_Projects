import pyautogui
import time

def send_whatsapp_message(message, repetitions, delay=1):
    """
    Sends a WhatsApp message repeatedly using WhatsApp Desktop.

    Parameters:
    - message: The text to send.
    - repetitions: Number of times to send the message.
    - delay: Time delay between sending messages (default is 1 second).
    """
    for i in range(repetitions):
        pyautogui.typewrite(message)  # Type the message
        pyautogui.press("enter")     # Press Enter to send
        print(f"Sent message {i + 1}: {message}")
        time.sleep(delay)            # Wait before sending the next message

# Customize your parameters
message_text = "Okay!"
number_of_times = 100
delay_between_messages = 1  # Delay in seconds between messages

# Wait 5 seconds to give time to focus on WhatsApp window
print("You have 5 seconds to focus on the WhatsApp chat window...")
time.sleep(5)

send_whatsapp_message(message_text, number_of_times, delay_between_messages)
