import re
import os

def parse_subdomains(file_path):
    path_domains = file_path + "\\domains\domains-all-sorted.txt"
    # print(path_domains)
    with open(path_domains) as file:
        data = file.read()

    res = re.findall(r'(.*)\n', data)
    return res

def parse_the_harvester_asn(file_path):
    path_file = file_path + "\\osint\\theharvester-skillbox.ru.txt"
    # print(path_file)
    with open(path_file) as file:
        data = file.read()

    res = re.findall(r'(\[\*\] ASNS found:.*\n-+\n)((.*\n)+)(\[\*\] Interesting Urls found)', data)
    res = list(filter(None,res[0][1].split('\n')))
    return res

def parse_the_harvester_interesting_url(file_path):
    path_file = file_path + "\\osint\\theharvester-skillbox.ru.txt"
    # print(path_file)
    with open(path_file) as file:
        data = file.read()

    res_temp = re.search(r'\[\*\] Interesting Urls found: \d+\n--------------------(.*\n)+\n\[\*] LinkedIn Links found', data)[0]
    res = re.search(r'(http.*\n)+', res_temp) [0]
    res = list(filter(None,res.split('\n')))
    return res

def parse_forms(file_path):
    path_forms = file_path + "\\web\\" + file_path + "_80-forms-sorted.txt"
    # print(path_domains)
    with open(path_forms) as file:
        data = file.read()

    res = re.findall(r'(.*)\n', data)
    return res

def parse_emails(file_path):
    path_forms = file_path + "\\web\\" + file_path + "_80-emails-sorted.txt"
    # print(path_domains)
    with open(path_forms) as file:
        data = file.read()

    res = re.findall(r'(.*)\n', data)
    return res

def parse_public_files(file_path):
    path_forms = file_path + "\\web\\static-extensions-" + file_path + ".txt"
    # print(path_domains)
    with open(path_forms) as file:
        data = file.read()

    res = re.findall(r'(.*)\n', data)
    return res

def parse_tech(file_path):
    path_forms = file_path + "\\web\\webtech-" + file_path + "-http-port80.txt"
    # print(path_domains)
    with open(path_forms) as file:
        data = file.read()

    res = re.findall(r'(.*)\n', data)
    return res

def parse_robots(file_path):
    path_robots = file_path + "\\web\\robots-" + file_path + "%3A80-http.txt"

    if os.path.isfile(path_robots) != True:
        path_robots = file_path + "\\web\\robots-" + file_path + ":80-http.txt"
        if os.path.isfile(path_robots) != True:
            return False

    # print(path_domains)
    with open(path_robots) as file:
        data = file.read()

    res = re.findall(r'(.*)\n', data)
    return res

