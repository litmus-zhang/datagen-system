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
        self.general = mimesis.Generic()
        self.financial = mimesis.Finance()
        self.text = mimesis.Text()

    def generate_person(self):
        return {
            "name": self.person.full_name(),
            "email": self.person.email(),
            "date of birth": self.person.birthdate().isoformat(),
            "phone": self.person.telephone(),
            "country": self.person.nationality(),
            "id": str(uuid.uuid4()),
            "gender": self.person.gender(),
        }

    def generate_cashflow(self):
        return {
            "to": self.generate_person(),
            "from": self.generate_person(),
            "amount": self.financial.price(),
            "date": self.datetime.date().isoformat(),
            "txn-id": str(uuid.uuid4()),
            "currency": random.choice(["USD", "EUR", "GBP"]),
            "description": self.text.sentence(),
        }

    def generate_credit_score(self):
        return {
            "date": self.datetime.date().isoformat(),
            "user": self.generate_person(),
            "score": self.general.random.randint(300, 850),
        }

    def generate_transaction(self, type: Annotated[str, ["card", "crypto"]]):
        if type == "card":
            return {
                "amount": round(random.random() * 1_000_000, 2),
                "cvv": self.transaction.cvv(),
                "card owner": self.transaction.credit_card_owner(),
                "card network": self.transaction.credit_card_network(),
                "currency": random.choice(["USD", "EUR", "GBP"]),
                "txn date": self.datetime.date().isoformat(),
                "txn id": str(uuid.uuid4()),
            }
        elif type == "crypto":
            return {
                "amount": round(random.random() * 1_000, 5),
                "crypto address": self.transaction.bitcoin_address(),
                "crypto currency": self.financial.cryptocurrency_symbol().capitalize(),
                "txn date": self.datetime.date().isoformat(),
                "txn id": str(uuid.uuid4()),
            }
