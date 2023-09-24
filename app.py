from flask import Flask, render_template
from routes.download_mp3 import download_mp3_bp
from routes.index import index_bp

app = Flask(__name__)

app.register_blueprint(download_mp3_bp, url_prefix='/mp3')
app.register_blueprint(index_bp, url_prefix='/')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)