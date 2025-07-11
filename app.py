from flask import Flask, request, jsonify
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# Logging Configuration
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler = RotatingFileHandler('app.log', maxBytes=5000000, backupCount=3)
handler.setFormatter(log_formatter)
handler.setLevel(logging.INFO)

app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

@app.route('/')
def home():
    app.logger.info('Home endpoint hit')
    return 'Welcome to Logging Backend!'

@app.route('/log', methods=['POST'])
def log():
    data = request.get_json()
    level = data.get('level', 'info').lower()
    message = data.get('message', 'No message provided.')

    if level == 'debug':
        app.logger.debug(message)
    elif level == 'warning':
        app.logger.warning(message)
    elif level == 'error':
        app.logger.error(message)
    else:
        app.logger.info(message)

    return jsonify({'status': 'logged'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)