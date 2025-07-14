from flask import Flask, send_file
import requests
import pandas as pd

app = Flask(__name__)

@app.route('/download')
def download_excel():
    url = "https://cryptobubbles.net/backend/data/bubbles1000.usd.json"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)
    file_path = 'bubbles_data.xlsx'
    df.to_excel(file_path, index=False, sheet_name='Bubbles')
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)