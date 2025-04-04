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

def create_zip_from_attachments():
        attachments_folder = "./src/file/attachments"
        zips_folder = "./src/file/zips"
        zip_filename = "anexos_compactados.zip"
        zip_path = os.path.join(zips_folder, zip_filename)
        
        try:
            os.makedirs(zips_folder, exist_ok=True)
            
            files_to_zip = [f for f in os.listdir(attachments_folder) 
                          if f.endswith('.pdf') and os.path.isfile(os.path.join(attachments_folder, f))]
            
            if not files_to_zip:
                return {"error": "Nenhum arquivo PDF encontrado na pasta attachments"}, 404
            
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as zipf:
                for file in files_to_zip:
                    file_path = os.path.join(attachments_folder, file)
                    zipf.write(file_path, os.path.basename(file))
            
            return {
                "message": "Arquivo ZIP criado com sucesso",
                "zip_path": zip_path,
                "files_included": files_to_zip
            }
        
        except Exception as e:
            return {"error": f"Erro ao criar ZIP: {str(e)}"}, 500

create_zip_from_attachments()