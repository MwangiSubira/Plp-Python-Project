from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/block_customer', methods=['POST'])
def block_customer():
    data = request.get_json()
    provider_name = data.get('provider_name')
 
    return jsonify({
        "status": "success", "message":f"Provider {provider_name} blocked successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)

