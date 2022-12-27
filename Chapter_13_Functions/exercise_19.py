"""
Write a function called verbose that, given an integer less than 10^15, returns the name of
the integer in English. As an example, verbose(123456) should return one hundred
twenty-three thousand, four hundred fifty-six.
"""

"""
Solution
--------
-> First let's divide the number into 5 sections 
    -> Trillions
    -> Billions
    -> Millions
    -> Thousands
    -> Hundreds
-> each sections has it's own (hundreds - tens - ones ) and section suffix.
"""

sections = ['', 'thousand', 'million', 'billion', 'trillion']  # Hundreds has no suffix
ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
sub_tens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
            'nineteen']
tens = [sub_tens, '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def get_console_input():
    integer = int(eval(input('Enter a number no more than 10^15')))
    if integer > 10e15:
        print('Bad input')
        exit()
    return integer


def pronounce_section(section):
    one = section % 10
    section_pronunciation = ones[one]
    ten = section % 100
    if section > 9:
        if 20 > ten > 9:
            section_pronunciation = sub_tens[ten - 10]
        else:
            ten //= 10
            if one > 0 and ten > 0:
                section_pronunciation = '-' + section_pronunciation
            section_pronunciation = tens[ten] + section_pronunciation if ten > 0 else section_pronunciation
    if section > 99:
        section_pronunciation = ' hundred ' + section_pronunciation
        hundred = section // 100
        section_pronunciation = ones[hundred] + section_pronunciation
    return section_pronunciation


def verbose(integer):
    result = ''
    i = 0
    while integer > 0:
        section = integer % 1000
        integer //= 1000
        result = pronounce_section(section) + ' ' + sections[i] + result
        i += 1
        if integer > 0:
            result = ', ' + result
    return result.strip() + '.'


print(verbose(123456))
