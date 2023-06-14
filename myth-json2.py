from os import popen
import json
from time import time



def main():
    
    sol_ = input('solidity file: ') # sem .sol 

    if sol_ == '0':

        sol_files_list = []

        dir_files = str(popen('ls').read()).split('\n')

        for item in dir_files:
            if '.sol' in item:
                sol_files_list.append(item.replace('.sol', ''))
                
        if sol_files_list == []:
            print('There is no solidity file on the directory')

        else: 
            for sol_file in sol_files_list:
                start_time = time()
                analysis = popen(f'myth analyze {sol_file}.sol -o json --max-depth 50').read()

                json.dump(
                    json.loads(analysis), 
                    open(f'{sol_file}_analized.json', 'w'), 
                    indent=4
                )

                time_spent = time() - start_time
                time_spent = [int(time_spent/60), round(time_spent%60)]
                print(f'Done {sol_file} analysis in {time_spent[0]} minutes and {time_spent[1]} seconds.')

    else:

        start_time = time()
        analysis = popen(f'myth analyze {sol_}.sol -o json --max-depth 50').read()
        
        json.dump(
            json.loads(analysis), 
            open(f'{sol_}_analized.json', 'w'), 
            indent=4
        )

        time_spent = time() - start_time
        time_spent = [int(time_spent/60), time_spent%60]
        print(f'Done {sol_} analysis in {time_spent[0]} minutes and {time_spent[1]} seconds.')

    print('Analysis complete.')

def set_imports(file):

    file = open(f'{file}.sol', 'r').read()

    index = 0
    imports = []
    
    while index != -1:

        first_quote_index = file.find('"', index)+1
        second_quote_index = file.find('"', first_quote_index)
        after_two_quotes = file.find('"', second_quote_index+1)

        imports.append(file[

            first_quote_index : second_quote_index

        ])
        index = after_two_quotes


    indexes_to_delete = []

    for item in imports:
        if item[0:3] != '../':
            indexes_to_delete.append(imports.index(item))
    del imports[indexes_to_delete[0]:]

    for i in range(len(imports)):
        # deleta o arquivo .sol do path
        imports[i] = list(imports[i])
        imports[i].reverse()
        imports[i] = imports[i][imports[i].index('/'):]
        imports[i].reverse()
        imports[i] = str().join(imports[i])


    imports = [ f'{imports[i][3:]}={imports[i]}' for i in range(len(imports))]
    # transforma '../libs/openzeppelin_v2_5_0/math/'
    # em 'libs/openzeppelin_v2_5_0/math/=../libs/openzeppelin_v2_5_0/math/'

    import_assets_json = {'remappings': imports}
    json.dump(
        import_assets_json,
        open('import_assets.json', 'w'),
        indent=4
    )



if __name__ == '__main__':
    set_imports('EthieToken')
    #main() 