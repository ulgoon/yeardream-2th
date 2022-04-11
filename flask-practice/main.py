from flask import Flask

# Create instance of the Flask object
# __name__: represents the name of the application package
# Let Flask to identify resources

app = Flask(__name__)

# first flask route
@app.route('/')
def index():
    return "flask works!"

# Do app.run() at __main__ entry point.
# Protect users from accidentally invoking the script when they didn't intend to.
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
