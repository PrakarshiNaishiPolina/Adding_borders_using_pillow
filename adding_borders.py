
# one way 

# from PIL import Image,ImageOps

# def add_border(image_path,output_path,border_size,border_color):
#     try:
#         #open the image
#         img=Image.open(image_path)
#         img_with_border=ImageOps.expand(img,border=border_size,fill=border_color)

#         # save the image
#         img_with_border.save(output_path)

#         #show the image
#         img_with_border.show()
#     except Exception as e:
#         print(f"An error occured: {e}")

# image_path="max verstappen (2).jpeg"
# output_path="mad max.jpg"
# border_size=20
# border_color="blue"

# add_border(image_path,output_path,border_size,border_color)

# another way

from PIL import Image,ImageOps

def add_border(image_path,output_path,border_size,border_color):
    try:
        #open the image
        img=Image.open(image_path)

        if isinstance(border_size,int):
            border=(border_size,border_size,border_size,border_size)
        elif isinstance(border_size,tuple) and len(border_size)==4:
            border=border_size
        else:
            raise ValueError("border_size must be an int or tuple of length 4")
        img_with_border=ImageOps.expand(img,border=border,fill=border_color)

        # save the image
        img_with_border.save(output_path)

        #show the image
        img_with_border.show()
    except Exception as e:
        print(f"An error occured: {e}")

image_path="max verstappen (2).jpeg"
output_path="mad max.jpg"
border_size=20
border_color="blue"

add_border(image_path,output_path,border_size,border_color)
