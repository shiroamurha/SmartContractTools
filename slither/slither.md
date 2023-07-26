<a href="https://crytic.github.io/slither/slither.html">slither docs</a>
<p>usage: slither arquivo.sol</p>

<p>É visivel, de acordo com a leitura das análises de mythril e slither, que cada um encontra falhas diferentes no mesmo contrato. slither é extremamente rápido e de mais fácil uso, mas identifica menos falhas, devido a sua profundidade de hashes*. Mythril tem uma análise frequentemente lenta, podendo demorar desde alguns minutos até várias horas, em contrapartida Mythril faz análises profundas nos contratos, identificando mais falhas nos contratos, porém tem um uso um pouco mais difícil, que o script python myth2json facilita.</p>
