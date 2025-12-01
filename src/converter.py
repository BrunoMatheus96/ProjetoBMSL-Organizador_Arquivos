# Lógica de conversão .docx → pdf

from docx2pdf import convert
import os
from config.settings import pasta_input, pasta_output

# Garante que a pasta de saída existe
if not os.path.exists(pasta_output):
    os.makedirs(pasta_output)

# Percorre os .docx na pasta de input
for nome in os.listdir(pasta_input):
    if nome.lower().endswith(".docx"):
        in_file = os.path.join(pasta_input, nome)
        # define caminho de saída com mesmo nome, extensão .pdf
        base = os.path.splitext(nome)[0]
        out_file = os.path.join(pasta_output, base + ".pdf")
        convert(in_file, out_file)
        print(f"Convertido: {in_file} → {out_file}")
