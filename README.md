# shape-discord-identification

A collection of scripts to identify the most dissimilar shape (i.e. the discord) in a given data-base of images. Used SAX-PAA to convert image data to time-series and then, implements an algorithm to find the most dissimilar shape in approximately O(n) complexity (instead of the O(n^2) of Euclidean distance).

## Requirements

1. A running Python installation. Python 3.x preferred, should work on Python 2.x as well.
2. saxpy by Paul Senin installed. Install it using pip:
	Python 3.x
	>pip3 install saxpy
	For Python 2.x
	>pip install saxpy
3. numpy, pandas, csv python libraries. If not already installed, can be done using pip3 (or pip).

## Instructions to use and run:

1. Run sax.py to get sax words in sax_words_ri_all_Lshifts.Enter data-set name as parameter.
2. Run buckets.py to generate buckets for all the sax words. (OPTIONAL)
3. Check values of m, n in find_heuristic.py. Update if required. 
4. Run find_heuristic.py to get collision matrix. Enter data-set name as command-line parameter.
5. Enter dataset location in main.py. Enter data-set name as command-line parameter.
6. Run main.py. The results from every data-set these scripts are run on will be updated in a file called results (will be created in the first run) in the root directory of the project.

After running main.py, a file called `results` will be created in the root directory. This contains the results in the following format `Name_of_dataset  Minimum_distance  Serial_number_of_the_most_dissimilar_image`.

This file will be updated in any iterations following the first one.

## Plotting and verifying results

The script `plot.py` can be used to plot **any** time-series. Use it as follows:

1. Make sure the file you are trying to plot exists in the folder /DATA/
2. Enter name of the data-set you wish to plot.
3. In case you wish to plot one specific time-series (or the time-seres for a specific image) enter the index of that time series. This menu option will be helpful when trying to verify the results from our algorithm. (i.e. index will be picked up from the results file in the root directory). 

The output will be plots of the required time-series or all the time-series in the dataset based on what options you chose.
The plots are automatically saved in the `Plots` folder.

## A few Results

The Plots folder in the results branch has results and plots from a few sample datasets. 
All new plots generated henceforth will also go to the same folder.
Below are 2 results:

| Dataset name | Time-series of all the images in the dataset | Most unusual shape identified by the algorithm |
| ------------------------- | ------------------------- | ------------------------- |
| ArrowHead_TRAIN | ![](https://github.com/atishayjain708/shape-discord-identification/blob/results/Plots/ArrowHead_TRAIN_all.png) | ![](https://github.com/atishayjain708/shape-discord-identification/blob/results/Plots/ArrowHead_TRAIN_23.png) |
| Butterfly_A | ![](https://github.com/atishayjain708/shape-discord-identification/blob/results/Plots/Butterfly_A_all.png) | ![](https://github.com/atishayjain708/shape-discord-identification/blob/results/Plots/Butterfly_A_31.png) |
 
We see one shape that sticks out as different. In the next image, it is the same shape identified by our algorithm.


These results can be verified for any number of data-sets. A few have been done, with images saved in the Plots folder in the results branch.

## Applications of these scripts
1. To clean datasets with images that have been wrongly classified.
2. To identify abnormalities in datasets - for example, in a dataset of red-blood-cell images of a patient the algorithm can be used to detect the most abnormally shaped cell, giving out a possible diagnosisi for sickle-cell anaemia.
3. Identifying deformities in human anatomy - joint structures or other skeletal abnormalities in a patient.
4. Idenitfying rare species of flowers, microorganisms etc, that have been mistakenly grouped with other common species.

These are a few of the possible applications; the scripts in this package can be used in any place that requires a machine to identify the most unique image in a given dataset, even if the dataset is prohibitively large for evaluation by humans.

## More about the scripts and tools here
This is a project that was an implementation of a publication on using SAX to find unusual shapes in a database (Keogh. et al, 2006).

## Credits and References

1. Li Wei, Eamonn Keogh and Xiaopeng Xi (2006) SAXually Explict Images: Finding Unusual Shapes. ICDM 2006.
2. UCR Data-Archive.
Note: The data used to run the scripts can be obtained from the [UCR Data Archive](https://www.cs.ucr.edu/~eamonn/time_series_data/UCR_TS_Archive_2015.zip).
Alternatively, you can download a few data files (to test and run the scripts) from this [link](https://drive.google.com/open?id=1Y9KprdCn3563Q20xR-3kMpS2_GrP7Bl5).
3. The [saxpy](https://pypi.org/project/saxpy/) library by Paul Senin.
