import { Link } from "react-router-dom";

export function Home() {
  return (
    <div className="text-center">
      <h1 className="text-6xl font-bold bg-gradient-to-r from-primary-400 to-cyan-400 bg-clip-text text-transparent mb-4">
        KlashAI
      </h1>
      <p className="text-xl text-gray-300 mb-8">
        Next-generation AI platform for gaming, coding, and productivity.
      </p>
      <div className="space-x-4">
        <Link to="/health" className="btn btn-primary">
          Check Health
        </Link>
        <button className="btn btn-secondary" disabled>
          Coming Soon
        </button>
      </div>
    </div>
  );
}
