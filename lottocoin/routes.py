from lottocoin.models import User
from lottocoin.forms import *
from flask import Flask, jsonify, request, render_template, url_for, flash, redirect
from lottocoin import app, db, bcrypt
from lottocoin import blockchainObj
from flask_login import login_user, current_user, logout_user, login_required
from Crypto.PublicKey import RSA
from expiringdict import ExpiringDict
import requests

#FLASK ROUTES 
current_sessions = ExpiringDict(max_len=500, max_age_seconds=500)

@app.route("/")
@app.route("/home")
@app.route("/blockchain")
def home():
    blockchainObj.resolveConflicts();
    return render_template('blockchain.html', title = "Blockchain", blockchain = blockchainObj);

@app.route("/transaction", methods=['GET', 'POST'])
def transaction():
    form = TransactionForm();
    formNL = TransactionFormNotLoggedIn();
    #print(form.sender.data, form.reciever.data, form.amount.data, form.key.data);
    #print("hi");
    if form.validate_on_submit():
        print("hi");
        #print(form.sender.data, form.reciever.data, form.amount.data, form.key.data);
        #print(type(form.key.data));
        if form.amount.data > blockchainObj.getBalance(form.sender.data):
            return render_template('error.html', title = "Error", error="You do not have enough coins to make this transaction.")
        feedback = blockchainObj.addTransaction(form.sender.data, form.reciever.data, form.amount.data, form.key.data, form.key.data);
        if feedback:
            flash(f'Transaction Made!', 'success');
        else:
            flash(f'Error!', 'danger');
        return render_template('transaction.html', title = "Transaction", blockchain = blockchainObj, form=form, formNL= formNL); 

    if formNL.validate_on_submit():
        return redirect(url_for('login'));

    return render_template('transaction.html', title = "Transaction", blockchain = blockchainObj, form=form, formNL= formNL);

@app.route("/minerPage")
def minerPage():
	return render_template('minerPage.html', title = "Mine", blockchain = blockchainObj);

@app.route("/purchase", methods=['GET', 'POST'])
def purchase():
    form = TransactionForm();
    formNL = TransactionFormNotLoggedIn();
    #print(form.sender.data, form.reciever.data, form.amount.data, form.key.data);
    #print("hi");
    if form.validate_on_submit():
        print("hi");
        #print(form.sender.data, form.reciever.data, form.amount.data, form.key.data);
        #print(type(form.key.data));
        feedback = blockchainObj.addTransaction(form.sender.data, form.reciever.data, form.amount.data, form.key.data, form.key.data);
        if feedback:
            flash(f'Transaction Made!', 'success');
        else:
            flash(f'Error!', 'danger');
    return render_template('purchase.html', title = "Purchase", blockchain = blockchainObj, form=form, formNL= formNL);  

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #password hashing
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8');
        keyGen = blockchainObj.generateKeys();
        user = User(name=form.name.data, username=form.username.data, email=form.email.data, password=hashed_password, key = keyGen);
        db.session.add(user);
        db.session.commit();
        login_user(user);
        nextPage = request.args.get('next');
        flash(f'Account created for @{form.username.data}! You are now logged in as well.', 'success')
        return redirect(nextPage) if nextPage else redirect(url_for('home'));
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first();
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data);
            nextPage = request.args.get('next');
            flash(f'Welcome! You are now logged in', 'success');
            global current_sessions
            current_sessions[user.username] = current_user
            print(current_sessions)
            return redirect(nextPage) if nextPage else redirect(url_for('home'));
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger');
            #return redirect(url_for('login'))
    return render_template('login.html', form=form);

@app.route("/logout")
def logout():
    global current_sessions
    current_sessions.pop(current_user.get_id())
    logout_user();
    return redirect(url_for('home'));

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account', blockchain = blockchainObj)



#BLOCKCHAIN BACKEND REQUESTS
@app.route('/mine', methods=['GET'])
def mine():
    print("madeit");
    miner = request.args.get('miner', None);
    lastBlock = blockchainObj.getLastBlock();

    if len(blockchainObj.pendingTransactions) <= 1:
        flash(f'Not enough pending transactions to mine! (Must be > 1)', 'danger');
    else:
        feedback = blockchainObj.minePendingTransactions(miner);
        if feedback:
            flash(f'Block Mined! You have a ticket for the lottery now!', 'success');
        else:
            flash(f'Error!', 'danger');
    return render_template('minerPage.html', title = "Mine", blockchain = blockchainObj);

  
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json();
    required = ['sender', 'reciever', 'amt']
    if not all(k in values for k in required):
        return 'Missing values', 400;

    index = blockchainObj.addTransaction(values['sender'], values['reciever'], values['amt'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201;

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchainObj.chainJSONencode(),
        'length': len(blockchainObj.chain),
    }
    return jsonify(response), 200

#blockchainObj DECENTRALIZED NODES
@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        blockchainObj.register_node(node)

    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchainObj.nodes),
    }
    return jsonify(response), 201


@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchainObj.resolveConflicts()

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchainObj.chainJSONencode()
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchainObj.chainJSONencode()
        }

    return jsonify(response), 200

@app.route('/lottery')
def lottery():
    return render_template('lottery.html', title='Lottery', blockchain = blockchainObj)

@app.route('/users')
def users():
    all_usernames = []
    all_users = User.query.all()
    for x in range(len(all_users)):
        all_usernames.append(all_users[x].username) 
    print(all_usernames)
    return render_template('users.html', users=current_sessions, allusers=all_usernames)