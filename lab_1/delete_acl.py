import subprocess
import os
from basic_functions import parse_output,run_command

def clear_lab_enviroment():
    user = parse_output(subprocess.check_output('whoami'))
    users = ['iit11', 'iit12', 'iit21', 'iit22', 'iit3']
    user_groups = ['group_iit1','group_iit2']
    
    print("Удаление папок и файлов")
    run_command(f"sudo rm -rf /home/{user}/pzs/")
    
    print("Удаление пользователей")
    for user in users:
        run_command(f"sudo userdel {user}")

    print("Удаление созданных групп")
    for group in user_groups:
        run_command(f"sudo groupdel {group}")

    print("Созданные пользователи, группы, папки и файлы успешно удалены")