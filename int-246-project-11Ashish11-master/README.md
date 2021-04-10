# int-246-project-11Ashish11


Topic : Fuzzy logic control for a wind/battery renewable energy production system

In this I implemented 3-4 plots related to the renewable energy system which has some formulas and with the help of fuzzy logic ,  I implemeneted them and plotted charts for the same.



I have included both the GUI code and simple non GUI jupyter notebook code in this same directory.
The jupyter notebook is with the name of Staticone.ipynb


For running this jupyter notebook one need to have jupyter notebook installed in his system
The librabries needed to run this one are numpy and skfuzzy

To install numpy 

> pip3 install numpy

To install skfuzzy

> pip3 install scikit-fuzzy

The program will run after the installation of this librabries


I have plotted 4 images in it .

2 are of simple frequency graph of number of wind mills and the speed of wind mills


## Frequency Graph of Number of Wind mills

![Screenshot from 2020-10-31 23-31-17](https://user-images.githubusercontent.com/43992346/97786637-ee4c6c00-1bd2-11eb-9b8e-caac7da5583f.png)

## Frequency Graph of WindSpeed
![Screenshot from 2020-10-31 23-48-27](https://user-images.githubusercontent.com/43992346/97786749-aed24f80-1bd3-11eb-9c93-15d6a24fe2f8.png)


## Graph of the various Rules which I created
![Screenshot from 2020-10-31 23-46-40](https://user-images.githubusercontent.com/43992346/97786702-703c9500-1bd3-11eb-8712-5c5868d323e4.png)


# Final Output Graph

![Screenshot from 2020-10-31 23-44-53](https://user-images.githubusercontent.com/43992346/97786669-33709e00-1bd3-11eb-8db0-eb74ce1f4dbd.png)






# GUI PART

First create a folder and make a virual environment in it 
so that whatever you make changes , the changes would be limited upto that folder only
and so , in this environment you will have to install every library again

## Installing virtualenv
> python3 -m pip install --user virtualenv

## Creating a virtual environment¶
> python3 -m venv venv

## Activate the environment¶
> pip3 install Flask

## Creating a virtual environment¶
> python3 -m venv env

#Activating a virtual environment¶
> source env/bin/activate

## Install Flask¶
> pip3 install Flask

## Install Fuzzy
> pip3 install fuzzywuzzy

## Install Matplotlib
> pip3 install matplotlib

## Install scikit-fuzzy
> pip install scikit-fuzzy

## Now to run the file
> python3 app.py

## To access the website go to  http://127.0.0.1:5000

These below are the snapshots of the working website

![Screenshot from 2020-11-06 19-38-32](https://user-images.githubusercontent.com/43992346/98375461-225add80-2068-11eb-8d61-74245c373ffc.png)


![Screenshot from 2020-11-06 19-39-38](https://user-images.githubusercontent.com/43992346/98375516-356dad80-2068-11eb-85ec-519f030d567e.png)

