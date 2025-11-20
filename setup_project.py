import os

# Estrutura de pastas e ficheiros
estrutura = {
    "src/video": ["capture.py", "utils.py"],
    "src/detection": ["detector.py", "landmarks.py"],
    "src/ui": ["visualizer.py"],
    "src": ["main.py", "__init__.py"],
    "tests": ["test_detector.py"],
    "data": [],
}

# Criar pastas e ficheiros
for pasta, ficheiros in estrutura.items():
    os.makedirs(pasta, exist_ok=True)
    for nome_ficheiro in ficheiros:
        caminho = os.path.join(pasta, nome_ficheiro)
        with open(caminho, 'w') as f:
            f.write(f"# {nome_ficheiro}\n")

# Criar ficheiros raiz
with open("requirements.txt", "w") as f:
    f.write("# Bibliotecas necessárias\n")

with open("README.md", "w") as f:
    f.write("# Projeto Hand Detection\n\nDescrição do projeto aqui.\n")

print("✅ Estrutura criada com sucesso.")
