from datetime import datetime

def getUserAndMessage(buffer):
	# Что показывает строка в чате: cypher_aaa: !hello
	# Что принимает на вход функция: :cypher_aaa!cypher_aaa@cypher_aaa.tmi.twitch.tv PRIVMSG #feelsn1man :!hello
	index = buffer.find('!')
	user = buffer[1:index]
	index = buffer.rfind(':') #находит нужный элемент (:), начиная с конца
	message = buffer[index+1:]
	return (user, message)

def getDate():
	date = datetime.now().date()
	date = date.strftime("%a, %b %d, %Y")
	return date

def getTime():
	time = datetime.now().time()
	time = time.strftime("%I:%M:%S %p")
	return time

def getCommands(commands):
	string = "Список доступных комманд: "
	for key in commands:
		string += key[:-1]
		if key != list(commands)[-1]:
			string += ", "
		else:
			string += "."

	return string