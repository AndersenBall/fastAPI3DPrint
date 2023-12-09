from fastapi import FastAPI,UploadFile,File
from fastapi.exceptions import HTTPException
import os
import shutil

UPLOAD_DIR = "uploads"

class STLObject:
    def __init__(self, filen: str, tech: str, infil: str, layerThick: str, material: str):
        self.filename = filen
        self.Technology = "FFF" if "FFF" in tech else "SLA" if "SLA" in tech else None
        self.Infil = self.convert_infil(infil)
        self.layerThickness = self.convert_layer_thickness(layerThick)
        self.material = "PLA" if "PLA" in tech else "ABS" if "ABS" in tech else None

    def convert_infil(self, infil_str: str) -> float:
        try:
            # Remove any non-numeric characters from the string (e.g., "10%" becomes "10")
            numeric_part = "".join(c for c in infil_str if c.isdigit())
            return float(numeric_part)
        except ValueError:
            # Handle the case where the conversion to float fails
            return None

    def convert_layer_thickness(self, layer_thickness_str: str) -> float:
        try:
            # Remove any non-numeric characters from the string (e.g., "0.1mm" becomes "0.1")
            numeric_part = "".join(c for c in layer_thickness_str if c.isdigit() or c == '.')
            return float(numeric_part)
        except ValueError:
            # Handle the case where the conversion to float fails
            return None
    def __str__(self):
        return (
            f"STLObject:\n"
            f"  Name: {self.filename}\n"
            f"  Technology: {self.Technology}\n"
            f"  Infill: {self.Infil}\n"
            f"  Layer Thickness: {self.layerThickness}\n"
            f"  Material: {self.material}"
        )



def Upload_File(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"filename": file.filename}

def Calc_Cost(stlObj: STLObject):

    file_path = os.path.join(UPLOAD_DIR, stlObj.filename)
    if not os.path.exists(file_path):
        
        raise HTTPException(status_code=404, detail="File not found")
    returnvalue = os.stat(file_path).st_size
    try:
        returnvalue = round(returnvalue/100000000,2)
        if stlObj.Technology =="SLA":
            returnvalue = returnvalue*1.1
        returnvalue = returnvalue * (stlObj.Infil +.1)
        returnvalue = returnvalue * (.9 + (stlObj.layerThickness))
        
    except Exception as e:
        raise HTTPException(status_code=400,detail="error calc price")
    return {"filename": stlObj.filename, "content": returnvalue}


def FindStlFilePath(filename):
    return filename
