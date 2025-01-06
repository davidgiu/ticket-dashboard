// src/firebase.js
import { initializeApp } from 'firebase/app'
import { getFirestore } from 'firebase/firestore'

const firebaseConfig = {
  apiKey: "AIzaSyCYw2nLi4YMWCoE-TbJfOYbIRKWKeylmNo",
  authDomain: "urbanisation-c5b41.firebaseapp.com",
  projectId: "urbanisation-c5b41",
  storageBucket: "urbanisation-c5b41.firebasestorage.app",
  messagingSenderId: "859305792948",
  appId: "1:859305792948:web:2fd826f21fe5a2d7e14ee1"
}

const app = initializeApp(firebaseConfig)
const db = getFirestore(app)

export { db }