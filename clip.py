import cv2
import os

def extract_images_from_video(video_path, output_folder, frame_interval=1):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    # Get video properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    

    # Iterate through frames and save images
    for frame_number in range(0, total_frames, frame_interval):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = cap.read()

        if not ret:
            break

        image_path = os.path.join(output_folder, f"frame_{frame_number // frame_interval}.jpg")
        cv2.imwrite(image_path, frame)

    # Release the video capture object
    cap.release()

    print(f"Images extracted successfully to {output_folder}")

# Example usage:
video_path = 'C:/Users/Dell/Downloads/indian.mp4'
output_folder = 'C:/Users/Dell/Desktop/clipped'
extract_images_from_video(video_path, output_folder, frame_interval=30)
