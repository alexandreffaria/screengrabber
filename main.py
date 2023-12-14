import cv2
import numpy as np 
from PIL import ImageGrab
import os
import time

# Define regions for six players and five additional positions around the center on the second monitor
player_regions = [
    (300, 100, 700, 450), # Pos 1
    (800, 60, 1150, 350), # Pos 2
    (1200, 100, 1700, 450), # Pos 3
    (1200, 400, 1700, 850), # Pos 4
    (800, 550, 1120, 860), # Pos 5
    (250, 430, 650, 850), # Pos 6
]
cardx = 105

center_positions = [
    (705, 380, 810, 520), # Flop 1
    (700 + (cardx * 1), 380, 805 + (cardx * 1), 520), # Flop 2
    (700  + (cardx * 2), 380, 805  + (cardx * 2), 520), # Flop 3
    (695  + (cardx * 3), 380, 800 + (cardx * 3), 520), # Turn
    (695 + (cardx * 4), 380, 800  + (cardx * 4), 520), # River
    (880, 350, 1030, 385), # Pot
]

# Create the "liveCapture" folder if it doesn't exist
players_folder = "liveCapture/players"
os.makedirs(players_folder, exist_ok=True)
table_folder = "liveCapture/table"
os.makedirs(table_folder, exist_ok=True)

while True:
    for i, region in enumerate(player_regions):
        # Capture the region of the second monitor
        screenshot = ImageGrab.grab(bbox=region)
        captured_image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Save the captured image to the "liveCapture" folder with appropriate filename
        output_path = os.path.join(players_folder, f"{i + 1} - Pos.png")
        cv2.imwrite(output_path, captured_image)

    for i, region in enumerate(center_positions):
        # Capture the region of the second monitor
        screenshot = ImageGrab.grab(bbox=region)
        captured_image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Save the captured image to the "liveCapture" folder with appropriate filename
        if i < 3:
            output_path = os.path.join(table_folder, f"{i + 1 } - Flop.png")
        elif i == 3:
            output_path = os.path.join(table_folder, "4 - Turn.png")
        elif i == 4:
            output_path = os.path.join(table_folder, "5 - River.png")
        elif i == 5:
            output_path = os.path.join(table_folder, "6 - Pot.png")

        cv2.imwrite(output_path, captured_image)

    time.sleep(1)
