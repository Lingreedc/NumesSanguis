# CC0
# Stef van der Struijk

import sys
import zmq
import time


def main(ip="127.0.0.1"):
    # ZMQ connection
    url = "tcp://{}:5550".format(ip)
    ctx = zmq.Context()
    socket = ctx.socket(zmq.PUB)
    socket.connect(url)  # publisher connects to subscriber
    print("Pub connected to: {}\nSending data...".format(url))

    i = 0
    topic = 'foo'.encode('ascii')

    # keep sending messages until program interruption
    while True:
        # user_msg = input("Please type a message to send: ")
        msg = str(i).encode('utf-8')
        # publish data
        socket.send_multipart([topic, msg])  # 'test'.format(i)
        print("On topic {}, send data: {}".format(topic, msg))
        # 60 fps
        time.sleep(1/60)

        i += 1
        if i > 100:
            i = 0


if __name__ == "__main__":
    # pass ip argument
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main()
