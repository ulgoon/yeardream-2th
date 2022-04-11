from flask import Flask, jsonify, render_template
import requests

# Create instance of the Flask object
# __name__: represents the name of the application package
# Let Flask to identify resources

app = Flask(__name__)

# first flask route
@app.route('/')
def index():
    return render_template('index.html')

# relay external data
@app.route('/posts')
def show_post_list():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    to_serve = response.json()
    return jsonify(to_serve)

# route with variables
@app.route('/post/<string:post_name>')
def show_post(post_name=None):
    return "This is post about {}".format(post_name)

# Do app.run() at __main__ entry point.
# Protect users from accidentally invoking the script when they didn't intend to.
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    # If you have trouble with running like "No module 'flask'", please run '$ pip install flask' once.  
