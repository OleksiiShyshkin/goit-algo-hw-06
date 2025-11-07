from __future__ import annotations
from collections import UserDict
import re
from typing import List, Optional


class Field:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value: str):
        v = (value or "").strip()
        if not v:
            raise ValueError("Name cannot be empty.")
        super().__init__(v)


class Phone(Field):
    _re = re.compile(r"^\d{10}$")

    def __init__(self, value: str):
        v = (value or "").strip()
        if not Phone._re.fullmatch(v):
            raise ValueError("Phone must be exactly 10 digits.")
        super().__init__(v)


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: List[Phone] = []

    def add_phone(self, phone: str) -> None:
        self.phones.append(Phone(phone))

    def find_phone(self, phone: str) -> Optional[Phone]:
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def remove_phone(self, phone: str) -> None:
        target = self.find_phone(phone)
        if not target:
            raise ValueError("Phone not found.")
        self.phones.remove(target)

    def edit_phone(self, old_phone: Optional[str], new_phone: str) -> None:
        if old_phone is None:
            if len(self.phones) == 1:
                replacement = Phone(new_phone)
                self.phones[0].value = replacement.value
                return
            raise ValueError("Specify old phone explicitly when contact has 0 or more than 1 phone.")

        target = self.find_phone(old_phone)
        if not target:
            raise ValueError("Old phone not found.")
        replacement = Phone(new_phone)
        target.value = replacement.value

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones) if self.phones else "—"
        return f"Contact name: {self.name.value}, phones: {phones}"


class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Optional[Record]:
        return self.data.get(name)

    def delete(self, name: str) -> None:
        if name in self.data:
            del self.data[name]

    def __str__(self) -> str:
        if not self.data:
            return "AddressBook is empty."
        lines = [str(self.data[k]) for k in sorted(self.data.keys())]
        return "\n".join(lines)
