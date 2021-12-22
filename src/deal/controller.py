def get_params_property(request):
    year = request['year'][0]
    city = request['city'][0]
    price = request['price'][0]
    return year, "'{}'".format(city), price