# Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image
# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    img = Image.open(filename)
    return img

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(imageObj):
    imageObj.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(imageObj, filename):
    imageObj.save(filename, "JPEG")
    show_img(imageObj)


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(imageObj):
    pixelData = imageObj.getdata()
    newImage = []
    darkBlue = (0,51,76)
    red = (217,26,33)
    lightBlue = (112,150,158)
    yellow = (252,227,166)
    for p in pixelData:
        intensity = p[0] + p[1] + p[2]
        if intensity < 182:
            newImage.append(darkBlue)
        elif intensity <= 364:
            newImage.append(red)
        elif intensity <=546:
            newImage.append(lightBlue)
        elif intensity > 546:
            newImage.append(yellow)
    finalImage = Image.new("RGB",ima geObj.size)
    finalImage.putdata(newImage)
    return finalImage
