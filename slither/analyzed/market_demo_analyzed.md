Summary
 - [controlled-array-length](#controlled-array-length) (3 results) (High)
 - [solc-version](#solc-version) (2 results) (Informational)
 - [naming-convention](#naming-convention) (15 results) (Informational)
 - [reentrancy-unlimited-gas](#reentrancy-unlimited-gas) (1 results) (Informational)
 - [too-many-digits](#too-many-digits) (1 results) (Informational)
 - [unused-state](#unused-state) (1 results) (Informational)
 - [constable-states](#constable-states) (1 results) (Optimization)
 - [external-function](#external-function) (1 results) (Optimization)
## controlled-array-length
Impact: High
Confidence: Medium
 - [ ] ID-0
[market](market_demo.sol#L2-L106) contract sets array length with a user-controlled value:
	- [assets.push(Asset(idAssest,_name,msg.sender,_price,true))](market_demo.sol#L64)

market_demo.sol#L2-L106


 - [ ] ID-1
[market](market_demo.sol#L2-L106) contract sets array length with a user-controlled value:
	- [rate[msg.sender].push(_seller)](market_demo.sol#L95)

market_demo.sol#L2-L106


 - [ ] ID-2
[market](market_demo.sol#L2-L106) contract sets array length with a user-controlled value:
	- [userItemsIds[msg.sender].push(_idAssest)](market_demo.sol#L61)

market_demo.sol#L2-L106


## solc-version
Impact: Informational
Confidence: High
 - [ ] ID-3
solc-0.4.22 is known to contain severe issues (https://solidity.readthedocs.io/en/latest/bugs.html)
 - [ ] ID-4
Pragma version[^0.4.22](market_demo.sol#L1) is known to contain severe issues (https://solidity.readthedocs.io/en/latest/bugs.html)

market_demo.sol#L1


## naming-convention
Impact: Informational
Confidence: High
 - [ ] ID-5
Parameter [market.rating(address)._seller](market_demo.sol#L85) is not in mixedCase

market_demo.sol#L85


 - [ ] ID-6
Event [market.showId(uint256)](market_demo.sol#L5) is not in CapWords

market_demo.sol#L5


 - [ ] ID-7
Parameter [market.getItemInfo(uint256)._itemId](market_demo.sol#L77) is not in mixedCase

market_demo.sol#L77


 - [ ] ID-8
Contract [market](market_demo.sol#L2-L106) is not in CapWords

market_demo.sol#L2-L106


 - [ ] ID-9
Parameter [market.createAsset(string,uint256)._name](market_demo.sol#L63) is not in mixedCase

market_demo.sol#L63


 - [ ] ID-10
Parameter [market.changePrice(uint256,uint256)._newPrice](market_demo.sol#L81) is not in mixedCase

market_demo.sol#L81


 - [ ] ID-11
Parameter [market.getUserVote(address)._userAddress](market_demo.sol#L98) is not in mixedCase

market_demo.sol#L98


 - [ ] ID-12
Parameter [market.buy(uint256)._idAssest](market_demo.sol#L30) is not in mixedCase

market_demo.sol#L30


 - [ ] ID-13
Parameter [market.changePrice(uint256,uint256)._idAssest](market_demo.sol#L81) is not in mixedCase

market_demo.sol#L81


 - [ ] ID-14
Event [market.listUser(string,address)](market_demo.sol#L4) is not in CapWords

market_demo.sol#L4


 - [ ] ID-15
Parameter [market.getUserItems(address)._userAddress](market_demo.sol#L73) is not in mixedCase

market_demo.sol#L73


 - [ ] ID-16
Parameter [market.setToSale(uint256,uint256)._idAssest](market_demo.sol#L101) is not in mixedCase

market_demo.sol#L101


 - [ ] ID-17
Parameter [market.setToSale(uint256,uint256)._price](market_demo.sol#L101) is not in mixedCase

market_demo.sol#L101


 - [ ] ID-18
Event [market.listAssets(string,uint256)](market_demo.sol#L3) is not in CapWords

market_demo.sol#L3


 - [ ] ID-19
Parameter [market.createAsset(string,uint256)._price](market_demo.sol#L63) is not in mixedCase

market_demo.sol#L63


## reentrancy-unlimited-gas
Impact: Informational
Confidence: Medium
 - [ ] ID-20
Reentrancy in [market.buy(uint256)](market_demo.sol#L30-L62):
	External calls:
	- [assets[_idAssest].idOwner.transfer(toCoin)](market_demo.sol#L41)
	State variables written after the call(s):
	- [assets[_idAssest].idOwner = msg.sender](market_demo.sol#L58)
	- [assets[_idAssest].forSale = false](market_demo.sol#L59)
	- [delete (userItemsIds[assets[_idAssest].idOwner])](market_demo.sol#L56)
	- [(userItemsIds[assets[_idAssest].idOwner]) = temp](market_demo.sol#L57)
	- [userItemsIds[msg.sender].push(_idAssest)](market_demo.sol#L61)

market_demo.sol#L30-L62


## too-many-digits
Impact: Informational
Confidence: Medium
 - [ ] ID-21
[market.buy(uint256)](market_demo.sol#L30-L62) uses literals with too many digits:
	- [toCoin = assets[_idAssest].price * 100000000 * 99 / 100](market_demo.sol#L39)

market_demo.sol#L30-L62


## unused-state
Impact: Informational
Confidence: High
 - [ ] ID-22
[market.idUser](market_demo.sol#L7) is never used in [market](market_demo.sol#L2-L106)

market_demo.sol#L7


## constable-states
Impact: Optimization
Confidence: High
 - [ ] ID-23
[market.idUser](market_demo.sol#L7) should be constant 

market_demo.sol#L7


## external-function
Impact: Optimization
Confidence: High
 - [ ] ID-24
createAsset(string,uint256) should be declared external:
	- [market.createAsset(string,uint256)](market_demo.sol#L63-L68)

market_demo.sol#L63-L68


