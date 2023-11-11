from constants import GREEN, RESET
from main import (
    book,
    help_page,
    add_contact,
    change_phone,
    change_name,
    del_phone,
    add_birthday,
    add_phones,
    name_find,
    search,
    show_all,
    delete_record,
)

# =============================================
#             test 2 (functions)
# =============================================

if __name__ == "__main__":
    filename = "book_test_2.bin"

    print(" ================== test 2 ===============")
    print(GREEN + "     виводимо help" + RESET)
    print(help_page())

    print(GREEN + "\n     додаємо новий контакт" + RESET)
    print(add_contact("Jill", "0677977166"))
    print(GREEN + "     намагаємося повторно додати той самий контакт" + RESET)
    print(add_contact("Jill", "0677977167"))
    print(GREEN + "\n     додаємо дату народження" + RESET)
    print(add_birthday("Jill", "06-11-1995"))
    print(GREEN + "     додаємо контакт з датою народження" + RESET)
    print(add_contact("Bill", "0997058845", "15-03-1999"))

    print(GREEN + "     додаємо контакт у якого 3 телефони та дата народження" + RESET)
    print(
        add_contact("Bill_t", "0997078845", "099 745-12-35", "0964523265", "13-11-2002")
    )

    print(GREEN + "\n     додаємо контакт у якого 4 телефони" + RESET)
    print(
        add_contact("Jill_t", "0677977176", "0956783423", "0669873456", "050 345 22 34")
    )
    print(
        GREEN
        + "\n     намагаємося додати новий номер до контакту, що вже існує, командою add_contact"
        + RESET
    )
    print(add_contact("Jill_t", "0677977188"))
    print(GREEN + "     робимо те саме, але правильно - командою add_phones" + RESET)
    print(add_phones("Jill_t", "0677977188"))
    print(
        GREEN
        + "     а тепер додаємо контакту ще 2 номери (однією командою add_phones)"
        + RESET
    )
    print(add_phones("Jill_t", "0677977155", "0668528526"))

    print(GREEN + "\n     міняємо номер телефону контакту" + RESET)
    print(change_phone("Jill_t", "0677977176", "0954122568"))
    print(
        GREEN + "     намагаємося поміняти номер, що не існує у даного контакту" + RESET
    )
    print(change_phone("Jill_t", "0677977176", "0954122568"))
    print(GREEN + "     намагаємося поміняти номер на такий самий" + RESET)
    print(change_phone("Jill_t", "0954122568", "+380954122568"))

    print(GREEN + "\n     видаляємо один з номерів контакту" + RESET)
    print(del_phone("Jill_t", "0503452234"))
    print(GREEN + "     намагаємося видалити номер, якого не існує" + RESET)
    print(del_phone("Jill_t", "0954122599"))
    print(
        GREEN + "     намагаємося видалити номер контакту, якого нема у списку" + RESET
    )
    print(del_phone("Jill_v", "0954122599"))

    print(GREEN + "\n     додаємо день народження існуючому контакту" + RESET)
    print(add_birthday("Jill_t", "28-03-1968"))

    print(GREEN + "\n     міняємо ім'я існуючого контакту!" + RESET)
    print(change_name("jill_t", "jill_v"))

    print(GREEN + "     ще раз міняємо ім'я контакту!" + RESET)
    print(change_name("Jill_v", "jill_n"))

    print(
        GREEN
        + "     намагаємося поміняти ім'я контакту, але не вказуємо нового імені"
        + RESET
    )
    print(change_name("jill_n"))

    print(GREEN + "\n     видаляємо існуючий контакт" + RESET)
    print(delete_record("jill_n"))

    print(GREEN + "     намагаємося видалити контакт, що вже не існує" + RESET)
    print(delete_record("jill_t"))

    print(GREEN + "\n     шукаємо всі записи, де є рядок '45'" + RESET)
    print(search("45"))
    print(GREEN + "     шукаємо всі записи, де є рядок 'ill'" + RESET)
    print(search("ill"))
    print(GREEN + "     забуваємо ввести строку для пошуку" + RESET)
    print(search())
    print(GREEN + "     шукаємо контакт за іменем (рудимент з минулих ДЗ)" + RESET)
    print(name_find("bill_t"))

    print(GREEN + "\n     друкуємо список контактів" + RESET)
    print(show_all())

    print(GREEN + "     зберігаємо список контактів" + RESET)
    print(book.write_contacts_to_file("book_test_2.bin"))

    # відновлення контактів з файлу успішно працює в тесті класів та в самому боті

    print(GREEN + "     видаляємо 2 контакти зі списку" + RESET)
    print(delete_record("Jill"))
    print(delete_record("Bill"))

    print(GREEN + "     друкуємо список контактів" + RESET)
    print(show_all())

    print(GREEN + "     відновлюємо список контактів з файлу" + RESET)

    add_contact("jill", "+380677977166", "12-11-1995")
    add_contact("Bill", "+380997058845", "15-03-1999")

    book = book.read_contacts_from_file("book_test_2.bin")

    print(GREEN + "     друкуємо відновлений список контактів" + RESET)
    print(show_all())

    print(GREEN + "\n     додаємо кілька нових контактів" + RESET)
    print(add_contact("Person_0", "(099)475-71-22"))
    print(add_contact("Person_9", "(099)475-31-11"))
    print(add_contact("Person_1", "(066)4525588", "10-11-1998"))
    print(add_contact("Person_7", "099 225 55 66", "22-04-1870"))
    print(add_contact("Person_2", "0675468899", "0997061212", "11-11-2001"))
    print(add_contact("Person_6", "0987654321", "09-11-1999"))
    print(add_contact("Person_3", "+38(098)221-15-44", "14-08-1988"))
    print(add_contact("Person_8", "0958645548", "08-11-1967"))
    print(add_contact("Person_4", "+380664589955", "07-11-1968"))
    print(add_contact("Person_5", "674567890", "0660554488"))

    print(
        GREEN
        + "     а тепер додаємо контакту, що НЕ існує номер телефону"
        + RESET
    )
    print(add_phones("Jill_e", "0677977155"))
    
    print(GREEN + "\n     додаємо день народження контакту, що НЕ існує" + RESET)
    print(add_birthday("Jill_e", "28-03-1968"))


    print(GREEN + "\n     друкуємо список контактів по 10 рядків на сторінку" + RESET)
    # print(show_all(10)

    print(show_all())
