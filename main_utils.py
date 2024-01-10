import docx
import argparse
from parse.parse_sn1per import *
from work_docx.generate_docx_utils import *

def main():
    parser = argparse.ArgumentParser(description='SOC CIB generator minimal template from sn1per workspace.')
    parser.add_argument('workspace', help='folder from workpace sn1per')
    parser.add_argument('output', help='output file docx')
    parser.add_argument('template', help='template docx')

    args = parser.parse_args()
    workspace = args.workspace
    output = args.output
    template = args.template

    document = docx.Document(template)
    # add_nmap(document, workspace)
    add_masscan(document, workspace)
    add_harvester_asn(document, workspace)
    add_harvester_interesting_url(document, workspace)
    add_harvester_subdomains(document, workspace)


    document.save(output)


main()