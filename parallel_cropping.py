import pandas as pd
import cv2
import openpyxl
import numpy as np
import multiprocessing # import the multiprocessing module

# define a function that takes an array of image names, center rows, center columns, labels, previous image name and image object and crops the images
def crop_images(image_names, center_rows, center_cols, labels, prev_image_name, img):
    # define the size of the cropped region (200px by 200px)
    size = 200

    # calculate the half of the size
    half_size = size / 2

    # calculate the left and upper coordinates by subtracting half of the size from the center points
    lefts = center_cols - half_size
    uppers = center_rows - half_size

    # calculate the right and lower coordinates by adding half of the size to the center points
    rights = center_cols + half_size
    lowers = center_rows + half_size

    # loop over each image name, label and corresponding coordinates
    for image_name, label, left, upper, right, lower in zip(image_names, labels, lefts, uppers, rights, lowers):
        # check if the image name is different from the previous one
        if image_name != prev_image_name:
            # read the image file using cv2.imread
            img = cv2.imread(image_name)
            # update the previous image name
            prev_image_name = image_name
            # get the height and width of the image
            height, width = img.shape[:2]

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
        cv2.imwrite(f"cropped_{image_name}_{label}_{index}.png", cropped_img)

    # return the previous image name and image object
    return prev_image_name, img

# define a function that takes a chunk of data from the excel file and calls the crop_images function on it
def process_chunk(chunk):
    # get the image names from the chunk
    image_names = chunk["Image Name"].to_numpy()

    # get the center rows from the chunk
    center_rows = chunk["Center Row"].to_numpy()

    # get the center columns from the chunk
    center_cols = chunk["Center Column"].to_numpy()

    # get the labels from the chunk
    labels = chunk["Label"].to_numpy()

    # initialize an empty string for previous image name
    prev_image_name = ""

    # initialize a None object for image object
    img = None

    # call the crop_images function on the chunk data and update the previous image name and image object
    prev_image_name, img = crop_images(image_names, center_rows, center_cols, labels, prev_image_name, img)

# read the excel file using pandas.read_excel
df = pd.read_excel("images.xlsx")

# get the number of rows in the dataframe
nrows = len(df)

# define a chunk size (how many rows to process at a time)
chunk_size = 100

# calculate how many chunks are needed to process all rows
nchunks = nrows // chunk_size + 1

# create a list of chunks by splitting the dataframe into equal parts using pandas.DataFrame.iloc
chunks = [df.iloc[i*chunk_size:(i+1)*chunk_size] for i in range(nchunks)]

# create a pool of processes using multiprocessing.Pool with as many processes as your CPU cores (or less if you want to limit them)
pool = multiprocessing.Pool(multiprocessing.cpu_count())

# map each chunk to the process_chunk function using pool.map and collect the results in a list (this will run in parallel)
results = pool.map(process_chunk, chunks)

# close and join the pool to release resources and prevent memory leaks
pool.close()
pool.join()