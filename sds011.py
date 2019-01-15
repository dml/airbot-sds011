"""
Reading format. See http://cl.ly/ekot

0 Header   '\xaa'
1 Command  '\xc0'
2 DATA1    PM2.5 Low byte
3 DATA2    PM2.5 High byte
4 DATA3    PM10 Low byte
5 DATA4    PM10 High byte
6 DATA5    ID byte 1
7 DATA6    ID byte 2
8 Checksum Low byte of sum of DATA bytes
9 Tail     '\xab'

"""

import machine
import ustruct as struct
import sys
import utime as time


class SDS011:
    def __init__(self):
        self.uart0 = machine.UART(0, 9600)
        self.uart0.init(9600, bits=8, parity=None, stop=1)

    def read(self):
        try:
            header = self.uart0.read(1)
            if header == b'\xaa':
                command = self.uart0.read(1)
                if command == b'\xc0':
                    return self.measurement(self.uart0.read(8))
                if command == b'\xc5':
                    self.response(self.uart0.read(8))
        except Exception as e:
            print('Problem attempting to read:', e)
            sys.print_exception(e)

    def response(self, payload):
        pass

    def measurement(self, payload):
        try:
            print('Payload:', payload)
            *data, checksum, tail = struct.unpack('<HHBBBs', payload)
            pm25 = data[0] / 10.0
            pm10 = data[1] / 10.0
            # device_id = str(data[2]) + str(data[3])
            isvalid = checksum == (sum(data) % 256)
            iscomplete = tail == b'\xab'
            status = 'OK' if (isvalid and iscomplete) else 'NOK'
            return (pm25, pm10, status)
        except Exception as e:
            print('Problem decoding packet:', e)
            sys.print_exception(e)
