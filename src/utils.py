import PIL
from PIL import Image, ImageTk

def load_and_resize(imgpath):
    size = 128
    img = Image.open(imgpath)
    img = img.resize((size, size), Image.ANTIALIAS)
#   img = ImageTk.PhotoImage(img)
    return img

imgpath = '../resources/images/castle/castle_3_pieces.PNG'
img = load_and_resize(imgpath)
img.show()
