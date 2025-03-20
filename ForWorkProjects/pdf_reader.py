import os
import re
from PyPDF2 import PdfReader


def extract_contract_number(text):
    # Регулярний вираз для пошуку номера договору у форматі "договір хх-хххх/xx-xx-x"
    match = re.search(r'договір № (\d{2}-\d{4})/\d{2}-\d{2}-\d', text, re.IGNORECASE)
    if match:
        return match.group(1)
    return None

def get_text_from_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ''

def rename_pdfs_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            text = get_text_from_pdf(file_path)
            contract_number = extract_contract_number(text)
            if contract_number:
                new_filename = f"{contract_number}.pdf"
                new_file_path = os.path.join(folder_path, new_filename)
                os.rename(file_path, new_file_path)
                print(f"Renamed '{filename}' to '{new_filename}'")

# Вкажіть шлях до папки з PDF-файлами
folder_path = r'C:\\Users\\user\\Desktop\\test_py\\error'  # або 'C:/Users/user/Desktop/test_py', або 'C:\\Users\\user\\Desktop\\test_py'
rename_pdfs_in_folder(folder_path)
