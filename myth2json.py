from os import popen
import json
from time import time



def main():
    
    sol_ = input('solidity file: ') # sem .sol 
    # TODO: trocar o input por parametro no main() pra utilizaçao na interface (talvez)

    # input zero pega todos os arquivos do diretório e faz análise um por um
    if sol_ == '0':

        sol_files_list = []

        dir_files = str(popen('ls').read()).split('\n')

        for item in dir_files:
            if '.sol' in item:
                sol_files_list.append(item.replace('.sol', ''))
                
        if sol_files_list == []:
            print('There is no solidity file on the directory')
        # retorna isso ai ^^^^ se nao achar nenhum arquivo .sol no diretorio

        else: 
            # se tiver arquivos .sol no diretorio, faz a analise um por um
            for sol_file in sol_files_list:

                set_imports(sol_file) 
                # cria o arquivo temporario imports_assets.json pra ser usado pelo comando de análise do mythril

                start_time = time() # pra cronometrar o tempo de execução de cada análise
                analysis = popen(f'myth analyze {sol_file}.sol -o json --max-depth 25 --solc-json import_assets.json').read()
                # comando de analise do mythril

                json.dump(
                    json.loads(analysis), 
                    open(f'{sol_file}_analyzed.json', 'w'), 
                    indent=4
                )
                # lança a analise num arquivo <nomedoarquivo>_analyzed.json

                time_spent = time() - start_time
                time_spent = [int(time_spent/60), round(time_spent%60)]
                # calculo de diferença do tempo

                print(f'Done {sol_file} analysis in {time_spent[0]} minutes and {time_spent[1]} seconds.')
                # output da analise com o tempo de execuçao de cada um
    else:

        set_imports(sol_)
        start_time = time()
        analysis = popen(f'myth analyze {sol_}.sol -o json --max-depth 25 --solc-json import_assets.json').read()
        
        json.dump(
            json.loads(analysis), 
            open(f'{sol_}_analyzed.json', 'w'), 
            indent=4
        )

        time_spent = time() - start_time
        time_spent = [int(time_spent/60), round(time_spent%60)]
        print(f'Done {sol_} analysis in {time_spent[0]} minutes and {time_spent[1]} seconds.')

    # deleta o arquivo de imports pq ele so serve pra o mythril analisar 
    popen('rm -f import_assets.json')
    print('Analysis complete.')

def set_imports(file):

    # abre o contrato especificado no argumento da funçao
    file = open(f'{file}.sol', 'r').read()

    index = 0
    imports = []
    
    # acha todos os conteudos entre " " e atribui a lista imports
    while index != -1:

        first_quote_index = file.find('"', index)+1
        second_quote_index = file.find('"', first_quote_index)
        after_two_quotes = file.find('"', second_quote_index+1)

        imports.append(file[

            first_quote_index : second_quote_index

        ])
        index = after_two_quotes

    # procura e deleta os itens de imports[] que nao contem "../" no começo (pq esses n precisam ser setados, ou nao sao imports)
    indexes_to_delete = []

    for item in imports:
        if item[0:3] != '../':
            indexes_to_delete.append(imports.index(item))
    del imports[indexes_to_delete[0]:]

    # deleta o arquivo .sol do path do import, as definiçoes de imports so precisam do diretorio
    for i in range(len(imports)):
        if imports[i].count('/') > 1: # se o remapping de import for só um ../contrato.sol, precisa deixar o arquivo no path de import
            imports[i] = list(imports[i])
            imports[i].reverse()
            imports[i] = imports[i][imports[i].index('/'):]
            imports[i].reverse()
            imports[i] = str().join(imports[i])

    # nao usa mais isso aqui (eu acho kk)
    # items_to_delete = []
    # for item in imports:
    #     if item == '../':
    #         items_to_delete.append(item)
    # for item in items_to_delete:
    #     imports.remove(item)


    imports = [ f'{imports[i][3:]}={imports[i]}' for i in range(len(imports))]
    # transforma '../libs/openzeppelin_v2_5_0/math/'
    # em 'libs/openzeppelin_v2_5_0/math/=../libs/openzeppelin_v2_5_0/math/'

    import_assets_json = {'remappings': imports}
    json.dump(
        import_assets_json,
        open('import_assets.json', 'w'),
        indent=4
    )
    # completa jogando o dicionario de imports dentro do arquivo import_assets.json



if __name__ == '__main__':
    main()