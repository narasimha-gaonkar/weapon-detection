import os
import shutil
import random

# Set the path to your dataset folder tes

dataset_folder = '/Users/gaonkar/Documents/Eitacies/Weapon Detection/Original Dataset'

# Set the path to the destination folder for the train and validation sets
train_folder = '/Users/gaonkar/Documents/Eitacies/Weapon Detection/Data/train'
val_folder = '/Users/gaonkar/Documents/Eitacies/Weapon Detection/Data/valid'



# Create the train and validation folders if they don't exist
os.makedirs(train_folder, exist_ok=True)
os.makedirs(os.path.join(train_folder, 'images'), exist_ok=True)
os.makedirs(os.path.join(train_folder, 'labels'), exist_ok=True)
os.makedirs(val_folder, exist_ok=True)
os.makedirs(os.path.join(val_folder, 'images'), exist_ok=True)
os.makedirs(os.path.join(val_folder, 'labels'), exist_ok=True)

# Set the desired split ratio (train:validation)
split_ratio = 0.7

# Get the list of image files in the dataset folder
image_files = [f for f in os.listdir(os.path.join(dataset_folder, 'images')) if f.endswith('.jpg')]

# Shuffle the image files randomly
random.shuffle(image_files)

# Calculate the number of images for the train and validation sets
num_train = int(len(image_files) * split_ratio)
num_val = len(image_files) - num_train

# Copy images and labels to the train set folder
for i in range(num_train):
    image_name = image_files[i]
    label_name = image_name[:-4] + '.txt'  # Assuming labels have the same name as images but with a different extension
    shutil.copy2(os.path.join(dataset_folder, 'images', image_name), os.path.join(train_folder, 'images', image_name))
    shutil.copy2(os.path.join(dataset_folder, 'labels', label_name), os.path.join(train_folder, 'labels', label_name))

# Copy images and labels to the validation set folder
for i in range(num_train, num_train + num_val):
    image_name = image_files[i]
    label_name = image_name[:-4] + '.txt'  # Assuming labels have the same name as images but with a different extension
    shutil.copy2(os.path.join(dataset_folder, 'images', image_name), os.path.join(val_folder, 'images', image_name))
    shutil.copy2(os.path.join(dataset_folder, 'labels', label_name), os.path.join(val_folder, 'labels', label_name))


