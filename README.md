# subtitles
Live-ish physical subtitles *displayed* using arduino

# components
- MAX7219 32x8 (x4 daisy chained 8x8)
- Arduino Nano and 5v power supply
- HC 05 Bluetooth Module

# diagram
(single matrix shown here)
<img src="assets/diagram.png" width=300>

# known issues
the parola display scrolling is a blocking operation. If another line of text is sent during a scroll, it doesn't register. ~fix~ workaround coming sometime. maybe.
