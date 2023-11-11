from collections import UserDict
from constants import RED, GRAY, CYAN, MAGENTA, RESET, LEN_OF_NAME_FIELD
from datetime import datetime
import os.path
import pickle
import re


class PhoneError(Exception):
    ...

class EmailError(Exception):
    ...

class BDayError(Exception):
    ...

class NoContactError(Exception):
    ...


class Field:
    def __init__(self, value) -> None:
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self)


class Name(Field):
    def __init__(self, value: str) -> None:
        super().__init__(str(value).title())


class Phone(Field):
    def __eq__(self, __value: object) -> bool:
        return self.value == __value.value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, phone: str):
        new_phone = str(phone).strip()
        for char in "+( )-.":
            new_phone = new_phone.replace(char, "")
        if len(new_phone) >= 9 and new_phone.isdigit():
            new_phone = "+380" + new_phone[-9:]
        else:
            raise PhoneError(f"{RED}{phone} - incorrect phone number{RESET}")
        self.__value = new_phone

class Email(Field):
    def __eq__(self, __value: object) -> bool:
        return self.value == __value.value
    
    def find_all_emails(text):
        result = re.findall(r"[A-z.]+\w+@[A-z]+\.[A-z]{2,}", text)
        return result

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, email: str):
        new_email = str(email).strip()
        # extend vemail check
        #if "@" in new_email and "." in new_email:
        if re.findall(r"[A-z.]+\w+@[A-z]+\.[A-z]{2,}", new_email):
            self.__value = new_email
        else:
            raise EmailError(f"{RED}{new_email} - invalid email, the email must contains only letters, digits, @ and .{RESET}")
        #self.__value = new_email

    def __str__(self) -> str:
        return f"{self.value}" if self.value else ""



class BirthDay(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if isinstance(value, datetime):
            self.__value = value
        else:
            try:
                self.__value = datetime.strptime(str(value), "%Y-%m-%d").date()
            except ValueError:
                self.__value = datetime.strptime(str(value), "%d-%m-%Y").date()
            else:
                raise BDayError(f"{RED}{self.__value} - incorrect date{RESET}")

    def __str__(self) -> str:
        return str(self.value)
    
class Address(Field):
    def __init__(self, value: str) -> None:
        super().__init__(str(value).title())

    def __str__(self) -> str:
        return f"Address: {self.value}" if self.value else ""


class Record:
    def __init__(
        self, name: Name, phone: Phone | None = None, birthday: BirthDay | None = None, email: Email | None = None, address: Address | None = None 
    ) -> None:
        self.name = Name(name)
        self.phones = [Phone(phone)] if phone else []
        self.emails = [Email(email)] if email else []
        self.birthday = BirthDay(birthday) if birthday else None
        self.address = Address(address) if address else None

    def add_birthday(self, birthday: BirthDay):
        self.birthday = BirthDay(birthday)
        return f"the date of birth for contact {self.name} is set to {self.datetime_to_str(self.birthday)} \n\t{self}"
    
    def add_address(self, address: Address):
        self.address = Address(address)
        return f"the address for contact {self.name} is set to {self.address} \n\t{self}"

    def add_phone(self, phone: Phone) -> str:
        phone = Phone(phone)
        if phone in self.phones:
            return f"{RED}number {phone} is already present in {self.name}'s contact list {RESET} \n\t{self}"
        self.phones.append(phone)
        return f"phone number {phone} has been added to {self.name}'s contact list  \n\t{self}"
    
    def add_email(self, email: Email) -> str:
        email = Email(email)
        if email in self.emails:
            return f"{RED}email {email} is already present in {self.name}'s contact list {RESET} \n\t{self}"
        self.emails.append(email)
        return f"email {email} has been added to {self.name}'s contact list  \n\t{self}"

    def datetime_to_str(self, date):
        date_to_str = str(date)
        return (
            date_to_str
            if all([date_to_str[2] == "-", date_to_str[5] == "-"])
            else date_to_str[8:] + "-" + date_to_str[5:7] + "-" + date_to_str[:4]
        )

    def days_to_birthday(self, birthday: BirthDay):
        today_date = datetime.today().date()
        try:
            birth_date = datetime.strptime(str(birthday), "%Y-%m-%d").date()
        except ValueError:
            birth_date = datetime.strptime(str(birthday), "%d-%m-%Y").date()
        bd_next = datetime(
            day=birth_date.day, month=birth_date.month, year=today_date.year
        )
        age = today_date.year - birth_date.year
        if today_date > bd_next.date():
            bd_next = datetime(
                day=birth_date.day, month=birth_date.month, year=today_date.year + 1
            )
            age += 1
        days_until = (bd_next.date() - today_date).days
        return days_until, age

    def edit_phone(self, old_phone: Phone, new_phone: Phone) -> str:
        old_phone = Phone(old_phone)
        new_phone = Phone(new_phone)
        if old_phone == new_phone:
            return f"{RED}you are trying to replace the phone number {old_phone} with the same one {new_phone}{RESET} \n\t{self}"
        if old_phone in self.phones:
            self.phones[self.phones.index(old_phone)] = new_phone
            return f"phone number {old_phone} has been successfully changed to {new_phone} for contact {self.name} \n\t{self}"
        return f"{RED}phone number {old_phone} is not among the contact numbers of {self.name}{RESET} \n\t{self}"
    
    def edit_email(self, old_email: Email, new_email: Email) -> str:
        old_email = Email(old_email)
        new_email = Email(new_email)
        if old_email == new_email:
            return f"{RED}you are trying to replace the email {old_email} with the same one {new_email}{RESET} \n\t{self}"
        if old_email in self.emails:
            self.emails[self.emails.index(old_email)] = new_email
            return f"email {old_email} has been successfully changed to {new_email} for contact {self.name} \n\t{self}"
        return f"{RED}email {old_email} is not among the contact numbers of {self.name}{RESET} \n\t{self}"


    def find_phone(self, phone: Phone):
        phone = Phone(phone)
        for ph in self.phones:
            if ph == phone:
                return f"phone number {phone} found among {self.name}'s contact numbers"
        return f"{RED}phone number {phone} not found {RESET}"
    
    def find_email(self, email: Email):
        email = Email(email)
        for em in self.emails:
            if em == email:
                return f"email {email} found among {self.name}'s contact numbers"
        return f"{RED}email {email} not found {RESET}"

    def remove_phone(self, phone: Phone):
        phone = Phone(phone)
        if phone not in self.phones:
            return f"{RED}phone number {phone} is not among the contact numbers of {self.name} {RESET}\n\t{self}"
        self.phones.remove(phone)
        return f"phone number {phone} has been removed from {self.name}'s contact list \n\t{self}"
    
    def remove_email(self, email: Email):
        email = Email(email)
        if email not in self.emails:
            return f"{RED}email {email} is not among the contact numbers of {self.name} {RESET}\n\t{self}"
        self.emails.remove(email)
        return f"email {email} has been removed from {self.name}'s contact list \n\t{self}"
    
    def remove_address(self):
        self.address = None
        return f"address of {self.name} has been removed \n\t{self}"

    def seek_phone(self, phone: Phone):
        for p in self.phones:
            ph = p.value[:]
            if str(phone) in str(ph):
                return True
            else:
                return False
            
    def seek_email(self, email: Email):
        for e in self.emails:
            em = e.value[:]
            if str(email) in str(em):
                return True
            else:
                return False

    def __str__(self) -> str:
        blanks = " " * (LEN_OF_NAME_FIELD - len(str(self.name)))
        emails_str = ", ".join(str(e) for e in self.emails)
        address_str = self.address if self.address else ""
        if self.birthday:
            if int(self.days_to_birthday(self.birthday)[0]) == 0:
                return f"{self.name} {blanks}: {', '.join(str(p) for p in self.phones)} {emails_str} {MAGENTA} birthday: {RESET} {self.datetime_to_str(self.birthday)} {MAGENTA}(today is {self.days_to_birthday(self.birthday)[1]}th birthday){RESET} {address_str}"
            elif self.days_to_birthday(self.birthday)[0] <= 7:
                return f"{self.name} {blanks}: {', '.join(str(p) for p in self.phones)} {emails_str} {GRAY} birthday: {RESET} {self.datetime_to_str(self.birthday)} {GRAY}({self.days_to_birthday(self.birthday)[0]} days until the {self.days_to_birthday(self.birthday)[1]}th birthday){RESET} {address_str}"
            else:
                return f"{self.name} {blanks}: {', '.join(str(p) for p in self.phones)} {emails_str} {GRAY} birthday: {RESET} {self.datetime_to_str(self.birthday)} {GRAY}({self.days_to_birthday(self.birthday)[0]} days until the {self.days_to_birthday(self.birthday)[1]}th birthday){RESET} {address_str}"
        else:
            return f"{self.name} {blanks}: {', '.join(str(p) for p in self.phones)} {emails_str} {address_str}"

    def __repr__(self) -> str:
        return str(self)


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
        return f"contact {record.name} has been successfully added \n\t{record}"

    def change_name(self, name: Name, new_name: Name):
        name = Name(name)
        for key in self.data:
            if str(key) == str(name):
                rec: Record = self.get(key)
        new_record = Record(
            Name(new_name),
            birthday=rec.datetime_to_str(rec.birthday) if rec.birthday else None,
        )
        for phone in rec.phones:
            new_record.add_phone(phone)
        self.add_record(new_record)
        self.delete_record(name)
        return f"the name of the contact {Name(name)} has been changed to {Name(new_name)} \n\t{new_record}"

    def delete_record(self, name: Name):
        # if name in self.data:
        #     del self.data[name]
        name = Name(name)
        for key, item in self.data.items():
            if str(key) == str(name):
                del self.data[key]
                return f"contact {name} has been successfully deleted"
        return f"{RED}contact {name} not found{RESET}"

    def find_name(self, name: Name):
        # self.data.get(name, None)
        name = Name(name)
        for key, item in self.data.items():
            if str(key) == str(name):
                return f"contact {name} found \n\t{item}"
        return f"{RED}contact {name} not found{RESET}"

    def iterator(self, n=None):
        counter = 0
        while counter < len(self):
            yield list(self.values())[counter : counter + n]
            counter += n

    def read_contacts_from_file(self, fn):
        if os.path.exists(fn):
            with open(fn, "rb") as fh:
                self = pickle.load(fh)
            self.data = dict(sorted(self.items()))
        print(f"{GRAY}the contact book has been successfully restored{RESET}")
        return self

    def write_contacts_to_file(self, fn):
        with open(fn, "wb") as fh:
            pickle.dump(self, fh)
        return f"{GRAY}the contact book has been saved successfully{RESET}"

    def __getitem__(self, key: str) -> Record:
        return self.data[key]

    def __str__(self):
        return "\n".join([str(r) for r in self.data.values()])
