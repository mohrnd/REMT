#!/bin/bash

oids=(
    '.1.3.6.1.2.1.2.2.1.2'  # NIC names
    '.1.3.6.1.2.1.2.2.1.10'  # Bytes IN
    '.1.3.6.1.2.1.2.2.1.16'  # Bytes OUT
    '1.3.6.1.2.1.25.3.3.1.2' # Number of CPU cores
)


fetch_oid_values() {
	echo "$(date)" >> oid_values.txt
    for oid in "${oids[@]}"; do
        snmpwalk -v3 -l authPriv -u roadmin -a SHA -A admin123 -x AES -X admin123 192.168.69.47 "$oid" >> oid_values.txt
    done
}
fetch_oid_values

echo "OID values have been fetched and written to oid_values.txt"
