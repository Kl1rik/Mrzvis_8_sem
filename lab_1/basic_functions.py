import subprocess
import os
def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True)
        return result
    except subprocess.CalledProcessError as e:
        if "useradd" in command:
            print(f"Такой пользователь уже есть или не хватает прав :{e}")
        elif "touch" in command:
            print(f"Нет доступа для создания файлов :{e}")
        elif ">>" in command:
            print(f"Нет доступа для редактирования :{e}")
        elif "rm" in command:
            print(f"Нет доступа для редактирования :{e}")

def parse_output(byte_string):
    decoded_string = byte_string.decode('utf-8')
    cleaned_string = decoded_string.strip()
    return cleaned_string

def crud_txt_file():
    print("Начало проверки")

    print("Cоздание файла")
    run_command("touch test.txt")

    print("Редактирование файла")
    run_command("ls >> test.txt")

    print("Удаление файла")
    run_command("rm test.txt")


def custom_user_run(program):
    program_path = parse_output(subprocess.check_output('pwd'))
    program = program_path + program
    users = ['iit11', 'iit12', 'iit21', 'iit22', 'iit3','root']
    for user in users:
        os.system(f"sudo -u {user} python3 {program}")