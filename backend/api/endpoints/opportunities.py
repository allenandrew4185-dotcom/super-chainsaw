from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from database.connection import get_db
from database.models import User, ArbitrageOpportunity
from security.jwt import get_current_user
from sqlalchemy import select, desc
from typing import List
from datetime import datetime

router = APIRouter()

class OpportunityResponse(BaseModel):
    id: str
    symbol: str
    exchange_a: str
    exchange_b: str
    price_a: float
    price_b: float
    spread: float
    profit_potential: float
    risk_score: float
    status: str
    detected_at: datetime

@router.get("/", response_model=List[OpportunityResponse])
async def get_opportunities(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    symbol: str = Query(None),
    status: str = Query("active"),
    db: AsyncSession = Depends(get_db)
):
    """Get arbitrage opportunities."""
    query = select(ArbitrageOpportunity).where(
        ArbitrageOpportunity.status == status
    )
    
    if symbol:
        query = query.where(ArbitrageOpportunity.symbol == symbol)
    
    query = query.order_by(desc(ArbitrageOpportunity.spread)).offset(skip).limit(limit)
    result = await db.execute(query)
    opportunities = result.scalars().all()
    
    return [OpportunityResponse(
        id=str(opp.id),
        symbol=opp.symbol,
        exchange_a=opp.exchange_a,
        exchange_b=opp.exchange_b,
        price_a=float(opp.price_a),
        price_b=float(opp.price_b),
        spread=float(opp.spread),
        profit_potential=float(opp.profit_potential),
        risk_score=float(opp.risk_score),
        status=opp.status,
        detected_at=opp.detected_at
    ) for opp in opportunities]

@router.get("/{opportunity_id}", response_model=OpportunityResponse)
async def get_opportunity(opportunity_id: str, db: AsyncSession = Depends(get_db)):
    """Get specific opportunity."""
    result = await db.execute(
        select(ArbitrageOpportunity).where(ArbitrageOpportunity.id == opportunity_id)
    )
    opp = result.scalar_one_or_none()
    
    if not opp:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    
    return OpportunityResponse(
        id=str(opp.id),
        symbol=opp.symbol,
        exchange_a=opp.exchange_a,
        exchange_b=opp.exchange_b,
        price_a=float(opp.price_a),
        price_b=float(opp.price_b),
        spread=float(opp.spread),
        profit_potential=float(opp.profit_potential),
        risk_score=float(opp.risk_score),
        status=opp.status,
        detected_at=opp.detected_at
    )
