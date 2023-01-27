import numpy as np
from PIL import Image 
import os

directory_list = os.listdir("captcha_images/")
for path in directory_list:
    img = np.array(Image.open("captcha_images/" + path ))
    M = img.shape[0]//2
    N = img.shape[1]//3
    tiles = [img[x:x+M,y:y+N] for x in range(0,img.shape[0],M) for y in range(0,img.shape[1],N)]
    tile_count = 0
    folder_name = "captcha_images/" + path.strip(".png") + "/"
    os.makedirs(folder_name)
    for tile in tiles:
        file_name = str(tile_count) + ".png"
        Image.fromarray(tile).save(folder_name + file_name)
        tile_count += 1
    tile_count = 0