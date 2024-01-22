# Вектора атак на сетевые узлы
class AttackVectorsRange: 
    
    Appointment = "Сервер test.test.ru"
    OS = "Windows Server"
    TCP_ports = "80, 81, 443, 5985, 6001, 7070, 47001, 49152, 49153, 49154, 49157, 49160, 49191, 49192, 49201"
    
    # name - название, TCP_ports - порт, characteristic - описание, liquidation - способ устранения
    def __init__(self, name, TCP_ports, characteristic, liquidation):
        self.name = name
        self.TCP_ports = TCP_ports
        self.characteristic = characteristic
        self.liquidation = liquidation

objects = [AttackVectorsRange("Множественные атаки на протокол Microsoft RPC", "47001, 49152, 49153, 49154, 49157, 49160, 49191, 49192, 49201.", "RPC — это система удаленного вызова процедур, разработанная для распределенной вычислительной среды", "Применение межсетевого экрана для ограничения доступных портов для публичного доступа")]

print(objects[0].name)
print(objects[0].TCP_ports)
print(objects[0].characteristic)   
print(objects[0].liquidation)   
