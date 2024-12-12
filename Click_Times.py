import pyautogui
import time

def click_multiple_positions(positions, clicks_per_position, delay=0.1):
    """
    Clicks the mouse multiple times at each position in a list.

    :param positions: List of tuples (x, y) for mouse click locations.
    :param clicks_per_position: Number of times to click at each position.
    :param delay: Delay between clicks in seconds.
    """
    for position in positions:
        print(f"Starting clicks at position: {position}")
        for i in range(clicks_per_position):
            pyautogui.click(position)
            time.sleep(delay)  # Pause between clicks
            print(f"Clicked {i + 1}/{clicks_per_position} at position {position}")
        print(f"Finished clicks at position: {position}\n")

# Example Usage
positions = [(340, 530), (417, 549), (521, 507)]  # List of coordinates
clicks_per_position = 50  # Number of clicks at each position
click_multiple_positions(positions, clicks_per_position, delay=0.1)
