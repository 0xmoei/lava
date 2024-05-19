# Import necessary dependencies
import time
import requests
import random

# Ethereum mainnet RPC endpoint
# TODO: input your Ethereum RPC here.
rpc_endpoint = 'https://eth1.lava.build/lava-referer-bbfb8dbe-46d5-41ce-a634-d7ea02fed7bf/'

# Wallet address (0x format) that we will check the balance for
# TODO: Input your wallet address
wallet_address = '0x76b0989Eb48E8cCc4c024564b15Cd209868a9179'

# txs counter
tx_counter = 0

#
# @param {wallet_address}: String. - Wallet address that we will check the balance for
# @returns {balance_wei}: Int - The correspending balance of the given address in Wei format
#
def get_balance(wallet_address):
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBalance",
        "params": [wallet_address, "latest"],
        "id": 1
    }
    response = requests.post(rpc_endpoint, json=payload)
    balance_hex = response.json()['result']
    balance_wei = int(balance_hex, 16)
    return balance_wei

def check_balance():
    # Get the balance of the wallet address
    balance_wei = get_balance(wallet_address)
    
    # Convert balance from Wei to Ether
    balance_in_ether = balance_wei / 1e18
    
    print(f'Wallet Address: {wallet_address}')
    print(f'Balance: {balance_in_ether} ETH')

while True:
    # Increase the transaction coutner
    tx_counter = tx_counter + 1
    print(f"Transaction no. {tx_counter}")

    try:
        check_balance()
    except Exception as e:
        print("An error occurred:", e)
    
    # Generate a random delay between 60 and 90 seconds
    random_delay = random.randint(60, 90)
    print(f"Waiting for {random_delay} seconds...")

    # Wait for the random delay finish before looping again
    time.sleep(random_delay) 
