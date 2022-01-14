#author: DMH 1/11/22

def add_foods(lst):
    sixth_letter = []
    not_foods = []
    short_foods = []
    for x in lst:
        try:
            sixth_letter.append(x[5])
        except IndexError:
            short_foods.append(x)
        except TypeError:
            not_foods.append(x)

    print(sixth_letter)
    print(not_foods)
    print(short_foods)


add_foods(['potatoes',True,'salsa','pie', 7,'cherries'])
