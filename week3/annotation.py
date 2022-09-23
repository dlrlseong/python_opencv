import numpy
import cv2
import os
import json
from pprint import pprint

class_id = 10329706
root_dir = r'C:\Users\VIP\Desktop\cv2\PipeDataset'
ann_folders = os.listdir(root_dir)
ann_folders = [folder for folder in ann_folders if "Area_crop" in folder]
for ann_folder in ann_folders:
    folder_nos = ''.join([ch for ch in ann_folder if ch.isdigit()])
    if folder_nos =="1":
        folder_nos = ""
    ann_path = os.path.join(root_dir,ann_folder,"jpeg"+folder_nos,"ann")
    imgs_dir =os.path.join(root_dir,ann_folder,"jpeg"+folder_nos,"img")
    mask_dir =os.path.join(root_dir,ann_folder,"jpeg"+folder_nos,"mask")
    os.makedirs(mask_dir,exist_ok=True)
    ann_files = os.listdir(ann_path)
    for ann_file in ann_files:
        ann_file_path = os.path.join(ann_path,ann_file)
        with open(ann_file_path,"r") as ann_json_file:
            ann_json = json.load(ann_json_file)
        # pprint(ann_json)
        size = tuple(ann_json["size"].values())
        # print(size)
        black = numpy.zeros(size)
        img_file_name = ann_file.replace(".json","")
        # img = cv2.imread(os.path.join(imgs_dir,img_file_name))

        objects = ann_json["objects"]
        pipes = [obj for obj in objects if obj["geometryType"] == "line"]
        print(len(pipes))
        for pipe in pipes:
            points = pipe["points"]["exterior"]
            # print(points)

            for i in range(len(points) - 1) :
                # cv2.line(img, tuple(points[i]), tuple(points[i + 1]), (0,0,255),10)
                cv2.line(black, tuple(points[i]), tuple(points[i + 1]), 255,10)

        # black_small = cv2.resize(black,(600,600))
        # img_small = cv2.resize(img,(600,600))
        # cv2.imshow("blck img",black_small)
        # cv2.imshow("img",img_small)
        cv2.imwrite(os.path.join(mask_dir,img_file_name.replace(".jpg",".png")),black)
        # cv2.waitKey(0)




