class RomanConverter:
    def __init__(self):
        self.roman_to_decimal_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        self.decimal_to_roman_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def roman_to_decimal(self, roman):
        total = 0
        prev_value = 0
        for char in reversed(roman):
            value = self.roman_to_decimal_map[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total

    def decimal_to_roman(self, number):
        if number <= 0 or number >= 4000:
            raise ValueError("Número fora do intervalo (1-3999)")
        result = []
        for value, numeral in self.decimal_to_roman_map:
            while number >= value:
                result.append(numeral)
                number -= value
        return ''.join(result)

# Exemplo de uso:
converter = RomanConverter()

# Teste de conversão de romano para decimal
try:
    roman_number = "MMMCMXCIX"
    decimal_result = converter.roman_to_decimal(roman_number)
    print(f"{roman_number} em decimal é {decimal_result}")
except ValueError as e:
    print(e)

# Teste de conversão de decimal para romano
try:
    decimal_number = 3999
    roman_result = converter.decimal_to_roman(decimal_number)
    print(f"{decimal_number} em romano é {roman_result}")
except ValueError as e:
    print(e)
