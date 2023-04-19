# Image Cropper 

the code is meant to crop images 200px by 200ox based on information provided on an xlsx file. 

the main script is ``image_cropping.py`` after making sure that all the packeges needed are installed and the paths to the folder are correct based on your system you simly run: 

```
python crop.py
```

## Packages 

1. OpenCV : ``conda install -c conda-forge opencv``
2. Pandas and Numpy, they usually come preinstalled with anaconda
3. openpyxl : ``conda install -c conda-forge openpyxl``


## Change Paths 

1. change ``root_folder`` in ``crop.py`` 
2. change ``image_root_folder`` by changing the string after the ``+``


# Image Annotater 
simply run  

```
python annotate.py
```

## Packages 

1. OpenCV : ``conda install -c conda-forge opencv``
2. Pandas and Numpy, they usually come preinstalled with anaconda
3. openpyxl : ``conda install -c conda-forge openpyxl``


## Change Paths 

1. change ``root_folder`` in ``annotate.py`` 
2. change ``image_root_folder`` by changing the string after the ``+``


# To Do

1. Accelerate image cropping by leveraging parallel computing.
2. Rotate images in case of portrait images.
3. Accelerate image annotation with parallel computing.