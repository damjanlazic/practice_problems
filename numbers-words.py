# for a user input of any integer between -million to million
# write a corresponding word in english
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
TEN_TWENTY = [
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
HUNDREDS = [i + " hundred" for i in ZERO]
THOUSANDS = [i + " thousand" for i in ZERO]
TENS_THOUSANDS = [i for i in TENS]
HUNDREDS_THOUSANDS = [i for i in HUNDREDS]
MILLIONS = [i + " million" for i in ZERO]

reference = {
    0: ZERO,
    1: TENS,
    2: HUNDREDS,
    3: THOUSANDS,
    4: TENS_THOUSANDS,
    5: HUNDREDS_THOUSANDS,
    6: MILLIONS,
}
special_reference = {
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


def write_number(ndigits, digits):
    for i in range(ndigits - 1, -1, -1):
        # print(i, end=" - ")
        c = reference[i]
        d = digits[i]
        if d != 0:
            print(c[d - 1], end=" ")
        else:
            if (ndigits - 1 == 4 or ndigits - 1 == 5) and i == 3:
                print("thousand", end=" ")


number = 1
while number != 0:
    number = int(input("number = "))

    n = number
    ndigits = 0
    digits = {}
    if n == 0:
        print("Zero!")
    else:
        while n != 0:
            digits[ndigits] = n % 10
            n = int(n // 10)
            ndigits += 1

    print(digits)

    if number >= 11 and number <= 19:
        print(special_reference[digits[0]])
    elif number >= 11000 and number <= 19999:

        # for i in range(ndigits-2,-1,-1):
        d = digits[3]
        print(special_reference[d] + "thousand")
        write_number(ndigits - 1, digits)
    else:
        write_number(ndigits, digits)

    print("\n")
