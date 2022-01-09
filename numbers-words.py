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

HUNDREDS = [i + " hundred" for i in ZERO]
THOUSANDS = [i + " thousand" for i in ZERO]
TENS_THOUSANDS = [i + " thousand" for i in TENS]
HUNDREDS_THOUSANDS = [i + " thousand" for i in HUNDREDS]
MILLIONS = [i + " million" for i in ZERO]


# n = int(input("number = "))
n = 98765
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

reference = {
    0: ZERO,
    1: TENS,
    2: HUNDREDS,
    3: THOUSANDS,
    4: TENS_THOUSANDS,
    5: HUNDREDS_THOUSANDS,
    6: MILLIONS,
}

for i in range(ndigits - 1, -1, -1):
    # print(i, end=" - ")
    c = reference[i]
    d = digits[i]
    print(c[d - 1], end=" ")
