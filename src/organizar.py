# Lógica para mover arquivos, criar pasta, zipar

import os
from config.settings import pasta_output
import zipfile


def zipar_pdf_das_pastas(nome_zip=None):
    """Compacta a pasta 'output_files' (dentro de pasta_output) e salva o .zip dentro dela."""
    if not os.path.isdir(pasta_output):
        raise FileNotFoundError(
            f"Pasta 'output_files' não encontrada -> {pasta_output}")

    pasta_zipados = os.path.join(pasta_output, "zipados")
    os.makedirs(pasta_zipados, exist_ok=True)

    zip_name = nome_zip if nome_zip else os.path.basename(
        pasta_output.rstrip(os.sep))
    zip_path = os.path.join(pasta_zipados, zip_name + ".zip")

    with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        for filename in os.listdir(pasta_output):
            if filename.lower().endswith(".pdf"):
                full_path = os.path.join(pasta_output, filename)
                zf.write(full_path, arcname=filename)

    print(f"Arquivos .pdf zipados com sucesso → {zip_path}")
    return zip_path
