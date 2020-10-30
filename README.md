# DSCI560
[![DOI](https://zenodo.org/badge/298402588.svg)](https://zenodo.org/badge/latestdoi/298402588)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/liling10822/DSCI560.git/master?filepath=Three%20Scripts.ipynb)

1.py works for generating 1000 random numbers between 0 to 100, and then resulting a 1.csv file.

2.py works for generating 1000 numbers based on 1.csv by using function y=3x+6, and then resulting a 2.csv file.

3.py works for visualizing the result of 1.csv and 2.csv, and then resulting a 3.png file.

Three Script.ipynb is a jupyter notebook which works for invoking above 3 files in one notebook.

 ## How to create a virtual environment for the GitHub project
 
1. Install virtualenv package on your computer by running command line below
 
      ```pip install virtualenv```
 
2. Copy the url of repository and clone it by running command line below
  
      ```git clone https://github.com/liling10822/DSCI560.git```
  
3. Running ```cd DSCI560```  to go to the folder that you cloned
 
4. Create a blank virtual environment called dsci560H4 by running command line below
 
     For macOS and Linux: ```python3 -m venv dsci560H4```
   
     For Windows: ```py -m venv dsci560H4```
5. Activate the dsci560H4 enviornment by running command line below:

     For macOS and Linux: ```source dsci560H4/bin/activate``
   
     For Windows: ```.\dsci560H4\Script\activate```
6. Install dependencies by running command line below:

    ````pip install -r requirements.txt````
    
   Otherwise, running command line below to manually install the packages that be needed:
    ````
pip install pandas
pip install matplotlib
