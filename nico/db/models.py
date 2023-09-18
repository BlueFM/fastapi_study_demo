import time

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True, comment="主键id")
    username = Column(String(20), nullable=False, comment="用户名")
    password_hash = Column(String(128), nullable=False, comment="哈希密码")
    email = Column(String(64), nullable=False, comment="邮箱")
    created_at = Column(Integer, nullable=False, default=int(time.time()), comment="创建时间")


class StrayCatInfo(Base):
    __tablename__ = "stray_cat_info"

    cat_id = Column(Integer, primary_key=True, autoincrement=True, comment="主键id")
    title = Column(String(20), nullable=False, comment="标题")
    description = Column(String(128), nullable=False, comment="描述")
    image_url = Column(String(128), nullable=False, comment="图片地址")
    location_lat = Column(Float, nullable=False, comment="纬度")
    location_lng = Column(Float, nullable=False, comment="经度")
    created_at = Column(Integer, nullable=False, default=int(time.time()), comment="创建时间")


class Comment(Base):
    __tablename__ = "comments"

    comment_id = Column(Integer, primary_key=True, autoincrement=True, comment="主键id")
    user_id = Column(Integer,ForeignKey("users.user_id"), nullable=False, comment="用户id")
    cat_id = Column(Integer,ForeignKey("stray_cat_info.cat_id"), nullable=False, comment="猫猫id")
    content = Column(String(128), nullable=False, comment="评论内容")
    created_at = Column(Integer, nullable=False, default=int(time.time()), comment="创建时间")
