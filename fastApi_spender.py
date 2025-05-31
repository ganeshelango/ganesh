from fastapi import FastAPI, HTTPException, Query
import requests
from fastapi.responses import FileResponse
import os
from common_utils import PdftoTable

app = FastAPI()

@app.post("/fileuploader")
def read_root(url: str):
    try:
        BankData = PdftoTable(url)
        if BankData.empty:
            raise HTTPException(status_code=404, detail="No table data found in PDF")
        csv_folder = url[:url.rfind('/')] + '/csv/'
        os.makedirs(csv_folder, exist_ok=True)
        filename = url[url.rfind('/') + 1:].lower().replace('pdf', 'csv')
        csv_path = os.path.join(csv_folder, filename)
        BankData.to_csv(csv_folder+filename,index=False)
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Failed to download PDF: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {e}")
