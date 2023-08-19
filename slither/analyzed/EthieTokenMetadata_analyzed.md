Summary
 - [shadowing-local](#shadowing-local) (3 results) (Low)
 - [assembly](#assembly) (2 results) (Informational)
 - [pragma](#pragma) (1 results) (Informational)
 - [dead-code](#dead-code) (16 results) (Informational)
 - [solc-version](#solc-version) (13 results) (Informational)
 - [low-level-calls](#low-level-calls) (2 results) (Informational)
 - [naming-convention](#naming-convention) (1 results) (Informational)
 - [redundant-statements](#redundant-statements) (1 results) (Informational)
 - [external-function](#external-function) (1 results) (Optimization)
## shadowing-local
Impact: Low
Confidence: High
 - [ ] ID-0
[EthieTokenMetadata._setBaseURI(string).baseURI](EthieTokenMetadata.sol#L83) shadows:
	- [EthieTokenMetadata.baseURI()](EthieTokenMetadata.sol#L94-L96) (function)

EthieTokenMetadata.sol#L83


 - [ ] ID-1
[EthieTokenMetadata.constructor(string,string).name](EthieTokenMetadata.sol#L39) shadows:
	- [EthieTokenMetadata.name()](EthieTokenMetadata.sol#L51-L53) (function)
	- [IERC721Metadata.name()](../libs/openzeppelin_v2_5_0/token/ERC721/IERC721Metadata.sol#L10) (function)

EthieTokenMetadata.sol#L39


 - [ ] ID-2
[EthieTokenMetadata.constructor(string,string).symbol](EthieTokenMetadata.sol#L39) shadows:
	- [EthieTokenMetadata.symbol()](EthieTokenMetadata.sol#L59-L61) (function)
	- [IERC721Metadata.symbol()](../libs/openzeppelin_v2_5_0/token/ERC721/IERC721Metadata.sol#L11) (function)

EthieTokenMetadata.sol#L39


## assembly
Impact: Informational
Confidence: High
 - [ ] ID-3
[ERC721._checkOnERC721Received(address,address,uint256,bytes)](../libs/openzeppelin_v2_5_0/token/ERC721/ERC721.sol#L327-L355) uses assembly
	- [INLINE ASM](../libs/openzeppelin_v2_5_0/token/ERC721/ERC721.sol#L344-L348)

../libs/openzeppelin_v2_5_0/token/ERC721/ERC721.sol#L327-L355


 - [ ] ID-4
[Address.isContract(address)](../libs/openzeppelin_v2_5_0/utils/Address.sol#L24-L33) uses assembly
	- [INLINE ASM](../libs/openzeppelin_v2_5_0/utils/Address.sol#L31-L32)

../libs/openzeppelin_v2_5_0/utils/Address.sol#L24-L33


## pragma
Impact: Informational
Confidence: High
 - [ ] ID-5
Different versions of Solidity are used:
	- Version used: ['^0.5.0', '^0.5.5']
	- [^0.5.0](../libs/openzeppelin_v2_5_0/GSN/Context.sol#L1)
	- [^0.5.0](../libs/openzeppelin_v2_5_0/drafts/Counters.sol#L1)
	- [^0.5.0](../libs/openzeppelin_v2_5_0/introspection/ERC165.sol#L1)
	- [^0.5.0](../libs/openzeppelin_v2_5_0/introspection/IERC165.sol#L1)
	- [^0.5.0](../libs/openzeppelin_v2_5_0/math/SafeMath.sol#L1)
	- [^0.5.0](../libs/openzeppelin_v2_5_0/token/ERC721/ERC721.sol#L1)
	- [^0.5.0](../libs/openzeppelin_v2_5_0/token/ERC721/IERC721.sol#L1)
	- [^0.5.0](../libs/openzeppelin_v2_5_0/token/ERC721/IERC721Metadata.sol#L1)
	- [^0.5.0](../libs/openzeppelin_v2_5_0/token/ERC721/IERC721Receiver.sol#L1)
	- [^0.5.5](EthieTokenMetadata.sol#L1)
	- [^0.5.5](../libs/StringUtils.sol#L1)
	- [^0.5.5](../libs/openzeppelin_v2_5_0/utils/Address.sol#L1)

../libs/openzeppelin_v2_5_0/GSN/Context.sol#L1


## dead-code
Impact: Informational
Confidence: Medium
 - [ ] ID-6
[SafeMath.mul(uint256,uint256)](../libs/openzeppelin_v2_5_0/math/SafeMath.sol#L73-L85) is never used and should be removed

../libs/openzeppelin_v2_5_0/math/SafeMath.sol#L73-L85


 - [ ] ID-7
[Address.sendValue(address,uint256)](../libs/openzeppelin_v2_5_0/utils/Address.sol#L63-L69) is never used and should be removed

../libs/openzeppelin_v2_5_0/utils/Address.sol#L63-L69


 - [ ] ID-8
[SafeMath.add(uint256,uint256)](../libs/openzeppelin_v2_5_0/math/SafeMath.sol#L26-L31) is never used and should be removed

../libs/openzeppelin_v2_5_0/math/SafeMath.sol#L26-L31


 - [ ] ID-9
[EthieTokenMetadata._setBaseURI(string)](EthieTokenMetadata.sol#L83-L85) is never used and should be removed

EthieTokenMetadata.sol#L83-L85


 - [ ] ID-10
[ERC721._burn(uint256)](../libs/openzeppelin_v2_5_0/token/ERC721/ERC721.sol#L291-L293) is never used and should be removed

../libs/openzeppelin_v2_5_0/token/ERC721/ERC721.sol#L291-L293


 - [ ] ID-11
[SafeMath.mod(uint256,uint256,string)](../libs/openzeppelin_v2_5_0/math/SafeMath.sol#L152-L155) is never used and should be removed

../libs/openzeppelin_v2_5_0/math/SafeMath.sol#L152-L155


 - [ ] ID-12
[StringUtils.fromUint256(uint256,uint256,uint256)](../libs/StringUtils.sol#L40-L78) is never used and should be removed

../libs/StringUtils.sol#L40-L78


 - [ ] ID-13
[SafeMath.div(uint256,uint256,string)](../libs/openzeppelin_v2_5_0/math/SafeMath.sol#L115-L122) is never used and should be removed

../libs/openzeppelin_v2_5_0/math/SafeMath.sol#L115-L122


 - [ ] ID-14
[Context._msgData()](../libs/openzeppelin_v2_5_0/GSN/Context.sol#L23-L26) is never used and should be removed

../libs/openzeppelin_v2_5_0/GSN/Context.sol#L23-L26


 - [ ] ID-15
[Address.toPayable(address)](../libs/openzeppelin_v2_5_0/utils/Address.sol#L41-L43) is never used and should be removed

../libs/openzeppelin_v2_5_0/utils/Address.sol#L41-L43


 - [ ] ID-16
[SafeMath.mod(uint256,uint256)](../libs/openzeppelin_v2_5_0/math/SafeMath.sol#L135-L137) is never used and should be removed

../libs/openzeppelin_v2_5_0/math/SafeMath.sol#L135-L137


 - [ ] ID-17
[ERC721._safeMint(address,uint256,bytes)](../libs/openzeppelin_v2_5_0/token/ERC721/ERC721.sol#L247-L250) is never used and should be removed

../libs/openzeppelin_v2_5_0/token/ERC721/ERC721.sol#L247-L250


 - [ ] ID-18
[SafeMath.div(uint256,uint256)](../libs/openzeppelin_v2_5_0/math/SafeMath.sol#L98-L100) is never used and should be removed

../libs/openzeppelin_v2_5_0/math/SafeMath.sol#L98-L100


 - [ ] ID-19
[ERC721._mint(address,uint256)](../libs/openzeppelin_v2_5_0/token/ERC721/ERC721.sol#L258-L266) is never used and should be removed

../libs/openzeppelin_v2_5_0/token/ERC721/ERC721.sol#L258-L266


 - [ ] ID-20
[ERC721._burn(address,uint256)](../libs/openzeppelin_v2_5_0/token/ERC721/ERC721.sol#L275-L284) is never used and should be removed

../libs/openzeppelin_v2_5_0/token/ERC721/ERC721.sol#L275-L284


 - [ ] ID-21
[ERC721._safeMint(address,uint256)](../libs/openzeppelin_v2_5_0/token/ERC721/ERC721.sol#L232-L234) is never used and should be removed

../libs/openzeppelin_v2_5_0/token/ERC721/ERC721.sol#L232-L234


## solc-version
Impact: Informational
Confidence: High
 - [ ] ID-22
Pragma version[^0.5.5](../libs/openzeppelin_v2_5_0/utils/Address.sol#L1) is known to contain severe issues (https://solidity.readthedocs.io/en/latest/bugs.html)

../libs/openzeppelin_v2_5_0/utils/Address.sol#L1


 - [ ] ID-23
Pragma version[^0.5.0](../libs/openzeppelin_v2_5_0/token/ERC721/IERC721.sol#L1) allows old versions

../libs/openzeppelin_v2_5_0/token/ERC721/IERC721.sol#L1


 - [ ] ID-24
Pragma version[^0.5.0](../libs/openzeppelin_v2_5_0/drafts/Counters.sol#L1) allows old versions

../libs/openzeppelin_v2_5_0/drafts/Counters.sol#L1


 - [ ] ID-25
Pragma version[^0.5.0](../libs/openzeppelin_v2_5_0/introspection/ERC165.sol#L1) allows old versions

../libs/openzeppelin_v2_5_0/introspection/ERC165.sol#L1


 - [ ] ID-26
Pragma version[^0.5.0](../libs/openzeppelin_v2_5_0/GSN/Context.sol#L1) allows old versions

../libs/openzeppelin_v2_5_0/GSN/Context.sol#L1


 - [ ] ID-27
Pragma version[^0.5.0](../libs/openzeppelin_v2_5_0/token/ERC721/IERC721Receiver.sol#L1) allows old versions

../libs/openzeppelin_v2_5_0/token/ERC721/IERC721Receiver.sol#L1


 - [ ] ID-28
Pragma version[^0.5.5](EthieTokenMetadata.sol#L1) is known to contain severe issues (https://solidity.readthedocs.io/en/latest/bugs.html)

EthieTokenMetadata.sol#L1


 - [ ] ID-29
Pragma version[^0.5.0](../libs/openzeppelin_v2_5_0/token/ERC721/IERC721Metadata.sol#L1) allows old versions

../libs/openzeppelin_v2_5_0/token/ERC721/IERC721Metadata.sol#L1


 - [ ] ID-30
Pragma version[^0.5.0](../libs/openzeppelin_v2_5_0/token/ERC721/ERC721.sol#L1) allows old versions

../libs/openzeppelin_v2_5_0/token/ERC721/ERC721.sol#L1


 - [ ] ID-31
solc-0.5.5 is known to contain severe issues (https://solidity.readthedocs.io/en/latest/bugs.html)
 - [ ] ID-32
Pragma version[^0.5.0](../libs/openzeppelin_v2_5_0/introspection/IERC165.sol#L1) allows old versions

../libs/openzeppelin_v2_5_0/introspection/IERC165.sol#L1


 - [ ] ID-33
Pragma version[^0.5.5](../libs/StringUtils.sol#L1) is known to contain severe issues (https://solidity.readthedocs.io/en/latest/bugs.html)

../libs/StringUtils.sol#L1


 - [ ] ID-34
Pragma version[^0.5.0](../libs/openzeppelin_v2_5_0/math/SafeMath.sol#L1) allows old versions

../libs/openzeppelin_v2_5_0/math/SafeMath.sol#L1


## low-level-calls
Impact: Informational
Confidence: High
 - [ ] ID-35
Low level call in [ERC721._checkOnERC721Received(address,address,uint256,bytes)](../libs/openzeppelin_v2_5_0/token/ERC721/ERC721.sol#L327-L355):
	- [(success,returndata) = to.call(abi.encodeWithSelector(IERC721Receiver(to).onERC721Received.selector,_msgSender(),from,tokenId,_data))](../libs/openzeppelin_v2_5_0/token/ERC721/ERC721.sol#L334-L340)

../libs/openzeppelin_v2_5_0/token/ERC721/ERC721.sol#L327-L355


 - [ ] ID-36
Low level call in [Address.sendValue(address,uint256)](../libs/openzeppelin_v2_5_0/utils/Address.sol#L63-L69):
	- [(success) = recipient.call.value(amount)()](../libs/openzeppelin_v2_5_0/utils/Address.sol#L67)

../libs/openzeppelin_v2_5_0/utils/Address.sol#L63-L69


## naming-convention
Impact: Informational
Confidence: High
 - [ ] ID-37
Parameter [ERC721.safeTransferFrom(address,address,uint256,bytes)._data](../libs/openzeppelin_v2_5_0/token/ERC721/ERC721.sol#L177) is not in mixedCase

../libs/openzeppelin_v2_5_0/token/ERC721/ERC721.sol#L177


## redundant-statements
Impact: Informational
Confidence: High
 - [ ] ID-38
Redundant expression "[this](../libs/openzeppelin_v2_5_0/GSN/Context.sol#L24)" in[Context](../libs/openzeppelin_v2_5_0/GSN/Context.sol#L13-L27)

../libs/openzeppelin_v2_5_0/GSN/Context.sol#L24


## external-function
Impact: Optimization
Confidence: High
 - [ ] ID-39
onERC721Received(address,address,uint256,bytes) should be declared external:
	- [IERC721Receiver.onERC721Received(address,address,uint256,bytes)](../libs/openzeppelin_v2_5_0/token/ERC721/IERC721Receiver.sol#L23-L24)
Moreover, the following function parameters should change its data location:
data location should be calldata

../libs/openzeppelin_v2_5_0/token/ERC721/IERC721Receiver.sol#L23-L24


