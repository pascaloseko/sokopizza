# sokopizza

## Local Set up
1. Clone Repo then change into project directory
2. Set up virtual env
```
python3 -m venv env
```
3. Install packages
```
pip install -r requirements.txt
```
4. Export db environment variables
```
export DB_NAME=db_name
export DB_USER=db_user
export DB_PASSWORD=db_password
```
5. Run Migrations
```
./manage.py makemigrations && ./manage.py migrate
```
6. Run Server
```
./manage.py runserver
```

## API DOCS
- Create Pizza Size
http://127.0.0.1:8000/order/pizza_size/
```
{
	"name": "Small",
	"price": 1200.00
}

Response 201
{
  "id": 1,
  "name": "Small",
  "price": "1200.00"
}
```

- Create Pizza Topping Type
http://127.0.0.1:8000/order/pizza_topping_type/
```
{
	"name": "Basic Toppings",
	"size": 1,
	"price": 50.00
}

Response 201
{
  "id": 1,
  "name": "Deluxe Toppings",
  "price": "50.00",
  "size": 1
}
```
- Create Pizza Topping
http://127.0.0.1:8000/order/pizza_topping/
```
{
    "name": "Olives",
    "topping_type": 1
}

Response 201
{
    "id": 1,
    "name": "Olives",
    "topping_type": 1
}
```
- Create Pizza
http://127.0.0.1:8000/order/pizza/
```
{
	"size": "Small",
	"toppings": [1, 4]
}

Response 201
{
  "id": 3,
  "price": "1300.00",
  "size": 1,
  "toppings": [
    1,
    4
  ]
}
```
- Create Order
http://127.0.0.1:8000/order/pizza_order/
```
{
	"pizzas": [1, 2, 3]
}

Response 201
{
  "id": 1,
  "subtotal": "5394.00",
  "total": "4650.00",
  "pizzas": [
    1,
    2,
    3
  ]
}
```