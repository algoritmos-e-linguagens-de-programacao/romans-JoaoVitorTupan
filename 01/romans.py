name: Roman Converter

on:
  workflow_dispatch:
    inputs:
      roman_number:
        description: 'Número romano para converter para decimal'
        required: false
        default: ''
      decimal_number:
        description: 'Número decimal para converter para romano'
        required: false
        default: ''

jobs:
  convert:
    runs-on: ubuntu-latest

    steps:
    - name: Check out repository code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip

    - name: Run Roman Converter
      run: |
        python -c "
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
            raise ValueError('Número fora do intervalo (1-3999)')
        result = []
        for value, numeral in self.decimal_to_roman_map:
            while number >= value:
                result.append(numeral)
                number -= value
        return ''.join(result)

converter = RomanConverter()
roman_number = '${{ github.event.inputs.roman_number }}'
decimal_number = ${{ github.event.inputs.decimal_number }}

if roman_number:
    try:
        decimal_result = converter.roman_to_decimal(roman_number)
        print(f'{roman_number} em decimal é {decimal_result}')
    except ValueError as e:
        print(e)

if decimal_number:
    try:
        decimal_result = int(decimal_number)
        roman_result = converter.decimal_to_roman(decimal_result)
        print(f'{decimal_result} em romano é {roman_result}')
    except ValueError as e:
        print(e)
        "
