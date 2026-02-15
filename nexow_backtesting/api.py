"""FastAPI application for nexow-backtesting service."""

from fastapi import FastAPI
from pydantic_settings import BaseSettings
import structlog

logger = structlog.get_logger(__name__)


class Settings(BaseSettings):
    """Application settings."""
    port: int = 8003
    environment: str = "development"


settings = Settings()

app = FastAPI(
    title="Nexow Backtesting Service",
    description="Historical simulation and performance metrics",
    version="0.1.0",
)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "nexow-backtesting"}


@app.get("/status")
async def get_status():
    """Get service status."""
    return {
        "service": "nexow-backtesting",
        "version": "0.1.0",
        "environment": settings.environment,
    }


# TODO: Add backtesting endpoints
# - POST /backtest - Run backtest
# - GET /backtest/{id} - Get backtest results
# - GET /backtest/{id}/metrics - Get performance metrics
