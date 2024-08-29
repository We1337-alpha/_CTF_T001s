from PIL import Image, ImageSequence
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import codecs

def decode_qr_from_frame(frame, frame_number):
    # Convert PIL Image to OpenCV format (numpy array)
    frame_cv = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
    
    # Decode QR code using pyzbar
    decoded_objects = decode(frame_cv)
    
    # Print QR code data for each frame
    if decoded_objects:
        print(f"Frame {frame_number}:")
        for obj in decoded_objects:
            qr_data = obj.data.decode("utf-8")
            print(f"  Type: {obj.type}")
            print(f"  Data: {qr_data}")

            # Convert qr_data to ROT13
            rot13_data = codecs.decode(qr_data, 'rot_13')
            print(f"  ROT13 Data: {rot13_data}")
    else:
        print(f"Frame {frame_number}: No QR code found.")

# Open the GIF file
gif_image_path = "QRRR!.gif"  # Replace with your GIF file path
gif_image = Image.open(gif_image_path)

# Loop through each frame in the GIF
frame_number = 0
for frame in ImageSequence.Iterator(gif_image):
    decode_qr_from_frame(frame, frame_number)
    frame_number += 1

