import pyautogui
import time
import keyboard  # For detecting the Escape key press, install with pip install keyboard

def main():
    # Get the screen width and height
    screen_width, screen_height = pyautogui.size()

    # Calculate the center of the screen
    center_x, center_y = screen_width / 2, screen_height / 2

    print("Script started. Press Escape to stop.")

    # Move the mouse to the center of the screen
    pyautogui.moveTo(center_x, center_y)

    try:
        while True:
            # Check if the Escape key is pressed
            if keyboard.is_pressed('esc'):
                print("Escape pressed, script stopping.")
                break
            
            # Perform a left click
            pyautogui.click(center_x, center_y)
            
            # Wait for 5 seconds
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("Script stopped.")

if __name__ == "__main__":
    main()
