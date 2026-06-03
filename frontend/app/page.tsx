'use client';

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 to-gray-800 text-white">
      <div className="max-w-7xl mx-auto px-4 py-20 text-center">
        <h1 className="text-5xl font-bold mb-4">🤖 AI Arbitrage Platform</h1>
        <p className="text-xl text-gray-300 mb-8">
          Detect and execute cryptocurrency arbitrage opportunities across multiple exchanges
        </p>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mt-12">
          <div className="bg-gray-800 p-6 rounded-lg">
            <h2 className="text-2xl font-bold mb-2">📊 Real-time Analysis</h2>
            <p className="text-gray-400">Monitor price discrepancies across Binance, Coinbase, and Kraken in real-time</p>
          </div>
          <div className="bg-gray-800 p-6 rounded-lg">
            <h2 className="text-2xl font-bold mb-2">🧠 AI Agents</h2>
            <p className="text-gray-400">Multi-agent architecture for intelligent market scanning and risk analysis</p>
          </div>
          <div className="bg-gray-800 p-6 rounded-lg">
            <h2 className="text-2xl font-bold mb-2">💰 Seamless Payments</h2>
            <p className="text-gray-400">Integrated with Stripe, PayPal, and Cash App for easy transactions</p>
          </div>
        </div>
        <div className="mt-12">
          <a href="/opportunities" className="bg-blue-600 text-white px-8 py-3 rounded-lg text-lg hover:bg-blue-700 inline-block">
            View Opportunities
          </a>
        </div>
      </div>
    </div>
  );
}
