"""Quick script to convert a URL to a base64 encoded string and use it as a filename."""
import base64
import os

URL = "https://marcellaslasagneria.net/"
encoded_url = base64.urlsafe_b64encode(URL.encode()).decode()

# You may need to truncate or modify the encoded URL to fit within the character limit.
# Then, you can create your filename.
filename = f"{encoded_url}.png"

# Get the list of files in the current directory with .png or .svg extensions
matching_files = [filename for filename in os.listdir() if filename.endswith(('.png', '.svg'))]

old_filename = ""

# Check if there are any matching files before trying to access the first one
if matching_files:
    old_filename = matching_files[0]
    # Do something with old_filename
else:
    print("No .png or .svg files found in the current directory.")

# Rename file old_filename to filename
os.rename(old_filename, filename)

# Check if file exists where we want to move it
if os.path.isfile(f"../content/en/supporters/images/{filename}"):
    print(f"File {filename} already exists in ../content/en/supporters/images/")
    # Exit the script
    exit()

# Move file to ../content/en/supporters/images/
os.replace(filename, f"../content/en/supporters/images/{filename}")
