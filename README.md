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
If another line of text is sent during a scroll, it may not register. ~fix~ workaround coming sometime. maybe.

# what next
Possible replacement of the nano with a Pi zero 2 W or similar proper IoT board, to move all speech to text and display operations onto a single board.
