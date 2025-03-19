import os

diretorio = "./"  # Substitua pelo caminho do seu diretório, se necessário
arquivo_destino = "todos_os_codigos.py"

# Abre o arquivo de destino com a codificação utf-8
with open(arquivo_destino, "w", encoding="utf-8") as destino:
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith(".py") and arquivo != arquivo_destino:
            destino.write(f"# -----------------------------\n")
            destino.write(f"# Conteúdo de {arquivo}\n")
            destino.write(f"# -----------------------------\n\n")
            # Lê os arquivos com codificação utf-8 também
            with open(os.path.join(diretorio, arquivo), "r", encoding="utf-8") as origem:
                destino.write(origem.read())
                destino.write("\n\n")
print(f"Todos os arquivos Python no diretório foram combinados em {arquivo_destino}!")
