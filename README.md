# shape-discord-identification
A collection of scripts to identify the most dissimilar shape (i.e. the discord) in a given data-base of images. Used SAX-PAA to convert image data to time-series and then, implements an algorithm to find the most dissimilar shape in approximately O(n) complexity (instead of the O(n^2) of Euclidean distance).


Instructions to use and run:

1. Run sax.py to get sax words in sax_words_ri_all_Lshifts <Enter data-set name as parameter>
2. Run buckets.py to generate buckets for all the sax words <OPTIONAL>
3. Check values of m, n in find_heuristic.py. Update if required. 
4. Run find_heuristic.py to get collision matrix. <Enter data-set name as command-line parameter>
5. Enter dataset location in main.py <Enter data-set name as command-line parameter>
6. Run main.py

Note: The data used to run the scripts can be obtained from 
Alternatively, you can download a few data files (to test and run the scripts) from the link: https://drive.google.com/open?id=1Y9KprdCn3563Q20xR-3kMpS2_GrP7Bl5
