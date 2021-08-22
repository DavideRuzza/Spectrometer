import serial
import serial.tools.list_ports
from threading import Thread
import sys
from time import sleep
import matplotlib.pyplot as plt


coms = serial.tools.list_ports.comports(True)
# print([(com.device,
#         com.name,
#         com.description,
#         com.hwid,
#         com.vid,
#         com.pid,
#         com.serial_number,
#         com.manufacturer,
#         com.product) for com in coms])
TEENSY_VID = 5824
TEENSY_PID = 1155


teensy = serial.Serial(port=coms[0].name, baudrate=115200)
teensy.close()
teensy.open()


def print_data(data):
    raw = []
    for i in range(0, len(data), 3):
        raw.append(int(data[i:i + 3], 16))
    plt.plot(raw)
    plt.show()


def wait_data(command, n_byte, reset=False, prog=0):
    teensy.write(command.encode())
    teensy.flush()

    if reset:
        while teensy.in_waiting < n_byte:
            pass
        teensy.reset_input_buffer()
        # print("done")
        return None
    else:
        for i in range(prog):
            teensy.read(1)
            print_a()
        read = teensy.read(n_byte).decode()
        return read


class thread_serial(Thread):
    def __init__(self, port, command, n_byte, reset=True):
        super().__init__()
        self.port = port
        self.command = command
        self.n_byte = n_byte
        self.reset = reset

    def run(self):
        self.port.open()
        self.port.write(self.command.encode())
        self.port.flush()
        while self.port.inWaiting() < self.n_byte:
            pass
        if self.reset:
            self.port.reset_input_buffer()
            return None
        else:
            read = self.port.read(self.n_byte).decode()
            print_data(read)


def print_a():
    print("a")


class thread_serial_progress(Thread):
    def __init__(self, port, command, n_byte, prog, reset=True):
        super().__init__()
        self.port = port
        self.command = command
        self.n_byte = n_byte
        self.reset = reset
        self.prog = prog

    def run(self):
        self.port.open()
        self.port.write(self.command.encode())
        self.port.flush()
        for i in range(self.prog):
            self.port.read(1)
            print_a()

        while self.port.inWaiting() < self.n_byte:
            pass
        if self.reset:
            self.port.reset_input_buffer()
            return None
        else:
            read = self.port.read(self.n_byte).decode()
            print_data(read)


# thread = Thread(target=wait_data, args=("i100", 1), kwargs={"reset": True})
wait_data("i10", 1, reset=True)
wait_data("n300", 1, reset=True)
data = wait_data("m", 3648*3, False, 300)
print(data)
teensy.close()

raw = []
for i in range(0, len(data), 3):
    raw.append(int(data[i:i + 3], 16))
print(raw)
plt.plot(raw)
plt.show()

# thread_serial_progress(teensy, "m", 3648*3, 20, reset=False).start()

print("fatto")

# print(res)
# print_data(res)


# print(res)
teensy.close()

