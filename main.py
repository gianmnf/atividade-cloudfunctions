def insertCarros(request):
    request_json = request.get_json()
    def getAttribute(attr):
        if request.args and attr in request.args:
            return request.args.get(attr)
        elif request_json and attr in request_json:
            return request_json[attr]
        else:
            return null
    placa = getAttribute('placa')
    cor = getAttribute('cor')
    preco = getAttribute('preco')
    modelo = getAttribute('modelo')
    marca = getAttribute('marca')
    return('Placa:' + placa + '\nCor:' + cor + '\nPreço:' + preco + '\nModelo:' + modelo + '\nMarca:' + marca) 