from classes import Record, AddressBook
from notes import Note, NotesBook
from constants import GREEN, RESET

# =============================================
#             test 1 (Classes)
# =============================================

if __name__ == "__main__":
    book = AddressBook()
    filename = "book_test_1.bin"

    print(GREEN + "     створюємо новий контакт" + RESET)
    print(book.add_record(Record("tom", "0995648525", birthday="08-11-1986")))

    print(
        GREEN + "     створюємо новий контакт, у якого тільки день народження" + RESET
    )
    print(book.add_record(Record("helen", birthday="11-11-1999")))

    print(GREEN + "     змінюємо ім'я 'tom' на 'thomas'" + RESET)
    print(book.change_name("tom", "thomas"))

    print(GREEN + "     створюємо новий контакт, у якого є тільки ім'я" + RESET)
    print(book.add_record(Record("jerry")))

    print(GREEN + "     створюємо новий контакт" + RESET)
    print(book.add_record(Record("garry", "0995647821", birthday="08-12-1975")))

    print(GREEN + "     створюємо новій контакт в 3 дії" + RESET)
    name = "bill"
    phone = "0677977166"
    # b_day = "27-10-1968"
    # rec = Record(name, phone, b_day)
    rec = Record(name, phone)
    print(book.add_record(rec))

    print(GREEN + "     додаємо дату народження контакту" + RESET)
    print(rec.add_birthday("10-11-2005"))

    print(GREEN + "     намагаємось додати вже існуючий телефон" + RESET)
    result = rec.add_phone("0677977166")
    print(result)

    print(GREEN + "     додаємо другий телефон" + RESET)
    print(rec.add_phone("0933903357"))

    print(GREEN + "     намагаємося поміняти телефон на такий самий" + RESET)
    print(rec.edit_phone("0677977166", "+380677977166"))

    print(GREEN + "     міняємо номер телефона на інший" + RESET)
    print(rec.edit_phone("0677977166", "0997058845"))

    print(GREEN + "     намагаємося поміняти неіснуючий номер телефона" + RESET)
    print(rec.edit_phone("0671234567", "1234567809"))

    print(GREEN + "     намагаємося видалити неіснуючий номер телефона" + RESET)
    print(rec.remove_phone("0677977166"))

    print(GREEN + "     видаляємо один з номерів телефону" + RESET)
    print(rec.remove_phone("0997058845"))

    print(GREEN + "     додаємо ще один номер" + RESET)
    print(rec.add_phone("0677977166"))

    print(GREEN + "     шукаємо номер" + RESET)
    print(rec.find_phone("0677977166"))

    print(GREEN + "     шукаємо номер" + RESET)
    print(rec.find_phone("0933903357"))

    print(GREEN + "     шукаємо неіснуючий номер" + RESET)
    print(rec.find_phone("0677977444"))

    print(GREEN + "     додаємо новий контакт" + RESET)
    print(book.add_record(Record("ivan", "0671234567")))

    print(GREEN + "     додаємо новий контакт" + RESET)
    print(book.add_record(Record("mary", "0671234555", "9-11-2000")))

    print(GREEN + "     додаємо новий контакт" + RESET)
    print(book.add_record(Record("jill", "0672223344", birthday="07-11-2012")))

    print(GREEN + "     шукаємо контакт" + RESET)
    print(book.find_name("bill"))

    print(GREEN + "     змінюємо ім'я 'bill' на 'billy'" + RESET)
    print(book.change_name("bill", "billy"))

    print(GREEN + "     шукаємо неіснуючий контакт" + RESET)
    print(book.find_name("john"))

    print(GREEN + "     перелік контактів до видалень контактів" + RESET)
    print("======= before delete =========")
    print(book)

    print(GREEN + "     зберігаємо контакти" + RESET)
    print(book.write_contacts_to_file(filename))

    print(GREEN + "     видаляємо 5 контактів" + RESET)
    print(book.delete_record("mary"))
    print(book.delete_record("tom"))
    print(book.delete_record("ivan"))
    print(book.delete_record("jill"))
    print(book.delete_record("billy"))

    print(GREEN + "     перелік контактів після видалень" + RESET)
    print("======== after delete ========")
    print(book)

    print(GREEN + "     відновлюємо контакти з файлу" + RESET)
    book = book.read_contacts_from_file(filename)

    print(
        GREEN
        + "     перелік контактів після відновлення (такий самий, як до видалення)"
        + RESET
    )
    print(
        GREEN
        + "     додано сортування контактів за алфавітом - відбувається під час читання файлу"
        + RESET
    )
    print("======== after restoring from a file ========")

    print(GREEN + "     перелік контактів" + RESET)
    print(book)

    print("======== Address fields ========")
    print(GREEN + "     додаємо адресу" + RESET)
    print(rec.add_address("Lviv"))
    print(rec.remove_address())
    print(rec.add_address("10001, New York, Manhattan 123b"))
    print(GREEN + "     перелік контактів" + RESET)
    print(book)

    print("======== Email fields ========")
    print(GREEN + "     додаємо email" + RESET)
    #print(rec.add_email("XXXXXXXXXXXXXX"))
    print(rec.add_email("asd@mail.com"))
    print(rec.remove_email("asdddd@mail.com"))
    print(rec.edit_email("asd@mail.com", "new_mail@mail.com"))
    print(rec.add_email("second@mail.com"))
    print(GREEN + "     перелік контактів" + RESET)
    print(book)

