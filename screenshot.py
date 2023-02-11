import pyautogui

# Take a screenshot of the current screen
image = pyautogui.screenshot()

# Save the screenshot as a PNG file
image.save(r'screenshot.png')
