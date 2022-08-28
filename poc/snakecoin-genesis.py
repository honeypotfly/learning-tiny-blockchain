import datetime as date

def create_genesis_block():
    # MAnually build the first block in our blockchain
    return Block(0, date.datetime.now(), "Genesis Block", "0")
    