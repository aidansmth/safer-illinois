import base64
import os

url = "https://touchstoneclimbing.com/dogpatch-boulders/"
encoded_url = base64.urlsafe_b64encode(url.encode()).decode()

# You may need to truncate or modify the encoded URL to fit within the character limit.
# Then, you can create your filename.
filename = f"{encoded_url}.svg"

old_filename = "dogpatch-boulders.svg"

# Rename file old_filename to filename
os.rename(old_filename, filename)
