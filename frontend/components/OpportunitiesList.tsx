'use client';

import { useState, useEffect } from 'react';
import apiClient from '@/lib/apiClient';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import toast from 'react-hot-toast';

interface Opportunity {
  id: string;
  symbol: string;
  exchange_a: string;
  exchange_b: string;
  spread: number;
  profit_potential: number;
  risk_score: number;
  status: string;
}

export default function OpportunitiesList() {
  const [opportunities, setOpportunities] = useState<Opportunity[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchOpportunities();
  }, []);

  const fetchOpportunities = async () => {
    try {
      const response = await apiClient.get('/api/opportunities');
      setOpportunities(response.data);
    } catch (error) {
      toast.error('Failed to fetch opportunities');
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div className="text-center py-8">Loading...</div>;

  return (
    <div className="p-6">
      <h2 className="text-3xl font-bold mb-6">🔍 Arbitrage Opportunities</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {opportunities.map((opp) => (
          <div key={opp.id} className="bg-white p-4 rounded-lg shadow border-l-4 border-blue-600">
            <h3 className="font-bold text-lg">{opp.symbol}</h3>
            <p className="text-sm text-gray-600">
              {opp.exchange_a} ↔️ {opp.exchange_b}
            </p>
            <div className="mt-2">
              <p className="text-green-600 font-bold">Spread: {opp.spread.toFixed(2)}%</p>
              <p className="text-blue-600">Profit Potential: ${opp.profit_potential.toFixed(2)}</p>
              <p className={`text-sm ${opp.risk_score < 50 ? 'text-green-600' : 'text-red-600'}`}>
                Risk Score: {opp.risk_score.toFixed(2)}
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
