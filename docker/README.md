# Docker and Infrastructure Setup

## Quick Start

### Prerequisites
- Docker
- Docker Compose
- Git

### Setup with Script

```bash
cd docker
chmod +x setup.sh
./setup.sh
```

### Manual Setup

1. **Copy environment variables:**
   ```bash
   cp docker/.env.example docker/.env
   ```

2. **Build and start services:**
   ```bash
   docker compose -f docker/docker-compose.yml up -d
   ```

3. **Access the application:**
   - Frontend: http://localhost:3000
   - Backend: http://localhost:8000
   - API Docs: http://localhost:8000/docs

### Services

- **PostgreSQL** (5432): Main database
- **Redis** (6379): Caching and sessions
- **Backend** (8000): FastAPI application
- **Frontend** (3000): Next.js application

### Useful Commands

```bash
# View logs
docker compose -f docker/docker-compose.yml logs -f

# Rebuild images
docker compose -f docker/docker-compose.yml build --no-cache

# Stop services
docker compose -f docker/docker-compose.yml down

# Remove volumes
docker compose -f docker/docker-compose.yml down -v

# Access backend shell
docker compose -f docker/docker-compose.yml exec backend bash

# Access frontend shell
docker compose -f docker/docker-compose.yml exec frontend sh

# Run backend tests
docker compose -f docker/docker-compose.yml exec backend pytest
```

### Troubleshooting

**Port already in use:**
```bash
# Change ports in docker-compose.yml
# Or kill existing processes:
lsof -i :3000
lsof -i :8000
```

**Database connection errors:**
```bash
# Check database logs
docker compose -f docker/docker-compose.yml logs postgres

# Rebuild and restart
docker compose -f docker/docker-compose.yml down -v
docker compose -f docker/docker-compose.yml up -d
```

### Production Deployment

For production deployment, update:
1. `JWT_SECRET` in `.env`
2. Payment API keys (Stripe, PayPal, Square)
3. Database credentials
4. CORS origins
5. Use environment-specific compose files
