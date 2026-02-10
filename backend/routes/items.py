from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlmodel import Session, select
from typing import Optional

from models.item import Item, ItemCreate, ItemUpdate
from models.user import User
from database import get_session
from utils.auth import get_current_user
from utils.dates import parse_date
from utils.file import save_upload

router = APIRouter(prefix="/items", tags=["Items"])

# -----------------------------
# CRUD ROUTES
# -----------------------------

@router.post("")
def create_item(
    item: ItemCreate,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user)
):
    db_item = Item.from_orm(item)
    db_item.user_id = user.id
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


@router.get("")
def list_items(
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user)
):
    return session.exec(select(Item).where(Item.user_id == user.id)).all()


@router.get("/{item_id}")
def get_item(
    item_id: int,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user)
):
    item = session.get(Item, item_id)
    if not item or item.user_id != user.id:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.patch("/{item_id}")
def update_item(
    item_id: int,
    item: ItemUpdate,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user)
):
    db_item = session.get(Item, item_id)
    if not db_item or db_item.user_id != user.id:
        raise HTTPException(status_code=404, detail="Item not found")

    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)

    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


@router.delete("/{item_id}")
def delete_item(
    item_id: int,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user)
):
    item = session.get(Item, item_id)
    if not item or item.user_id != user.id:
        raise HTTPException(status_code=404, detail="Item not found")

    session.delete(item)
    session.commit()
    return {"message": "Item deleted"}


# -----------------------------
# FILE UPLOAD ROUTE
# -----------------------------

@router.post("/upload")
def upload_item(
    name: str = Form(...),
    category: str = Form(...),
    type: str = Form(...),

    expiration_date: Optional[str] = Form(None),
    renewal_date: Optional[str] = Form(None),
    billing_cycle: Optional[str] = Form(None),
    price: Optional[float] = Form(None),

    document_number: Optional[str] = Form(None),
    notes: Optional[str] = Form(None),
    file: UploadFile = File(None),

    session: Session = Depends(get_session),
    user: User = Depends(get_current_user)
):

    expiration_date = parse_date(expiration_date)
    renewal_date = parse_date(renewal_date)
    file_path = save_upload(file)

    item = Item(
        name=name,
        category=category,
        type=type,
        expiration_date=expiration_date,
        renewal_date=renewal_date,
        billing_cycle=billing_cycle,
        price=price,
        document_number=document_number,
        notes=notes,
        file_path=file_path,
        user_id=user.id
    )

    session.add(item)
    session.commit()
    session.refresh(item)
    return item