import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image
from skimage.io import imread, imsave
#==============================================================================
test_f = open("E:/ML/all_data/all_data/test_images.txt", "r")
test_data = test_f.readlines()
test_f.close()

test_f2 = open("E:/ML/all_data/all_data/test_labels.txt", "r")
test_labels = test_f2.readlines()
test_f2.close()

train_f = open("E:/ML/all_data/all_data/train_images.txt", "r")
train_data = train_f.readlines()
train_f.close()

train_f2 = open("E:/ML/all_data/all_data/train_labels.txt", "r")
train_labels = train_f2.readlines()
train_f2.close()

test_data = test_data[0].split()
test_labels = test_labels[0].split()
train_data = train_data[0].split()
train_labels = train_labels[0].split()

temp_img = cv2.imread("E:/ML/all_data/all_data/img.png")
temp_img = cv2.cvtColor(temp_img, cv2.COLOR_BGR2GRAY)
temp_img = cv2.resize(temp_img, (28, 28))


data = train_data
labels = train_labels

arr = []
temp = []
cnt = 0

for i in range(0, len(data)):

    temp.append(int(data[i]))
    
    cnt+=1
    if cnt==784:
        arr.append(temp)
        temp = []
        cnt=0

cnt_ = 3600
for i in range(0, len(arr)):
    
    arr2 = arr[i]
    len1 = len(arr2)
    B = np.reshape(arr2, (-1, 28))
    name = labels[i]
    #print(B)
    imsave("E:/ML/Bangla_Digit/"+str(cnt_)+"-0"+str(name)+".jpeg", B)
    #print(arr2)
    """f= open("E:/ML/Bangla_Digit/"+str(cnt_)+"-"+str(name)+".txt","w+")
    cnt__=0"""
    """for j in arr2:
        cnt1=cnt1+1
    f.close()"""
    cnt_ = cnt_ + 1
    #print(arr2)
    print(name)
    
print(cnt_)    
