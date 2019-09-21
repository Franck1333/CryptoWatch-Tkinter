

# CryptoWatch Tkinter Version

This Software allow you to get financials informations about cryptocurrencies by using Python3 and the Tkinter UI that will let you interact to the software with a basic graphic user interface.
[![Image](https://alternative.me/crypto/fear-and-greed-index.png)](https://alternative.me/crypto/fear-and-greed-index.png)  

## Getting Started  
  
To get a copy of the project , you can go on the GitHub's webpage of the project and click on the green button to download as a .ZIP file. However , if you're using a prompt console on an Unix machine use this line :

```
git clone https://github.com/Franck1333/CryptoWatch-Tkinter.git
```
  
### Prerequisites  
  
To use the project , you will need some Hardware :
  
```  
A Raspberry Pi (Last Version is better) or any Linux computer compatible,
An Internet Connection,
A Micro S.D card (8 Gb Minimum),
A Display (like the Pimoroni 4inch HyperPixel Display --> https://bit.ly/2FVOy5j).
```  
  And you will also need some libraries and softwares :

```
- Python version 3
- An OS up to date
```

Now especially for the *Pimoroni HyperPixel 4* in our case :
```
	- The Github page : https://github.com/pimoroni/hyperpixel4
	- The command line Setup (need to be install) : https://get.pimoroni.com/hyperpixel4 | bash 
```
  
### Downloading/Installing - EASY WAY !!!  
To get and downloaded the files , use this line : 
```
git clone https://github.com/Franck1333/CryptoWatch-Tkinter.git
```
- When the project is Downloaded , check your "pi" folder , and you will see the folder "CryptoWatch-Tkinter"
When you did it , you will have to launch the file called "setup.py" to install the dependencies neccessary for the project with this command line : 

```
  sudo python3 setup.py install
```

## Run
#### First Way to run the project :
To run the project , you can run the small script file called "Start.sh" in the main folder ; it's will launch the project in the background.

#### Second Way to run the project :
To run the project ; if you want to see the console activities , you can launch the file called "Interface_CryptoView.py"  into the Command Line Prompt with "sudo python Interface_CryptoView.py" in the main folder.

## Running the tests  
  
That's how to test features:

    sudo python3 <file>.py

## The Folders and Files

In this project we've got three folders

#### Folders
```
Example 	: 	Any help or example that I used for the project
Services	:	Main features 
```
#### Files in "/CryptoWatch-Tkinter/Services/"
- Main features of the program
```
- Graph.py : This feature allow the 'Historical_CMC.py' to draw a new graph with the data that has been received.

- Historical_CMC.py : This feature obtains the "Close" price of a choosen crypto by a given period.

- Info_Coins.py : This feature can get the Main data about a choosen crypto from 2 sources that are CoinbasePro and Cryptonator.
The data that you will receive are :  Price , Volume (24H) , diference of price (24H) , lowest price (24H) , highest price (24H) , Volume exchanged over 30 Days , Liquidity data [Bids,Asks] (Now). 

- Info_Hardware.py : This feature allow to the Main program to get informations about the status of processors(Usage,Temp),RAM(Usage). 

- Info_complementaires.py : This feature allow to the main program to get the real-time price of the Bitcoin in EURO; (Source: blockchain.info);
This feature allow also to the main program to download an Image on the website alternative.me/ that display an Index about the emotional status of the Investors on the BTC Market.

- Re_tailler_une_image.py : This feature allow to resize a picture.

- nettoyage_du_cache.py : Ancient program that allow all the program which using to delete all the Python2 Cache Files.
```
 - Folders inside
 ```
 - Divers : 
 - MAP_downloads : 
 ```

## Authors

-   **Franck ROCHAT**  -  _Initial work_  -  [Franck ROCHAT](https://github.com/Franck1333)  Thank You !  :heart:

[![Image](https://i.goopics.net/51JA2.jpg)](https://goopics.net/i/51JA2)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTIyMzIwMzM2NSw3NDM1NjU0MDEsLTIyOD
MyNDIxMSwxMjU2MTU4MTIxLDE3NDkyODYwOTYsMTk2OTcwMjk2
LC0xNDQ3NDc2NTE2LDIwODYyNTI4NDgsLTQ5Mzk3NjA1NF19
-->
