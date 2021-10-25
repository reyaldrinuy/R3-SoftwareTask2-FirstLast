README FILE

Note(s):
- For the directions of the rover, I used arrow keys as keyboard inputs. 
- Video showcase link is at the bottom

Server Program:
The server python program starts with grabbing the ip adress of the host, which is to be used later to bind it to the port. Protocol transmission is established on line 12, with 'socket.AF_INET' labelling the socket as an internet socket, while 'socket.SOCK_STREAM' is basically saying that it is using TCP. Line 18 takes the IP address grabbed from earlier and binds it to a port, and then the whole server program will wait until there is a client connected to it. 

After the client sends a connection request, the server accepts using the code on line 31. It represents that connection with a separate socket object, which in this case is named 'csocket', short for clientsocket. It also grabs the IP address of the client in another object called 'address' which is not used for much in this program except for print statements. There are print statements included in the code just to ensure connection between the server and the client.

The outer while loop contains many different things. On line 42, the server grabs any data sent from the client, which in this case are the inputs from the keyboard, and decodes them. It can receive up to 1024 bytes, and then assigns that value to a variable named 'data'. Thus, 'data' in the server program represents the keyboard inputs of the user. I then created a list containing the valid speed options used to represent PWM. The code on line 46 checks if the keyboard input is a number (which we can assume that it can be one of the speed options) and sends it to a for loop that checks if that number is one of the valid speed options in the list called 'speed_setting'. If it is, then that must mean the user chose to switch/establish a speed setting, so the code labels the variable 'speed' as a constant speed option until changed by the user once more. 

There are five key variables in the print statement of the rover server— 'roverSpeed' and 'm1', 'm2',... 'm4'. First, 'roverSpeed' contains the motor speed of each wheel, each dependent on the speed setting selected by the user. To calculate the speed of the motor, the code multiplies the speed setting by 51. So if user selects speed option 3, the motor speed of each wheel would be 153. Base value is 51 as the max speed is 255, so 255 / 5 = 51. On the other hand, the direction of each wheel is depended on the arrow key inputs of the user. As the arrow keys are pressed, they are transferred to the server program as strings phrased as 'Key.up', 'Key.left', and so on. The code checks whether the input matches that string, and if it does, it changes the direction variables (m1, m2, m3, m4) based on their corresponding path. It will label each variable as either 'f' or 'r', meaning forward or reverse correspondingly. Lastly, the code will print the values of the motor speed and direction of each wheel.


Client Program:
Similar to the server program, the client program establishes the transmission protocol as TCP and IPv4 with 'socket.SOCK_STREAM' and 'socket.AF_INET'. It then sends a connection request to the server using the code on line 11 by using the same port established on the server program. The server will then accept the connection request and the client program will print out a message if connection is achieved. The Listener class on line 25 and 26 listens to any keyboard inputs of the user and transfers that to the function called 'on_press'. A simple print statement is included just for the user to be aware of their own keyboard inputs. The variable which holds the input, 'key' would then be overwritten with a version of itself without and ' ', as pynput automatically prints character values with quotation marks surrounding them. The reason for this is to make reading the input easier for the server program. It will then get overwritten again with an encoded version of itself and is finally sent to the server program using the code on line 22. 

Video Link:
https://drive.google.com/drive/folders/1d0nQSW2WFCMd-BhF3Cpipi9LoYccPQRJ?usp=sharing
