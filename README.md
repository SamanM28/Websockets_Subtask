# Websockets_Subtask
This is the repository from Team Hustlers consisting of members - Saman Mallikarjun S and Hithesha P


Report - This is the readme file for the Websockets subtask. 

a)Introduction

The problem statement requires the creation of a client and server in Python, with the server sending data to connected clients and the client collecting the data in blocks of arbitrary block size, logging the blocks received along with the timestamps, and sending a response back to the server. The server should be able to handle multiple concurrent connections and the client should have a mechanism to re-establish the connection with the server if it stops and restarts. Additionally, there are bonus points for analyzing the difference in the time taken for different block sizes, allowing for a graceful disconnection of a client from the server, and allowing the client to specify the kind of data to be received from the server.

Methodology

To accomplish the task, the following steps were followed:

Simple Client and Server: A simple client and server were created where the server sends messages to the client, which receives all of them and logs them. The client used the Python websocket module for sending and receiving messages from the server. The server used the same module to receive messages from the client and send messages to it.

Collecting Messages in Blocks: The client was modified to collect messages from the server in blocks of arbitrary block size instead of receiving all messages at once. The client used a buffer to store messages until the desired block size was reached. Once the block size was reached, the client calculated the total time taken to receive the entire block and logged the block along with its timestamps.

Multiple Concurrent Connections: The server was modified to handle multiple concurrent connections by using the Python threading module. The server created a new thread for each new client that connected to it and used the multiprocessing module to send messages to all connected clients instead of just one.

Re-Establishing Connection: The client was modified to have a mechanism to re-establish the connection with the server if it stops and restarts. This was done by adding error handling and subsequent action taken in case of an error. The client used the try and except statements to catch any errors that might occur during communication with the server and retry to connect to the server if an error occurred.

Graceful Disconnection: The feature of a graceful disconnection of a client from the server was added by removing the client from the list of connected clients when the client requested to disconnect. The server used the close method of the socket module to close the connection to the client.

Results

The results of the analysis of different block sizes showed that the total time taken to receive the data decreased as the block size increased. This was expected as the total time taken to receive the data is proportional to the number of messages that have to be transmitted and the overhead of transmitting each message.


Implementation - 
To complete the task of creating a client and server in Python, the following steps were taken:

Installed the necessary libraries such as faker, numpy, and asyncio if not already installed.
Created a server script that generates data using faker or numpy and sends it to the clients one message at a time. The server also logs messages received from clients.
Created a client script that connects to the server and collects data in blocks of a specified size (e.g., 5 messages). The client logs the blocks received in a text file or console, along with the timestamps of each message in the block.
Added the feature of handling multiple concurrent connections in the server. To achieve this, the server script was modified to send messages to all connected clients instead of just one. The server maintains a list of connected clients and iterates through it to send messages.
Implemented error handling in the client script to re-establish the connection with the server in case the server stops or there is a connection error. The client continuously tries to reconnect until a successful connection is established.
(Optional) Analyzed the difference in the time taken for different block sizes and higher numbers of clients connected to the server.
(Optional) Added the feature of allowing the client to specify the kind of data to be received from the server, such as random user information data or random arrays.
(Optional) Added the feature of allowing a graceful disconnection of a client from the server, such as removing the client from the list of connected clients in the server.

b) Steps I had taken to finish the task -
1. First I ran all the codes from the shared repository and checked how it functions.
2. As I am still very new to python and am only used to coding in C, I had to refer a lot of resources. 
3. Multiple python files were created to test out different functionalities.
4. I did normal time logging first and then made them into blocks with time.
5. Then I used a faker to generate random names.
6. I had to make a few attempts to get multiple clients to work.
7. I have sent a few files that were made taking care of all the pointers.

Regarding the first question of bonus points - Each client makes blocks or different files and the timing of each changes according to requirement. If the message takes 2 seconds to be sent and block is created after 5 messages then the command to create the block is given at the 8th second when the 5th message is received.

c) Instructions-
For checking the pointers - Run stt3.py and then ctt4.py, ctt11.py, ctt22.py, ctt33.py, ctt44.py and all the pointers work.
To run the main files, first run the server python file, and then run the client python file. In the case of having multiple clients, open concurrent terminal sessions and run the client programs.

d) Description of the modules - To develop this program, the "websocket" and "asyncio" libraries were used. As the name suggests, the websocket library helped develop the websocket server and client programs, and handle tasks like connecting, sending and receiving data, etc. The asyncio library was used to handle asynchronous tasks.

e)Screenshots - I couldn't submit the screenshots on time as it kept giving me an error while trying to upload them. I only just restarted and tried and was able to link the screenshots in the main file itself. I apologize for the disorganised manner in which in have made this repository. I am quite new when it comes to creating repositories and wasn't able to figure out things in time. 
Thank you.
