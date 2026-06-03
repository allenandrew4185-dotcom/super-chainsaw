'use client';

import Navbar from '@/components/Navbar';
import { Toaster } from 'react-hot-toast';
import './globals.css';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-gray-50">
        <Navbar />
        {children}
        <Toaster />
      </body>
    </html>
  );
}
