Summary
 - [missing-zero-check](#missing-zero-check) (1 results) (Low)
 - [solc-version](#solc-version) (2 results) (Informational)
## missing-zero-check
Impact: Low
Confidence: Medium
 - [ ] ID-0
[DSAuth.setOwner(address).owner_](DSAuth.sol#L36) lacks a zero-check on :
		- [owner = owner_](DSAuth.sol#L40)

DSAuth.sol#L36


## solc-version
Impact: Informational
Confidence: High
 - [ ] ID-1
Pragma version[>=0.4.23](DSAuth.sol#L14) allows old versions

DSAuth.sol#L14


 - [ ] ID-2
solc-0.5.5 is known to contain severe issues (https://solidity.readthedocs.io/en/latest/bugs.html)
