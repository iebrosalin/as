#!/bin/bash
cat tz_domains_list.txt | xargs -n1 -P100 dig +short +retry=3 | grep -E '^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' > resolve_tz_domains_list.txt
awk '!seen[$0]++' resolve_tz_domains_list.txt > uniq_resolve_tz_domains_list.txt

cat uniq_resolve_tz_domains_list.txt > fact_ips_list.txt
cat tz_ips_list.txt >> fact_ips_list.txt
awk '!seen[$0]++' fact_ips_list.txt  > uniq_fact_ips_list.txt

cat uniq_fact_ips_list.txt | xargs -n1 -P100 

while read -r line; do
    echo "whois $line" >> whois_report.txt
    whois $line >> whois_report.txt
done <uniq_fact_ips_list.txt

masscan $(tr '\n' , < uniq_fact_ips_list.txt) -p0-65535 -oJ masscan.json

while read -r line; do
    echo "whois $line" >> whois_report.txt
    whois $line >> whois_report.txt
done <uniq_fact_ips_list.txt

mkdir theHarvester

while read -r line; do
    echo "theHarvester -d $line -b all -f ./theHarvester/$line.json -v -t"
    theHarvester -d $line -b all -f ./theHarvester/$line.json -v -t
done <tz_domains_list.txt

python '../../../parse/parse_masscan.py' ./
echo "Nmap TCP"
nmap -Pn -sS -iL ./nmap_ips.txt -p $(tr '\n' , <./nmap_ports.txt)  -A  -T5 –oX ./nmap_tcp_report.xml -vvv

echo "Nmap UDP"
nmap -Pn -sU-iL ./nmap_ips.txt -p-  -A  -T5 –oX ./nmap_udp_report.xml -vvv