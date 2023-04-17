import timeit # import the timeit module

# define a setup code that imports the modules and defines the functions
setup_code = """
import os
import scandir

def find_image_path_os_walk(image_name, root_folder):
    # split the image name by underscore and get the first element
    first_word = image_name.split("_")[0]

    # join the root folder name and the first word with a slash to get the first level folder name
    first_level_folder = os.path.join(root_folder, first_word)

    # use os.walk to iterate over all subdirectories and files under the first level folder
    for dirpath, dirnames, filenames in os.walk(first_level_folder):
        # check if the image name is in the filenames list
        if image_name in filenames:
            # join the dirpath and the image name with a slash to get the full path of the image
            full_path = os.path.join(dirpath, image_name)
            # return the full path
            return full_path

    # if the image name is not found, return None
    return None

def find_image_path_scandir(image_name, root_folder):
    # split the image name by underscore and get the first element
    first_word = image_name.split("_")[0]

    # join the root folder name and the first word with a slash to get the first level folder name
    first_level_folder = os.path.join(root_folder, first_word)

    # use scandir.walk to iterate over all subdirectories and files under the first level folder
    for dirpath, dirnames, filenames in scandir.walk(first_level_folder):
        # check if the image name is in the filenames list
        if image_name in filenames:
            # join the dirpath and the image name with a slash to get the full path of the image
            full_path = os.path.join(dirpath, image_name)
            # return the full path
            return full_path

    # if the image name is not found, return None
    return None

# define some sample arguments for testing
image_name = "DAMAGE1_A_IMG_8675.JPG"
root_folder = "/Volumes/iop/BONieuwenhuis/Processed_Data/3D_classification_trial/Red Sea Global data/Imagery_Rhonda_RSG"
"""

# define a test code that calls find_image_path_os_walk with sample arguments
test_code_os_walk = """
find_image_path_os_walk(image_name, root_folder)
"""

# define a test code that calls find_image_path_scandir with sample arguments
test_code_scandir = """
find_image_path_scandir(image_name, root_folder)
"""

# use timeit.timeit to measure how long it takes to run each test code 100 times
time_os_walk = timeit.timeit(test_code_os_walk, setup=setup_code, number=100)
time_scandir = timeit.timeit(test_code_scandir, setup=setup_code, number=100)

# print out the results
print(f"Time taken by os.walk: {time_os_walk} seconds")
print(f"Time taken by scandir: {time_scandir} seconds")