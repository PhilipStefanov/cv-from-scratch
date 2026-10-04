import os
import numpy as np 
import random
from PIL import Image, ImageDraw

def create_directories():

    dirs = [
        "dataset/train/circles",
        "dataset/train/squares",
        "dataset/test/circles",
        "dataset/test/squares"
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)

def draw_shape(shape_type, img_size=28):

    #create black canvas
    img = Image.new("L", (img_size, img_size), color=0)
    draw = ImageDraw.Draw(img)

    radius_or_half_size = random.randint(4, 9)

    center_x = random.randint(
        radius_or_half_size + 2, img_size - radius_or_half_size - 2
    )

    center_y = random.randint(
        radius_or_half_size + 2, img_size - radius_or_half_size - 2
    )

    x0 = center_x - radius_or_half_size
    x1 = center_x + radius_or_half_size
    y0 = center_y - radius_or_half_size
    y1 = center_y + radius_or_half_size

    if shape_type == 'circle':
        draw.ellipse([x0,y0,x1,y1], fill=255)

    elif shape_type == 'square':
        draw.rectangle([x0,y0,x1,y1], fill=255)

    return img

def generate_dataset(num_train=400, num_test=100):

    create_directories()
    shapes = ["circles", "squares"]

    for shape in shapes:
        for i in range(num_train):
            img = draw_shape(shape[:-1])
            img.save(f"dataset/train/{shape}/{i}.png")

        for i in range(num_test):
            img = draw_shape(shape[:-1])
            img.save(f"dataset/test/{shape}/{i}.png")

    print(f"Dataset generated successfully!")
    print(f"Train: {num_train} circles, {num_train} squares")
    print(f"Test:  {num_test} circles, {num_test} squares")

if __name__ == "__main__":
    generate_dataset()