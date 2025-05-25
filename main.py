import subprocess
import os


diretorio_base = os.path.dirname(os.path.abspath(__file__))

# Lista com os caminhos dos arquivos
arquivos = [
    os.path.join(diretorio_base, 'atividade1', 'atividade1.py'),
    os.path.join(diretorio_base, 'atividade2', 'atividade2.py'),
    os.path.join(diretorio_base, 'atividade3', 'atividade3.py')
]

# Executar cada arquivo
for arquivo in arquivos:
    if os.path.exists(arquivo):
        print(f'Executando {arquivo}')
        subprocess.run(['python', arquivo])
    else:
        print(f'Arquivo não encontrado: {arquivo}')