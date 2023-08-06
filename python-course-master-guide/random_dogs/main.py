import requests
import os


url = "https://random.dog/woof"

response = requests.get(url)
if not response.status_code == 200:
    print("Something went wrong!")
    exit()

image_name = response.text
new_url = "https://random.dog/" + image_name


image = requests.get(new_url)
if not image.status_code == 200:
    print("Something went wrong!")
    exit()

image_path = "images/" + image_name
file = open(image_path, "wb")
file.write(image.content)
file.close()

os.startfile(os.path.abspath(image_path))
