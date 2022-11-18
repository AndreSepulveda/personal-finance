from typing import Any

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base


class Actor(Base):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False)

    # groups = relationship("Group", back_populates="group_actors")
    # transactions = relationship("Transaction", back_populates="transaction_actor")

    def __init__(self, first_name, last_name, gender, email, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email


class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, autoincrement=True)
    label = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    creator_id = Column(Integer, ForeignKey("actors.id"), nullable=False)
    created_at = Column(DateTime, nullable=False)
    deleted_at = Column(DateTime, nullable=True)

    # actors = relationship("Actor", back_populates="actor_groups")

    def __init__(self, label, description, creator_id, created_at, deleted_at, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.label = label
        self.description = description
        self.creator_id = creator_id
        self.created_at = created_at
        self.deleted_at = deleted_at


class GroupMember(Base):
    __tablename__ = "group_members"

    group_id = Column(Integer, ForeignKey("groups.id"), primary_key=True, nullable=False)
    member_id = Column(Integer, ForeignKey("users.id"), primary_key=True, nullable=False)
    joined_at = Column(DateTime, nullable=False)
    left_at = Column(DateTime, nullable=True)

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)