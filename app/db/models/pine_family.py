import time

from sqlalchemy import Column, Integer, String, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PineFamily(Base):
    __tablename__ = "pine_family"

    pk_id = Column(Integer, primary_key=True, autoincrement=True, comment="主键id")
    name = Column(String(20), nullable=False, comment="姓名")
    sex = Column(String(20), nullable=False, comment="性别")
    age = Column(SMALLINT, nullable=False, comment="年龄")
    profession = Column(String(20), nullable=False, comment="职业")
    hobby = Column(String(20), nullable=False, comment="爱好")
    motto = Column(String(50), nullable=False, comment="座右铭")
    add_time = Column(Integer, nullable=False, default=int(time.time()), comment="添加时间")
    is_delete = Column(SMALLINT, nullable=False, default=0, comment="是否删除")

    @staticmethod
    def to_dict(data: list, fields: list):
        result = list()
        for d in data:
            data_dict = dict()
            for index in range(len(fields)):
                data_dict[fields[index]] = d[index]
            result.append(data_dict)
        return result
