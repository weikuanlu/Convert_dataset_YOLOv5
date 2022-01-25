import os
import shutil
saveBasePath="./VOC2007/ImageSets/Main/"

with open(os.path.join(saveBasePath,'train.txt')) as f:
    train_number = f.readlines()

with open(os.path.join(saveBasePath,'val.txt')) as f:
    val_number = f.readlines()

with open(os.path.join(saveBasePath,'test.txt')) as f:
    test_number = f.readlines()

train_image = []
val_image = []
test_image = []

for i in train_number:
    i = i.rstrip('\n')
    i_image = i+'.jpg'
    # print(i_image)
    train_image.append(i_image)
print(train_image)

for i in val_number:
    i = i.rstrip('\n')
    i_image = i+'.jpg'
    # print(i_image)
    val_image.append(i_image)
print(val_image)

for i in test_number:
    i = i.rstrip('\n')
    i_image = i + '.jpg'
    # print(i_image)
    test_image.append(i_image)
print(test_image)

new_train = "./images/train/"
if not os.path.exists('./images/train/'):
    os.makedirs('./images/train/')
new_val = "./images/val/"
if not os.path.exists('./images/val/'):
    os.makedirs('./images/val/')
new_test = "./images/test/"
if not os.path.exists('./images/test/'):
    os.makedirs('./images/test/')

dir_path =  "./VOC2007/JPEGImages/"
for i in train_image:
    for root,dirs,files in os.walk(dir_path):
        for file in files:
            if file == i:
                shutil.copy(os.path.join(root,file),new_train)

for i in val_image:
    for root,dirs,files in os.walk(dir_path):
        for file in files:
            if file == i:
                shutil.copy(os.path.join(root,file),new_val)

for i in test_image:
    for root,dirs,files in os.walk(dir_path):
        for file in files:
            if file == i:
                shutil.copy(os.path.join(root,file),new_test)