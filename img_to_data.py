"This script converts an image to a base64 encoded string."

import base64

file_directory = "cat.jpg" # change this to the file directory of the image you want to convert

with open(file_directory, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    print(encoded_string)
