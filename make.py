import subprocess

# Lista de comandos de compilação com o Python especificado
commands = [
    ["python3", "install.py", "-s", "-O2", "-std=c++17", "-o", "info", "-Wall", "-Wextra", "-Wpedantic", "main.cpp", "MazeGen8.cpp", "-luser32", "-lgdi32", "-lgdiplus", "-lopengl32", "-lSHlwapi", "-ldwmapi", "-lstdc++fs", "-lwinmm", "-Wl,-subsystem,windows"],
    ["python3", "install.py", "-s", "-O2", "-std=c++17", "-o", "info", "-Wall", "-Wextra", "-Wpedantic", "main.cpp", "MazeGen8.cpp", "-luser32", "-lgdi32", "-lgdiplus", "-lopengl32", "-lSHlwapi", "-ldwmapi", "-lstdc++fs", "-lwinmm"],
    ["python3", "install.py", "-g", "-Og", "-std=c++17", "-o", "info", "-Wall", "-Wextra", "-Wpedantic", "main.cpp", "MazeGen8.cpp", "-luser32", "-lgdi32", "-lgdiplus", "-lopengl32", "-lSHlwapi", "-ldwmapi", "-lstdc++fs", "-lwinmm", "-Wl,-subsystem,windows"],
    ["python3", "install.py", "-g", "-Og", "-std=c++17", "-o", "info", "-Wall", "-Wextra", "-Wpedantic", "main.cpp", "MazeGen8.cpp", "-luser32", "-lgdi32", "-lgdiplus", "-lopengl32", "-lSHlwapi", "-ldwmapi", "-lstdc++fs", "-lwinmm"]
]

# Executando cada comando
for command in commands:
    try:
        # Subprocess para rodar os comandos com o Python
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print(f"Output do comando:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {e}")
        print(f"Saída de erro:\n{e.stderr}")
