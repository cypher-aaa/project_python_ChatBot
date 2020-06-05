from Socket import sendMessage
from Settings import NICKNAME
def joinRoom(sock):
    readBuffer = ""
    Loading = True

    while Loading:
        readBuffer = readBuffer + sock.recv(2048).decode('utf-8')
        temp = readBuffer.split('\n')
        readBuffer = temp.pop()

        for line in temp:
            print(line)
            Loading = loadingComplete(line)

    sendMessage(sock, "HeyGuys HeyGuys HeyGuys")

def loadingComplete(line):
    if "End of /NAMES list" in line:
        return False
    else:
        return True
