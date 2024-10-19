# [TODO]: Only allow current ip to access routes

from flask import Flask, render_template, request, jsonify
import db

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  db.create_table(table_name = "budget", columns = ["transaction_type", "amount", "sender"])
  res = db.get_data(table_name = "budget")
  return render_template('index.html', data = res)

@app.route('/budget_submit', methods=['POST'])
def credit():
  transaction_type = request.args.get('type', '')
  amount = request.args.get('amount', '')
  sender = request.args.get('sender', '')
  
  db.insert_data(table_name="budget", data = [transaction_type, amount, sender])

  return index()
