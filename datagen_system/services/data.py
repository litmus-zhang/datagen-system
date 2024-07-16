from typing import Annotated
import mimesis
import random
import uuid


class DataGenerator:
    def __init__(self):
        self.person = mimesis.Person()
        self.address = mimesis.Address()
        self.datetime = mimesis.Datetime()
        self.transaction = mimesis.Payment()

    def generate_person(self):
        return {
            "name": self.person.full_name(),
            "email": self.person.email(),
            "age": self.person.birthdate(),
            "phone": self.person.telephone(),
            "country": self.person.nationality(),
            "id": str(uuid.uuid4()),
        }

    def generate_address(self):
        return {
            "address": self.address.address(),
            "city": self.address.city(),
            "country": self.address.country(),
        }

    def generate_datetime(self):
        return {
            "date": self.datetime.date(),
            "time": self.datetime.time(),
            "timestamp": self.datetime.timestamp(),
        }

    def generate_transaction(self, type: Annotated[str, ["card", "crypto"]]):
        if type == "card":
            return {
                "amount": round(random.random() * 1_000, 2),
                "card expiry": self.transaction.credit_card_expiration_date(),
                "card number": self.transaction.credit_card_number(),
                "cvv": self.transaction.cvv(),
                "card owner": self.transaction.credit_card_owner(),
                "card network": self.transaction.credit_card_network(),
                "txn date": self.datetime.date().isoformat(),
                "txn id": str(uuid.uuid4()),
            }
        elif type == "crypto":
            return {
                "amount": round(random.random() * 1_000, 5),
                "crypto address": self.transaction.bitcoin_address(),
                "crypto currency": self.transaction.random(["BTC", "ETH", "LTC"]),
                "date": self.datetime.date().isoformat(),
                "txn id": str(uuid.uuid4()),
            }
