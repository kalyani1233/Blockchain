from web3 import Web3
import json
#Connect with ganache
ganache_url = "HTTP://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))
# check if it is connected or not
print(web3.isConnected())

# address of contract
address=web3.toChecksumAddress("0xa5cCa05EEaC4BC96964A2645C18f76f089C1ED7E")
# abi of contract
abi=json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"Total","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_a","type":"uint256"},{"internalType":"uint256","name":"_b","type":"uint256"}],"name":"add","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_a","type":"uint256"},{"internalType":"uint256","name":"_b","type":"uint256"}],"name":"div","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getContractBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"manager","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_a","type":"uint256"},{"internalType":"uint256","name":"_b","type":"uint256"}],"name":"mul","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"participant","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"sendEth","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_a","type":"uint256"},{"internalType":"uint256","name":"_b","type":"uint256"}],"name":"sub","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"total","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"value","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]')

contract = web3.eth.contract(address = address,abi = abi)

# call smart contract function
print("Application to  Perform Mathematical Operations:")
print("1:Addition \n 2:Substract\n 3.multiplication\n 4.Division")

while(True):
    # perform all the arithmetic operations
    choice = int(input("Enter your choice:"))
    val1 = int(input("Enter value 1:"))
    val2 = int(input("Enter value 2:"))
    if (choice ==1):
        print("Addition is :", contract.functions.add(val1, val2).call())
    elif(choice ==2):
        print("Subtraction is :", contract.functions.sub(val1, val2).call())
    elif(choice==3):
        print("Multiplication is :", contract.functions.mul(val1, val2).call())
    elif(choice==4):
        print("Division is:", contract.functions.div(val1, val2).call())
    else:
        print("Invalid Choice:")
        ip=input("Do you want to continue? yes/no:")
        if ip=="no":break
    ip = input("Do you want to continue? yes/no:")
    if ip == "no": break







