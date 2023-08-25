import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value ={
    "A": 2,
    "B": 1.75,
    "C": 1.5,
    "D": 1.25
}

def get_slot_spin(rows, cols, symbols):
    all_symbols= []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = [[], [], []]
    for _ in range(ROWS):
        for j in range(COLS):
            randomSymbol = all_symbols.pop(random.randint(0, len(all_symbols)) -1)
            columns[j].append(randomSymbol)
    return columns

def deposit():
    while True:
        amount = input("Ingrese el monto a depositar: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Debe se mayor que 0")
        else:
            print("Ingrese un numero")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Ingrese la cantidad de lineas en la que quiere apostar (Entre 1 y {str(MAX_LINES)})")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= 3:
                break
            else:
                print("Ingrese un numero entre 1 y 3")
        else:
            print("Ingrese un numero")
    return lines


def get_bet(balance, lines):
    while True:
        amount = input("Ingrese el monto a apostar en cada linea: $")
        if amount.isdigit() and ((int(amount)*lines) < balance):
            amount = int(amount)
            if (MIN_BET <= amount <= MAX_BET):
                break
            else:
                print(f"lmonto debe estar entre ${MIN_BET} y ${MAX_BET}")
        elif((int(amount)*lines)> balance):
            print("No tiene suficiente dinero, ingrese otra apuesta")
        else:
            print("Ingrese un numero")
    return amount

def verify_wins(result):
    columnsWon = 0
    for col in range(len(result)):
       flag = True
       actualCol = result[col]
       for row in range(len(actualCol)):
           if row == 0:
               firstSym = actualCol[row]
           else:
               if actualCol[row] != firstSym:
                   flag = False
       if flag:
           +columnsWon
    return columnsWon

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet(balance, lines)
    print(f"Estas apostando ${bet} en {lines} lineas, apuesta total: ${bet*lines}")
    ganadas = 0
    while ganadas == 0:
        result = get_slot_spin(ROWS, COLS, symbol_count)
        print(str(result))
        print(f"\nColumnas ganadas: {ganadas}")
main()