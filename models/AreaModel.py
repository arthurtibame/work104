import pandas as pd 

class Area():
    df = pd.ExcelFile(r"area_code.xlsx")
    sheet_names = df.sheet_names

    def __init__(self, sheet_names, area_en, area_zh_tw, area_code):
        
        self.area_en = area_en
        self.area_zh_tw = area_zh_tw
        self.area_code = area_en

