#!/usr/bin/node
const admin = require('firebase-admin');
const express = require('express');
const bodyParser = require('body-parser');

const serviceAccount = require('../../../../sic-demo-firebase-adminsdk-bkbu9-769bed6810.json');

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

const db = admin.firestore();

const doc = db.collection('demo').doc('test');

const app = express();
const port = 3000;
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.post('/', (req, res) => {
  doc.set(req.body);
  res.send('');
});

app.listen(port);
