from dateutil.relativedelta import relativedelta
from random import randint

from faker import Faker
from tables import Transactions, TransactionSplit, Actors, Groups, GroupMembers

"""
Need to take a quick look at the created entries on each csv
as the fake class might create some text with line break 
and this would cause some problems at the csv
"""
fake = Faker()

for i in range(1, 101):
    actor = Actors(i, fake)
    actor.to_csv(file='./csv/actors.csv')

for i in range(1, 51):
    group = Groups(i, fake)
    group.to_csv(file='./csv/groups.csv')

    member_creator = GroupMembers(i, join=group.created_at, member=group.creator_id)
    member_creator.to_csv(file='./csv/groupmembers.csv')
    member = randint(1, 100)
    member_another = GroupMembers(i, join=group.created_at + relativedelta(days=+randint(0, 7)),
                                  member=member if member != group.creator_id else member + 1)
    member_another.to_csv(file='./csv/groupmembers.csv')

    for j in range(1, randint(10, 45)):
        transaction = Transactions(j, fake, actor=member_creator.member_id)
        transaction.to_csv(file='./csv/transactions.csv')

        if randint(1, 2) == 1:
            transaction_split_1 = TransactionSplit(member_creator.member_id, 100)
            transaction_split_1.__class__.class_id += 1
        else:
            transaction_split_1 = TransactionSplit(member_creator.member_id, 50)
            transaction_split_1.__class__.class_id += 1
            transaction_split_2 = TransactionSplit(member_another.member_id, 50)
            transaction_split_2.to_csv(file='./csv/transacionssplit.csv')
            transaction_split_2.__class__.class_id += 1
        transaction_split_1.to_csv(file='./csv/transacionssplit.csv')
