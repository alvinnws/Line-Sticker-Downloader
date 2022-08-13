import requests
from bs4 import BeautifulSoup
import os

# Insert full URL of page
URL = "https://store.line.me/stickershop/product/19741101/en"

# Get page content and use BS4 to parse
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# Find images and title
results = soup.find_all("span", class_="mdCMN09Image FnPreview")
title = soup.find("p", class_="mdCMN38Item01Ttl")

# Create output folder
number = 0
while True:
    try:
        dir = "./" + str(title.string) + str(number)
        os.makedirs(dir)
        break
    except:
        number += 1

# Download image and create new png file in output folder
number = 0
for item in results:
    # File name, open file
    toOpen = dir + "/" + str(number) + ".png"
    file = open(toOpen, "wb")
    # URL for picture, download image
    picURL = item.get('style').replace("background-image:url(", "").replace(");", "") 
    response = requests.get(picURL)
    # Store download to opened file, close file, iterate file number
    file.write(response.content)
    file.close()
    number = number + 1