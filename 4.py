from web3 import Web3
import json
import requests

ganache_url="http://127.0.0.1:7545"
web3=Web3(Web3.HTTPProvider(ganache_url))

req=requests.get('https://ethgasstation.info/json/ethgasAPI.json')
t=json.loads(req.content)
print('safeLow',t['safeLow'])
print('average',t['average'])
print('fast',t['fast'])
print('fastest',t['fastest'])

gas_price1=web3.eth.gasPrice
print(gas_price1/10**8)