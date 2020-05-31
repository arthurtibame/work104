import pandas as pd

class Country():
    
    df = pd.ExcelFile(r"area_code.xlsx")
    sheet_names = df.sheet_names
    area_names = df.parse("Taiwan").iloc[:,1].tolist()
    def __init__(self, sheet_names):
        self.sheet_names = sheet_names
    
    def getSheetNames(self):        
        return self.sheet_names
