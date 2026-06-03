#!/bin/bash
# Cleanup script for AI Arbitrage Platform

set -e

echo "🧹 Cleaning up AI Arbitrage Platform..."

# Stop and remove containers
echo "Stopping containers..."
docker compose -f docker/docker-compose.yml down

# Remove volumes (optional)
read -p "Do you want to remove data volumes? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🗑️  Removing volumes..."
    docker compose -f docker/docker-compose.yml down -v
fi

echo "✅ Cleanup complete"
