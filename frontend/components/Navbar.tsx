'use client';

import { useAuthStore } from '@/lib/store';
import Link from 'next/link';

export default function Navbar() {
  const { user, logout } = useAuthStore();

  return (
    <nav className="bg-gray-900 text-white shadow-lg">
      <div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
        <Link href="/" className="text-2xl font-bold text-blue-400">
          🤖 AI Arbitrage Platform
        </Link>
        <div className="flex gap-4 items-center">
          <Link href="/opportunities" className="hover:text-blue-400">
            Opportunities
          </Link>
          <Link href="/market" className="hover:text-blue-400">
            Market
          </Link>
          {user ? (
            <>
              <span className="text-sm">{user.email}</span>
              <button
                onClick={logout}
                className="bg-red-600 px-4 py-2 rounded hover:bg-red-700"
              >
                Logout
              </button>
            </>
          ) : (
            <>
              <Link href="/login" className="bg-blue-600 px-4 py-2 rounded hover:bg-blue-700">
                Login
              </Link>
              <Link href="/register" className="bg-green-600 px-4 py-2 rounded hover:bg-green-700">
                Register
              </Link>
            </>
          )}
        </div>
      </div>
    </nav>
  );
}
