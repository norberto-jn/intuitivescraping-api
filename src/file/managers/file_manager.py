from flask import send_file
from io import BytesIO
import zipfile
import unicodedata
import os
from pathlib import Path
import logging

class FileManager:

    @staticmethod
    def get_zip_as_buffer(name: str = None):
        zip_path = Path("./src/file/zips") / f"{FileManager.format_name(name) if name else 'anexos_compactados'}.zip"
        
        try:
            if not zip_path.exists():
                raise FileNotFoundError(f"Arquivo {zip_path} não encontrado.")
            
            with zip_path.open('rb') as zip_file:
                zip_buffer = BytesIO(zip_file.read())
            
            response = send_file(
                zip_buffer,
                mimetype='application/zip',
                as_attachment=True,
                download_name=zip_path.name
            )
            response.headers['Content-Disposition'] = f'attachment; filename="{zip_path.name}"'
            response.headers['Access-Control-Expose-Headers'] = 'Content-Disposition'
            zip_buffer.seek(0)
            return response
        
        except Exception as e:
            print(e)
            logging.error(f"Erro ao ler arquivo ZIP: {str(e)}")
            return {"error": f"Erro ao ler arquivo ZIP: {str(e)}"}, 500

    @staticmethod
    def compress_csv_files_to_zip(name: str):
        try:
            zip_filename = Path("/usr/src/workspace/intuitivescraping-api/src/file/zips") / f"{FileManager.format_name(name)}.zip"
            zip_filename.parent.mkdir(parents=True, exist_ok=True)

            csv_directory = Path("/usr/src/workspace/intuitivescraping-api/src/file/csvs")
            if not csv_directory.exists():
                raise FileNotFoundError(f"O diretório {csv_directory} não foi encontrado.")
            
            with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for csv_file in csv_directory.rglob("*.csv"):
                    zip_file.write(csv_file, csv_file.relative_to(csv_directory))
            
            return {
                "status": "success",
                "message": f"Arquivos CSV para {name} processados com sucesso e ZIP criado."
            }

        except Exception as e:         
            logging.error(f"Erro ao criar o ZIP para {name}: {str(e)}")
            return {
                "status": "error",
                "message": str(e)
            }

    @staticmethod
    def format_name(name: str) -> str:
        name_without_accents = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode('ASCII')
        
        formatted_name = name_without_accents.replace(" ", "_").lower()
        
        return formatted_name