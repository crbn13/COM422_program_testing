
def calculate_ticket_price(age:int, student:bool=False) -> int:
    if age >= 19 and age < 65:
        return 4
    elif age < 3:
        return 0
    elif age > 64:
        return 0
    pass
