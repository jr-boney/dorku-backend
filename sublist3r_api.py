
from flask import Flask, request, jsonify
import subprocess
from flask_cors import CORS  

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

@app.route('/subdomains', methods=['GET'])
def get_subdomains():
    domain = request.args.get('domain')
    if not domain:
        return jsonify({"error": "Domain parameter is required"}), 400

    try:
        # Run Sublist3r using subprocess
        result = subprocess.run(
            ['python', r'sublist3r.py', '-d', domain],
            
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )# C:\Users\Path\to\your\File\Sublist3r\sublist3r.py  on running locally :)


        # Get the output from Sublist3r
        subdomains = result.stdout.decode('utf-8').split('\n')

        # Return the subdomains as a JSON response
        return jsonify({"subdomains": subdomains})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
   
    app.run(host='0.0.0.0', port=3000, debug=True)




# from flask import Flask, request, jsonify
# import subprocess

# app = Flask(__name__)

# @app.route('/subdomains', methods=['GET'])
# def get_subdomains():
#     domain = request.args.get('domain')
#     if not domain:
#         return jsonify({"error": "Domain parameter is required"}), 400

#     try:
#         # Run Sublist3r using subprocess
#         result = subprocess.run(
#             ['python', r'C:\Users\Path\to\Your\File\Sublist3r\sublist3r.py', '-d', domain],
#             stdout=subprocess.PIPE, stderr=subprocess.PIPE
#         )

#         # Get the output from Sublist3r
#         subdomains = result.stdout.decode('utf-8').split('\n')

#         # Return the subdomains as a JSON response
#         return jsonify({"subdomains": subdomains})

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)
