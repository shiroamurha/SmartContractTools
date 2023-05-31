pragma solidity ^0.8.7;
//SPDX-License-Identifier: UNLICENSED

contract String1{
	string palavra;

	function get() view public returns(string memory){
    		return palavra;
	}
	function set(string memory pal) public	{
    		palavra = pal;
	}
}


// contract HelloWorld {
//     string public message;

//     constructor() {
//         message = "Ola Mundo";
//     }

//     function getMessage() public view returns (string memory) {
//         return message;
//     }
// }