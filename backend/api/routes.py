from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database.connection import get_db
from api.endpoints import auth, users, opportunities, exchanges, payments, market

router = APIRouter()

# Auth routes
router.include_router(auth.router, prefix="/api/auth", tags=["auth"])

# User routes
router.include_router(users.router, prefix="/api/users", tags=["users"])

# Opportunities routes
router.include_router(opportunities.router, prefix="/api/opportunities", tags=["opportunities"])

# Exchange routes
router.include_router(exchanges.router, prefix="/api/exchanges", tags=["exchanges"])

# Payment routes
router.include_router(payments.router, prefix="/api/payments", tags=["payments"])

# Market routes
router.include_router(market.router, prefix="/api/market", tags=["market"])
