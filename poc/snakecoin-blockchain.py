# Create the blockchain and add genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Smoll chain, add 15 blocks after genesis
num_of_blocks_to_add = 15

for i in range(0, num_of_blocks_to_add):
    # Create block
    block_to_add = next_block(previous_blocks)

    # Add new block to chain
    blockchain.append(block_to_add)

    # New block is now old block
    previous_block = block_to_add

    # Logging
    print("Block #{} has been added to the blockchain".format(block_to_add.index))
    print("Hash: {}\n".format(block_to_add.hash))