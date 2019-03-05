# shape-discord-identification

A collection of scripts to identify the most dissimilar shape (i.e. the discord) in a given data-base of images. Used SAX-PAA to convert image data to time-series and then, implements an algorithm to find the most dissimilar shape in approximately O(n) complexity (instead of the O(n^2) of Euclidean distance).

## More about the scripts and tools here
This is a project that was an implementation of a publication on using SAX to find unusual shapes in a database (Keogh. et al, 2006).

## Instructions to use and run:

1. Run sax.py to get sax words in sax_words_ri_all_Lshifts.Enter data-set name as parameter.
2. Run buckets.py to generate buckets for all the sax words. (OPTIONAL)
3. Check values of m, n in find_heuristic.py. Update if required. 
4. Run find_heuristic.py to get collision matrix. Enter data-set name as command-line parameter.
5. Enter dataset location in main.py. Enter data-set name as command-line parameter.
6. Run main.py. The results from every data-set these scripts are run on will be updated in a file called results (will be created in the first run) in the root directory of the project.

After running main.py, a file called 'results' will be created in the root directory. This contains the results in the following format 'Name_of_dataset  Minimum_distance  Serial_number_of_the_most_dissimilar_image'.

This file will be updated in any iterations following the first one.

## A few Results

The Plots folder in the results branch has results and plots from a few sample datasets. 
All new plots generated henceforth will also go to the same folder.
Below are 2 results:
![A plot of time-series of all the images in the data-set; ArrowHead_TRAIN in our case](/Plots/ArrowHead_TRAIN_all.png).
We see one shape that sticks out as different. In the next image, it is the same shape identified by our algorithm.
![The Discord (Shape number 23 as recognized by our algorithm)](/Plots/ArrowHead_TRAIN_23.png).

These results can be verified for any number of data-sets. A few have been done, with images saved in the Plots folder in the results branch.

## Credits and References

1. Li Wei, Eamonn Keogh and Xiaopeng Xi (2006) SAXually Explict Images: Finding Unusual Shapes. ICDM 2006.
2. UCR Data-Archive.
Note: The data used to run the scripts can be obtained from the [UCR Data Archive](https://www.cs.ucr.edu/~eamonn/time_series_data/UCR_TS_Archive_2015.zip).
Alternatively, you can download a few data files (to test and run the scripts) from this [link](https://drive.google.com/open?id=1Y9KprdCn3563Q20xR-3kMpS2_GrP7Bl5).
