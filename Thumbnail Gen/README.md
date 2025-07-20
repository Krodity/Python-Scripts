# Video Thumbnail Generator

This script automatically generates thumbnails for all video files in a specified folder.

## Features
- Supports video formats: `.mp4`, `.avi`, `.mov`, `.mkv`
- Captures a frame at a specified time (default: 3 seconds)
- Saves thumbnails as JPEG images in the output folder

## Requirements
- Python 3.6 or higher
- [OpenCV](https://pypi.org/project/opencv-python/) (`cv2`)

## Installation

1. **Clone or download this repository.**
2. **Install the required Python package:**

```sh
pip install opencv-python
```

## Usage

Run the script from the command line:

```sh
python thumbnail.py <input_folder> <output_folder> [--time TIME]
```

- `<input_folder>`: Path to the folder containing video files.
- `<output_folder>`: Path to the folder where thumbnails will be saved.
- `--time TIME`: (Optional) Time in seconds to capture the thumbnail (default: 3).

### Example

```sh
python thumbnail.py "C:/Users/yourname/Videos" "C:/Users/yourname/Thumbnails" --time 5
```

This will generate thumbnails from all supported videos in the `Videos` folder, capturing a frame at 5 seconds, and save them in the `Thumbnails` folder.

## Notes
- Make sure you have permission to read from the input folder and write to the output folder.
- Thumbnails will be named as `<video_filename>_thumbnail.jpg`.

## Troubleshooting
- If you see `Import "cv2" could not be resolved`, make sure you have installed OpenCV with `pip install opencv-python`.
- For other issues, ensure your Python version is compatible and all dependencies are installed. 