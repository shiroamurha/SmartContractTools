from os import popen
import json



sol_file = input('solidity file: ') # sem .sol 

var = popen(f'myth analyze {sol_file}.sol -o json --max-depth 50').read()

json.dump(
    json.loads(var), 
    open(f'{sol_file}_analized.json', 'w'), 
    indent=4
)