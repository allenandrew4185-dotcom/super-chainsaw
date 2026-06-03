import { create } from 'zustand';

interface User {
  id: string;
  email: string;
  full_name: string;
  is_active: boolean;
}

interface AuthStore {
  user: User | null;
  token: string | null;
  isLoading: boolean;
  login: (email: string, password: string) => Promise<void>;
  register: (email: string, password: string, fullName: string) => Promise<void>;
  logout: () => void;
  setUser: (user: User | null) => void;
  setToken: (token: string | null) => void;
}

export const useAuthStore = create<AuthStore>((set) => ({
  user: null,
  token: typeof window !== 'undefined' ? localStorage.getItem('token') : null,
  isLoading: false,
  login: async (email: string, password: string) => {
    set({ isLoading: true });
    try {
      const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
      });
      const data = await response.json();
      localStorage.setItem('token', data.access_token);
      set({ token: data.access_token, user: { id: data.user_id, email, full_name: '', is_active: true } });
    } finally {
      set({ isLoading: false });
    }
  },
  register: async (email: string, password: string, fullName: string) => {
    set({ isLoading: true });
    try {
      const response = await fetch('/api/auth/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password, full_name: fullName }),
      });
      const data = await response.json();
      localStorage.setItem('token', data.access_token);
      set({ token: data.access_token, user: { id: data.user_id, email, full_name: fullName, is_active: true } });
    } finally {
      set({ isLoading: false });
    }
  },
  logout: () => {
    localStorage.removeItem('token');
    set({ user: null, token: null });
  },
  setUser: (user) => set({ user }),
  setToken: (token) => set({ token }),
}));
