import docx
from docx.shared import Cm, Inches
import argparse
from parse_sn1per import *
from generate_docx import *
from generate_docx_utils import *

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

    add_subdomains(document, workspace)
    add_harvester_asn(document, workspace)
    add_harvester_interesting_url(document, workspace)
    add_forms(document, workspace)
    add_emails(document, workspace)
    add_public_files(document, workspace)
    add_tech(document, workspace)
    add_robots(document, workspace)
    # add_masscan(document, workspace)


    document.save(output)


main()