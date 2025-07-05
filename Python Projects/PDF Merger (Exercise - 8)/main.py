from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir('PDF') if file.endswith('.pdf')]

for pdf in files:
    merger.append(pdf)
    
merger.write("All Cheetshets by CWH (Merged PDF).pdf")
merger.close()