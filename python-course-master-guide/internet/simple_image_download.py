import requests

url = "https://www.techtalents.es/wp-content/uploads/2014/10/logo_techtalens.png"

response = requests.get(url)

my_file = open("image.png", "wb")
my_file.write(response.content)
my_file.close()
