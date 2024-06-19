def int_to_roman(num):
    # Tabela de valores dos algarismos romanos
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

def roman_to_int(s):
    # Tabela de valores dos algarismos romanos
    roman = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000,
        'IV': 4, 'IX': 9, 'XL': 40,
        'XC': 90, 'CD': 400, 'CM': 900
    }
    i = 0
    num = 0
    while i < len(s):
        # Verifica se um par especial está presente
        if i + 1 < len(s) and s[i:i+2] in roman:
            num += roman[s[i:i+2]]
            i += 2
        else:
            num += roman[s[i]]
            i += 1
    return num

# Exemplos de uso
print(int_to_roman(1994))  # Deve retornar 'MCMXCIV'
print(roman_to_int("MCMXCIV"))  # Deve retornar 1994
