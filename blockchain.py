from datetime import datetime
import hashlib
import json
from unittest.mock import NonCallableMagicMock


class Blockchain:
    """
    The previous_hash is set to 0 initially
    The nonce is set to 1 

    """


    def __init__(self):
        self.chain = []
        self.create_block(nonce=1, previous_hash='0')

    # return the block created.
    def create_block(self, nonce, previous_hash):
        #create new block as python dictionary 
        dict = {
            'index': self.get_chain_len(),
            'timestamp': str(datetime.now()),
            'nonce': nonce,
            'previous_hash': previous_hash
        }
        #add block to the chain
        self.chain.append(dict)
        return  dict

    # return the new nonce value.
    def proof_of_work(self, previous_nonce):
        
        new_nonce = previous_nonce
        hash_operation = hashlib.sha256(str(1).encode()).hexdigest()
        while not (hash_operation[:4] == "0000"):
            previous_nonce = new_nonce
            new_nonce = new_nonce + 1
            hash_operation = hashlib.sha256(str(new_nonce ** 2 - previous_nonce** 2).encode()).hexdigest()
        print(hash_operation, '\n')
        print(new_nonce,'\n')
        return new_nonce
    
        
        #hash_operation = hashlib.sha256(str((previous_nonce + 1) ** 2 - previous_nonce** 2).encode()).hexdigest()
        #if(hash_operation [:4] == "0000"):
        #    return previous_nonce + 1
        #self.proof_of_work(previous_nonce + 1)

    # returns True if the chain is valid, False otherwise
    def is_chain_valid(self, chain):
        for block in chain:
            if(block.get('previous_hash') != self.hash_block(self.get_previous_block())):
                return False
            # add the nonce check
        return True

    """
    Helper methods: 

    get_chain(self): returns the entire chain with its length
    get_chain_len(self): returns the length of the chain 
    get_previous_block(self): returns the previous block in the chain
    hash_block(self, block): returns the hash of the given block 
    
    """

    def get_chain(self):
        response = {'chain': self.chain, 'length': len(self.chain)}
        return response

    def get_chain_len(self):
        return len(self.chain)

    def get_previous_block(self):
        return self.chain[-1]

    def hash_block(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()