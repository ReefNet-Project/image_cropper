# Image Cropper 

the code is meant to crop images 200px by 200ox based on information provided on an xlsx file. 

the main script is ``image_cropping.py`` after making sure that all the packeges needed are installed and the paths to the folder are correct based on your system you simly run: 

```
python image_cropping.py
```

# Packages 

1. OpenCV : ``conda install -c conda-forge opencv``
2. Pandas and Numpy, they usually come preinstalled with anaconda
3. openpyxl : ``conda install -c conda-forge openpyxl``


# Change Paths 

1. change ``root_folder`` in ``image_cropping.py`` 
2. change ``image_root_folder`` by changing the string after the ``+``