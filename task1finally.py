
def decorate_function(function_to_decorate):
    def wayFound(vl,vs,t):
        try:
            a = function_to_decorate(vl,vs,t)
            s = vs* t + (a * (t**2))//2
            print(s)

        except TypeError:
            print('Данные введены неверно, подсчитать путь невозможно')
    return wayFound

@decorate_function
def boostFound(vl, vs, t):
    try:
        a = (vl - vs)//t
        print(a)
        return a
    except ZeroDivisionError:
        print('Время равно 0')
    except TypeError:
        print('Невозможно преобразовать в число')
        

print(boostFound(10, 15, 5))

print(boostFound(10,15, 0))

print(boostFound('dsfs', 15, 0))

