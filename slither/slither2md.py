from os import popen



solfile = input('sol file (without .sol): ')
analysis = popen(f'slither {solfile}.sol --checklist --show-ignored-findings').read()
open(f'{solfile}_analyzed.md', 'w').write(analysis)