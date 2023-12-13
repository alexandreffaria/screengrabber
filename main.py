import cv2
import numpy as np 
from PIL import ImageGrab
import os
import time

# Define regions for six players and five additional positions around the center on the second monitor
player_regions = [
    (300, 100, 700, 450),
    (800, 60, 1150, 350),
    (1200, 100, 1700, 450),
    (1200, 400, 1700, 850),
    (800, 550, 1120, 860),
    (250, 430, 650, 850),
]

center_positions = [
    (650, 100, 850, 300),
    (650, 400, 850, 600),
    (200, 250, 400, 450),
    (650, 250, 850, 450),
    (1100, 250, 1300, 450),
]

# Create the "liveCapture" folder if it doesn't exist
output_folder = "liveCapture"
os.makedirs(output_folder, exist_ok=True)

while True:
    for i, region in enumerate(player_regions):
        # Capture the region of the second monitor
        screenshot = ImageGrab.grab(bbox=region)
        captured_image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Save the captured image to the "liveCapture" folder with appropriate filename
        output_path = os.path.join(output_folder, f"pos{i + 1}.png")
        cv2.imwrite(output_path, captured_image)

    for i, region in enumerate(center_positions):
        # Capture the region of the second monitor
        screenshot = ImageGrab.grab(bbox=region)
        captured_image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Save the captured image to the "liveCapture" folder with appropriate filename
        if i < 3:
            output_path = os.path.join(output_folder, f"flop{i + 1}.png")
        elif i == 3:
            output_path = os.path.join(output_folder, "turn.png")
        elif i == 4:
            output_path = os.path.join(output_folder, "river.png")

        cv2.imwrite(output_path, captured_image)

    time.sleep(.1)
