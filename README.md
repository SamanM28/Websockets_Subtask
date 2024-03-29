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

HAEDWARE SUBTASK
This is the submission of the hardware subtask. We could somewhat complete the first 2 milestones.

circuit diagram -
![f1e83ea8-0e2e-4642-8f58-e97d2b2d4fe9](https://user-images.githubusercontent.com/75972994/218158424-a246d8e9-7e75-4157-a2f5-ec53472205c9.png)
![NodeMCU GPIOs](https://user-images.githubusercontent.com/75972994/218158497-3c672981-19a4-4ae9-a866-9de758afdd37.png)


picture of the bread board -
![WhatsApp Image 2023-02-10 at 23 08 09](https://user-images.githubusercontent.com/75972994/218159022-543030ef-da85-47a3-8184-86c5d021dccf.jpg)

Video Link - https://drive.google.com/drive/folders/1rgswAtozLoc3ZL9QPceh1eV6TpHtArn1?usp=sharing

Screenshot -
![WhatsApp Image 2023-02-10 at 23 08 09](https://user-images.githubusercontent.com/75972994/218159627-58180d85-ec05-43c0-81e2-13d941ccc606.jpg)

Codes - 
continuity_checker.ino
001.ino

FINAL EMBEDATHON TASK -
All files are either here or found in the main file with the names mentioned here.

Milestone 1 - video link - https://drive.google.com/drive/folders/1IJ1NxZtfI1UXiRBbpzAtPFC4FpAX-u5D?usp=sharing
Screenshot of video details and time - ![WhatsApp Image 2023-02-11 at 13 42 21](https://user-images.githubusercontent.com/75972994/218247925-f078a1c2-47c9-4b08-9ae5-f39ee51d99d6.jpg)

Arduino code - m1.ino
serial monitor output text (as in video) - [gyro_data.txt](https://github.com/SamanM28/Websockets_Subtask/files/10712918/gyro_data.txt)

Milestone 2 - 
Arduino code - m2.ino
Python code - final2.py
Output screenshot - ![WhatsApp Image 2023-02-11 at 13 27 22](https://user-images.githubusercontent.com/75972994/218247720-971e6b80-989a-4cd5-949f-44cdaa07c39d.jpg)

Milestone 3 - 
Video - https://drive.google.com/drive/folders/1pChk38zq8kK2uhZhIihqd05kGWu4RMXy?usp=sharing
Arduino code - m3.ino
output text data - newgyrocord.txt
Screenshot - ![Screenshot_18](https://user-images.githubusercontent.com/75972994/218248832-46c5c6e7-cde8-4b76-ab43-8f6e1fc47d8e.png)

Milestone 4 - 
Arduino code - m4.ino
Video of the pc receiving the data - https://drive.google.com/drive/folders/19zv9-aVwFf2Z1kshsmCZlue5hWYKsvim?usp=sharing
Picture of the voltage divider circuit - ![Voltage divider circuit](https://user-images.githubusercontent.com/75972994/218292618-53884490-528a-4911-81d7-586a4127429e.jpg)
Potential pc code (python) - m4ish.py

We couldn't implement it because of not figuring out the pc code. On paper, the code is supposed to be uploaded onto the nodemcu and then unplugged from the source laptop. Then voltage from 9v battery must be reduced to the working voltage of the nodemcu and then the previous code will resume again. The pc connected to the nodemcu's hotspot will receive the data. The python code should take the mpu6050 data and cause keyboard inputs and cause movement in the game that is open.
