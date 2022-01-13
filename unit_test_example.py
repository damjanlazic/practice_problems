from numberwords import NumberWord
from unittest import TestCase
#
# entry = input("Enter an integer: ")
# while entry != "":
#
#     try:
#         number = int(entry)
#     except:
#         print("Enter an integer!")
#
#     nw = NumberWord(number)
#     print(nw.word_number)
#
#     entry = input("Enter an integer: ")

class TestNumberWords(TestCase):

    def prepare_data_for_processing(self):
        a = '123'
        return a

    def test_init(self):
        number_to_check = 64

        a = NumberWord(number_to_check)

        self.assertEqual(a.word_number, 'sixty four')

    def test_again(self):
        a = NumberWord(55)

        self.assertEqual(a.word_number, 'fifty five')

    def test1(self):
        self.assertEqual(1, 1)

    def test_thousand(self):
        a = NumberWord(1000)

        self.assertEqual(a.word_number, 'one thousand')

    def test_ten_thousand(self):
        a = NumberWord(10000)

        self.assertEqual(a.word_number, 'ten thousand')