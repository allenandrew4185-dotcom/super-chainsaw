#!/bin/bash
# Setup script for AI Arbitrage Platform

set -e

echo "🚀 Starting AI Arbitrage Platform Setup..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

echo "✅ Docker is installed"

# Create .env file from template
if [ ! -f docker/.env ]; then
    echo "📝 Creating .env file from template..."
    cp docker/.env.example docker/.env
    echo "⚠️  Please update docker/.env with your actual credentials"
fi

# Build Docker images
echo "🔨 Building Docker images..."
docker compose -f docker/docker-compose.yml build

# Start services
echo "🔧 Starting services..."
docker compose -f docker/docker-compose.yml up -d

# Wait for backend to be ready
echo "⏳ Waiting for backend to be ready..."
for i in {1..30}; do
    if curl -f http://localhost:8000/health > /dev/null 2>&1; then
        echo "✅ Backend is ready!"
        break
    fi
    echo "Waiting... ($i/30)"
    sleep 2
done

echo ""
echo "✅ AI Arbitrage Platform is running!"
echo ""
echo "📱 Frontend: http://localhost:3000"
echo "🔌 Backend: http://localhost:8000"
echo "🗄️  Database: localhost:5432"
echo "💾 Redis: localhost:6379"
echo ""
echo "📚 Documentation:"
echo "  - Backend API Docs: http://localhost:8000/docs"
echo "  - ReDoc: http://localhost:8000/redoc"
echo ""
echo "🛑 To stop services: docker compose -f docker/docker-compose.yml down"
