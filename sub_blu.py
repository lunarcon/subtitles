import speech_recognition as sr
import bluetooth as bl

print("Searching for nearby devices...")
nearby_devices = bl.discover_devices()
target_device_address = "00:14:03:05:07:FC"
port = 1
sock = bl.BluetoothSocket(bl.RFCOMM)
sock.connect((target_device_address, port))
print("Connected to {0}".format(target_device_address))

r = sr.Recognizer()
with sr.Microphone(device_index=None) as source:
	print("Adjusting for ambient noise... (5 sec)")
	r.adjust_for_ambient_noise(source, duration=5)
	print("Listening...")
	while True:
		audio = r.listen(source)
		try:
			text = r.recognize_google(audio)
			sock.send(text.encode('ascii'))
		except sr.UnknownValueError:
			sock.send("(?)".encode('ascii'))
		except sr.RequestError as e:
			sock.send("(E!) {0}".format(e).encode('ascii'))
		except KeyboardInterrupt:
			break
