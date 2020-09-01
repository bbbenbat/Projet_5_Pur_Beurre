

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



ask_integer('Test',1)