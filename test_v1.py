from random import randint
from unittest import TestCase

from numberwords import NumberWord


class TestNumberWords(TestCase):
    def prepare_numbers():
        file = open("twodigits.txt", "w")
        number = []
        a = 0
        b = 10
        for i in range(0, 10):
            number.append(randint(a, b))
            file.write(str(number[i]) + "\n")
            a += 10
            b += 10
        file.close()
        return number

    def test_less100(self):
        file1 = open("twodigits.txt", "r")
        file2 = open("two_digits_words.txt", "r")
        nw = []
        word = []

        for i in file1:
            i = i.rstrip()
            nw.append(NumberWord(i))
        for w in file2:
            w = w.rstrip("\n")
            word.append(w)

        for m in range(0, len(word)):
            self.assertEqual(nw[m].word_number.rstrip(), word[m])
