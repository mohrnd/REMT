import pandas as pd
import matplotlib.pyplot as plt
import json

# Example JSON data with missing timestamps
json_data = '''
[
    {
        "timestamp": "2024-01-01 00:00:00",
        "LOAD1min": 6.55,
        "LOAD5min": 9.02,
        "LOAD15min": 1.76,
        "CPUcores": 4,
        "CPUusage": 46,
        "RAMtotal": 8192,
        "RAMusage": 46,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:00:30",
        "LOAD1min": 8.79,
        "LOAD5min": 9.94,
        "LOAD15min": 7.52,
        "CPUcores": 4,
        "CPUusage": 2,
        "RAMtotal": 8192,
        "RAMusage": 39,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:01:00",
        "LOAD1min": 7.42,
        "LOAD5min": 4.74,
        "LOAD15min": 7.32,
        "CPUcores": 4,
        "CPUusage": 18,
        "RAMtotal": 8192,
        "RAMusage": 4,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:01:30",
        "LOAD1min": 7.95,
        "LOAD5min": 4.2,
        "LOAD15min": 2.58,
        "CPUcores": 4,
        "CPUusage": 10,
        "RAMtotal": 8192,
        "RAMusage": 39,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:02:00",
        "LOAD1min": 8.79,
        "LOAD5min": 0.63,
        "LOAD15min": 9.82,
        "CPUcores": 4,
        "CPUusage": 46,
        "RAMtotal": 8192,
        "RAMusage": 38,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:02:30",
        "LOAD1min": 3.56,
        "LOAD5min": 5.85,
        "LOAD15min": 4.04,
        "CPUcores": 4,
        "CPUusage": 50,
        "RAMtotal": 8192,
        "RAMusage": 9,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:03:00",
        "LOAD1min": 1.08,
        "LOAD5min": 9.26,
        "LOAD15min": 4.31,
        "CPUcores": 4,
        "CPUusage": 41,
        "RAMtotal": 8192,
        "RAMusage": 27,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:03:30",
        "LOAD1min": 1.18,
        "LOAD5min": 0.8,
        "LOAD15min": 8.79,
        "CPUcores": 4,
        "CPUusage": 37,
        "RAMtotal": 8192,
        "RAMusage": 36,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:04:00",
        "LOAD1min": 4.87,
        "LOAD5min": 7.32,
        "LOAD15min": 0.88,
        "CPUcores": 4,
        "CPUusage": 9,
        "RAMtotal": 8192,
        "RAMusage": 49,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:04:30",
        "LOAD1min": 7.58,
        "LOAD5min": 0.36,
        "LOAD15min": 2.26,
        "CPUcores": 4,
        "CPUusage": 41,
        "RAMtotal": 8192,
        "RAMusage": 7,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:05:00",
        "LOAD1min": 0.32,
        "LOAD5min": 0.56,
        "LOAD15min": 2.66,
        "CPUcores": 4,
        "CPUusage": 31,
        "RAMtotal": 8192,
        "RAMusage": 30,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:05:30",
        "LOAD1min": 2.23,
        "LOAD5min": 3.4,
        "LOAD15min": 7.97,
        "CPUcores": 4,
        "CPUusage": 32,
        "RAMtotal": 8192,
        "RAMusage": 32,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:06:00",
        "LOAD1min": 7.07,
        "LOAD5min": 8.74,
        "LOAD15min": 8.14,
        "CPUcores": 4,
        "CPUusage": 28,
        "RAMtotal": 8192,
        "RAMusage": 12,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:06:30",
        "LOAD1min": 1.03,
        "LOAD5min": 0.27,
        "LOAD15min": 3.1,
        "CPUcores": 4,
        "CPUusage": 21,
        "RAMtotal": 8192,
        "RAMusage": 36,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:07:00",
        "LOAD1min": 7.01,
        "LOAD5min": 9.98,
        "LOAD15min": 5.35,
        "CPUcores": 4,
        "CPUusage": 47,
        "RAMtotal": 8192,
        "RAMusage": 16,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:07:30",
        "LOAD1min": 1.52,
        "LOAD5min": 5.88,
        "LOAD15min": 0.4,
        "CPUcores": 4,
        "CPUusage": 10,
        "RAMtotal": 8192,
        "RAMusage": 43,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:08:00",
        "LOAD1min": 0.75,
        "LOAD5min": 8.37,
        "LOAD15min": 0.67,
        "CPUcores": 4,
        "CPUusage": 29,
        "RAMtotal": 8192,
        "RAMusage": 24,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:08:30",
        "LOAD1min": 8.81,
        "LOAD5min": 5.15,
        "LOAD15min": 9.03,
        "CPUcores": 4,
        "CPUusage": 5,
        "RAMtotal": 8192,
        "RAMusage": 0,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:09:00",
        "LOAD1min": 2.34,
        "LOAD5min": 5.56,
        "LOAD15min": 4.03,
        "CPUcores": 4,
        "CPUusage": 45,
        "RAMtotal": 8192,
        "RAMusage": 18,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:09:30",
        "LOAD1min": 0.46,
        "LOAD5min": 3.82,
        "LOAD15min": 5.93,
        "CPUcores": 4,
        "CPUusage": 14,
        "RAMtotal": 8192,
        "RAMusage": 2,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:10:00",
        "LOAD1min": 6.6,
        "LOAD5min": 9.59,
        "LOAD15min": 3.02,
        "CPUcores": 4,
        "CPUusage": 45,
        "RAMtotal": 8192,
        "RAMusage": 2,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:10:30",
        "LOAD1min": 3.98,
        "LOAD5min": 5.83,
        "LOAD15min": 9.59,
        "CPUcores": 4,
        "CPUusage": 26,
        "RAMtotal": 8192,
        "RAMusage": 41,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:11:00",
        "LOAD1min": 6.1,
        "LOAD5min": 4.02,
        "LOAD15min": 4.1,
        "CPUcores": 4,
        "CPUusage": 12,
        "RAMtotal": 8192,
        "RAMusage": 23,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:11:30",
        "LOAD1min": 3.19,
        "LOAD5min": 1.95,
        "LOAD15min": 2.97,
        "CPUcores": 4,
        "CPUusage": 37,
        "RAMtotal": 8192,
        "RAMusage": 27,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:12:00",
        "LOAD1min": 9.46,
        "LOAD5min": 0.76,
        "LOAD15min": 1.22,
        "CPUcores": 4,
        "CPUusage": 6,
        "RAMtotal": 8192,
        "RAMusage": 18,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:12:30",
        "LOAD1min": 3.64,
        "LOAD5min": 8.73,
        "LOAD15min": 6.27,
        "CPUcores": 4,
        "CPUusage": 43,
        "RAMtotal": 8192,
        "RAMusage": 18,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:13:00",
        "LOAD1min": 7.75,
        "LOAD5min": 3.2,
        "LOAD15min": 3.28,
        "CPUcores": 4,
        "CPUusage": 38,
        "RAMtotal": 8192,
        "RAMusage": 23,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:13:30",
        "LOAD1min": 8.01,
        "LOAD5min": 0.65,
        "LOAD15min": 2.32,
        "CPUcores": 4,
        "CPUusage": 14,
        "RAMtotal": 8192,
        "RAMusage": 21,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:14:00",
        "LOAD1min": 0.49,
        "LOAD5min": 1.64,
        "LOAD15min": 0.77,
        "CPUcores": 4,
        "CPUusage": 46,
        "RAMtotal": 8192,
        "RAMusage": 28,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:22:00",
        "LOAD1min": 0.81,
        "LOAD5min": 4.73,
        "LOAD15min": 3.0,
        "CPUcores": 4,
        "CPUusage": 50,
        "RAMtotal": 8192,
        "RAMusage": 12,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:22:30",
        "LOAD1min": 0.09,
        "LOAD5min": 8.72,
        "LOAD15min": 5.7,
        "CPUcores": 4,
        "CPUusage": 16,
        "RAMtotal": 8192,
        "RAMusage": 46,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:23:02",
        "LOAD1min": 9.06,
        "LOAD5min": 2.35,
        "LOAD15min": 9.33,
        "CPUcores": 4,
        "CPUusage": 49,
        "RAMtotal": 8192,
        "RAMusage": 0,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:23:32",
        "LOAD1min": 9.46,
        "LOAD5min": 5.84,
        "LOAD15min": 8.75,
        "CPUcores": 4,
        "CPUusage": 29,
        "RAMtotal": 8192,
        "RAMusage": 36,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:24:02",
        "LOAD1min": 4.29,
        "LOAD5min": 1.68,
        "LOAD15min": 6.04,
        "CPUcores": 4,
        "CPUusage": 11,
        "RAMtotal": 8192,
        "RAMusage": 34,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:24:32",
        "LOAD1min": 2.96,
        "LOAD5min": 5.43,
        "LOAD15min": 7.02,
        "CPUcores": 4,
        "CPUusage": 15,
        "RAMtotal": 8192,
        "RAMusage": 0,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:25:02",
        "LOAD1min": 3.51,
        "LOAD5min": 6.52,
        "LOAD15min": 1.1,
        "CPUcores": 4,
        "CPUusage": 17,
        "RAMtotal": 8192,
        "RAMusage": 7,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:25:32",
        "LOAD1min": 1.35,
        "LOAD5min": 2.77,
        "LOAD15min": 2.52,
        "CPUcores": 4,
        "CPUusage": 45,
        "RAMtotal": 8192,
        "RAMusage": 45,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:26:02",
        "LOAD1min": 2.39,
        "LOAD5min": 0.12,
        "LOAD15min": 0.82,
        "CPUcores": 4,
        "CPUusage": 3,
        "RAMtotal": 8192,
        "RAMusage": 28,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:26:32",
        "LOAD1min": 8.98,
        "LOAD5min": 5.02,
        "LOAD15min": 8.46,
        "CPUcores": 4,
        "CPUusage": 0,
        "RAMtotal": 8192,
        "RAMusage": 28,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    },
    {
        "timestamp": "2024-01-01 00:27:02",
        "LOAD1min": 1.68,
        "LOAD5min": 7.33,
        "LOAD15min": 5.23,
        "CPUcores": 4,
        "CPUusage": 33,
        "RAMtotal": 8192,
        "RAMusage": 38,
        "DISKtotal": 1024000,
        "DISKusage": 36,
        "UPTIME": "10:00:00",
        "TotalSWAP": 1434345,
        "AvailableSWAP": 2131421,
        "TotalCachedMemory": 312435,
        "NICnames": [
            "NIC1",
            "NIC2"
        ],
        "dataIN": [
            "1000",
            "200"
        ],
        "dataOUT": [
            "200",
            "400"
        ]
    }
]
'''
# Load JSON data into a DataFrame
df = pd.read_json(json_data)

# Convert 'timestamp' column to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Set 'timestamp' as index
df.set_index('timestamp', inplace=True)

# Remove non-numeric columns
non_numeric_columns = ['UPTIME', 'NICnames', 'dataIN', 'dataOUT']
df = df.drop(columns=non_numeric_columns)

# Resample data into 30-second intervals and fill missing values with zeros
df_resampled = df.resample('1Min').fillna(method=None)

# Specify the start and end dates
StartDate = "2024-01-01 00:00:00"
EndDate = "2024-01-01 00:15:00"

# Check if the specified start and end dates are within the available data range
# if StartDate not in df_resampled.index or EndDate not in df_resampled.index:
#     print("Error: Start date or end date not found in the data.")
# else:
# Slice the DataFrame based on the start and end dates
sliced_df = df_resampled.loc[StartDate:EndDate]
# Check if there is enough data available within the specified range
if len(sliced_df) == 0:
    print("Error: Not enough data available within the specified range.")
else:
    # Plot the sliced data
    plt.figure(figsize=(10, 6))  # Adjust figure size
    plt.plot(sliced_df.index, sliced_df['CPUusage'], marker='.', color='b')  # Add markers and change line color
    plt.xlabel('Time')
    plt.ylabel('CPU Usage')
    plt.title('CPU Usage Over Time')
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    plt.grid(True)  # Add gridlines
    plt.tight_layout()  # Adjust layout for better spacing
    # Iterate through the DataFrame to identify consecutive missing data points
    is_missing = sliced_df['CPUusage'].isnull()
    missing_intervals = []
    start = None
    for timestamp, missing in is_missing.items():
        if missing and start is None:
            start = timestamp - pd.Timedelta(minutes=1) 
        elif not missing and start is not None:
            end = timestamp
            missing_intervals.append((start, end))
            start = None
    # Draw rectangles to represent missing intervals
    for start, end in missing_intervals:
        plt.axvspan(start, end, color='red', alpha=0.2)
    
    plt.show()
    
    
# ISUES:
'''
-the missing data is being averaged

'''