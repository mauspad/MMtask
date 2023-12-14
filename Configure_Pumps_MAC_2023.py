import serial
import serial.tools.list_ports
import time


# Get serial ports
def find_serial_port():
    return next((port.device for port in serial.tools.list_ports.comports() if "serial" in port.device.lower()), None)

serial_port = find_serial_port()
print(serial_port)


# Assuming the first port is the one you want (this may need to be modified)
s1 = serial.Serial(port=serial_port, baudrate=19200, bytesize=8, timeout=1)
s1.write(b'\r')  # Terminator character

for i in range(3):
    print(i)
    # Phase 1
    s1.write(f"{i}dia26.59\r".encode())
    time.sleep(0.1)
    s1.write(f"{i}phn01\r".encode())
    time.sleep(0.1)
    s1.write(f"{i}funrat\r".encode())
    time.sleep(0.1)
    s1.write(f"{i}rat15mm\r".encode())
    time.sleep(0.1)
    s1.write(f"{i}vol.3\r".encode())
    time.sleep(0.1)
    s1.write(f"{i}dirinf\r".encode())
    time.sleep(0.1)
    
    # Phase 2
    s1.write(f"{i}phn02\r".encode())
    time.sleep(0.1)
    s1.write(f"{i}funrat\r".encode())
    time.sleep(0.1)
    s1.write(f"{i}rat10mm\r".encode())
    time.sleep(0.1)
    s1.write(f"{i}vol.5\r".encode())
    time.sleep(0.1)
    s1.write(f"{i}dirinf\r".encode())
    time.sleep(0.1)
    
    # Phase 3
    s1.write(f"{i}phn03\r".encode())
    time.sleep(0.1)
    s1.write(f"{i}funrat\r".encode())
    time.sleep(0.1)
    s1.write(f"{i}rat15mm\r".encode())
    time.sleep(0.1)
    s1.write(f"{i}vol.3\r".encode())
    time.sleep(0.1)
    s1.write(f"{i}dirwdr\r".encode())
    time.sleep(0.1)
    
    # Phase 4
    s1.write(f"{i}phn04\r".encode())
    time.sleep(0.1)
    s1.write(f"{i}funstp\r".encode())
    time.sleep(0.1)
    
    #Run pumps
    s1.write(f"{i}run\r".encode())
   

s1.close()
