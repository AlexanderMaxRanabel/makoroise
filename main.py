from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

def mk_req(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text  # Contains the HTML content as a string
            return html_content
        else:
            print(f"Failed to retrieve HTML: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-url', methods=['POST'])
def submit_url():
    url = request.form['url']
    html_body = mk_req(url)
    return html_body

@app.route('/redirect', methods=['POST'])
def redirect_page():
    # Logic to process form data if needed
    # Redirect to another page or URL
    return redirect(url_for('another_page'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5277, debug=True)

