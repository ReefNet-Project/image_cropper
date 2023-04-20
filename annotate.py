import pandas as pd 
import cv2
import openpyxl
import numpy as np
from find_image import find_image_path


def annotate_image(name, row, col, label, index,length):
    global points_and_labels
    global previous_name    
    global vertical_images
    print(f"Annotating Image {name}")
    if name != previous_name:
        if previous_name is not None:
            image_path = find_image_path(previous_name, image_root_folder)
            # If yes, load the image with the current image name
            image = cv2.imread(image_path)
            height, width, _ = image.shape
            if (height > width):
                # save image name in case of a vertical image 
                vertical_images.append(previous_name)
                image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
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
        height, width, _ = image.shape
        if (height > width):
            vertical_images.append(previous_name)
            image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

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

        image_names_df = pd.DataFrame()
        image_names_df["Vertical Image Name"] = vertical_images
        image_names_df.to_excel("vertical_images_names.xlsx", engine="openpyxl")


    previous_name = name
    return previous_name


# root of the images 
root_folder = "/Volumes/iop/BONieuwenhuis/Processed_Data/3D_classification_trial/Red Sea Global data/"

image_root_folder = root_folder + "Photos_with_Annotation"

# read the xlsx file into a DataFrame using openpyxl engine
df = pd.read_excel(root_folder + "Manual Annotations_RSG_CoralNet_MatchedtoImages.xlsx", sheet_name="AnnotationImages", engine="openpyxl", nrows=20)

names = df["Name"].to_numpy()
cols = df["Column"].to_numpy()
rows = df["Row"].to_numpy()
labels = df["Label"].to_numpy()
indices = np.arange(len(names))
length = len(names)

points_and_labels = []
previous_name = None
vertical_images = []

vfunc = np.vectorize(annotate_image, excluded={"length"}) 
vfunc(names, rows, cols, labels , indices, length)
print(f"Done Annotating {length} image, check your annotated_images folder!")
