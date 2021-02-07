from PIL import Image

# pic path = /home/zakaria/Documents/regex-cheatsheet-1-728.jpg
picturePath = input("Enter pictures path:\n")
rawImage = Image.open(picturePath)
print(rawImage)