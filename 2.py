from web3 import Web3, HTTPProvider
from detail_eth import detail_contract, detail_method
from openpyxl import Workbook
import threading


w3 = Web3(HTTPProvider('https://mainnet.infura.io/v3/cc1dea670fb5488eb123c82350ed8944'))
if w3.is_connected():
    print("Connected to Ethereum node")
else:
    print("Failed to connect to Ethereum node")


wb = Workbook()
ws = wb.active
ws.append(['from', 'to', 'token','amount' , 'block' ,'timeStamp','Method'])


def decoder(input):

    method = detail_method[input[:10]]
    to_addrs = f'0x{input[34:74]}'
    amount = int(f'0x{input[74:]}', 16)

    decode = [{"method": method, "to_addrs": to_addrs, "amount": amount}]
    return decode



def write_data (data):
    
    for item in data:
        ws.append([item[1]["from"], item[0]["to_addrs"], item[1]["Token"], item[0]["amount"], item[1]["block number"],item[1]["timestamp"], item[0]["method"]])
   
    wb.save("data.xlsx")



def get_tx_data(block_number, contract_address, method):
    Data = []
    block = w3.eth.get_block(block_number, full_transactions=True)
    
    for tx in block['transactions']:

        if tx['to'] == contract_address and tx['input'] != "0x" and tx["input"][:10] == method:

            blockData = {"from": tx["from"], "Token": detail_contract[contract_address],
                         "block number": tx["blockNumber"], "chainId": tx["chainId"], "timestamp": block.timestamp}
            list_decode = decoder(tx["input"])
            list_decode.append(blockData)
            Data.append(list_decode)

    write_data(Data)



block_number = 17576705

def my_code():
    global block_number
    while True:
        get_tx_data(block_number, '0xB8c77482e45F1F44dE1745F52C74426C631bDD52', "0xa9059cbb")
        block_number += 1

for i in range(5):
    t = threading.Thread(target=my_code)
    t.start()