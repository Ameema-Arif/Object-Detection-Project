import cv2
import numpy as np

#load YOLO Algorithm
net = cv2.dnn.readNet("E:\SE\SELabs\SEProject\OpenCVPractice\yolov3.weights", "E:\darknet-master\cfg\yolov3.cfg")

#loading classes
classes = []
with open("E:\darknet-master\data\coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Loading image

img = cv2.imread("E:/SE/SELabs/SEProject/OpenCVPractice/room.jpg")
img = cv2.resize(img, None, fx=0.4, fy=0.4)

# Detecting objects
#blob extracts features from the image
#normally we use RGB and here we have BGR so thats why we have set swapRB as True
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

for b in blob:
    for n, img_blob in enumerate(b):
        cv2.imshow(str(n), img_blob)
        
#net.setInput(blob)
#outs = net.forward(output_layers)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

