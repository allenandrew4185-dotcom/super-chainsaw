from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from database.connection import get_db
from database.models import User, ExchangeCredential
from security.jwt import get_current_user
from sqlalchemy import select
from typing import List
import uuid

router = APIRouter()

class ExchangeCredentialRequest(BaseModel):
    exchange_name: str
    api_key: str
    api_secret: str

class ExchangeCredentialResponse(BaseModel):
    id: str
    exchange_name: str
    is_active: bool

@router.post("/", response_model=ExchangeCredentialResponse)
async def add_exchange(
    request: ExchangeCredentialRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Add exchange credentials."""
    # In production, encrypt the API key and secret
    credential = ExchangeCredential(
        id=uuid.uuid4(),
        user_id=current_user.id,
        exchange_name=request.exchange_name,
        api_key_encrypted=request.api_key,  # Should be encrypted
        api_secret_encrypted=request.api_secret  # Should be encrypted
    )
    db.add(credential)
    await db.commit()
    await db.refresh(credential)
    
    return ExchangeCredentialResponse(
        id=str(credential.id),
        exchange_name=credential.exchange_name,
        is_active=credential.is_active
    )

@router.get("/", response_model=List[ExchangeCredentialResponse])
async def get_exchanges(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get user's exchange credentials."""
    result = await db.execute(
        select(ExchangeCredential).where(ExchangeCredential.user_id == current_user.id)
    )
    credentials = result.scalars().all()
    
    return [ExchangeCredentialResponse(
        id=str(c.id),
        exchange_name=c.exchange_name,
        is_active=c.is_active
    ) for c in credentials]
