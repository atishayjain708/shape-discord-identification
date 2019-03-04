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

## A few Results
https://github.com/atishayjain708/shape-discord-identification/blob/master/Plots/ArrowHead_TRAIN_all.png
![A plot of time-series of all the images in the data-set; ArrowHead_TRAIN in our case]((/Plots/ArrowHead_TRAIN_all.png).
![The Discord (Shape number 23 as recognized by our algorithm)](/Plots/ArrowHead_TRAIN_23.png).

## Credits and References

1. Li Wei, Eamonn Keogh and Xiaopeng Xi (2006) SAXually Explict Images: Finding Unusual Shapes. ICDM 2006.
2. UCR Data-Archive.
Note: The data used to run the scripts can be obtained from the [UCR Data Archive](https://www.cs.ucr.edu/~eamonn/time_series_data/UCR_TS_Archive_2015.zip).
Alternatively, you can download a few data files (to test and run the scripts) from this [link](https://drive.google.com/open?id=1Y9KprdCn3563Q20xR-3kMpS2_GrP7Bl5).
