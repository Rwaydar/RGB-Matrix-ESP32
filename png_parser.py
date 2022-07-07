from token import RARROW
from tracemalloc import start
from PIL import ImageGrab, Image
import json
import numpy as np
import requests

import time
def send_image(im):
    start_time = time.time()
    image_width = im.width
    image_height = im.height
    pixels = list(im.getdata())
    im.close()
    brightness = 100

    columns = []
    # For each row of pixels
    header = {'Content-type': 'application/json'}
    for i in range(image_width):
        column = []
        output_json = {}
        for j in range(image_height):
            pixel_json = {}
            pixel_json['x_pos'] = i
            pixel_json['y_pos'] = j
            pixel_json['values'] = pixels[(i + (j * image_width))]
            column.append(pixel_json)
        output_json["brightness"] = brightness
        output_json["height"] = image_height
        output_json["pixels"] = column
        output_json["num_pixels"] = image_height
        
        requests.post("http://192.168.20.35/image", json = output_json, headers=header)

    print(time.time() - start_time)
    
def send_pixels(im):
    start_time = time.time()
    image_width = im.width
    image_height = im.height
    pixels = list(im.getdata())
    im.close()

    brightness = 100

    # For each row of pixels
    header = {'Content-type': 'application/json'}
    for i in range(image_width):
        for j in range(image_height):
            pixel_json = {}
            pixel_json['x_pos'] = i
            pixel_json['y_pos'] = j
            pixel_json['values'] = pixels[(i + (j * image_width))]
        
            request = requests.post("http://192.168.20.35/pixel", json = pixel_json, headers=header)

no_of_images = 2
while True == True:
    for i in range(no_of_images):
        image = Image.open(f"{i}.png")
        send_image(image)
        time.sleep(4)
    














    
# json_start = '{"image" : ['

# output_json = {}
# for index, each in enumerate(rows):
#     print(each)
#     input()
#     output_json[index] = each
    
# out_put = json.dumps(output_json)

# print(out_put)
# input()

# input = json.loads(out_put)

#print(input)


# start_time = time.time()
# rows = []
# for row in input:
#     #print(f"Column {column}")
#     pixels_in_row = []
#     for column in input[row]:
#        pixels_in_row.append(tuple(column))
#     rows.append(pixels_in_row)
# print(time.time() - start_time)

# print(rows)

# array = np.array(rows, dtype=np.uint8)
# print(array)

# new_image = Image.fromarray(array)
# new_image.save('new.png')

        
    
    