from flask import Flask, request, jsonify
import sys, logging
 
app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ])

@app.route('/acr_webhook', methods=['POST'])
def receive_json():
    try:
        # Check if the request contains JSON data
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data received"}), 400

        # Process the JSON data (here, just print it)
        # print("Received JSON:", data)
        logging.debug('Received JSON: %s', data)

        # Respond with a success message and echo the received data
        return jsonify({
            "message": "JSON data received successfully",
            "received_data": data
        }), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
 