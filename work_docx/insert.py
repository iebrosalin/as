from docx import *
import re

def move_table_after(doc, table, search):
    search_paragraph(doc, search)._p.addnext(table._element)

def move_header_after(doc, header, search):
    search_paragraph(doc, search)._p.addnext(header._p)

def search_table(doc, search):
  for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:               
                    if len(re.findall(search, cell.text)) > 0:
                        return table
            
def search_paragraph(doc, search):
    for p in doc.paragraphs:
        if p.text.find(search)>=0:
            return p
