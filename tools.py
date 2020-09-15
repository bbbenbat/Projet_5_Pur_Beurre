def ask_integer(name, max_int, min_int=0):
    assert type(name) == str
    assert type(min_int) == int
    assert type(max_int) == int
    while True:
        numb = input(f"Entrez une valeur de {name.lower()} comprise entre {min_int} et {max_int} : ")
        try:
            check = int(numb)
            if check > max_int or check < min_int:
                raise ValueError
            break
        except ValueError:
            pass
    return numb


def rp2cara(req, x, y, z):
    cara_1 = x
    cara_2 = y
    repl_1 = z
    string = cara_1 + cara_2
    for carac in string:
        req = req.replace(carac, repl_1)
    return req


# create a liste with a tuple by store's categories
def splite_tuple_to_liste(x):
    list_s = []
    list_s = (x.split(','))
    # print("***-***", descStore)
    return list_s


