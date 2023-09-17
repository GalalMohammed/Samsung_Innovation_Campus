#!/usr/bin/node
const admin = require('firebase-admin');

const serviceAccount = require('../../../../sic-demo-firebase-adminsdk-bkbu9-769bed6810.json');

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

const db = admin.firestore();

const data = {
  name: 'Test',
  age: 10
};

const doc = db.collection('demo').doc('test');

doc.set(data);
