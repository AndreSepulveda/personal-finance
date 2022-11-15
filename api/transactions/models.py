from typing import Any

from sqlalchemy import Column, ForeignKey, ForeignKeyConstraint, DateTime, Float, Integer, String
from sqlalchemy.orm import relationship

from api.db import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    currency_id = Column(Integer, ForeignKey("currencies.id"))
    total_price = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False)
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=False)
    actor_id = Column(Integer, nullable=False)
    cancelled_at = Column(DateTime, nullable=True)
    cancel_reason = Column(String(255), nullable=True)
    group_id = Column(Integer, nullable=False)
    category_id = Column(Integer, nullable=False)
    subcategory_id = Column(Integer, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(["actor_id", "group_id"], ["group_members.member_id", "group_members.group_id"]),
    )

    # actor = relationship("Actor", back_populates="actor_transactions")

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)


class TransactionSplit(Base):
    __tablename__ = "transaction_split"

    transaction_id = Column(Integer, nullable=False)
    actor_id = Column(Integer, nullable=False)
    transaction_perc = Column(Float, nullable=False)
    __table_args = (
        ForeignKeyConstraint(["transaction_id", "actor_id"], ["transactions.id", "transactions.actor_id"])
    )

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, auto_increment=True)
    label = Column(String(50), nullable=False)

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)


class SubCategory(Base):
    __tablename__ = "subcategories"

    id = Column(Integer, primary_key=True, auto_increment=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)


class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True, auto_increment=True)
    currency_code = Column(String(5), nullable=False)

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, auto_increment=True)
    city = Column(String(55), nullable=False)
    province = Column(String(5), nullable=False)
    country_name = Column(String(55), nullable=False)
    country_code = Column(String(5), nullable=False)

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
