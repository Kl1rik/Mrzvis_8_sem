import subprocess
import os
from colorama import Fore,Back,Style
def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True ,stdout=subprocess.DEVNULL ,stderr=subprocess.DEVNULL)
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
        elif "sh" in command:
            print(f"Нет доступа для исполнения файла :{e}")

def parse_output(byte_string):
    decoded_string = byte_string.decode('utf-8')
    cleaned_string = decoded_string.strip()
    return cleaned_string

def crud_txt_file():
    user = "iit11"
    # parse_output(subprocess.check_output("whoami"))
    files_path_user = f"/home/{user}/pzs/pzs11"
    files_path_group = f"/home/{user}/pzs/pzs12"
    files_path_others = f"/home/{user}/pzs/pzs13"
    files_path_all = f"/home/{user}/pzs/pzs14"
    files_path_root = f"/home/{user}/pzs/pzs15"

    folder_list = [files_path_user ,files_path_group , files_path_others , files_path_all , files_path_root]

    files_path_group = files_path_user
    files_path_others =files_path_user
    files_path_all = files_path_user
    files_path_root = files_path_user


    files_user = [f'{files_path_user}/file11',f'{files_path_user}/file12',f'{files_path_user}/file13',f'{files_path_user}/file14',f'{files_path_user}/file15']
    files_group = [f'{files_path_group}/file21',f'{files_path_group}/file22',f'{files_path_group}/file23',f'{files_path_group}/file24',f'{files_path_group}/file25']
    files_others = [f'{files_path_others}/file31',f'{files_path_others}/file32',f'{files_path_others}/file33',f'{files_path_others}/file34',f'{files_path_others}/file35']
    files_all = [f'{files_path_all}/file41',f'{files_path_all}/file42',f'{files_path_all}/file43',f'{files_path_all}/file44',f'{files_path_all}/file45']
    files_root = [f'{files_path_root}/file51',f'{files_path_root}/file52',f'{files_path_root}/file53',f'{files_path_root}/file54',f'{files_path_root}/file55']
    
    files_test_variable_list = files_user + files_group + files_others + files_all


        
    print(Fore.RED + "Начало проверки файлов")

    for file in files_test_variable_list:
        print(Fore.WHITE + f"Файл {file}(Исполнение/Редактирование/Удаление)")
        # print(Fore.WHITE + f"Исполнение файла {file}")
        read = os.access(file, os.R_OK)
        print("Да" if read else "Нет")

        # print(Fore.WHITE + f"Редактирование файла {file}")
        write = os.access(file, os.W_OK)
        print("Да" if write else "Нет")

        # print(Fore.WHITE + f"Удаление файла {file}")
        execute = os.access(file, os.X_OK)
        print("Да" if execute else "Нет")
        
       

    print(Fore.MAGENTA + "Начало проверки директорий")
    
    for folder in folder_list:
        print(Fore.LIGHTCYAN_EX + f"Проверка папки {folder}")

        file = f"{folder}/test_dir"
        print(Fore.WHITE + f"Создание файла {file}")
        run_command(f"touch {file}")
        

        print(Fore.WHITE + f"Редактирование файла {file}")
        # run_command(f"ls >> {file}")
        write_dir = os.access(file, os.W_OK)
        print("Да" if write_dir else "Нет")

        print(Fore.WHITE + f"Удаление файла {file}")
        # run_command(f"rm {file}")
        execute_dir = os.access(file, os.X_OK)
        print("Да" if execute_dir else "Нет")



def custom_user_run(program):
    program_path = parse_output(subprocess.check_output("pwd"))
    program_full_path = program_path + program
    users = ['iit11', 'iit12', 'iit21', 'iit22', 'iit3','root']
    for user in users:
        print(Fore.YELLOW + f"Проверка пользователя {user}")
        os.system(f"sudo -u {user} python3 {program_full_path}")