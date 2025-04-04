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

def download_attachments():
        base_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
        download_folder = "./src/file/attachments"
        
        os.makedirs(download_folder, exist_ok=True)
        
        try:
            response = requests.get(base_url, timeout=20)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            downloaded_files = []
            
            for link in soup.find_all('a', href=True):
                href = link['href']
                if ("Anexo_I" in href or "Anexo_II" in href) and href.lower().endswith('.pdf'):
                    full_url = urljoin(base_url, href)
                    filename = os.path.join(download_folder, full_url.split('/')[-1])
                    
                    try:
                        print(f"Baixando {full_url}...")
                        response = requests.get(full_url, stream=True, timeout=30)
                        response.raise_for_status()
                        
                        with open(filename, 'wb') as f:
                            for chunk in response.iter_content(chunk_size=8192*4):
                                f.write(chunk)
                        
                        downloaded_files.append(filename)
                        print(f"Download concluído: {filename}")
                    
                    except Exception as e:
                        print(f"Erro ao baixar {full_url}: {str(e)}")
                        continue
            
            return {
                "message": "Downloads concluídos com sucesso",
                "downloaded_files": downloaded_files
            }
        
        except Exception as e:
            return {"error": f"Ocorreu um erro: {str(e)}"}, 500

download_attachments()