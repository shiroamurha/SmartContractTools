from os import popen
from os import getcwd



solfile = input('sol file (without .sol): ')
current_path = f'../{getcwd().split("/")[-1]}/{solfile}' # becomes ../current_dir/file

analysis = popen(f'slither {current_path}.sol --checklist --show-ignored-findings').read()
open(f'{solfile}_analyzed.md', 'w').write(analysis)