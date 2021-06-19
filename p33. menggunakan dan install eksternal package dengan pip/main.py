from PIL import Image

im = Image.open("background.jpg")

print("format file: " + im.format)
print("ukuran file: " + str(im.size))
print("model file: " + im.mode)

im.show()
