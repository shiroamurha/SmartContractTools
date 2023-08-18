Summary
 - [missing-zero-check](#missing-zero-check) (1 results) (Low)
 - [reentrancy-benign](#reentrancy-benign) (1 results) (Low)
 - [solc-version](#solc-version) (3 results) (Informational)
## missing-zero-check
Impact: Low
Confidence: Medium
 - [ ] ID-0
[DSAuth.setOwner(address).owner_](DSAuth.sol#L36) lacks a zero-check on :
		- [owner = owner_](DSAuth.sol#L40)

DSAuth.sol#L36


## reentrancy-benign
Impact: Low
Confidence: Medium
 - [ ] ID-1
Reentrancy in [DSGuardFactory.newGuard()](DSGuard.sol#L79-L83):
	External calls:
	- [guard.setOwner(msg.sender)](DSGuard.sol#L81)
	State variables written after the call(s):
	- [isGuard[address(guard)] = true](DSGuard.sol#L82)

DSGuard.sol#L79-L83


## solc-version
Impact: Informational
Confidence: High
 - [ ] ID-2
Pragma version[>=0.4.23](DSGuard.sol#L18) allows old versions

DSGuard.sol#L18


 - [ ] ID-3
Pragma version[>=0.4.23](DSAuth.sol#L14) allows old versions

DSAuth.sol#L14


 - [ ] ID-4
solc-0.5.5 is known to contain severe issues (https://solidity.readthedocs.io/en/latest/bugs.html)
