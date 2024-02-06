from configparser import ConfigParser

config = ConfigParser()

config["DEFAULT"] = {
    "ipaddress" : "192.168.69.41",
    "username" : "server1"    
}

with open(r"C:\Users\BALLS2 (rip BALLS)\Desktop\REST-PFE\REST-Remote-Execution-and-Security-Toolkit-Linux\Tests\config files test\settings.ini", "w") as f:
    config.write(f)