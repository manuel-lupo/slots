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

def get_slot_spint(rows, cols, symbols):
    all_symbols= []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = [[], [], []]
    
    return

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

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet(balance, lines)
    print(f"Estas apostando ${bet} en {lines} lineas, apuesta total: ${bet*lines}")

main()