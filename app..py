import time
import pyautogui
import random

# Set up coordinates for the game window and start button
game_coords = (550, 400, 800, 500)
start_button_coords = (700, 450)

# Set up the key to make the dinosaur jump
jump_key = 'space'

# Wait for the user to open the game and get ready
print('Get ready to start the game!')
time.sleep(3)

# Click the start button to begin
pyautogui.click(start_button_coords)

# Set up a loop to play the game
while True:
    # Take a screenshot of the game window
    screenshot = pyautogui.screenshot(region=game_coords)

    # Check if there are any obstacles (cacti) in the screenshot
    for x in range(120, 220, 20):
        for y in range(330, 370, 20):
            if screenshot.getpixel((x, y))[0] < 100:
                # Jump over the obstacle
                pyautogui.press(jump_key)
                break

    # Add some randomness to the jump frequency
    time.sleep(random.uniform(0.1, 0.3))
