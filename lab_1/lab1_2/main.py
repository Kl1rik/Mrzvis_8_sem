import subprocess
import os


def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True )
        return result
    except subprocess.CalledProcessError as e:
        if "compose" in command:
            print(f"Ошибка в compose.yaml :{e}")
        

print("Запуск веб приложения (Jenkins)")
run_command("docker-compose up")