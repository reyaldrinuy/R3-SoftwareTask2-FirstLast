import socket

# grabs ip of the host
ip = socket.gethostbyname(socket.gethostname())

def server():
    print(f'[STARTING ROVER SERVER...]')

    # establishes that the messages will be sent through the internet, IPv4
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    print(f'[ROVER SERVER HAS STARTED]')

    # binds IP address of the host server to a port
    s.bind((ip, 1234))

    # waits until client(s) have connected (up to a maximum of five clients)
    s.listen(5)

    print(f'[SERVER IS LISTENING FOR CLIENTS]')
    print(' ')

    while True:

        # after the client connects using connect(), the server accepts the connection using accept()
        # csocket represents the connection between the server and the existing client
        # address holds the ip address of the client
        csocket, address = s.accept()
        print(f'Connectron from {address} has been established!')
        csocket.send(bytes(f"Welcome to the rover server, {address}!", "utf-8"))

        speed = 0
        inputSpeed = 0
        f = 'f'
        r = 'r'

        while True:
            # grabs keyboard input data from the client server
            data = csocket.recv(1024).decode("utf-8")
            speed_setting = [1, 2, 3, 4, 5]

            # detects if the input is a digit, used for switching through motor speed options
            if data.isdigit():
                inputSpeed = int(data)

            # if input number is one of the available motor speed options, label that as the selected speed option
            for i in speed_setting:
                if i == inputSpeed:
                    speed = inputSpeed

            # calculates the PWM of the rover depending on the selected speed option
            roverSpeed = speed * 51

            # keyboard input determines whether each wheel motor goes forward or backwards (reverse)
            if data == 'Key.up':
                m1, m2, m3, m4 = f, f, f, f
            elif data == 'Key.right':
                m1, m2, m3, m4 = f, f, r, r
            elif data == 'Key.left':
                m1, m2, m3, m4 = r, r, f, f
            elif data == 'Key.down':
                m1, m2, m3, m4 = r, r, r, r

            # displays the PWM and direction of the rover
            print(f'[{m1}{roverSpeed}][{m2}{roverSpeed}][{m3}{roverSpeed}][{m4}{roverSpeed}]')

if __name__ == "__main__":
    server()


