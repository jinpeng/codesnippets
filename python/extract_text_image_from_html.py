import requests
import os
from bs4 import BeautifulSoup

# Read the HTML file as a string
with open("example.html", "r") as f:
    html_string = f.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_string, "html.parser")

# Extract all image tags from the HTML and get the src attribute for each one
image_urls = []
for img in soup.find_all("img"):
    image_urls.append(img.get("src"))

# Create the images directory if it doesn't exist
if not os.path.exists("./images"):
    os.makedirs("./images")

# Download each image into the images directory
for url in image_urls:
    response = requests.get(url)
    filename = url.split("/")[-1]
    with open("./images/" + filename, "wb") as f:
        f.write(response.content)

# Print a message indicating that the download is complete
print("Images downloaded successfully!")

