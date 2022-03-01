
##  Final Project - Chat base on Netwoek

**Created by Nir Meir**

Table of Contents
1. [About the Project](#About)
2. [Code Description](#code)
3. [GUI](#gui)
4. [How to Run](#run)
5. [Dependencies](#dependencies)

## About the Project 
This is task 7 in our course.
The project have 3 steps, in this README we related to step 1 and step 2 .

Step 1 - we needed to build a chat base on network like Messenger.

Step 2 - we need to add a feature of send files over UDP with congetion control between server and client

## Code Description 

The code are seperate to Client and Server 

##### Server folder:
in the Server folder thear is :
* Filesdir - this folder are keeping the file are avialebale to download for the client.

* Logs - this folde are saving the logs between the server and the client 
 
* safeqthreads - this folder have 3 files :
      - `Descriptors.py` - Implement stop_running attribute for our threads.
      - `Errors.py` -Implement define errors.
      - `SafeQThreads.py` - set the attribute of the threads.

 - `Logs.py` - here i create module to manage application loges and printing.

 - `Utils.py` - Implement functions are handles with all the communication between the Server and the Client.
 
* Serverapp - 


##### Client folder:
in the Client folder thear is :

* safeqthreads - this folder have 3 files :
      - `Descriptors.py` - Implement stop_running attribute for our threads.
      - `Errors.py` -Implement define errors.
      - `SafeQThreads.py` - set the attribute of the threads.

- `Logs.py` - here i create module to manage application loges and printing.

- `Utils.py` - Implement functions are handles with all the communication between the Server and the Client.

- `clientapp.py` - 

## GUI Example 

![](https://i.imgur.com/1dOYx6D.png)


## How to Run

Firstly, to run this project, download the files from the github.
Then check if the requirements are install .
After that run the `serverapp.py` and open the cmd in the Client folder of the project
Write " python `clientapp.py` " then press Enter button .
Write your Nickname and in the address bar write `127.0.0.1` then press on Login button.


## Dependencies 
This project is using Python version `3.9`.
i am using `tPy - 2.0.0` for the UI implementasion
And `PySide2 - 5.15.2` for the framework
