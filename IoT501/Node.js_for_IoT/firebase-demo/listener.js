#!/usr/bin/node
const admin = require('firebase-admin');

const serviceAccount = require('../../../../sic-demo-firebase-adminsdk-bkbu9-769bed6810.json');

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

const db = admin.firestore();

const collection = db.collection('demo');

const observer = collection.onSnapshot(querySnapshot => {
  querySnapshot.forEach(docSnapShot => {
    console.log(docSnapShot.id + ': ');
    console.log(docSnapShot.data());
  });
}, error => {
  console.log(error);
});
