import os, ctypes, time, threading

import socket

os.system("title Scrolling Display")
os.system("color 0a")
os.system("mode con cols=20 lines=1")
LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("nFont", ctypes.c_ulong),
                ("dwFontSize", COORD),
                ("FontFamily", ctypes.c_uint),
                ("FontWeight", ctypes.c_uint),
                ("FaceName", ctypes.c_wchar * LF_FACESIZE)]
    
font = CONSOLE_FONT_INFOEX()
font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
font.nFont = 12
font.dwFontSize.X = 0
font.dwFontSize.Y = 64
font.FontFamily = 54
font.FontWeight = 400
font.FaceName = "Consolas"
handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
ctypes.windll.kernel32.SetCurrentConsoleFontEx(
        handle, ctypes.c_long(False), ctypes.pointer(font))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
time.sleep(2)
s.connect((host, port))
def recv():
    global ALLTEXTS
    while True:
        data = s.recv(64)
        if data:
            ALLTEXTS.append(list(data.decode('ascii')))
t = threading.Thread(target=recv, args=())
t.start()

ALLTEXTS = [
    list("Waiting...")
]

displaying = " "*20
TEXT = ""
ch = " "
while True:
    if len(TEXT) == 0:
        if len(ALLTEXTS) == 0:
            ch = " "
        else:
            TEXT = ALLTEXTS.pop(0)
            ch = " "
    else:
        ch = TEXT.pop(0)
    displaying = displaying[1:] + ch
    print(displaying, end='\r')
    time.sleep(0.1)