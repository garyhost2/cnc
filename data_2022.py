import os
import re
from PIL import Image
from pytesseract import pytesseract

results_2022 = []
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
n = input('quell est le nom de votre institut ')
if n == 'ipeit' :
    folder_path =r'C:\Users\moham\OneDrive\Documents\cnc rang\ipeit\2021' 
    
elif n == 'ipeib' :
    folder_path = r'C:\Users\moham\OneDrive\Documents\cnc rang\ipeib'
else :print ('votre institut est introvable ')
os.chdir(folder_path)
file_paths = []

for file in os.listdir():
    if file.endswith(".png"):
        file_paths.append(file)
    
#func that scan image to a list 
def scan(file_path):
    im = Image.open(file_path)
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(im)
    x = text.split()
    return x

#list of all results_2022 

for file_path in file_paths :
    result =  scan(file_path)
    results_2022.append(result)
#tandhifa
results_2022 = [int(n) for n in re.findall(r'-?\d+(?:\.\d+)?', str(results_2022))]
def sort():
    results_2022.sort()
    return results_2022
sort()