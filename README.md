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

The feature of a graceful disconnection of a client from the server was successfully implemented and tested. The client was able to request to disconnect from the server and the server closed the connection to the client.


b) Steps I had taken to finish the task -
1. First I ran all the codes from the shared repository and checked how it functions.
2. As I am still very new to python and am only used to coding in C, I had to refer a lot of resources. 
3. Multiple python files were created to test out different functionalities.
4. I did normal time logging first and then made them into blocks with time.
5. Then I used a faker to generate random names.
6. I had to make a few attempts to get multiple clients to work.
7. I have sent a few files that were made taking care of all the pointers.

Regarding the first question of bonus points - Each client makes blocks or different files and the timing of each changes according to requirement. If the message takes 2 seconds to be sent and block is created after 5 messages then the command to create the block is given at the 8th second when the 5th message is received.

d) Description of the modules - To develop this program, the "websocket" and "asyncio" libraries were used. As the name suggests, the websocket library helped develop the websocket server and client programs, and handle tasks like connecting, sending and receiving data, etc. The asyncio library was used to handle asynchronous tasks.

e) Screenshots are in the main file.
