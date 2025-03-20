import os
import re
from PyPDF2 import PdfReader


source_dir = input("Введіть шлях до папки з PDF-файлами: ").strip()

# Перетворити шлях у сирий рядок
source_dir = r"{}".format(source_dir)

f = open(f"{source_dir}\\test3.pdf", "r")
print(f.read())


