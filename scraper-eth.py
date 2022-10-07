from web3 import Web3

print("Hello World")

w3_http = Web3(Web3.HTTPProvider('https://rpc.ankr.com/eth'))
print(w3_http.isConnected())