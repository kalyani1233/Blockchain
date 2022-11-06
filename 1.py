# import web3.py
from web3 import Web3

#Connect with ganache
ganache_url = "HTTP://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))

# check if it is connected or not
print(web3.isConnected())
# to get the block number
print(web3.eth.blockNumber)

# account address stored
account="0xD6974F5D4e7Bd7eA58Af736be91d3f4AA47A5Ffd"

# to get balance from that account
balance = web3.eth.getBalance(account)
print(web3.fromWei(balance,"ether"))
