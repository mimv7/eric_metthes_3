def print_models(unprinted_designs, completed_models):
    """
    Имитирует печать 3D-моделей, пока список не опустеет.
    Каждая модель после печати перемещается в completed_models.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Печать модели: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Выводит список всех готовых моделей."""
    print("\nСледующие модели были напечатаны:")
    for model in completed_models:
        print(model)

    print(completed_models)

def display_message():
    print('You are going through the eighth chapter, which is called "Function."')
display_message()

def make_shirt(size,inscription):
    """выводит текст с размером и надписью на рубашке """
    print(f'Your T-shirt size is {size}, and it says "{inscription}" on it.')