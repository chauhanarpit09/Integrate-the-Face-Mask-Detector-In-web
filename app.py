from flask import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '959121b6ce54245c32bb1c09fae3cf16'

@app.route("/")
@app.route("/home")
def home():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug = True)