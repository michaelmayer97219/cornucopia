from app import app
@app.route('/')
def index():
	return "you've reached the index!"