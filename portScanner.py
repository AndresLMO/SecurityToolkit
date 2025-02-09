
from scapy.all import sr1, IP, TCP
class PortScanner:
    
    def __init__(self):
        pass
        
        
    
    
    def scan(self,target,ports):
        print(f"Scanning {target} for open ports...")
        for port in ports:
            response = sr1(IP(dst=target)/TCP(dport=port, flags="S"), timeout=1, verbose=1)
            if response:
                for received in response:
                    if received.haslayer(TCP) and received[TCP].flags == 18:   # 18 significa "SYN-ACK". Basicamente, este valor se encuentra en uno de los espacios del paquete tcp.
                        print( f"Port {port} is open")                         # Nos indica, en terminos simples, si se estableció una conexión con x hosts en x puerto.
                    elif received.haslayer(TCP) and received[TCP].flags == 20:  # RST (reset) --> Error en establecimiento de conexion. El puerto esta cerrado.
                        print(f"Port {port} is closed")
            else:
                print(f"Port {port} is filtered or no response")

# # Dirección IP de tu host
# target_ip = "192.168.100.7"  # Cambia esto a la IP de tu host

# # Lista de puertos comunes a escanear
# ports = [22, 80, 443, 3389, 8080]

# # Escanear puertos
# scan(target_ip,ports)


# #Fuente: https://denizhalil.com/2025/01/14/port-scanning-with-scapy/
        
        
        
        