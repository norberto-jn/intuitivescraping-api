from flask import Blueprint, request
from ..managers.file_manager import FileManager

file_controller = Blueprint('file', __name__)

@file_controller.route('/api/v1/file/download/csv', methods=['GET'])
def download_csv():
    name = request.args.get('name')
    if not name:
        return {"error": "Parâmetro 'name' é obrigatório."}, 400
    
    return FileManager.get_zip_as_buffer(name)

@file_controller.route('/api/v1/file/download/attachments', methods=['GET'])
def downloads_attachments():
    return FileManager.get_zip_as_buffer()

@file_controller.route('/api/v1/file/compress-csv-files-to-zip', methods=['POST'])
def compress_csv_files_to_zip():  
    data = request.get_json()
    name = data.get('name')    
    if not name:
        return {"error": "O campo 'name' é obrigatório."}, 400
    
    result = FileManager.compress_csv_files_to_zip(name)
    
    if result['status'] == 'error':
        return {"error": result['message']}, 500

    return {"message": result['message']}, 200