from flask import send_file
from io import BytesIO
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os, zipfile, pdfplumber
import time
import fitz
import csv
import pandas as pd
import eventlet


def convert_to_description(value):
    if value == "OD":
        return "Seg. Odontológica"
    elif value == "AMB":
        return "Seg. Ambulatorial"
    else:
        return value

def extract_and_save_tables_from_pdf() :
        try:
            os.chdir(os.path.dirname(os.path.abspath(__file__)))
            with pdfplumber.open("./src/file/attachments/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf") as pdf:
                tables_df = []

                for page in pdf.pages:
                    table = page.extract_table()

                    if table is not None:
                        table_df = pd.DataFrame(table[1:], columns=table[0])
                        tables_df.append(table_df)

                merged_df = pd.concat(tables_df)
                merged_df = merged_df.applymap(convert_to_description)
                merged_df.to_csv("./src/file/csvs/anexo_I.csv", index=False)
                
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
        
extract_and_save_tables_from_pdf()