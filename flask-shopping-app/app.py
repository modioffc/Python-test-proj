from flask import Flask, render_template

app = Flask(__name__)

# Sample products data
products = [
    {"id": 1, "name": "Laptop", "price": 1000, "description": "A high-end gaming laptop"},
    {"id": 2, "name": "Smartphone", "price": 700, "description": "A new smartphone with the latest features"},
    {"id": 3, "name": "Headphones", "price": 150, "description": "Noise-cancelling wireless headphones"}
]

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    return render_template('product_detail.html', product=product)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

