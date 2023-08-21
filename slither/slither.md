<a href="https://crytic.github.io/slither/slither.html">slither docs</a>
<p>usage:<br>
<code>> py slither2md.py</code> <br>
<code>> nomedoarquivo</code> (sem .sol)
</p>

<p>Problemas conhecidos: 
  <ul>
    <li>imports de contratos com versões diferentes do contrato sendo testado, em ambas ferramentas, levanta um erro no compilador de Solidity.</li>
    <li>de vez em quando rodar slither com o prefixo que faz os imports funcionarem as vezes faz os imports não funcionarem (?????), para resolver basta não usar o prefixo do diretório.</li>
  </ul>
</p>
<p>É visivel, de acordo com a leitura das análises de mythril e slither, que cada um encontra falhas diferentes no mesmo contrato. slither é extremamente rápido e de mais fácil uso, mas identifica menos falhas, devido a sua profundidade de exploração de estados. Mythril tem uma análise frequentemente lenta, podendo demorar desde alguns minutos até várias horas, em contrapartida Mythril faz análises profundas nos contratos, identificando mais falhas nos contratos, porém tem um uso um pouco mais difícil, que o script python myth2json facilita.</p>
<p>Slither se mostra como uma ferramenta de testes rápidos, não muito profunda mas bastante informacional. Diversas das outputs das analises são sobre melhorias abstratas no código como nomenclatura de variáveis. Ademais, Slither provê uma extensa documentação sobre as vulnerabilidades, explicando como elas acontecem. Essa ferramenta, pelas caracteristicas descritas, se encaixa muito bem como uma ferramenta a ser utilizada durante o desenvolvimento intermediário de smart contracts. </p>
