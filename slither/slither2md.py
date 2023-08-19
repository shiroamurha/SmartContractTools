from os import popen
from os import getcwd


with_path = True
solfile = input('sol file (without .sol): ')
path = getcwd().split("\\")[-1]
current_path = f'..\\{path}\\{solfile}'
if with_path:
    analysis = popen(f'slither {current_path}.sol --checklist --show-ignored-findings').read()
else:
    analysis = popen(f'slither {solfile}.sol --checklist --show-ignored-findings').read()
open(f'{solfile}_analyzed.md', 'w').write(analysis)