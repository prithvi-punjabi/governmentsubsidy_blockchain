import datetime
import hashlib
class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data, sup_name, prod_name, batch_id, quant, price, gst_in):
        self.data = data
        self.sup_name = sup_name
        self.prod_name = prod_name
        self.batch_id = batch_id
        self.quant = quant
        self.price = price
        self.gst_in = gst_in

    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.sup_name).encode('utf-8') +
        str(self.prod_name).encode('utf-8') +
        str(self.batch_id).encode('utf-8') +
        str(self.quant).encode('utf-8') +
        str(self.price).encode('utf-8') +
        str(self.gst_in).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\nPrevious Hash: " + str(self.previous_hash) + "\n--------------"

class Blockchain:

    diff = 20
    maxNonce = 2**32
    target = 2 ** (256-diff)

    block = Block("Genesis", "Government of India", "none", "none", "none", "none", "none")
    dummy = head = block

    def add(self, block):

        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1


if __name__ =='__main__':
 blockchain = Blockchain()


 n=0
 ch=0
 while(ch!=1):
  sup_n = input("Enter the supplier name:")
  prod_n = input("Enter the product name:")
  b_id = input("Enter the starting batch id:")
  q = input("Enter the quantity:")
  p = input("Enter the price:")
  g_in = input("Enter the gst number:")
  ch = int(input("Do you have to make another transaction?(Enter 1 for no):"))
  blockchain.mine(Block("Block " + str(n+1),sup_n,prod_n,b_id,q,p,g_in))
  n+=1
 while blockchain.head != None:
  print(blockchain.head)
  blockchain.head = blockchain.head.next

