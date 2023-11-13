def create_valid(qwery, count):
    valid = True
    if not qwery['name'] or not qwery['price'] or not qwery['quantity']:
        valid = False
    else:
        if float(qwery['price']) < 0 or float(qwery['quantity']) < 0:
            valid = False
        else:
            if 1 > int(qwery['category']) > count:
                valid = False

    return valid
