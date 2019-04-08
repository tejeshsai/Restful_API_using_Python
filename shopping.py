from bottle import run,get,delete,post,request

products = [{'name': 'Tommy Hilfiger', 'type': 'watch'},
            {'name': 'Lee_021', 'type': 'shirt'},
            {'name': 'PepeJeans_210', 'type': 'jeans'}]

@get('/product')
def getall():
    return {'products': products}

@get('/product/<name>')
def getOne(name):
    the_product=[product for product in products if product['name'] == name]
    return {'product': the_product[0]}

@post('/product')
def addOne():
    new_product = {'name': request.json.get('name'), 'type': request.json.get('type')}
    products.append(new_product)
    return {'products': products}

@delete('/product/<name>')
def deleteOne(name):
    the_product = [product for product in products if product['name'] == name]
    products.remove(the_product[0])
    return {'products': products}

run(reloader=True, debug=True)