from web3 import Web3
# we are transfering eth from one account to another account

ganache_url="http://127.0.0.1:7545"
web3=Web3(Web3.HTTPProvider(ganache_url))
account_1="0xf7899BB224964C8A2807352c57cc954CA48e0581"
private_key1="9cd8ccbd12d94d877223273b9b953a0c5994a564b1fc0430d7b6808adbda0500"
account_2="0xc3818ADDbE04b961DB058427BF4102D807830B97"

# get the nonce
nonce=web3.eth.getTransactionCount(account_1)
tx={
    'nonce':nonce,
    'to':account_2,
    'value': web3.toWei(2,'ether'),
    'gas':2000000,
    'gasPrice':web3.toWei('50','gwei')

}
# sign the transaction
signed_tx =web3.eth.account.sign_transaction(tx,private_key1)

tx_hash=web3.eth.sendRawTransaction(signed_tx.rawTransaction)
# get transaction
print(web3.toHex(tx_hash))