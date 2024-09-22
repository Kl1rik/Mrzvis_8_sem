import subprocess
from basic_functions import parse_output

program = parse_output(subprocess.check_output("pwd"))

print(program)
print(type(program))