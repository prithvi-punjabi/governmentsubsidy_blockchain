from flask import Flask, render_template, request
from finalbc import Block, Blockchain
import json



app = Flask(__name__)
hash_list = []
bno_list = []
data_list = []
nonce_list = []
prh_list = []
blockchain = Blockchain()

@app.route('/')
def index():
    return render_template("hackathon.html")


@app.route('/hackathon',methods = ['POST', 'GET'])
def result(n=0):
    if request.method == 'POST':
        name1=request.form['sname']
        name2=request.form['name']
        batch1=request.form['batch']
        qn1=request.form['qn']
        rs1=request.form['rs']
        gst1=request.form['gst']
        blockchain.mine(Block("Block " + str(n + 1), name1, name2, batch1, qn1, rs1, gst1))
        n+=1
        hb = blockchain.head.hash()
        bn = blockchain.head.blockNo
        bd = blockchain.head.data
        hashes = blockchain.head.nonce
        pr_h = blockchain.head.previous_hash
        hash_list.append(hb)
        bno_list.append(bn)
        data_list.append(bd)
        nonce_list.append(hashes)
        prh_list.append(pr_h)
        blockchain.head = blockchain.head.next
        return render_template('/hackathon.html')


@app.route('/index2', methods=['GET','POST'])
def index2():
    return render_template('/index2.html',l1=hash_list, l2=bno_list, l3=data_list, l4=nonce_list, l5=prh_list, l6=len(hash_list))



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)


