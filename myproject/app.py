from flask import Flask
import os
from datetime import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Your Full Name" 
    username = os.getlogin()
    ist_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S') 


    top_output = subprocess.getoutput('top -bn1')

    html_response = f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {full_name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (UTC):</strong> {ist_time}</p>
    <h2>Top Command Output:</h2>
    <pre>{top_output}</pre>
    """
    return html_response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
