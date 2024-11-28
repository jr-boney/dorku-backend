from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/get-subdomains', methods=['GET'])
def get_subdomains():
    domain = request.args.get('domain')
    if not domain:
        return jsonify({"error": "Domain parameter is required"}), 400

    try:
        # Run Sublist3r using subprocess
        result = subprocess.run(
            ['python', r'C:\Users\aswin\Projects\Personal\Sublist3r\sublist3r.py', '-d', domain],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        # Get the output from Sublist3r
        subdomains = result.stdout.decode('utf-8').split('\n')

        # Return the subdomains as a JSON response
        return jsonify({"subdomains": subdomains})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
