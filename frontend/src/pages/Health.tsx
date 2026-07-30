import { useEffect, useState } from "react";
import { api } from "../services/api";
import { HealthResponse } from "../types/api";

export function Health() {
  const [health, setHealth] = useState<HealthResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const checkHealth = async () => {
      try {
        const response = await api.get<HealthResponse>("/health");
        setHealth(response.data);
      } catch (err) {
        setError(err instanceof Error ? err.message : "Unknown error");
      } finally {
        setLoading(false);
      }
    };

    checkHealth();
  }, []);

  if (loading) {
    return <div className="text-center">Loading...</div>;
  }

  if (error) {
    return (
      <div className="text-center text-red-400">
        Error: {error}
      </div>
    );
  }

  return (
    <div className="text-center">
      <h2 className="text-3xl font-bold mb-4">System Health</h2>
      {health && (
        <div className="bg-gray-800 rounded-lg p-6 max-w-md mx-auto">
          <div className="grid grid-cols-2 gap-4 text-left">
            <div className="font-medium">Status:</div>
            <div className="text-green-400">{health.status}</div>
            <div className="font-medium">Version:</div>
            <div>{health.version}</div>
            <div className="font-medium">Timestamp:</div>
            <div className="text-sm">{health.timestamp}</div>
          </div>
        </div>
      )}
    </div>
  );
}
