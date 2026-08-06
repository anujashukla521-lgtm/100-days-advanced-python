class CPU:
    def start(self):
        print("CPU started")

class RAM:
    def load(self):
        print("RAM loading programs")

class Storage:
    def read_data(self):
        print("Reading data")

class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()
        self.storage = Storage()

    def boot(self):
        self.cpu.start()
        self.ram.load()
        self.storage.read_data()
        print("Computer is ready")

pc = Computer()
pc.boot()