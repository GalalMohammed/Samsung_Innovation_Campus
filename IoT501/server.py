#!/usr/bin/python3
from flask import Flask, request
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate(
        '../../sic-demo-firebase-adminsdk-bkbu9-769bed6810.json')
firebase_admin.initialize_app(cred)

@app.route('/upload', methods=['POST'])
def upload():
    db = firestore.client()
    doc = db.collection('demo').document('test')
    doc.set({'image': request.json['image']})
    return ""

if __name__ == '__main__':
    app.run()
