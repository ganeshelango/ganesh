import pdfplumber
import pandas as pd

def PdftoTable(url):
    monthData = []
    with pdfplumber.open(url) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    for row in table:
                        monthData.append(row)
    if len(monthData) == 0:
        return pd.DataFrame()
    else:
        return pd.DataFrame(monthData[1:], columns=monthData[0])
