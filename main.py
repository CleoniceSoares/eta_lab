from src.phonebook import Phonebook

test_phone_book = Phonebook()
test_phone_book.add("Maria", "12345677")
test_phone_book.add("Ana", "123456533")

# test_phone_book.add("Carlos", "222")
# print(test_phone_book.lookup('Carlos'))
# print(test_phone_book.get_names)
# print(test_phone_book.entries)
# print(test_phone_book.change_number('José', '222323212'))
# print(test_phone_book.entries)
# print(test_phone_book.change_number('Antônio', '443223234'))
# print(test_phone_book.get_numbers())
# print(test_phone_book.get_phonebook_sorted())

print(test_phone_book.get_name_by_number("123456533"))
print(test_phone_book.get_name_by_number("122134"))
