from token import RARROW
from tracemalloc import start
from PIL import ImageGrab, Image
import json
import numpy as np
import requests

import time
from tkinter import *
import tkinter as tk
import win32gui

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = 0
        # Creating elements
        self.canvas = tk.Canvas(self, width=1024, height=256, bg = "black", cursor="cross")
        #self.label = tk.Label(self, text="Thinking..", font=("Helvetica", 48))
        self.classify_btn = tk.Button(self, text = "Send Image", command = self.send_image) 
        self.button_clear = tk.Button(self, text = "Clear", command = self.clear_all)
        # Grid structure
        self.canvas.grid(row=0, column=0, pady=2, sticky=W, )
        #self.label.grid(row=0, column=1,pady=2, padx=2)
        self.classify_btn.grid(row=1, column=1, pady=2, padx=2)
        self.button_clear.grid(row=1, column=0, pady=2)
        #self.canvas.bind("<Motion>", self.start_pos)
        self.canvas.bind("<B1-Motion>", self.draw_lines)
    def clear_all(self):
        self.canvas.delete("all")
        request = requests.post("http://192.168.20.35/clear")
    def draw_lines(self, event):
        self.x = event.x
        self.y = event.y
        r=3
        self.canvas.create_oval(self.x-r, self.y-r, self.x + r, self.y + r, fill='white', outline='white')
    def send_image(self):
        HWND = self.canvas.winfo_id() # get the handle of the canvas
        rect = win32gui.GetWindowRect(HWND) # get the coordinate of the canvas
        im = ImageGrab.grab(rect)
        im = im.resize((128,32))
        image_width = im.width
        image_height = im.height
        pixels = list(im.getdata())

        brightness = 100
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
            
            payload = json.dumps(output_json)

            request = requests.post("http://192.168.20.35/image", json = output_json, headers=header)
            #print(request.url)
    
app = App()
mainloop()


start_time = time.time()
im = Image.open('test.png')
image_width = im.width
image_height = im.height
pixels = list(im.getdata())
im.close()
print(time.time() - start_time)

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
    
    payload = json.dumps(output_json)
    #print(payload)

    request = requests.post("http://192.168.20.35/image", json = output_json, headers=header)
    #print(request.url)














    
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

        
    
    