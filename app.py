# Flask Dependency
from flask import Flask

# Create a New Flask App Instance
app = Flask(__name__)

# Create Flask Routes with a function
@app.route('/')
def hello_world():
	return 'Hello world'
