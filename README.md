# Objetivo
Esse projeto tem por objetivo:
- Converter `.docx` em `.pdf`
- Zipar a pasta com os documentos em `.pdf`
- Mover um arquivo `.xlsx` para a pasta `output_file`

## Projeto
Para rodar o projeto corretamente é necessário colocar o caminho correto das pastas e arquivos na pasta `config`, mais especificamente em `settings.py`.

- `pasta_input` é a pasta que você quer converter os arquivos `.docx`.
- `xlsx_input` é caminho onde está o arquivo Excel.
- `pasta_output` é a pasta onde os arquivos `.pdf` e onde os mesmos são zipados.
<br>
<br>
> *OBS*: As pastas `input_files` e `output_files` são exemplares para esse projeto. Se for usar em alguma pasta sua já criada as mesmas podem ser excluídas.
<br>

Após colocar os caminhos corretos no `settings.py` você vai precisar:
- Abrir o terminal
- Rodar o comando `python main.py`