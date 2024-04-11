from datetime import datetime
from uuid import uuid4

from sqlalchemy import (
    DECIMAL,
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.dialects.postgresql import UUID

from core import database as db


class Category(db.Model):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    slug = Column(String, nullable=False, unique=True)
    is_active = Column(
        Boolean, nullable=False, server_default=str(False), default=False
    )
    parent_id = Column(Integer, ForeignKey(column="category.id"))


class Product(db.Model):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    p_uid = Column(UUID(as_uuid=True), unique=True, nullable=False, default=uuid4)
    name = Column(String, nullable=False, unique=True)
    slug = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=True)
    is_digital = Column(
        Boolean, nullable=False, server_default=str(False), default=False
    )

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=True, onupdate=datetime.utcnow)

    category_id = Column(Integer, ForeignKey(column="category.id"))
    seasonal_event = Column(
        Integer, ForeignKey(column="seasonal_event.id"), nullable=True
    )

    is_active = Column(
        Boolean, nullable=False, server_default=str(False), default=False
    )
    stock_status = Column(String, server_default="OUT_OF_STOCK", nullable=False)


class ProductLine(db.Model):

    __tablename__ = "product_line"

    id = Column(Integer, primary_key=True)
    price = Column(DECIMAL(precision=5, scale=2), nullable=False)
    sku = Column(UUID(as_uuid=True), unique=True, nullable=False, default=uuid4)
    stock_qty = Column(Integer, default=0)
    is_active = Column(Boolean, nullable=False, default=False)
    order = Column(Integer)
    weight = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    product_id = Column(Integer, ForeignKey(column="product.id"))


class ProductImage(db.Model):
    __tablename__ = "product_image"
    id = Column(Integer, primary_key=True)
    alternative_text = Column(String, nullable=False)
    url = Column(String, nullable=False)
    order = Column(Integer, nullable=False)
    product_line_id = Column(Integer, ForeignKey(column="product_line.id"))


class SeasonalEvent(db.Model):

    __tablename__ = "seasonal_event"
    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    name = Column(String, unique=True)


class ProductType(db.Model):
    __tablename__ = "product_type"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    parent_id = Column(Integer, ForeignKey(column="product_type.id"), nullable=True)


class Attribute(db.Model):
    __tablename__ = "attribute"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)


class AttributeValue(db.Model):
    __tablename__ = "attribute_value"
    id = Column(Integer, primary_key=True)
    attribute_value = Column(String)
    attribute_id = Column(Integer, ForeignKey(column="attribute.id"))


class Product_ProductType(db.Model):
    __tablename__ = "product_product_type"

    id = Column(Integer, primary_key=True)
    product_type_id = Column(Integer, ForeignKey(column="product_type.id"))
    product_id = Column(Integer, ForeignKey(column="product.id"))


class ProductLine_AttributeValue(db.Model):
    __tablename__ = "product_line_attribute_value"
    id = Column(Integer, primary_key=True)
    attribute_value_id = Column(Integer, ForeignKey("attribute_value.id"))
    product_line_id = Column(Integer, ForeignKey("product_line.id"))
