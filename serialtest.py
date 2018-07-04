import serial

def test_serial(baudrate):
   print baudrate
   ser = serial.Serial('COM5', baudrate)
   ser.write("\r\n"*5)
   print repr(ser.read(5))
   ser.close()

#baudrates = [300, 600, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600]
baudrates = [921600, 460800, 230400, 115200, 57600, 38400, 19200, 9600, 4800, 2400, 1200, 600, 300]
for baudrate in baudrates:
   test_serial(baudrate)