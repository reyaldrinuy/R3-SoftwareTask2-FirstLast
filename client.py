import socket

from pynput.keyboard import Listener

print('[CONNECTING] You are connecting...')

# establishes that the messages will be sent through the internet, IPv4
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# once it finds a host server, it will send a connection request to it
s.connect((socket.gethostname(), 1234))
print('[CONNECTED] You have connected to the rover server!')


def on_press(key):

    print(f'User has pressed: {key}')
    key = str(key).replace("'", "")

    # sends the input in string format to the rover server
    key = key.encode(("utf-8"))
    s.sendall(key)

# listens to keyboard inputs of the user
with Listener(on_press=on_press) as listener:
    listener.join()
