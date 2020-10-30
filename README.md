# DSCI560
[![DOI](https://zenodo.org/badge/298402588.svg)](https://zenodo.org/badge/latestdoi/298402588)

random_num.py works for generating 1000 random numbers between 0 to 100, and then resulting a random_num.csv file.

function_random_num.py works for generating 1000 numbers based on random_num.csv by using function y=3x+6, and then resulting a function_random_num.csv file.

visualization_nums.py works for visualizing the result of random_num.csv and function_random_num.csv, and then resulting a visualization_nums.png file.

Three Script.ipynb is a jupyter notebook which works for invoking above 3 files in one notebook and generating the distributions and linear plot of initial, intermediate and final results.

 ## How to create and use a virtual environment for DSCI560 repository in your computer
 
1. Install virtualenv package on your computer by running the command line below:
 
      ```pip install virtualenv```
 
2. Copy the url of repository and clone it by running the command line below:
  
      ```git clone https://github.com/liling10822/DSCI560.git```
  
3. Running ```cd DSCI560```  to go to the folder that you cloned
 
4. Create a blank virtual environment called dsci560H4 by running the command line below:
 
     For macOS and Linux: ```python3 -m venv dsci560H4```
   
     For Windows: ```py -m venv dsci560H4```
5. Activate the dsci560H4 enviornment by running the command line below:

     For macOS and Linux: ```source dsci560H4/bin/activate```
   
     For Windows: ```.\dsci560H4\Script\activate```
6. Install dependencies by running the command line below:

    ````pip install -r requirements.txt````
    
   Otherwise, running the command line below to manually install the packages that will be needed:
    ````
    pip install seaborn
    pip install matplotlib
    ````
    After installing, run ```pip freeze``` in dsci560H4 environment to list all the packages in the environment (which shows empty before installing the packages), it should be like below:
    ```
    certifi==2020.6.20
    cycler==0.10.0
    kiwisolver==1.3.0
    matplotlib==3.3.2
    numpy==1.19.3
    pandas==1.1.3
    Pillow==8.0.1
    pyparsing==2.4.7
    python-dateutil==2.8.1
    pytz==2020.1
    scipy==1.5.3
    seaborn==0.11.0
    six==1.15.0
    ```

7. To run scripts in the DSCI560 repository, excuting the commmand line below:

    ```
    python random_num.py
    ```
    ```
    python function_random_num.py
    ```
    ```
    python visualization_nums.py
    ```
    For example, we run random_num.py successfully in our dsci560H4 environment in macOS, the terminal will show as below (the screenshot):
    
    ![image](https://raw.githubusercontent.com/liling10822/DSCI560/master/screeshot_of_run_random_num.png)
  
 8. A binder badge to click [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/liling10822/DSCI560.git/master?filepath=Three%20Scripts.ipynb)
for showing distributions and linear plot of DSCI560 repository.


 
