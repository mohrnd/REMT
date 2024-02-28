#!/bin/bash
#turn into an executable with: chmod +x setup.sh
#run as root

echo "Installing net-snmp RPMs..."
yum install -y net-snmp net-snmp-libs net-snmp-utils net-snmp-agent-libs


echo "Adding SNMP v3 users..."
echo "createUser roadmin SHA admin123 AES" >> /etc/snmp/snmpd.conf
echo "createUser rwadmin SHA admin321 AES" >> /etc/snmp/snmpd.conf
echo "rouser roadmin authpriv system" >> /etc/snmp/snmpd.conf
echo "rwuser rwadmin authpriv system" >> /etc/snmp/snmpd.conf


echo "Enabling and starting snmpd service..."
systemctl enable snmpd
systemctl start snmpd
systemctl restart snmpd

echo "SNMP configuration completed."
