import speech_recognition as sr

import socket
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
s.bind((host, port))
s.listen(1)
clientsocket = None
addr = None

def get_connection():
	global clientsocket
	global addr
	s.settimeout(10)
	clientsocket, addr = s.accept()
	print("Got a connection from %s" % str(addr))
	return
t = threading.Thread(target=get_connection, args=())
t.start()

r = sr.Recognizer()
with sr.Microphone(device_index=None) as source:
	print("Adjusting for ambient noise... (5 sec)")
	r.adjust_for_ambient_noise(source, duration=5)
	while True:
		audio = r.listen(source)
		try:
			text = r.recognize_google(audio)
			if clientsocket:
				clientsocket.send(text.encode('ascii'))
			else:
				print(text)
		except sr.UnknownValueError:
			if clientsocket:
				clientsocket.send("(?)".encode('ascii'))
			else:
				print("(?)")
		except sr.RequestError as e:
			if clientsocket:
				clientsocket.send("(E!) {0}".format(e).encode('ascii'))
			else:
				print("(E!) {0}".format(e))
