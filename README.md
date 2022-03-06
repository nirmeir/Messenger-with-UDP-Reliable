
##  Final Project - Chat base on Netwoek

**Created by Nir Meir**

Table of Contents
1. [About the Project](#About)
2. [Code Description](#code)
3. [GUI](#gui)
4. [How to Run](#run)
5. [Requirements](#dependencies)

## About the Project 
This is task 7 in our course.
The project have 3 steps, in this README we related to step 1 and step 2 .

Step 1 - we needed to build a chat base on network like Messenger.

Step 2 - we need to add a feature of send files over reliable UDP with congetion control between server and client

## Code Description 

The code are seperate to Client and Server 

##### Server folder:
in the Server folder there is :


* Filesdir - this folder are keeping the file are avialebale to download for the client.

 - `Serverapp.py` - Module to handle all communication between the server and clients

 


##### Client folder:
in the Client folder there is :


- `backend.py` - Implements functions are handles with all the communication between the Server and the Client.

- `clientapp.py` - represent all the GUI functions

## GUI Example 

![](https://i.imgur.com/1dOYx6D.png)


## How to Run

Firstly, to run this project, download the files from the github.
Then check if the requirements are install .
After that open the cmd in the Server folder of the project
Write " python `serverapp.py` " then press Enter button .

Do the same steps for the `clientapp.py`

Write your Nickname and in the address bar write `127.0.0.1` then press on Login button.


## How to Run the tests

open the cmd in the Server folder of the project
Write " python `serverapp.py` " then press Enter button 

then run the tests one by one


## Requirements 
This project is using Python version `3.9`.

 `PySide2 - 5.15.2` fully-functional GUI applications
