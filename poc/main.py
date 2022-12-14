import hashlib as hasher
from time import time
import datetime as date


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(
            str(self.index).encode('utf-8') + 
            str(self.timestamp).encode('utf-8') + 
            str(self.data).encode('utf-8') + 
            str(self.previous_hash).encode('utf-8')
            )
        return sha.hexdigest()


def create_genesis_block():
    # MAnually build the first block in our blockchain
    return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hello, I am block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


def main():
    # Create the blockchain and add genesis block
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    # Smoll chain, add 15 blocks after genesis
    num_of_blocks_to_add = 15

    for i in range(0, num_of_blocks_to_add):
        # Create block
        block_to_add = next_block(previous_block)

        # Add new block to chain
        blockchain.append(block_to_add)

        # New block is now old block
        previous_block = block_to_add

        # Logging
        print("Block #{} has been added to the blockchain".format(block_to_add.index))
        print("Hash: {}\n".format(block_to_add.hash))

if __name__== "__main__":
    main()
