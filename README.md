# Mythril-repo
idk just testing



Para rodar <a href="https://mythril-classic.readthedocs.io/en/master/tutorial.html">mythril</a>: ``myth analyze nomedoarquivo.sol``<br><br>
Utilizando o codigo mythril.sol, que nao ha erros, rodando myth no contrato, retorna a seguinte mensagem no terminal: ``The analysis was completed successfully. No issues were detected.``<br><br>
Ao rodar o codigo _mythril.sol com mythril, que ha falhas, retorna o seguinte relatorio:<br>
```==== Exception State ====
SWC ID: 110
Severity: Medium
Contract: Exceptions
Function name: assert1()
PC address: 791
Estimated Gas Usage: 229 - 514
An assertion violation was triggered.
It is possible to trigger an assertion violation. Note that Solidity assert() statements should only be used to check invariants. Review the transaction trace generated for this issue and either make sure your program logic is correct, or use require() instead of assert() if your goal is to constrain user inputs or enforce preconditions. Remember to validate inputs from both callers (for instance, via passed arguments) and callees (for instance, via return values).
--------------------
In file: ./Downloads/_mythril.sol:12

assert(i == 0)

--------------------
Initial State:

Account: [CREATOR], balance: 0x0, nonce:0, storage:{}
Account: [ATTACKER], balance: 0x0, nonce:0, storage:{}

Transaction Sequence:

Caller: [CREATOR], calldata: , decoded_data: , value: 0x0
Caller: [CREATOR], function: assert1(), txdata: 0xb34c3610, value: 0x0

==== Exception State ====
SWC ID: 110
Severity: Medium
Contract: Exceptions
Function name: assert3(uint256)
PC address: 791
Estimated Gas Usage: 504 - 789
An assertion violation was triggered.
It is possible to trigger an assertion violation. Note that Solidity assert() statements should only be used to check invariants. Review the transaction trace generated for this issue and either make sure your program logic is correct, or use require() instead of assert() if your goal is to constrain user inputs or enforce preconditions. Remember to validate inputs from both callers (for instance, via passed arguments) and callees (for instance, via return values).
--------------------
In file: ./Downloads/_mythril.sol:27

assert(input != 23)

--------------------
Initial State:

Account: [CREATOR], balance: 0x0, nonce:0, storage:{}
Account: [ATTACKER], balance: 0x0, nonce:0, storage:{}

Transaction Sequence:

Caller: [CREATOR], calldata: , decoded_data: , value: 0x0
Caller: [ATTACKER], function: assert3(uint256), txdata: 0x546455b50000000000000000000000000000000000000000000000000000000000000017, decoded_data: (23,), value: 0x0
  
``````
