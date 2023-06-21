# Mythril-repo


<h1 align="center">Tutorial</h1>
<h3>Requisitos:</h3>
<ul>
    <li>Python 3.9+ instalado; </li>
    <li>Mythril instalado, pode ser feito com o comando <code>pip install mythril</code> </li>
    <p><i><b>OBS: Mythril só tem suporte para sistemas baseados em Linux</i></b></p>
</ul>
<p>O processo de automação das configurações da ferramenta de testes de Smart Contracts chamada Mythril se torna necessário a partir do momento em que os contratos recebem uma grande quantidade de imports, mas também quando precisa-se testar contratos em massa.</p>
<p>O script python myth2json.py automatiza esse processo inteiro de configurações de imports dos contratos em um arquivo temporário, e após utiliza o comando <code>myth analyze <file> -o json --max-depth 25 --solc-json import_assets.json </code> para análise em si do contrato, retornando o tempo da execução no terminal e um arquivo json com a análise do contrato no padrão NomeDoArquivo_analyzed.json. A profundidade de hashes testados imposta <code>--max-depth 25</code> é padrão como 22 mas pode ser alterada com essa definição, que pode ser alterada no código dependendo da necessidade. A definição <code>-o json</code> serve para retornar a análise no formato json, que por padrão é apenas um texto no terminal. A configuração <code>--solc-json import_assets.json</code> serve para apontar o arquivo import_assets.json (que é o arquivo temporário criado pelo script) como os remapeamentos de imports para a análise do contrato.</p>
<p>Para a utilização do script, basta pô-lo no diretório onde encontram-se os contratos a serem analisados e abrí-lo com o comando <code>python3 myth2json.py</code> (Linux). Após a inicialização, haverá uma entrada a ser feita com o nome do contrato (sem incluir a extensão .sol) a se analisar, pode ser utilizada a entrada 0 para que se analise todos os contratos do diretório onde o script se encontra.</p>
<blockquote> <b>A DECIDIR: interface gráfica do script, facilitando ainda mais o processo de testes</b> </blockquote>


<h1 align="center">Análises de Smart Contracts</h1>
<ul>
<h3>Problemas conhecidos</h3>
    <li> Quando um contrato importado por outro usa uma versão diferente de solidity do contrato principal, mythril não completa a análise, retornando um erro no output da análise.</li>
<h3>CryptoKitties</h3>    
    <li><i><b> /contracts/GameVarAndFee.sol: </b></i> Erro com a versão do authority/Owned.sol, todos os contratos usam solidity 0.5.5 e Owned usa 0.5.0. Alterando a sua versão não muda o resultado.</li>
    <li><i><b> /contracts/CronJob.sol: </b></i>Mesmo erro de versão do authority/Owned.sol</li>
    <li><i><b> /contracts/DSNote.sol: </b></i> Nenhum erro foi detectado. Checar DSNote_analyzed.json no repositório. </li>
    <li><i><b> /contracts/authority/Owned.sol: </b></i> Falha identificada - Exception State: an assertion violation was triggered. Checar Owned_analyzed.json no repositorio.</li>
    <li><i><b> /contracts/ethie/EthieToken.sol: </b></i> Falha identificada - Integer Arithmetic Bugs: é possível de se causar overflow ou underflow de números inteiros a partir de operadores aritméticos. Checar EthieToken_analyzed.json no repositório.</li> 
    <li><i><b> /contracts/ </b></i> </li> 
    
</ul>
