class PortsRange:
    def __init__(self, port, number, condition, service):
        self.port = port
        self.number = number
        self.condition = condition
        self.service = service

objects = [PortsRange("TCP", "22", "open", "SSH")]

print(objects[0].port)
print(objects[0].number)
print(objects[0].condition)   
print(objects[0].service)   