import openpyxl
#from .models import EarlyWorksDoc, Correspondence, Uop_Bpd, Uop_spec
from app import db
from datetime import datetime
import os

wb = openpyxl.load_workbook('./xlsx/midorewd.xlsx')
ws = wb.active
session = db.session
file_list = []
error_list = []
file_dict = {}

def date_parse(date):
    if isinstance(date, int): return datetime.utcfromtimestamp(date)
    if isinstance(date, datetime): return date

    if date == '' or date is None: return None

    return datetime.strptime(date,'%d/%m/%y')

def check_extension(document_code, file_dict):
    
    if file_dict:
        print('ok')
    try:
        return file_dict[document_code]
    except:
        print('Wrong Extension', document_code)
        return None

# 
#upload_correspondence()
#print(error_list)
#upload_uop_bdp()
#upload_uop_spec() 


from app.init_helpers import init_dras

#init_dras()