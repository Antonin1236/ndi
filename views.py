# salut


from flask import Flask

app = Flask(__name__)



app.config.from_object('config')

@app.route('/')
def index():
    return "Hello world !"


@app.route('/home')
def home():
	return 'home'

if __name__ == "__main__":
    app.run()
