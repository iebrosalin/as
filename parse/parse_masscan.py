import argparse
import json
import ipaddress

def parse_masscan(file_path):
    path_file= file_path + 'masscan.json'

    f = open(path_file)
    data = json.load(f)

    res = {}
    
    for item in data:
        if res.get(item['ip']) == None:
            res [item['ip']] = [
                item['ports'][0]['port']
            ]
        else:
            res [item['ip']]. append(item['ports'][0]['port'])
    
    ip_list = []

    for item in res:
        res[item] = sorted(res[item])

    for key in res:
        ip_list.append(ipaddress.ip_address(key))
    ip_list.sort()

    ip_str_list = []
    port_list = []

    for item in ip_list:
        ip_str_list.append(str(item))
        port_list.extend(res[str(item)])

    port_list = set(port_list) 
    
    with open(file_path + '/nmap_ports.txt','w+') as f:
        i=1
        for port in port_list:
            if len(port_list)!=i:  
                f.write(str(port)+",")
            else:
                f.write(str(port))
            i= i+1

    with open(file_path +'/nmap_ips.txt','w+') as f:
        for ip in ip_str_list:  
            f.write(ip+"\n")
    res ={
        'data': res,
        'ip_list_sorted': ip_str_list
    }

    return res


parser = argparse.ArgumentParser(description='SOC CIB generator minimal template from sn1per workspace.')
parser.add_argument('workspace', help='folder from workpace sn1per')
args = parser.parse_args()
workspace = args.workspace

parse_masscan(workspace)