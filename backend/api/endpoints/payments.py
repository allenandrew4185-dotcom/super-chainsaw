from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from database.connection import get_db
from database.models import User, Payment
from security.jwt import get_current_user
from services.payment_service import PaymentService
from sqlalchemy import select
from typing import List
import uuid
from decimal import Decimal

router = APIRouter()
payment_service = PaymentService()

class PaymentRequest(BaseModel):
    amount: float
    payment_method: str  # stripe, paypal, cashapp
    description: str = "Dusty Dollars Payment"

class PaymentResponse(BaseModel):
    id: str
    amount: float
    status: str
    transaction_id: str

@router.post("/", response_model=PaymentResponse)
async def create_payment(
    request: PaymentRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Process a payment."""
    # Process payment
    result = await payment_service.process_payment(
        method=request.payment_method,
        amount=request.amount,
        description=request.description
    )
    
    if not result.get("success"):
        raise HTTPException(status_code=400, detail=result.get("error"))
    
    # Save payment record
    payment = Payment(
        id=uuid.uuid4(),
        user_id=current_user.id,
        amount=Decimal(str(request.amount)),
        payment_method=request.payment_method,
        transaction_id=result.get("transaction_id"),
        status="completed"
    )
    db.add(payment)
    await db.commit()
    await db.refresh(payment)
    
    return PaymentResponse(
        id=str(payment.id),
        amount=float(payment.amount),
        status=payment.status,
        transaction_id=payment.transaction_id
    )

@router.get("/", response_model=List[PaymentResponse])
async def get_payments(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get user's payment history."""
    result = await db.execute(
        select(Payment).where(Payment.user_id == current_user.id)
    )
    payments = result.scalars().all()
    
    return [PaymentResponse(
        id=str(p.id),
        amount=float(p.amount),
        status=p.status,
        transaction_id=p.transaction_id
    ) for p in payments]
