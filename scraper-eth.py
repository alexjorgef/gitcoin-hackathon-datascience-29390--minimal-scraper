import asyncio
import json
import requests
import logging

from web3 import Web3
from websockets import connect
from web3.exceptions import TransactionNotFound

logger = logging.getLogger(__name__)

eth_http_endpoint = 'https://rpc.ankr.com/eth'
eth_ws_endpoint = 'wss://main-light.eth.linkpool.io/ws'
eth_infura_http_endpoint = 'https://mainnet.infura.io/v3/d7763e66dcdb4d7286f471a429e4cc24'
eth_infura_ws_endpoint = 'wss://mainnet.infura.io/ws/v3/d7763e66dcdb4d7286f471a429e4cc24'

account = '0xde30da39c46104798bb5aa3fe8b9e0e1f348163f'

w3_http = Web3(Web3.HTTPProvider(eth_infura_http_endpoint))
w3 = Web3(Web3.WebsocketProvider(eth_infura_ws_endpoint))

# Subscribing to Pending Transactions
async def get_pending_txs():
    # Prevent error 1006: https://stackoverflow.com/a/58993145/2042014
    async with connect(eth_infura_ws_endpoint, ping_interval=None) as ws:
        await ws.send('{"jsonrpc": "2.0", "id": 1, "method": "eth_subscribe", "params": ["newPendingTransactions"]}')
        subscription_response = await ws.recv()
        print(subscription_response)

        while True:
            try:
                message = await asyncio.wait_for(ws.recv(), timeout=15)
                response = json.loads(message)
                txHash = response['params']['result']
                try:
                    tx = w3_http.eth.get_transaction(txHash)
                    if tx.to == account:
                        print(txHash)
                        print({
                            "hash": txHash,
                            "from": tx["from"],
                            "value": Web3.fromWei(tx["value"], 'ether')
                        })
                    else:
                        pass
                except KeyboardInterrupt:
                    break
                except TransactionNotFound:
                    pass
                except Exception as e:
                    print(e)
                    pass
                pass
            except Exception as e:
                print(e)
                pass
            except KeyboardInterrupt:
                break

if __name__ == "__main__":
    from tqdm import tqdm

    def run():
        logging.basicConfig(level=logging.INFO)
        print("Hello World")
    
    run()

    latest_block = w3_http.eth.get_block('latest', full_transactions=True)
    print("Ping: %s" % (w3_http.isConnected()))
    print("Number: %d" % (latest_block.number))
    print("Total Difficulty: %d" % (latest_block.totalDifficulty))
    print("Num. Transactions: %d" % (len(latest_block.transactions)))

    print("----")

    import pandas

    grants = pandas.read_csv('data/gr15_grants.csv')
    print(grants)

    # grants = pandas.read_json('data/gr15_grants.json')
    # print(grants)

    grants_applications = pandas.read_json('data/grants_applications_gr15.json')
    print(grants_applications)

    print("----")

    from gitcoin import Gitcoin
    api = Gitcoin()
    all_bounties = api.bounties.all()
    print("Num. Bounties: %d" % (len(all_bounties)))

    print("----")

    # loop = asyncio.get_event_loop()
    # try:
    #     loop.run_until_complete(get_pending_txs())
    # except KeyboardInterrupt:
    #     print("Received exit, exiting")
    # finally:
    #     loop.stop()
    #     loop.close()