from find_image import find_image_path 
import pandas as pd

# image_name = "DAMAGE1_A_IMG_8675.JPG"
# root_folder = "/Volumes/iop/BONieuwenhuis/Processed_Data/3D_classification_trial/Red Sea Global data/Imagery_Rhonda_RSG/"


# root of the images 
root_folder = "/Volumes/iop/BONieuwenhuis/Processed_Data/3D_classification_trial/Red Sea Global data/"

image_root_folder = root_folder + "Imagery_Rhonda_RSG/"

# read the xlsx file into a DataFrame using openpyxl engine
df = pd.read_excel("Manual_Annotations_RSG_CoralNet_MatchedtoImages.xlsx", sheet_name="AnnotationImages", nrows=5)

# add a new column called image_path by applying the find_image_path function to the image_name column 
# and passing the root_folder as a second parameter

df["image_path"] = df["Name"].apply(find_image_path, args=(image_root_folder,))



