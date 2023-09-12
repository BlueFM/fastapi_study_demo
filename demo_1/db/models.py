import time

from sqlalchemy import Column, Integer, String, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Cat(Base):
    __tablename__ = "cats"

    pk_id = Column(Integer, primary_key=True, autoincrement=True, comment="主键id")
    name = Column(String(20), nullable=False, comment="猫猫名字")
    breed = Column(String(20), nullable=False, comment="猫猫品种")
    skin_color = Column(String(20), nullable=False, comment="猫猫皮肤颜色")
    age = Column(SMALLINT, nullable=False, comment="猫猫年龄")
    owner = Column(String(20), nullable=False, comment="猫猫主人")
    add_time = Column(Integer, nullable=False, default=int(time.time()), comment="添加时间")
    is_delete = Column(SMALLINT, nullable=False, default=0, comment="是否删除")

    @staticmethod
    def to_dict(data: list, fields: list):
        data_dict = dict()
        for index in range(len(fields)):
            data_dict[fields[index]] = data[index]
        return data_dict
