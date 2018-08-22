import filters

def main():
    filename = input("What is the name of the photo you want to filter: ")
    image = filters.load_img(filename)
    filteredImage = filters.obamicon(image)
    filters.save_img(filteredImage, "obamifiedImage.jpg")



if __name__ == "__main__":
    main()
