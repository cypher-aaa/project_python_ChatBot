from Socket import openSocket,sendMessage
from Initialize import joinRoom
from Funcs import getUserAndMessage, getTime, getDate, getCommands
from datetime import datetime

sock = openSocket()
joinRoom(sock)

readBuffer = ""
while True:
    readBuffer = readBuffer + sock.recv(2048).decode('utf-8')
    temp = readBuffer.split('\n')
    readBuffer = temp.pop()

    for line in temp:
        user, message = getUserAndMessage(line)
        commands = {"!hello\r" : "HeyGuys, @" + user + "! Я - twitchKMBot!",
                    "!clear\r" : "/clear",
                    "!date\r" : getDate(),
                    "!time\r" : getTime(),
                    "!commands\r" : ""}
        commands["!commands\r"] = getCommands(commands)

        print(user + " typed :" + message)

        if message in commands:
            sendMessage(sock, commands[message])

        # отвечает на сообщение Twitch'a 'PING :tmi.twitch.tv', показывая, что бот не АФК
        if line.startswith('PING'):
            sendMessage(sock, "Hey, Twitch! I'm not AFK! SMOrc SMOrc SMOrc")
            sock.send(('PONG :tmi.twitch.tv' + "\r\n").encode('utf-8'))