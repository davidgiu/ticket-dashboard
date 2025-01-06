import hmac
import hashlib
import json
import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, request, jsonify
from datetime import datetime
 
app = Flask(__name__)
 
# Initialiser Firebase
cred = credentials.Certificate("hookServer/urbanisation-c5b41-firebase-adminsdk-5d7y6-f6163c31f2.json")
firebase_admin.initialize_app(cred)
 
# Référence à Firestore
db = firestore.client()
 
# Secret partagé pour vérifier la signature
SECRET = "AEeyJhbGciOiJIUzUxMiIsImlzcyI6"  # Remplace avec ton propre secret
 
# Fonction pour vérifier la signature HMAC
def verify_signature(body, signature):
    unix_timestamp = str(int(datetime.timestamp(datetime.now())))
    body_to_sign = f'{unix_timestamp}.{body}'.encode('utf-8')
    digest = hmac.new(SECRET.encode(), body_to_sign, hashlib.sha256).hexdigest()
    expected_signature = f't={unix_timestamp},v1={digest}'
   
    return hmac.compare_digest(signature, expected_signature)
 
# Route pour recevoir le webhook
@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # Récupérer le corps de la requête
    body = request.data.decode('utf-8')
   
    # Vérifier la signature
    signature = request.headers.get('Petzi-Signature', '')
   
    if not verify_signature(body, signature):
        return jsonify({"error": "Invalid signature"}), 400
   
    # Analyser les données JSON envoyées
    try:
        data = json.loads(body)
        event = data.get('event')
       
        if event == 'ticket_created':
            ticket_info = data['details']['ticket']
            ticket_number = ticket_info['number']
 
            print(f"Ticket créé: {ticket_info['number']} pour l'événement {ticket_info['event']} de type de ticket : {ticket_info['category']}")
           
            # Insérer chaque attribut individuellement dans Firestore
            doc_ref = db.collection('tickets').document(ticket_number)
            doc_ref.set({
                'ticket_number': ticket_info['number'],
                'type': ticket_info['type'],
                'title': ticket_info['title'],
                'category': ticket_info['category'],
                'event': ticket_info['event'],
                'eventId': ticket_info['eventId'],
                'cancellationReason': ticket_info['cancellationReason'],
                'generatedAt': ticket_info['generatedAt'],
                'promoter': ticket_info['promoter'],
                'price': {
                    'amount': ticket_info['price']['amount'],
                    'currency': ticket_info['price']['currency']
                },
                'sessions': [
                    {
                        'name': session['name'],
                        'date': session['date'],
                        'time': session['time'],
                        'doors': session['doors'],
                        'location': {
                            'name': session['location']['name'],
                            'street': session['location']['street'],
                            'city': session['location']['city'],
                            'postcode': session['location']['postcode']
                        }
                    } for session in ticket_info['sessions']
                ],
                'buyer': {
                    'role': data['details']['buyer']['role'],
                    'firstName': data['details']['buyer']['firstName'],
                    'lastName': data['details']['buyer']['lastName'],
                    'postcode': data['details']['buyer']['postcode']
                }
            })
 
            print(f"Ticket {ticket_number} enregistré dans Firestore.")
            return jsonify({"status": "success", "message": "Ticket reçu et traité"}), 200
       
        else:
            return jsonify({"error": "Event not recognized"}), 400
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON"}), 400
 
 
if __name__ == '__main__':
    # Démarrer le serveur Flask sur le port 5000
    app.run(debug=True, port=5000)