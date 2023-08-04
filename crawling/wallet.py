import requests
import pandas
import json
from datetime import datetime

class Transaction():
    def __init__(self, TransactionJSON) -> None:
        self.hash = TransactionJSON['hash']
        self.time = datetime.fromtimestamp(TransactionJSON['time'])
        self.input = []
        self.output = []

        for idx in range(0, len(TransactionJSON['out'])):
            if TransactionJSON['out'][idx]['value'] != 0:
                self.output.append([TransactionJSON['out'][idx]['addr'], TransactionJSON['out'][idx]['value']])

        for idx in range(0, len(TransactionJSON['inputs'])): 
            if TransactionJSON['inputs'][idx]['prev_out']['value'] != 0: 
                self.input.append([TransactionJSON['inputs'][idx]['prev_out']['addr'], TransactionJSON['inputs'][idx]['prev_out']['value']])

class UserInformation(): 
    def __init__(self, address) -> None:
        self.address = address
        requestData = requests.get('https://blockchain.info/rawaddr/' + self.address).json()
        self.amountTransaction = requestData['n_tx']
        self.transaction = [Transaction(x) for x in requestData['txs']]
        self.balance = requestData['final_balance']
        self.alreadySent = requestData['total_sent']
        self.alreadyReceived = requestData['total_received']