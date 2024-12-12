import pyautogui

print("Hover your mouse over the desired position and wait for 5 seconds.")
pyautogui.sleep(5)
position = pyautogui.position()
print(f"The mouse position is: {position}")
