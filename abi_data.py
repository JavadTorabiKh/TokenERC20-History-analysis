import json

abi_string = '''
[
   {
      "constant": true,
      "inputs": [],
      "name": "name",
      "outputs": [
         {
            "internalType": "string",
            "name": "",
            "type": "string"
         }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
   },
   {
      "constant": false,
      "inputs": [
         {
            "internalType": "address",
            "name": "spender",
            "type": "address"
         },
         {
            "internalType": "uint256",
            "name": "value",
            "type": "uint256"
         }
      ],
      "name": "approve",
      "outputs": [
         {
            "internalType": "bool",
            "name": "",
            "type": "bool"
         }
      ],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
   },
   {
      "constant": true,
      "inputs": [],
      "name": "totalSupply",
      "outputs": [
         {
            "internalType": "uint256",
            "name": "",
            "type": "uint256"
         }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
   },
   {
      "constant": false,
      "inputs": [
         {
            "internalType": "address",
            "name": "from",
            "type": "address"
         },
         {
            "internalType": "address",
            "name": "to",
            "type": "address"
         },
         {
            "internalType": "uint256",
            "name": "value",
            "type": "uint256"
         }
      ],
      "name": "transferFrom",
      "outputs": [
         {
            "internalType": "bool",
            "name": "",
            "type": "bool"
         }
      ],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
   },
   {
      "constant": true,
      "inputs": [],
      "name": "decimals",
      "outputs": [
         {
            "internalType": "uint8",
            "name": "",
            "type": "uint8"
         }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
   },
   {
      "constant": false,
      "inputs": [
         {
            "internalType": "address",
            "name": "spender",
            "type": "address"
         },
         {
            "internalType": "uint256",
            "name": "addedValue",
            "type": "uint256"
         }
      ],
      "name": "increaseAllowance",
      "outputs": [
         {
            "internalType": "bool",
            "name": "",
            "type": "bool"
         }
      ],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
   },
   {
      "constant": false,
      "inputs": [
         {
            "internalType": "address",
            "name": "to",
            "type": "address"
         },
         {
            "internalType": "uint256",
            "name": "value",
            "type": "uint256"
         }
      ],
      "name": "mint",
      "outputs": [
         {
            "internalType": "bool",
            "name": "",
            "type": "bool"
         }
      ],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
   },
   {
      "constant": true,
      "inputs": [
         {
            "internalType": "address",
            "name": "owner",
            "type": "address"
         }
      ],
      "name": "balanceOf",
      "outputs": [
         {
            "internalType": "uint256",
            "name": "",
            "type": "uint256"
         }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
   },
   {
      "constant": true,
      "inputs": [],
      "name": "symbol",
      "outputs": [
         {
            "internalType": "string",
            "name": "",
            "type": "string"
         }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
   },
   {
      "constant": false,
      "inputs": [
         {
            "internalType": "address",
            "name": "spender",
            "type": "address"
         },
         {
            "internalType": "uint256",
            "name": "subtractedValue",
            "type": "uint256"
         }
      ],
      "name": "decreaseAllowance",
      "outputs": [
         {
            "internalType": "bool",
            "name": "",
            "type": "bool"
         }
      ],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
   },
   {
      "constant": false,
      "inputs": [
         {
            "internalType": "address",
            "name": "to",
            "type": "address"
         },
         {
            "internalType": "uint256",
            "name": "value",
            "type": "uint256"
         }
      ],
      "name": "transfer",
      "outputs": [
         {
            "internalType": "bool",
            "name": "",
            "type": "bool"
         }
      ],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
   },
   {
      "constant": true,
      "inputs": [
         {
            "internalType": "address",
            "name": "owner",
            "type": "address"
         },
         {
            "internalType": "address",
            "name": "spender",
            "type": "address"
         }
      ],
      "name": "allowance",
      "outputs": [
         {
            "internalType": "uint256",
            "name": "",
            "type": "uint256"
         }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
   },
   {
      "inputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "constructor"
   },
   {
      "anonymous": false,
      "inputs": [
         {
            "indexed": true,
            "internalType": "address",
            "name": "from",
            "type": "address"
         },
         {
            "indexed": true,
            "internalType": "address",
            "name": "to",
            "type": "address"
         },
         {
            "indexed": false,
            "internalType": "uint256",
            "name": "value",
            "type": "uint256"
         }
      ],
      "name": "Transfer",
      "type": "event"
   },
   {
      "anonymous": false,
      "inputs": [
         {
            "indexed": true,
            "internalType": "address",
            "name": "owner",
            "type": "address"
         },
         {
            "indexed": true,
            "internalType": "address",
            "name": "spender",
            "type": "address"
         },
         {
            "indexed": false,
            "internalType": "uint256",
            "name": "value",
            "type": "uint256"
         }
      ],
      "name": "Approval",
      "type": "event"
   }
]
'''

abi = json.loads(abi_string)


contract_string = '''
[
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_owner",
				"type": "address"
			}
		],
		"name": "balanceOf",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "balance",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_value",
				"type": "uint256"
			}
		],
		"name": "transfer",
		"outputs": [
			{
				"internalType": "bool",
				"name": "success",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
 {
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "value",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "bytes",
				"name": "data",
				"type": "bytes"
			}
		],
		"name": "ForwarderDeposited",
		"type": "event"
	},
	{
		"stateMutability": "payable",
		"type": "fallback"
	},
	{
		"inputs": [],
		"name": "flush",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "tokenContractAddress",
				"type": "address"
			}
		],
		"name": "flushTokens",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_parentAddress",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_operator",
				"type": "address"
			}
		],
		"name": "init",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "operator",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "parentAddress",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"stateMutability": "payable",
		"type": "receive"
	},
 {
		"inputs": [
			{
				"internalType": "address",
				"name": "_implementationAddress",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "newForwarderAddress",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "parentAddress",
				"type": "address"
			}
		],
		"name": "ForwarderCreated",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "parent",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_operator",
				"type": "address"
			},
			{
				"internalType": "bytes32",
				"name": "salt",
				"type": "bytes32"
			}
		],
		"name": "createForwarder",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "parent",
				"type": "address"
			},
			{
				"internalType": "bytes32",
				"name": "salt",
				"type": "bytes32"
			}
		],
		"name": "getAddress",
		"outputs": [
			{
				"internalType": "address",
				"name": "predicted",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "implementationAddress",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
'''


contract_abi = json.loads(contract_string)
