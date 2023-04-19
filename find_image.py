import os # import the os module

# define a function that takes an image name and a root folder name and returns the full path of the image
def find_image_path(image_name, root_folder):
    # use os.walk to iterate over all subdirectories and files under the first level folder
    for dirpath, dirnames, filenames in os.walk(root_folder):
        # check if the image name is in the filenames list
        if image_name in filenames:
            # join the dirpath and the image name with a slash to get the full path of the image
            full_path = os.path.join(dirpath, image_name)
            # return the full path
            return full_path

    # if the image name is not found, return None
    return None