from flask import Flask, request, render_template
from wakeonlan import send_magic_packet
import socket

app = Flask(__name__)

# main page
@app.route('/')
def index():
    return render_template('index.html')

# send api with gui (post)
@app.route('/wake', methods=['POST'])
def wake():
    mac_address = request.form.get('mac_address')
    if mac_address:
        send_magic_packet(mac_address)
        return {'status': 'success', 'message': f'Magic Packet gesendet an {mac_address}'}
    return {'status': 'error', 'message': 'MAC-Adresse fehlt'}, 400

# send api (get)
@app.route('/api/wake/<mac_address>', methods=['GET'])
def wake_get(mac_address):
    try:
        send_magic_packet(mac_address)
        return {'status': 'success', 'message': f'Magic Packet gesendet an {mac_address}'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}, 400

if __name__ == '__main__':
    # Starte den Server auf allen verfügbaren IP-Adressen
    app.run(host='0.0.0.0', port=5000, debug=True)
