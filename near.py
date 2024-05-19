# Import necessary dependencies
import requests
import random
import time  

# NEAR Mainnet RPC endpoint
# TODO: input your NEAR Mainnet RPC here.
near_rpc_endpoint = 'https://near.lava.build/lava-referer-bbfb8dbe-46d5-41ce-a634-d7ea02fed7bf/'

# NEAR account ID to check balance in Hexadecimal format.
# YOUr WALLET NEEDS SOME NEAR, OTHERWISE IT'LL RETURN ERROR!!!!!
# TODO: input your NEAR account ID here.
account_id = 'hansforyou.near'

# txs counter
tx_counter = 0

#
# @param {wallet_address}: String. - Wallet address that we will check the balance for
# @returns {balance_wei}: Int - The correspending balance of the given address
#
def get_balance(account_id):
    payload = {
        "jsonrpc": "2.0",
        "method": "query",
        "params": {
            "request_type": "view_account",
            "finality": "final",
            "account_id": account_id
        },
        "id": "1"
    }
    response = requests.post(near_rpc_endpoint, json=payload)
    data = response.json()
    if 'result' in data:
        return data['result']['amount']
    else:
        return None

while True:
    tx_counter = tx_counter + 1
    print(f"transaction no. {tx_counter}")

    try:
        balance = get_balance(account_id)
        if balance is not None:
            print(f'Account ID: {account_id}')
            print(f'Balance: {balance} NEAR')
        else:
            print(f'Failed to retrieve balance for account: {account_id}')
    except Exception as e:
        print("An error occurred:", e)

    # Generate a random delay between 60 and 90 seconds
    random_delay = random.randint(60, 90)
    print(f"Waiting for {random_delay} seconds...")
    
  # Wait for the random delay before looping again
    time.sleep(random_delay)
