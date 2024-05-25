import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView,QVBoxLayout, QScrollArea,QSizePolicy
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QTimer,QTime
from PyQt5.QtGui import *
from qfluentwidgets import (TimePicker, NavigationItemPosition, MessageBox, setTheme, setThemeColor, Theme, FluentWindow,
                            NavigationAvatarWidget, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, CheckBox, PushButton, PrimaryPushButton)
from .Ui_Main_data_viewer_window import Ui_Form
from PyQt5.QtWidgets import QMainWindow
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
from datetime import datetime

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self, Machine_Name, Machine_Ip):
        super().__init__()
        self.setupUi(self)
        self.Machine_Name = Machine_Name
        self.Machine_Ip = Machine_Ip
        Enddate = self.Enddate()  # Appel de la fonction pour obtenir le dernier timestamp
        self.LoadsLastHour.setLayout(QVBoxLayout())  # Définir un QVBoxLayout pour LoadsLastHour
        self.plot_load_data_last_hour(Enddate)  # Appel de la fonction  au démarrage
        self.CPULastHour.setLayout(QVBoxLayout())
        self.plot_CPU_last_hour(Enddate)  # Appel de la fonction  au démarrage
        self.NetworkLastHour.setLayout(QVBoxLayout())
        self.plot_data_in_out_last_hour(Enddate) 
        self.LoadsLast24Hours.setLayout(QVBoxLayout())
        self.plot_load_data_last_24hours(Enddate)  # Appel de la fonction  au démarrage
        self.CPULast24Hours.setLayout(QVBoxLayout())
        self.plot_CPU_last_24hours(Enddate)  # Appel de la fonction  au démarrage
        self.NetworkLast24Hours.setLayout(QVBoxLayout())
        self.plot_data_in_out_last_24hours(Enddate)
        self.PlotButton.clicked.connect(self.plot_custom_graphs)
        self.LoadsCustom.setLayout(QVBoxLayout())
        self.CPUCustom.setLayout(QVBoxLayout())
        self.NetworkCustom.setLayout(QVBoxLayout())
        self.FillData()
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.FillData)
        # self.timer.start(10000)  # 10000 milliseconds -> 10 seconds
        
        
        # Redimensionner la fenêtre
        self.resize(1080, 850)


        
        
        
        
    def FillData(self):
        
        # change the filepath !!!!
        filepath = f"C:\ProgramData\REMT\{self.Machine_Name}.json"
        
        
        with open(filepath, 'r') as f:
            data = json.load(f)
            Latest_line = data[-1]
            
        timestamp = Latest_line['timestamp']
        load_1min = Latest_line['LOAD1min']
        load_5min = Latest_line['LOAD5min']
        load_15min = Latest_line['LOAD15min']
        cpu_cores = Latest_line['CPUcores']
        cpu_usage = Latest_line['CPUusage']
        ram_total = convert_to_gb_or_mb(Latest_line['RAMtotal'])
        ram_usage = Latest_line['RAMusage']
        disk_total = convert_to_gb_or_mb(Latest_line['DISKtotal'])
        disk_usage = Latest_line['DISKusage']
        uptime_hundredths = Latest_line['UPTIME']
        uptime = convert_uptime(uptime_hundredths)
        total_swap = convert_to_gb_or_mb(Latest_line['TotalSWAP'])
        available_swap = convert_to_gb_or_mb(Latest_line['AvailableSWAP'])
        total_cached_memory = convert_to_gb_or_mb(Latest_line['TotalCachedMemory'])
        nic_names = ', '.join(Latest_line['NICnames'])
        table = []
        for item in Latest_line['dataOUT']:
            converted = convert_to_gb_or_mb(item)
            table.append(converted)
            data_out = ', '.join(table)
        table2 = []
        for item in Latest_line['dataIN']:
            converted = convert_to_gb_or_mb(item)
            table2.append(converted)
            data_in = ', '.join(table2)
            
        self.TimestampLabel.setText(f" As of {timestamp}")
        self.MachineName.setText(self.Machine_Name)
        self.MachineIP.setText(self.Machine_Ip)
        self.Uptime.setText(uptime)
        self.TotalDisk.setText(disk_total)
        self.CpuCores.setText(cpu_cores)
        self.TotalRam.setText(ram_total)
        self.Nics.setText(nic_names)
        self.TotalCachedMemory.setText(total_cached_memory)
        self.TotalSwap.setText(total_swap)
        self.AvailableSwap.setText(available_swap)
        self.NetworkOut.setText(data_out)
        self.NetworkIn.setText(data_in)


        self.CPUusagering.setProperty("value", cpu_usage)
        self.RAMusagering.setProperty("value", ram_usage)
        self.Diskusagering.setProperty("value", disk_usage)
        load_1min = float(load_1min) * 100
        load_5min = float(load_5min) * 100
        load_15min = float(load_15min) * 100
        self.min1LoadRing.setProperty("value", load_1min)
        self.min5LoadRing.setProperty("value", load_5min)
        self.min15LoadRing.setProperty("value", load_15min)
        
        
    def load_data(self):
        # Chemin vers le fichier JSON
        filepath = fr"C:\ProgramData\REMT\{self.Machine_Name}.json"
        
        # Variables pour stocker les données
        timestamps = []
        load1min = []
        load5min = []
        load15min = []
        cpucores = []
        cpuusage = []
        ramtotal = []
        ramusage = []
        disktotal = []
        diskusage = []
        uptime = []
        totalswap = []
        availableswap = []
        totalcachedmemory = []
        nicnames = []
        datain = []
        dataout = []
        
        # Charge les données à partir du fichier JSON
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        # Parcourt chaque entrée dans les données
        for entry in data:
            timestamps.append(entry["timestamp"])
            load1min.append(entry["LOAD1min"])
            load5min.append(entry["LOAD5min"])
            load15min.append(entry["LOAD15min"])
            cpucores.append(entry["CPUcores"])
            cpuusage.append(entry["CPUusage"])
            ramtotal.append(entry["RAMtotal"])
            ramusage.append(entry["RAMusage"])
            disktotal.append(entry["DISKtotal"])
            diskusage.append(entry["DISKusage"])
            uptime.append(entry["UPTIME"])
            totalswap.append(entry["TotalSWAP"])
            availableswap.append(entry["AvailableSWAP"])
            totalcachedmemory.append(entry["TotalCachedMemory"])
            nicnames.append(entry["NICnames"])
            datain.append(entry["dataIN"])
            dataout.append(entry["dataOUT"])
        
        # Retourne les données séparées
        return timestamps, load1min, load5min, load15min, cpuusage,ramusage, diskusage,nicnames,datain,dataout
            

    def Enddate(self):
    
        file_path = fr"C:\ProgramData\REMT\{self.Machine_Name}.json"
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Initialisation du timestamp le plus récent au premier timestamp de la liste
        Enddate = data[0]['timestamp']

        # Parcours de la liste d'objets pour trouver le timestamp le plus récent
        for item in data:
            current_timestamp = item['timestamp']
            if current_timestamp > Enddate:
                Enddate = current_timestamp
        
        print("Dernier timestamp:", Enddate)
        
        return Enddate


    def plot_load_data_last_hour(self, Enddate):
        # Appelle la fonction load_data pour récupérer les données
        timestamps, load1min, load5min, load15min, cpuusage, ramusage, diskusage, nicnames, datain, dataout = self.load_data()
    
        # Création d'un DataFrame à partir des données
        df = pd.DataFrame({
            'Timestamp': timestamps,
            'LOAD1min': load1min,
            'LOAD5min': load5min,
            'LOAD15min': load15min,
            'CPUusage': cpuusage,
            'RAMusage': ramusage,
            'DISKusage': diskusage,
            'NICnames': nicnames,
        })
    
        # Convertir la colonne 'Timestamp' en index de type datetime
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df.set_index('Timestamp', inplace=True)
    
        # Trier le DataFrame par index (timestamp)
        df.sort_index(inplace=True)
    
        # Date de début pour la période d'une heure précédant Enddate
        Startdate = pd.to_datetime(Enddate) - pd.Timedelta(hours=1)
    
        # Vérifier si la date de fin spécifiée existe dans l'index du DataFrame
        if pd.to_datetime(Enddate) not in df.index:
            print("Error: End date not found in the data.")
            return
    
        # Trancher le DataFrame en fonction des dates de début et de fin
        sliced_df = df.loc[Startdate:Enddate]
    
        # Vérifier s'il y a suffisamment de données disponibles dans la plage spécifiée
        if len(sliced_df) == 0:
            print("Error: Not enough data available within the specified range.")
            return
    
        # Création du graphe
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(sliced_df.index, sliced_df['LOAD1min'], label='LOAD1min', marker='.')
        ax.plot(sliced_df.index, sliced_df['LOAD5min'], label='LOAD5min', marker='.')
        ax.plot(sliced_df.index, sliced_df['LOAD15min'], label='LOAD15min', marker='.')
        ax.set_xlabel('Time')
        ax.set_ylabel('Load')
        ax.set_title('Load Over Time')
        ax.legend()
        ax.grid(True)
        fig.tight_layout()
    
        # Création du canevas de dessin Matplotlib
        self.canvas = FigureCanvas(fig)
    
        # Ajout du canevas au layout du widget LoadsLastHour
        self.LoadsLastHour.layout().addWidget(self.canvas)

    def plot_CPU_last_hour(self, Enddate):
        # Appelle la fonction load_data pour récupérer les données
        timestamps, load1min, load5min, load15min, cpuusage,ramusage, diskusage,nicnames,datain,dataout = self.load_data()

        # Création d'un DataFrame à partir des données
        df = pd.DataFrame({
            'Timestamp': timestamps,
            'LOAD1min': load1min,
            'LOAD5min': load5min,
            'LOAD15min': load15min,
            'CPUusage': cpuusage,
            'RAMusage': ramusage,
            'DISKusage': diskusage,
            'NICnames': nicnames
        })

        # Convertir la colonne 'Timestamp' en index de type datetime
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df.set_index('Timestamp', inplace=True)

        # Date de début pour la période d'une heure précédant Enddate
        Startdate = pd.to_datetime(Enddate) - pd.Timedelta(hours=1)
        print("REAL_cpu_last_hour = ",Startdate)

        # Vérifier si la date de début spécifiée existe dans l'index du DataFrame
        if Startdate not in df.index:
            # Convertir la date de type str en type datetime
            Startdate = pd.to_datetime(Startdate)
            # Initialiser une variable pour l'incrémentation de 1 minute
            increment = pd.Timedelta(minutes=1)
            # Tant que la Startdate n'existe pas dans l'index du DataFrame
            while Startdate not in df.index:
                # Incrémenter Startdate de 1 minute
                Startdate += increment
            # Convertir Startdate en str pour l'affichage
            Startdate = Startdate.strftime('%Y-%m-%d %H:%M:%S')
            print("NEAREST_cpu_last_hour = ",Startdate)


        # Vérifier si la date de fin spécifiée existe dans l'index du DataFrame
        if pd.to_datetime(Enddate) not in df.index:
            print("Error: End date not found in the data.")
            return

        # Trancher le DataFrame en fonction des dates de début et de fin
        sliced_df = df.loc[Startdate:Enddate]

        # Vérifier s'il y a suffisamment de données disponibles dans la plage spécifiée
        if len(sliced_df) == 0:
            print("Error: Not enough data available within the specified range.")
            return

        # Création du graphe
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(sliced_df.index, sliced_df['CPUusage'], label='CPUusage', marker='.')
        ax.plot(sliced_df.index, sliced_df['RAMusage'], label='RAMusage', marker='.')
        ax.plot(sliced_df.index, sliced_df['DISKusage'], label='DISKusage', marker='.')
        ax.set_xlabel('Time')
        ax.set_ylabel('Usage')
        ax.set_title('Usage Over Time')
        ax.legend()
        ax.grid(True)
        fig.tight_layout()

        # Création du canevas de dessin Matplotlib
        self.canvas = FigureCanvas(fig)

        # Ajout du canevas au layout du widget LoadsLastHour
        self.CPULastHour.layout().addWidget(self.canvas)
        
        
    def plot_data_in_out_last_hour(self, Enddate):
        timestamps, load1min, load5min, load15min, cpuusage, ramusage, diskusage, nicnames, datain, dataout = self.load_data()

        df = pd.DataFrame({
            'Timestamp': timestamps,
            'NICnames': nicnames,
            'datain': datain,
            'dataout': dataout
        })

        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df.set_index('Timestamp', inplace=True)

        # Date de début pour la période d'une heure précédant Enddate
        Startdate = pd.to_datetime(Enddate) - pd.Timedelta(hours=1)
        print("REAL_network_last_hour = ",Startdate)

        # Vérifier si la date de début spécifiée existe dans l'index du DataFrame
        if Startdate not in df.index:
            # Convertir la date de type str en type datetime
            Startdate = pd.to_datetime(Startdate)
            # Initialiser une variable pour l'incrémentation de 1 minute
            increment = pd.Timedelta(seconds=1)
            # Tant que la Startdate n'existe pas dans l'index du DataFrame
            while Startdate not in df.index:
                # Incrémenter Startdate de 1 minute
                Startdate += increment
            # Convertir Startdate en str pour l'affichage
            Startdate = Startdate.strftime('%Y-%m-%d %H:%M:%S')
            print("NEAREST_network_last_hour = ",Startdate)

        # Vérifier si la date de fin spécifiée existe dans l'index du DataFrame
        if pd.to_datetime(Enddate) not in df.index:
            print("Error: End date not found in the data.")
            return

        # Trancher le DataFrame en fonction des dates de début et de fin
        sliced_df = df.loc[Startdate:Enddate]

        # Vérifier s'il y a suffisamment de données disponibles dans la plage spécifiée
        if len(sliced_df) == 0:
            print("Error: Not enough data available within the specified range.")
            return

        nicnames_unique = set([nic for sublist in df['NICnames'] for nic in sublist])

        for nic in nicnames_unique:
            data_in = []
            data_out = []
            for idx, row in sliced_df.iterrows():
                if nic in row['NICnames']:
                    nic_index = row['NICnames'].index(nic)
                    data_in.append((idx, int(row['datain'][nic_index])))
                    data_out.append((idx, int(row['dataout'][nic_index])))

            data_in_df = pd.DataFrame(data_in, columns=['Timestamp', 'DataIN']).set_index('Timestamp')
            data_out_df = pd.DataFrame(data_out, columns=['Timestamp', 'DataOUT']).set_index('Timestamp')

            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(data_in_df.index, data_in_df['DataIN'], label='Data IN')
            ax.plot(data_out_df.index, data_out_df['DataOUT'], label='Data OUT')
            ax.set_title(f'Data IN/OUT for {nic}')
            ax.set_xlabel('Timestamp')
            ax.set_ylabel('Data (bytes)')
            ax.legend()
            ax.grid(True)
            fig.tight_layout()

            # Ajouter le canevas de dessin Matplotlib au layout PyQt5
            self.canvas = FigureCanvas(fig)
            self.NetworkLastHour.layout().addWidget(self.canvas)
        
    def plot_load_data_last_24hours(self,Enddate):
        # Appelle la fonction load_data pour récupérer les données
        timestamps, load1min, load5min, load15min, cpuusage,ramusage, diskusage,nicnames,datain,dataout = self.load_data()

        # Création d'un DataFrame à partir des données
        df = pd.DataFrame({
            'Timestamp': timestamps,
            'LOAD1min': load1min,
            'LOAD5min': load5min,
            'LOAD15min': load15min,
            'CPUusage': cpuusage,
            'RAMusage': ramusage,
            'DISKusage': diskusage,
            'NICnames': nicnames
        })

        # Convertir la colonne 'Timestamp' en index de type datetime
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df.set_index('Timestamp', inplace=True)

        # Date de début pour la période d'un jour précédant Enddate
        Startdate = pd.to_datetime(Enddate) - pd.Timedelta(days=1)
        print("REAL_load_last_24hours = ",Startdate)

        # Vérifier si la date de début spécifiée existe dans l'index du DataFrame
        if Startdate not in df.index:
            # Convertir la date de type str en type datetime
            Startdate = pd.to_datetime(Startdate)
            # Initialiser une variable pour l'incrémentation de 1 minute
            increment = pd.Timedelta(seconds=1)
            # Tant que la Startdate n'existe pas dans l'index du DataFrame
            while Startdate not in df.index:
                # Incrémenter Startdate de 1 minute
                Startdate += increment
            # Convertir Startdate en str pour l'affichage
            Startdate = Startdate.strftime('%Y-%m-%d %H:%M:%S')
            print("NEAREST_load_last_24hours = ",Startdate)


        # Vérifier si la date de fin spécifiée existe dans l'index du DataFrame
        if pd.to_datetime(Enddate) not in df.index:
            print("Error: End date not found in the data.")
            return

        # Trancher le DataFrame en fonction des dates de début et de fin
        sliced_df = df.loc[Startdate:Enddate]

        # Vérifier s'il y a suffisamment de données disponibles dans la plage spécifiée
        if len(sliced_df) == 0:
            print("Error: Not enough data available within the specified range.")
            return

        # Création du graphe
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(sliced_df.index, sliced_df['LOAD1min'], label='LOAD1min', marker='.')
        ax.plot(sliced_df.index, sliced_df['LOAD5min'], label='LOAD5min', marker='.')
        ax.plot(sliced_df.index, sliced_df['LOAD15min'], label='LOAD15min', marker='.')
        ax.set_xlabel('Time')
        ax.set_ylabel('Load')
        ax.set_title('Load Over Time')
        ax.legend()
        ax.grid(True)
        fig.tight_layout()

        # Création du canevas de dessin Matplotlib
        self.canvas = FigureCanvas(fig)

        # Ajout du canevas au layout du widget LoadsLastHour
        self.LoadsLast24Hours.layout().addWidget(self.canvas)
        
        
    def plot_CPU_last_24hours(self, Enddate):
        # Appelle la fonction load_data pour récupérer les données
        timestamps, load1min, load5min, load15min, cpuusage,ramusage, diskusage,nicnames,datain,dataout = self.load_data()

        # Création d'un DataFrame à partir des données
        df = pd.DataFrame({
            'Timestamp': timestamps,
            'LOAD1min': load1min,
            'LOAD5min': load5min,
            'LOAD15min': load15min,
            'CPUusage': cpuusage,
            'RAMusage': ramusage,
            'DISKusage': diskusage,
            'NICnames': nicnames
        })

        # Convertir la colonne 'Timestamp' en index de type datetime
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df.set_index('Timestamp', inplace=True)

        # Date de début pour la période d'un jour précédant Enddate
        Startdate = pd.to_datetime(Enddate) - pd.Timedelta(days=1)
        print("REAL_cpu_last_24hours = ",Startdate)

        # Vérifier si la date de début spécifiée existe dans l'index du DataFrame
        if Startdate not in df.index:
            # Convertir la date de type str en type datetime
            Startdate = pd.to_datetime(Startdate)
            # Initialiser une variable pour l'incrémentation de 1 minute
            increment = pd.Timedelta(seconds=1)
            # Tant que la Startdate n'existe pas dans l'index du DataFrame
            while Startdate not in df.index:
                # Incrémenter Startdate de 1 minute
                Startdate += increment
            # Convertir Startdate en str pour l'affichage
            Startdate = Startdate.strftime('%Y-%m-%d %H:%M:%S')
            print("NEAREST_cpu_last_24hours = ",Startdate)


        # Vérifier si la date de fin spécifiée existe dans l'index du DataFrame
        if pd.to_datetime(Enddate) not in df.index:
            print("Error: End date not found in the data.")
            return

        # Trancher le DataFrame en fonction des dates de début et de fin
        sliced_df = df.loc[Startdate:Enddate]

        # Vérifier s'il y a suffisamment de données disponibles dans la plage spécifiée
        if len(sliced_df) == 0:
            print("Error: Not enough data available within the specified range.")
            return

        # Création du graphe
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(sliced_df.index, sliced_df['CPUusage'], label='CPUusage', marker='.')
        ax.plot(sliced_df.index, sliced_df['RAMusage'], label='RAMusage', marker='.')
        ax.plot(sliced_df.index, sliced_df['DISKusage'], label='DISKusage', marker='.')
        ax.set_xlabel('Time')
        ax.set_ylabel('Usage')
        ax.set_title('Usage Over Time')
        ax.legend()
        ax.grid(True)
        fig.tight_layout()

        # Création du canevas de dessin Matplotlib
        self.canvas = FigureCanvas(fig)

        # Ajout du canevas au layout du widget LoadsLastHour
        self.CPULast24Hours.layout().addWidget(self.canvas)
        
    def plot_data_in_out_last_24hours(self,Enddate):
        timestamps, load1min, load5min, load15min, cpuusage, ramusage, diskusage, nicnames, datain, dataout = self.load_data()

        df = pd.DataFrame({
            'Timestamp': timestamps,
            'NICnames': nicnames,
            'datain': datain,
            'dataout': dataout
        })

        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df.set_index('Timestamp', inplace=True)

        # Date de début pour la période d'une heure précédant Enddate
        Startdate = pd.to_datetime(Enddate) - pd.Timedelta(days=1)
        print("REAL_network_last_24hours = ",Startdate)

        # Vérifier si la date de début spécifiée existe dans l'index du DataFrame
        if Startdate not in df.index:
            # Convertir la date de type str en type datetime
            Startdate = pd.to_datetime(Startdate)
            # Initialiser une variable pour l'incrémentation de 1 minute
            increment = pd.Timedelta(seconds=1)
            # Tant que la Startdate n'existe pas dans l'index du DataFrame
            while Startdate not in df.index:
                # Incrémenter Startdate de 1 minute
                Startdate += increment
            # Convertir Startdate en str pour l'affichage
            Startdate = Startdate.strftime('%Y-%m-%d %H:%M:%S')
            print("NEAREST_network_last_24hours = ",Startdate)

        # Vérifier si la date de fin spécifiée existe dans l'index du DataFrame
        if pd.to_datetime(Enddate) not in df.index:
            print("Error: End date not found in the data.")
            return

        # Trancher le DataFrame en fonction des dates de début et de fin
        sliced_df = df.loc[Startdate:Enddate]

        # Vérifier s'il y a suffisamment de données disponibles dans la plage spécifiée
        if len(sliced_df) == 0:
            print("Error: Not enough data available within the specified range.")
            return

        nicnames_unique = set([nic for sublist in df['NICnames'] for nic in sublist])

        for nic in nicnames_unique:
            data_in = []
            data_out = []
            for idx, row in sliced_df.iterrows():
                if nic in row['NICnames']:
                    nic_index = row['NICnames'].index(nic)
                    data_in.append((idx, int(row['datain'][nic_index])))
                    data_out.append((idx, int(row['dataout'][nic_index])))

            data_in_df = pd.DataFrame(data_in, columns=['Timestamp', 'DataIN']).set_index('Timestamp')
            data_out_df = pd.DataFrame(data_out, columns=['Timestamp', 'DataOUT']).set_index('Timestamp')

            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(data_in_df.index, data_in_df['DataIN'], label='Data IN')
            ax.plot(data_out_df.index, data_out_df['DataOUT'], label='Data OUT')
            ax.set_title(f'Data IN/OUT for {nic}')
            ax.set_xlabel('Timestamp')
            ax.set_ylabel('Data (bytes)')
            ax.legend()
            ax.grid(True)
            fig.tight_layout()

            # Ajouter le canevas de dessin Matplotlib au layout PyQt5
            self.canvas = FigureCanvas(fig)
            self.NetworkLast24Hours.layout().addWidget(self.canvas)
        
        
    def plot_custom_graphs(self):
        
        # Supprimer directement le graphe existant
        try:
            self.canvas.setParent(None)
        except AttributeError:
            pass  # Si self.canvas n'existe pas encore, ignorer l'erreur
        
        StartDate = self.StartDate.text()
        EndDate = self.EndDate.text()
        start_time = self.StartTime.time.toString()
        end_time = self.EndTime.time.toString()
        Ticks = self.Ticks.text()
        
        StartDate = f"{StartDate} {start_time}"
        EndDate = f"{EndDate} {end_time}"

        # Faire quelque chose avec les valeurs récupérées, comme par exemple tracer un graphique
        # print("StartDate:", StartDate)
        # print("EndDate:", EndDate)
        # print("StartTime:", start_time)
        # print("EndTime:", end_time)
        # print("Ticks:", Ticks)
        
        print("StartDate_load_custom:", StartDate)
        print("EndDate_load_custom:", EndDate)
        
        
        # Appelle la fonction load_data pour récupérer les données
        timestamps, load1min, load5min, load15min, cpuusage,ramusage, diskusage,nicnames,datain,dataout = self.load_data()

        # Création d'un DataFrame à partir des données
        df = pd.DataFrame({
            'Timestamp': timestamps,
            'LOAD1min': load1min,
            'LOAD5min': load5min,
            'LOAD15min': load15min,
            'CPUusage': cpuusage,
            'RAMusage': ramusage,
            'DISKusage': diskusage,
            'NICnames': nicnames,
            'datain': datain,
            'dataout': dataout
        })

        # Convertir la colonne 'Timestamp' en index de type datetime
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df.set_index('Timestamp', inplace=True)


        # Vérifier si la date de début spécifiée existe dans l'index du DataFrame
        if StartDate not in df.index:
            # Convertir la date de type str en type datetime
            StartDate = pd.to_datetime(StartDate)
            # Initialiser une variable pour l'incrémentation de 1 minute
            increment = pd.Timedelta(seconds=1)
            # Tant que la Startdate n'existe pas dans l'index du DataFrame
            while StartDate not in df.index:
                # Incrémenter Startdate de 1 minute
                StartDate += increment
            # Convertir Startdate en str pour l'affichage
            StartDate = StartDate.strftime('%Y-%m-%d %H:%M:%S')
            print("NEAREST_start_load_custom = ",StartDate)
            
            
        # Vérifier si la date de début spécifiée existe dans l'index du DataFrame
        if EndDate not in df.index:
            # Convertir la date de type str en type datetime
            EndDate = pd.to_datetime(EndDate)
            # Initialiser une variable pour l'incrémentation de 1 minute
            increment = pd.Timedelta(seconds=1)
            # Tant que la Startdate n'existe pas dans l'index du DataFrame
            while EndDate not in df.index:
                # Incrémenter Startdate de 1 minute
                EndDate -= increment
            # Convertir Startdate en str pour l'affichage
            EndDate = EndDate.strftime('%Y-%m-%d %H:%M:%S')
            print("NEAREST_end_load_custom = ",EndDate)


        # Vérifier si la date de fin spécifiée existe dans l'index du DataFrame
        if pd.to_datetime(EndDate ) not in df.index:
            print("Error: End date not found in the data.")
            return

        # Trancher le DataFrame en fonction des dates de début et de fin
        sliced_df = df.loc[StartDate:EndDate]

        # Vérifier s'il y a suffisamment de données disponibles dans la plage spécifiée
        if len(sliced_df) == 0:
            print("Error: Not enough data available within the specified range.")
            return

        # Création du graphe
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(sliced_df.index, sliced_df['LOAD1min'], label='LOAD1min', marker='.')
        ax.plot(sliced_df.index, sliced_df['LOAD5min'], label='LOAD5min', marker='.')
        ax.plot(sliced_df.index, sliced_df['LOAD15min'], label='LOAD15min', marker='.')
        ax.set_xlabel('Time')
        ax.set_ylabel('Load')
        ax.set_title('Load Over Time')
        ax.legend()
        ax.grid(True)
        fig.tight_layout()

        # Création du canevas de dessin Matplotlib
        self.canvas = FigureCanvas(fig)

        # Ajout du canevas au layout du widget LoadsLastHour
        self.LoadsCustom.layout().addWidget(self.canvas)
        
        # Création du graphe
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(sliced_df.index, sliced_df['CPUusage'], label='CPUusage', marker='.')
        ax.plot(sliced_df.index, sliced_df['RAMusage'], label='RAMusage', marker='.')
        ax.plot(sliced_df.index, sliced_df['DISKusage'], label='DISKusage', marker='.')
        ax.set_xlabel('Time')
        ax.set_ylabel('Usage')
        ax.set_title('Usage Over Time')
        ax.legend()
        ax.grid(True)
        fig.tight_layout()

        # Création du canevas de dessin Matplotlib
        self.canvas = FigureCanvas(fig)

        # Ajout du canevas au layout du widget LoadsLastHour
        self.CPUCustom.layout().addWidget(self.canvas)
        
        nicnames_unique = set([nic for sublist in df['NICnames'] for nic in sublist])

        for nic in nicnames_unique:
            data_in = []
            data_out = []
            for idx, row in sliced_df.iterrows():
                if nic in row['NICnames']:
                    nic_index = row['NICnames'].index(nic)
                    data_in.append((idx, int(row['datain'][nic_index])))
                    data_out.append((idx, int(row['dataout'][nic_index])))

            data_in_df = pd.DataFrame(data_in, columns=['Timestamp', 'DataIN']).set_index('Timestamp')
            data_out_df = pd.DataFrame(data_out, columns=['Timestamp', 'DataOUT']).set_index('Timestamp')

            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(data_in_df.index, data_in_df['DataIN'], label='Data IN')
            ax.plot(data_out_df.index, data_out_df['DataOUT'], label='Data OUT')
            ax.set_title(f'Data IN/OUT for {nic}')
            ax.set_xlabel('Timestamp')
            ax.set_ylabel('Data (bytes)')
            ax.legend()
            ax.grid(True)
            fig.tight_layout()

            # Ajouter le canevas de dessin Matplotlib au layout PyQt5
            self.canvas = FigureCanvas(fig)
            self.NetworkCustom.layout().addWidget(self.canvas)

        


def convert_to_gb_or_mb(value):
    value = int(value)
    if value >= 1024 * 1024: 
        return f"{value / (1024 * 1024):.2f} GB"
    elif value >= 1024: 
        return f"{value / 1024:.2f} MB"
    else:
        return f"{value} KB"

def convert_uptime(uptime_hundredths):
    uptime_seconds = int(uptime_hundredths) / 100  # Convert to seconds
    if uptime_seconds < 60:
        return f"{uptime_seconds:.2f} seconds"
    elif uptime_seconds < 3600:
        uptime_minutes = uptime_seconds / 60
        return f"{uptime_minutes:.2f} minutes"
    elif uptime_seconds < 86400:
        uptime_hours = uptime_seconds / 3600
        return f"{uptime_hours:.2f} hours"
    else:
        uptime_days = uptime_seconds / 86400
        return f"{uptime_days:.2f} days"

def main(MachineName, MachineIP):
    color = QColor('#351392')
    setThemeColor(color ,Qt.GlobalColor , '') 
    app = QApplication(sys.argv)
    window = MainWindow(MachineName, MachineIP) 
    window.show()

    sys.exit(app.exec_())

# if __name__ == "__main__":
#     main('SERVER1', '192.168.69.44')
