# for a user input of any integer between -million to million
# write a corresponding word in english

from typing import Dict


class NumberWord:

    ZERO = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    TENS = [
        "ten",
        "twenty",
        "thirty",
        "fourty",
        "fifty",
        "sixty",
        "seventy",
        "eigthty",
        "ninety",
    ]

    HUNDREDS = [i + " hundred" for i in ZERO]
    THOUSANDS = [i + " thousand" for i in ZERO]
    MILLIONS = [i + " million" for i in ZERO]

    reference = {
        0: ZERO,
        1: TENS,
        2: HUNDREDS,
        3: THOUSANDS,
        4: TENS,
        5: HUNDREDS,
        6: MILLIONS,
    }
    special_reference = {
        0: "ten",
        1: "eleven",
        2: "twelve",
        3: "thirteen",
        4: "fourteen",
        5: "fifteen",
        6: "sixteen",
        7: "seventeen",
        8: "eighteen",
        9: "nineteen",
    }

    number: int
    word_number: str
    digits: Dict

    def __init__(self, number):
        self.number = number

        n = abs(number)
        ndigits = 0
        digits = {}
        while n != 0:
            digits[ndigits] = n % 10
            n = int(n // 10)
            ndigits += 1

        self.digits = digits
        self.transmute_number(digits)

    def write_number(self, ndigits, digits):
        i = ndigits - 1
        word = ""
        while i >= 0:

            c = self.reference[i]
            d = digits[i]
            if d != 0:
                if d == 1 and i == 4:
                    i = 3
                    word += self.special_reference[digits[i]] + " "
                    word += " thousand "

                elif d == 1 and i == 1:
                    i = 0
                    word += self.special_reference[digits[i]] + " "

                else:
                    word += c[d - 1] + " "
            else:
                if (ndigits - 1 == 4 or ndigits - 1 == 5) and i == 3:
                    word += " thousand "

            i -= 1
        self.word_number = word
        return word

    def transmute_number(self, digits: Dict) -> str:

        n = abs(self.number)
        word = ""

        ndigits = len(digits)

        if digits == {}:
            word = "Zero!"

        else:

            if self.number < 0:
                word = "minus "

            if n >= 11 and n <= 19:
                word = self.special_reference[digits[0]]

            elif n >= 11000 and n <= 19999:
                d = digits[3]
                word += self.special_reference[d] + " thousand "
                word += self.write_number(ndigits - 2, digits)
            else:
                word += self.write_number(ndigits, digits)
        self.word_number = word
        return word
