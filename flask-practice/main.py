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

# Show comments of specific post from json placeholder
@app.route('/post/<int:post_num>/comments')
def show_comments(post_num):
    response = requests.get('https://jsonplaceholder.typicode.com/posts/{}/comments'.format(post_num))
    to_serve = response.json()
    return jsonify(to_serve)

# rendering with template

# data
# TODO: Connect sqlite3 or mongodb and import data from it.
product_list = [
  {
    'product_id': 10000001,
    'product_name': 'shoes',
    'price': 12000,
    'currency': 'KRW',
  },
  {
    'product_id': 10000002,
    'product_name': 'cap',
    'price': 25.99,
    'currency': 'USD',
  },
  {
    'product_id': 10000003,
    'product_name': 'pants',
    'price': 40000,
    'currency': 'KRW',
  },
]

# get all products
@app.route('/products')
def show_product_list():
  result={'items':product_list}
  return render_template('products.html', items=result)

# get product detail
@app.route('/products/<int:product_id>')
def show_product(product_id=None):
  result = next(item for item in product_list if item['product_id']==product_id)
  return render_template('product.html',item=result)

# Do app.run() at __main__ entry point.
# Protect users from accidentally invoking the script when they didn't intend to.
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    # If you have trouble with running like "No module 'flask'", please run '$ pip install flask' once.  
