from pprint import pprint
import cv2
import os
import numpy as np
import json

root_dir = r'Area_crop1'

ann_dir = os.path.join(root_dir, "jpeg", "ann")
mask_dir = os.path.join(root_dir, "jpeg", "mask")
os.makedirs(mask_dir, exist_ok = True)
ann_files = os.listdir(ann_dir)
# ann_file = ann_files[0]
for ann_file in ann_files:
    mask_file_name = ann_file.replace(".json","")
    ann_file_path = os.path.join(ann_dir,ann_file)
    with open(ann_file_path) as ann_json_file:
        ann_json = json.load(ann_json_file)
    # pprint(ann_json)
    size = tuple(ann_json["size"].values())
    # print(size)
    black = np.zeros(size)

    objects = ann_json["objects"]

    for pipe in objects:
        points = pipe["points"]["exterior"]
        # print(points)
        for i in range(len(points)-1):
            cv2.line(black,tuple(points[i]), tuple(points[i+1]), 255, 4)
    cv2.imwrite(os.path.join(mask_dir,mask_file_name.replace(".jpg",".png")), black)
print(mask_file_name)
     
            
            
