from scapy.all import ARP, Ether, srp
import netifaces
import socket  # Importer le module socket pour connaitre le nom de la hote (hostname)
import time  # Importer le module time pour utiliser la fonction sleep

def get_local_ip_range():
    # Obtenir l'adresse IP et le masque de sous-réseau de l'interface réseau active
    interface = netifaces.gateways()['default'][netifaces.AF_INET][1]
    ip_info = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]
    ip = ip_info['addr']
    netmask = ip_info['netmask']

    # Convertir l'adresse IP et le masque de sous-réseau en binaire
    ip_binary = [int(i) for i in ip.split('.')]
    netmask_binary = [int(i) for i in netmask.split('.')]

    # Calculer l'adresse réseau
    network_address_binary = [ip_binary[i] & netmask_binary[i] for i in range(4)]

    # Convertir l'adresse réseau en format string
    network_address = '.'.join(map(str, network_address_binary))

    # Calculer le nombre de bits pour le masque de sous-réseau
    mask_bits = sum([bin(int(x)).count('1') for x in netmask.split('.')])

    # Calculer le nombre d'adresses disponibles dans le sous-réseau
    num_addresses = 2 ** (32 - mask_bits)

    # Construire la plage d'adresses IP
    ip_range = f"{network_address}/{mask_bits}"

    return ip_range

def get_hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]  # Résolution du nom d'hôte à partir de l'adresse IP
    except socket.herror:
        hostname = "N/A"  # Si la résolution du nom d'hôte échoue, attribuer "N/A"
    return hostname

def scan_network(ip_range):
    # Créer une trame Ethernet avec l'adresse de broadcast
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Créer une trame ARP avec l'adresse IP de destination spécifiée
    arp = ARP(pdst=ip_range)
    # Concaténer la trame Ethernet avec la trame ARP
    packet = broadcast / arp

    # Envoyer le paquet et récupérer la réponse
    result = srp(packet, timeout=3, verbose=False)[0]

    # Liste pour stocker les adresses IP découvertes avec leur nom d'hôte
    connected_devices = []

    # Parcourir les réponses reçues
    for sent, received in result:
        # Ajouter l'adresse IP et le nom d'hôte de l'appareil connecté à la liste
        connected_devices.append({ 'hostname': get_hostname(received.psrc), 'ip': received.psrc, 'mac': received.hwsrc})

    return connected_devices

if __name__ == "__main__":
    while True:  # Boucle infinie
        ip_range = get_local_ip_range()  # Obtenir automatiquement la plage d'adresses IP
        devices = scan_network(ip_range)
        print("Machines connectées sur le réseau:")
        for device in devices:
            print(f"Nom: {device['hostname']}, IP: {device['ip']}, MAC: {device['mac']}")
        print("------------------------------------------------------------")  # Ajouter une ligne pour l'espacement entre chaque fois que le test se répéte
        time.sleep(10)  # Attendre 10 secondes avant de répéter le test

