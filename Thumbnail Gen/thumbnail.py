import cv2
import os




input_folder = ""
output_folder = ""



def generate_thumbnail(video_path, output_folder, time_sec=3):
    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    cap.set(cv2.CAP_PROP_POS_MSEC, time_sec * 1000)

    success, frame = cap.read()
    if success:
        video_name = os.path.splitext(os.path.basename(video_path))[0]
        thumbnail_path = os.path.join(output_folder, f"{video_name}_thumbnail.jpg")
        cv2.imwrite(thumbnail_path, frame)
        print(f"Thumbnail saved: {thumbnail_path}")
    else:
        print(f"Failed to generate thumbnail for {video_path}")

    cap.release()

def generate_thumbnails_from_directory(input_folder, output_folder, time_sec=3):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.endswith(('.mp4', '.avi', '.mov', '.mkv')):
            video_path = os.path.join(input_folder, filename)
            generate_thumbnail(video_path, output_folder, time_sec)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Automatically generate thumbnails for videos.")
    parser.add_argument("input_folder", help="Folder containing video files.")
    parser.add_argument("output_folder", help="Folder to save thumbnails.")
    parser.add_argument("--time", type=int, default=3, help="Time (in seconds) to capture the thumbnail.")

    args = parser.parse_args()
    generate_thumbnails_from_directory(args.input_folder, args.output_folder, args.time)
