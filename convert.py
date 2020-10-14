# -*- coding: utf-8 -*-
import pandas as pd
import base64
import numpy as np
import cv2
import os


'''
(0 = Tức giận, 1 = Ghê tởm, 2 = Sợ hãi, 3 = Hạnh phúc,
 4 = Buồn, 5 = Bất ngờ, 6 = Trung lập).
'''
BINH_THUONG = 6
KHONG_DONG_TINH = (0, 1,)
HOANG_MANG = 2
BUON = 4
HUNG_THU = 5
HANH_PHUC = 3

def Set_Kind_Of_Image(emotion):
    if emotion == BINH_THUONG:
        return "DATA/binhthuong/binhthuong"
    elif emotion == HOANG_MANG:
        return "DATA/hoangmang/hoangmang"
    elif emotion == BUON:
        return "DATA/buon/buon"
    elif emotion == HUNG_THU:
        return "DATA/hungthu/hungthu"
    elif emotion == HANH_PHUC:
        return "DATA/hanhphuc/hanhphuc"
    elif emotion in KHONG_DONG_TINH:
        return "DATA/khongdongtinh/khongdongtinh"


def Save_Image():
    with open("fer2013.csv") as f:
        content = f.readlines()
        
    lines = np.array(content)

    num_of_instances = lines.size

    for i in range(1, num_of_instances):
        img = lines[i].split(",")
        img[1] = img[1].replace('"', '')
        img[1] = img[1].replace('\n', '')
        pixels = img[1].split(" ")
        pixels = np.array(pixels, 'float32')
        image = pixels.reshape(48, 48)
        #path_file_name = f"output/{i} {img[0]}.jpg"
        path_file_name = Set_Kind_Of_Image(int(img[0]))
        path_file_name = f"{path_file_name}[{img[0]}]{i}.png"
        cv2.imwrite(path_file_name, image)
        print(path_file_name)




if __name__ == "__main__":
    Save_Image()