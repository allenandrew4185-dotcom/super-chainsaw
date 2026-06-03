export const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export const API_ENDPOINTS = {
  AUTH: {
    LOGIN: '/api/auth/login',
    REGISTER: '/api/auth/register',
  },
  OPPORTUNITIES: '/api/opportunities',
  MARKET: '/api/market',
  USERS: '/api/users',
  PAYMENTS: '/api/payments',
  EXCHANGES: '/api/exchanges',
};
