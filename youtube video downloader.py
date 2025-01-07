from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    """
    Download a YouTube video in the highest resolution.

    Args:
        url (str): The URL of the YouTube video to download.
        save_path (str): The directory where the video will be saved.

    Returns:
        None
    """
    try:
        # Create a YouTube object for the given URL
        yt = YouTube(url)

        # Filter streams for progressive download with MP4 format
        streams = yt.streams.filter(progressive=True, file_extension="mp4")

        # Get the highest resolution stream available
        highest_res_stream = streams.get_highest_resolution()

        # Download the video to the specified directory
        highest_res_stream.download(output_path=save_path)

        print("Video downloaded successfully!")
    except Exception as e:
        # Print any exceptions that occur during the download process
        print(f"An error occurred: {e}")

def open_file_dialog():
    """
    Open a dialog to select a folder where the video will be saved.

    Returns:
        str: The selected folder path.
    """
    folder = filedialog.askdirectory()  # Open a folder selection dialog
    if folder:
        print(f"Selected folder: {folder}")  # Print the selected folder
    return folder

if __name__ == "__main__":
    # Initialize the Tkinter root window in hidden mode
    root = tk.Tk()
    root.withdraw()

    # Prompt the user to enter a YouTube video URL
    video_url = input("Please enter a YouTube URL: ")

    # Open the file dialog to select the save location
    save_dir = open_file_dialog()

    if save_dir:
        # If a valid save location is selected, start the download
        print("Started download...")
        download_video(video_url, save_dir)
    else:
        # Handle the case where no valid location is selected
        print("Invalid save location.")
