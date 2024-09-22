import subprocess
import os
from basic_functions import parse_output,run_command
from delete_acl import clear_lab_enviroment


def create_users():
    print("Create users")
    users = ['iit11', 'iit12', 'iit21', 'iit22', 'iit3']
    for user in users:
        run_command(f"sudo useradd -m {user}")

def create_groups():
    print("Create groups (-f flag return positive if group exists)")
    groups = ['group_iit1', 'group_iit2']
    for group in groups:
        run_command(f"sudo groupadd -f {group}")

def add_users_to_groups():
    print("Adding users to groups")
    run_command("sudo usermod -aG group_iit1 iit11")
    run_command("sudo usermod -aG group_iit1 iit12")
    run_command("sudo usermod -aG group_iit2 iit21")
    run_command("sudo usermod -aG group_iit2 iit22")
    print("Add root access for user")
    run_command("sudo usermod -aG sudo iit21")

def create_folders(user):
    print("Create folders with ACL")
    
    home_path = f"/home/{user}/"
    folders = [
        (f'{home_path}pzs', 0o700),
        (f'{home_path}pzs/pzs11', 0o700),
        (f'{home_path}pzs/pzs12', 0o70),
        (f'{home_path}pzs/pzs13', 0o7),
        (f'{home_path}pzs/pzs14', 0o777),
        (f'{home_path}pzs/pzs15', 0o700)
    ]
    for folder, mode in folders:
        os.makedirs(folder, mode=mode, exist_ok=True)
    run_command(f"sudo chown root {home_path}pzs/pzs15")

def add_files_and_set_permissions(user):
    print("Add files")
    
    files_path_user = f"/home/{user}/pzs/pzs11"
    files_path_group = f"/home/{user}/pzs/pzs12"
    files_path_others = f"/home/{user}/pzs/pzs13"
    files_path_all = f"/home/{user}/pzs/pzs14"
    files_path_root = f"/home/{user}/pzs/pzs15"

    files_path_group = files_path_user
    files_path_others =files_path_user
    files_path_all = files_path_user
    files_path_root = files_path_user



    files_user = [f'{files_path_user}/file11',f'{files_path_user}/file12',f'{files_path_user}/file13',f'{files_path_user}/file14',f'{files_path_user}/file15']
    files_group = [f'{files_path_group}/file21',f'{files_path_group}/file22',f'{files_path_group}/file23',f'{files_path_group}/file24',f'{files_path_group}/file25']
    files_others = [f'{files_path_others}/file31',f'{files_path_others}/file32',f'{files_path_others}/file33',f'{files_path_others}/file34',f'{files_path_others}/file35']
    files_all = [f'{files_path_all}/file41',f'{files_path_all}/file42',f'{files_path_all}/file43',f'{files_path_all}/file44',f'{files_path_all}/file45']
    files_root = [f'{files_path_root}/file51',f'{files_path_root}/file52',f'{files_path_root}/file53',f'{files_path_root}/file54',f'{files_path_root}/file55']
    
    files_list = files_user + files_group + files_others + files_all + files_root
    files_test_variable_list = files_user + files_group + files_others + files_all

    for file in files_list:
        open(file, 'a').close() 
    
    for file in files_test_variable_list:
        run_command(f"echo \"read testVariable\" >> {file}")
    
    for file in files_root:
        run_command(f"echo \"echo \"Hello World\"\" >> {file}")
    


    permissions = {
        'user': ['100', '200', '400', '600', '700'],
        'group': ['110','220', '440', '660', '770'],
        'others': ['101','202', '404', '606', '707'],
        'all': ['111','222', '444', '666', '777'],
        'root': ['100', '200', '400', '600', '700'],
    }

    for perm in range(len(permissions['user'])):
        
        run_command(f"sudo chmod {permissions['user'][perm]} {files_user[perm]}")
            
    for perm in range(len(permissions['group'])):    
        run_command(f"sudo chmod {permissions['group'][perm]} {files_group[perm]}")
    for perm in range(len(permissions['others'])):
        run_command(f"sudo chmod {permissions['others'][perm]} {files_others[perm]}")
    for perm in range(len(permissions['all'])):        
        run_command(f"sudo chmod {permissions['all'][perm]} {files_all[perm]}")
    for perm in range(len(permissions['root'])):
        run_command(f"sudo chmod {permissions['root'][perm]} {files_root[perm]}")

def main():
    user = parse_output(subprocess.check_output('whoami'))
    create_users()
    create_groups()
    add_users_to_groups()
    create_folders(user)
    add_files_and_set_permissions(user)

if __name__ == "__main__":
    main()
