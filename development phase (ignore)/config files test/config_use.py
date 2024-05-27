from configparser import ConfigParser

config = ConfigParser()
config.read(r"C:\Users\BALLS2 (rip BALLS)\Desktop\REST-PFE\REST-Remote-Execution-and-Security-Toolkit-Linux\Tests\config files test\settings.ini")

config_data = config["DEFAULT"]

ip_address = config_data['ipaddress']  

print(ip_address)
