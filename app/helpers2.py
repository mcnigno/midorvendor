import os
from openpyxl import load_workbook
from config import UPLOAD_FOLDER

for path, directory, files in os.walk(UPLOAD_FOLDER):
    print(files)