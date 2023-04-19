import pandas as pd
import cv2
import openpyxl
import numpy as np
from find_image import find_image_path

# define a function that takes an array of image names, center rows, center columns, labels, previous image name and image object and crops the images
def crop_images(image_name, image_path,center_row, center_col, label, index):
    global img
    global prev_image_name

    # define the size of the cropped region (200px by 200px)
    size = 200
    # calculate the half of the size
    half_size = size / 2
    # calculate the left and upper coordinates by subtracting half of the size from the center points
    left = int(center_row - half_size)
    upper = int(center_col - half_size)

    # calculate the right and lower coordinates by adding half of the size to the center points
    right = int(center_row+ half_size)
    lower = int(center_col + half_size)

    if image_name != prev_image_name:
        # read the image file using cv2.imread
        img = cv2.imread(image_path)
        # update the previous image name
        prev_image_name = image_name
        

    # get the height and width of the image
    # width, height = img.shape
    height, width, _ = img.shape
    # check if any of the coordinates are out of bounds and adjust them if needed
    if left < 0:
        left = 0
    if upper < 0:
        upper = 0
    if right > width:
        right = width
    if lower > height:
        lower = height

    # crop the image using slicing notation (start_y:end_y, start_x:end_x)
    cropped_img = img[upper:lower, left:right]
    # write the cropped image with a new name using the label and index as a suffix using cv2.imwrite
    
    cropped_image_path = f"output/{image_name.split('.')[0]}_{label}_{index}.png"
    cv2.imwrite(cropped_image_path, cropped_img)

    # return the previous image name and image object as outputs
    return
# root of the images 
root_folder = "/Volumes/iop/BONieuwenhuis/Processed_Data/3D_classification_trial/Red Sea Global data/"

image_root_folder = root_folder + "Imagery_Rhonda_RSG/"

# read the xlsx file into a DataFrame using openpyxl engine
df = pd.read_excel(root_folder + "Manual Annotations_RSG_CoralNet_MatchedtoImages.xlsx", sheet_name="AnnotationImages", engine="openpyxl", nrows=10)

# add a new column called image_path by applying the find_image_path function to the image_name column 
# and passing the root_folder as a second parameter
    
df["image_path"] = df["Name"].apply(find_image_path, args=(image_root_folder,))

# convert the DataFrame columns to numpy arrays
image_names = df["Name"].to_numpy()
image_paths = df["image_path"].to_numpy()
center_rows = df["Row"].to_numpy()
center_cols = df["Column"].to_numpy()
labels = df["Label"].to_numpy()
indices = np.arange(len(image_names))

# initialize a variable to store the previous image name as None
prev_image_name = None

# initialize a variable to store the image object as None
img = None

# # apply the crop_images function to the numpy arrays using np.vectorize and pass the previous image name, image object and image path as additional arguments
vfunc = np.vectorize(crop_images) 
# add signature='(),(),(),(),(),()->(),(),()' to specify the output signature as a tuple of three arrays 
vfunc(image_names, image_paths, center_rows, center_cols, labels, indices)
print("Done Cropping images check your output folder!")
