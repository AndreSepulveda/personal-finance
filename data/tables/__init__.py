import csv
from datetime import timezone
from dateutil.relativedelta import relativedelta
from random import randint, random


class Row:
    def to_csv(self, file):
        try:
            with open(file, 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.__dict__.keys(), quoting=csv.QUOTE_NONNUMERIC)
                for data in [self.__dict__]:
                    writer.writerow(data)
        except IOError:
            print("I/O error")


class Actors(Row):
    def __init__(self, i, fake):
        self.id = i
        self.first_name = fake.first_name_male() if i % 2 == 0 else fake.first_name_female()
        self.last_name = fake.last_name()
        self.gender = 'Male' if i % 2 == 0 else 'Female'
        self.email = fake.email()


class Groups(Row):
    def __init__(self, i, fake):
        self.id = i
        self.label = fake.text(max_nb_chars=15)
        self.description = fake.text(max_nb_chars=120)
        self.creator_id = randint(1, 100)
        self.created_at = fake.date_time_this_year(before_now=True, tzinfo=timezone.utc)
        self.deleted_at = self.created_at + relativedelta(months=+randint(0, 6)) if i % 3 == 0 else None


class GroupMembers(Row):
    def __init__(self, i, join, member):
        self.group_id = i
        self.member_id = member
        self.joined_at = join
        self.left_at = self.joined_at + relativedelta(days=+randint(0, 45)) if i % 7 == 0 else None


class Transactions(Row):
    def __init__(self, i, fake, actor):
        self.id = i
        self.currency_id = randint(1, 4)
        self.total_price = round(random(), 2)
        self.created_at = fake.date_time_this_year(before_now=True, tzinfo=timezone.utc)
        self.location_id = randint(1, 5)
        self.actor_id = actor
        self.cancelled_at = self.created_at + relativedelta(days=+randint(0, 60)) if i % 27 == 0 else None
        self.cancel_reason = fake.text(max_nb_chars=10) if i % 27 == 0 else None
        self.group_id = randint(1, 50)
        self.category_id = randint(1, 3)
        self.subcategory_id = randint(1, 15)


class TransactionSplit(Row):
    class_id = 0

    def __init__(self, actor_id, perc):
        self.id = self.class_id + 1
        self.actor_id = actor_id
        self.transaction_perc = perc
