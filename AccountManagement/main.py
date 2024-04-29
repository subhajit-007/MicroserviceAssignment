import requests, os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

from producer import publish
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Initializing Flask app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
CORS(app)

# with app.app_context():
db = SQLAlchemy(app)


@dataclass
class AccountDetail(db.Model):
    account_no: int
    balance: int

    account_no = db.Column(db.Integer, primary_key=True, autoincrement=False)
    balance = db.Column(db.Integer)


@app.route('/api/accountdetails', methods=['GET'])
def account_details():
    return jsonify(AccountDetail.query.all())


@app.route('/api/accountdetail', methods=['POST'])
def add_account():
    # Parse the JSON data from the request
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    try:
        # Create a new AccountDetail object
        new_account = AccountDetail(
            account_no=data.get('account_no'),
            balance=data.get('balance')
        )

        # Add the new account to the database
        db.session.add(new_account)
        db.session.commit()

        return jsonify({"message": "Account added successfully"}), 201
    except:
        return jsonify({"Error": "Something went wrong"}), 400



@app.route('/api/accountdetail/<int:account_no>', methods=['GET'])
def get_account(account_no):
    account = AccountDetail.query.filter_by(account_no=account_no).first()
    if account:
        return jsonify(account)
    else:
        return jsonify({"error": "Account not found"}), 404


@app.route('/api/accountdetail/<int:account_no>', methods=['PUT'])
def update_account(account_no):
    # Parse the JSON data from the request
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Find the account to update
    account = AccountDetail.query.filter_by(account_no=account_no).first()
    if not account:
        return jsonify({"error": "Account not found"}), 404

    # Update account details
    account.balance = data.get('balance')

    # Commit changes to the database
    db.session.commit()
    publish("update_balance", data)
    return jsonify({"message": "Account updated successfully"})


@app.route('/api/accountdetail/<int:account_no>', methods=['DELETE'])
def delete_account(account_no):
    # Find the account to delete
    account = AccountDetail.query.filter_by(account_no=account_no).first()
    if not account:
        return jsonify({"error": "Account not found"}), 404

    # Delete the account from the database
    db.session.delete(account)
    db.session.commit()

    publish("account_delete", account_no)

    return jsonify({"message": "Account deleted successfully"})


if __name__ == '__main__':
    app.run(debug=os.getenv("DEBUG"), host='0.0.0.0')
