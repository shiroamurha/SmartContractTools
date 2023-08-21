Summary
 - [uninitialized-state](#uninitialized-state) (1 results) (High)
 - [function-init-state](#function-init-state) (1 results) (Informational)
 - [solc-version](#solc-version) (2 results) (Informational)
 - [naming-convention](#naming-convention) (3 results) (Informational)
 - [unused-state](#unused-state) (2 results) (Informational)
 - [constable-states](#constable-states) (4 results) (Optimization)
 - [external-function](#external-function) (1 results) (Optimization)
## uninitialized-state
Impact: High
Confidence: High
 - [ ] ID-0
[BCS.owner](SimpleBCS.sol#L6) is never initialized. It is used in:

SimpleBCS.sol#L6


## function-init-state
Impact: Informational
Confidence: High
 - [ ] ID-1
[BCS.productModulus](SimpleBCS.sol#L25) is set pre-construction with a non-constant function or state variable:
	- 10 ** productDigit

SimpleBCS.sol#L25


## solc-version
Impact: Informational
Confidence: High
 - [ ] ID-2
solc-0.4.18 is not recommended for deployment

 - [ ] ID-3
Pragma version[^0.4.18](SimpleBCS.sol#L3) allows old versions

SimpleBCS.sol#L3


## naming-convention
Impact: Informational
Confidence: High
 - [ ] ID-4
Parameter [BCS.createProduct(address,string,uint256)._ownerProduct](SimpleBCS.sol#L37) is not in mixedCase

SimpleBCS.sol#L37


 - [ ] ID-5
Parameter [BCS.createProduct(address,string,uint256)._productPrice](SimpleBCS.sol#L37) is not in mixedCase

SimpleBCS.sol#L37


 - [ ] ID-6
Parameter [BCS.createProduct(address,string,uint256)._productName](SimpleBCS.sol#L37) is not in mixedCase

SimpleBCS.sol#L37


## unused-state
Impact: Informational
Confidence: High
 - [ ] ID-7
[BCS.userItemsId](SimpleBCS.sol#L12) is never used in [BCS](SimpleBCS.sol#L5-L48)

SimpleBCS.sol#L12


 - [ ] ID-8
[BCS.itemIdUserOwner](SimpleBCS.sol#L13) is never used in [BCS](SimpleBCS.sol#L5-L48)

SimpleBCS.sol#L13


## constable-states
Impact: Optimization
Confidence: High
 - [ ] ID-9
[BCS.seller](SimpleBCS.sol#L7) should be constant 

SimpleBCS.sol#L7


 - [ ] ID-10
[BCS.productDigit](SimpleBCS.sol#L24) should be constant 

SimpleBCS.sol#L24


 - [ ] ID-11
[BCS.buyer](SimpleBCS.sol#L8) should be constant 

SimpleBCS.sol#L8


 - [ ] ID-12
[BCS.owner](SimpleBCS.sol#L6) should be constant 

SimpleBCS.sol#L6


## external-function
Impact: Optimization
Confidence: High
 - [ ] ID-13
createProduct(address,string,uint256) should be declared external:
	- [BCS.createProduct(address,string,uint256)](SimpleBCS.sol#L37-L41)

SimpleBCS.sol#L37-L41


