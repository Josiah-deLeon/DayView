# Author: Josiah de Leon
# File: pdf_converter
# Description: Converts the pdf into a csv
#               for easier data manipulation

import PyPDF2
import re
import pandas as pd

def pdf_to_csv_pypdf2(pdf_path, csv_path):
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            
            for page in pdf_reader.pages:
                text += page.extract_text() +"\n"
        
        lines = text.strip().split('\n')
        data = []
        
        for line in lines:
            if line.strip():
                row = re.split(r'\s{2,}', line.strip())
                data.append(row)
                
        if data:
            df= pd.DataFrame(data[1:], columns=data[0])
        else:
            df = pd.DataFrame()
            
        df.to_csv(csv_path, index=False)
        print(f"Sucessfully converted {pdf_path} to {csv_path}")
        return df
                
    except Exception as e:
        print(f"Error: {e}")
        return None
    
if __name__ =="__main__":
    pdf_file = "July Week 1.pdf"
    csv_file = "output.csv"
    
    df = pdf_to_csv_pypdf2(pdf_file, csv_file)
    
    if df is not None:
        print("\nFirst few rows:")
        print(df.head())
        