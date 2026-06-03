from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import List, Dict, Any
from agents.scanner_agent import ScannerAgent
from agents.research_agent import ResearchAgent
from agents.coordinator import AgentCoordinator

router = APIRouter()
coordinator = AgentCoordinator()

class MarketDataResponse(BaseModel):
    symbol: str
    binance_price: float
    coinbase_price: float
    spread: float

class AnalysisResponse(BaseModel):
    market_data: Dict[str, Any]
    analysis: Dict[str, Any]
    risk: Dict[str, Any]
    recommendation: str

@router.get("/prices")
async def get_market_prices(symbols: str = Query("BTC,ETH")) -> List[MarketDataResponse]:
    """Get current market prices across exchanges."""
    symbol_list = symbols.split(",")
    scanner = ScannerAgent()
    
    results = []
    for symbol in symbol_list:
        prices = await scanner.get_prices(symbol.strip())
        if prices:
            results.append(MarketDataResponse(**prices))
    
    return results

@router.get("/analyze")
async def analyze_market(symbol: str = Query("BTC")) -> AnalysisResponse:
    """Run complete market analysis using all agents."""
    result = await coordinator.run(symbol)
    return AnalysisResponse(**result)
