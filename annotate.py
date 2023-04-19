import pandas as pd 
import cv2
import openpyxl
import numpy as np
from find_image import find_image_path


def annotate_image(name, row, col, label, index,length):
    global points_and_labels
    global previous_name    
    if name != previous_name:
        if previous_name is not None:
            image_path = find_image_path(previous_name, image_root_folder)
            # If yes, load the image with the current image name
            image = cv2.imread(image_path)
            # Loop over the points and labels for the current image
            for point, label in points_and_labels:
                # Get the row and column coordinates
                row, col = point

                # Draw a circle on the image at the point
                cv2.circle(image, (col, row), 10, (0, 255, 0), -1)

                # Write the label on the image at the point
                cv2.putText(image, label, (col + 30, row + 15), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5)

            # Save the image into an output folder
            cv2.imwrite("annotated_images/" + previous_name, image)
        
        previous_name = name
        points_and_labels = []


    points_and_labels.append(((row, col), label))
    # last image case
    if(index == length-1):
        image_path = find_image_path(previous_name, image_root_folder)
        # If yes, load the image with the current image name
        image = cv2.imread(image_path)
        # Loop over the points and labels for the current image
        for point, label in points_and_labels:
            # Get the row and column coordinates
            row, col = point

            # Draw a circle on the image at the point
            cv2.circle(image, (col, row), 10, (0, 255, 0), -1)

            # Write the label on the image at the point
            cv2.putText(image, label, (col + 30, row + 15), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5)

        # Save the image into an output folder
        cv2.imwrite("annotated_images/" + previous_name, image)

    previous_name = name
    return previous_name


# root of the images 
root_folder = "/Volumes/iop/BONieuwenhuis/Processed_Data/3D_classification_trial/Red Sea Global data/"

image_root_folder = root_folder + "Imagery_Rhonda_RSG/"

# read the xlsx file into a DataFrame using openpyxl engine
df = pd.read_excel(root_folder + "Manual Annotations_RSG_CoralNet_MatchedtoImages.xlsx", sheet_name="AnnotationImages", engine="openpyxl", nrows=5)

names = df["Name"].to_numpy()
rows = df["Column"].to_numpy()
cols = df["Row"].to_numpy()
labels = df["Label"].to_numpy()
indices = np.arange(len(names))
length = len(names)

points_and_labels = []
previous_name = None

vfunc = np.vectorize(annotate_image, excluded={"length"}) 
vfunc(names, rows, cols, labels , indices, length)
print("Done Annotating check your output folder!")
