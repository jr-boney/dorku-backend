
# Dorku Backend Project

## Overview
This project uses **Flask** to expose an API that runs the `sublist3r.py` script to gather subdomains for a given domain. The application can be run locally or deployed on a server (e.g., Render).

## Prerequisites
1. **Python 3**: Make sure you have Python 3 installed on your machine.
2. **Virtual Environment**: It’s recommended to use a virtual environment to manage dependencies.

## Cloning the Repository

To get started with the project, you first need to clone the repository to your local machine.

1. Open **Terminal** or **Command Prompt**.
2. Run the following command to clone the repository:
   ```bash
   git clone https://github.com/jr-boney/dorku-backend.git


3. Navigate to the project directory:
   ```bash
   cd dorku-backend
   ```

## Setting Up the Environment

### For Windows:
1. Open **Command Prompt** or **PowerShell**.
2. Navigate to the project directory where the `requirements.txt` file is located.
3. Run the following command to create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   ```bash
   .\venv\Scripts\activate
   ```
5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### For Linux/macOS:
1. Open **Terminal**.
2. Navigate to the project directory where the `requirements.txt` file is located.
3. Run the following command to create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
4. Activate the virtual environment:
   - For **Linux**:
     ```bash
     source venv/bin/activate
     ```
   - For **macOS**:
     ```bash
     source venv/bin/activate
     ```
5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Locally

### Modify Code (If Running Locally)
Sometimes the relative path to the `sublist3r.py` file may not work as expected due to different working directories. If you're running the project locally, **you may need to modify the path to `sublist3r.py`**.

1. Open `sublist3r_api.py`.
2. Find line 20 (where `sublist3r.py` is executed).
3. Change the path to `sublist3r.py` based on its location on your local machine.

**Change this line:**
```python
result = subprocess.run(
    ['python', r'sublist3r.py', '-d', domain],  # Original code
    stdout=subprocess.PIPE, stderr=subprocess.PIPE
)
```

**To this (adjust the path based on your local setup):**
```python
result = subprocess.run(
    ['python', r'path_to_your_local_sublist3r_folder\sublist3r.py', '-d', domain],  # Adjust this path
    stdout=subprocess.PIPE, stderr=subprocess.PIPE
)
```

For example (if `sublist3r.py` is located in the `dorku-backend` folder):
```python
result = subprocess.run(
    ['python', r'C:\path\to\dorku-backend\sublist3r.py', '-d', domain],  # Windows example
    stdout=subprocess.PIPE, stderr=subprocess.PIPE
)
```

For Linux/macOS, it might look like this:
```python
result = subprocess.run(
    ['python3', r'/path/to/dorku-backend/sublist3r.py', '-d', domain],  # Linux/macOS example
    stdout=subprocess.PIPE, stderr=subprocess.PIPE
)
```

### Running the Flask Application Locally
Once the path is updated, you can run the Flask application locally.

1. Make sure your virtual environment is activated.
2. Run the Flask application:
   ```bash
   python app.py
   ```
   This will start the Flask app on `http://127.0.0.1:5000`.

### Testing the API Locally
You can test the `/subdomains` API endpoint using a tool like **Postman** or simply through a browser by visiting the following URL:
```
http://127.0.0.1:5000/subdomains?domain=example.com
```

This will return a list of subdomains for the given domain.

## Deployment to Render

If you're deploying this application on **Render** (or any other cloud platform):

1. Push your code to GitHub.
2. Set up your project on **Render**:
   - Choose **Python** as the environment.
   - Point Render to the `main` branch of your GitHub repository.
3. Render will automatically install dependencies from `requirements.txt` and deploy your Flask app.

Once deployed, you can test the `/subdomains` endpoint on Render:

```
http://your-app-name.onrender.com/subdomains?domain=example.com
```




## License

Sublist3r is licensed under the GNU GPL license. take a look at the [LICENSE](https://github.com/aboul3la/Sublist3r/blob/master/LICENSE) for more information.


## Credits

* [TheRook](https://github.com/TheRook) - The bruteforce module was based on his script **subbrute**. 
* [Bitquark](https://github.com/bitquark) - The Subbrute's wordlist was based on his research **dnspop**. 

## Thanks

* Special Thanks to [Ibrahim Mosaad](https://twitter.com/ibrahim_mosaad) for his great contributions that helped in improving the tool.

## Version
**Current version is 1.0**
