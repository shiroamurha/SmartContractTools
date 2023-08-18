Summary
 - [events-access](#events-access) (1 results) (Low)
 - [solc-version](#solc-version) (2 results) (Informational)
## events-access
Impact: Low
Confidence: Medium
 - [ ] ID-0
[Owned.transferOwnership(address)](Owned.sol#L12-L16) should emit an event for: 
	- [owner = newOwner](Owned.sol#L14) 

Owned.sol#L12-L16


## solc-version
Impact: Informational
Confidence: High
 - [ ] ID-1
solc-0.5.5 is known to contain severe issues (https://solidity.readthedocs.io/en/latest/bugs.html)
 - [ ] ID-2
Pragma version[^0.5.0](Owned.sol#L1) allows old versions

Owned.sol#L1


