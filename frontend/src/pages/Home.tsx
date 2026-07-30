export function Home() {
  return (
    <div className="text-center">
      <h1 className="text-4xl font-bold mb-4">
        Welcome to KlashAI
      </h1>
      <p className="text-lg text-gray-300 mb-6">
        Next-generation AI platform for gaming, coding, server management, and more.
      </p>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-2xl mx-auto">
        <div className="bg-gray-800 rounded-lg p-6">
          <h3 className="text-xl font-semibold mb-2">Gaming</h3>
          <p className="text-gray-400">
            AI-powered assistants for game development, matchmaking, and analytics.
          </p>
        </div>
        <div className="bg-gray-800 rounded-lg p-6">
          <h3 className="text-xl font-semibold mb-2">Coding</h3>
          <p className="text-gray-400">
            Smart code generation, debugging, and pair programming tools.
          </p>
        </div>
        <div className="bg-gray-800 rounded-lg p-6">
          <h3 className="text-xl font-semibold mb-2">Server Management</h3>
          <p className="text-gray-400">
            Automated deployment, monitoring, and scaling for your infrastructure.
          </p>
        </div>
        <div className="bg-gray-800 rounded-lg p-6">
          <h3 className="text-xl font-semibold mb-2">AI Assistant</h3>
          <p className="text-gray-400">
            Conversational AI for documentation, support, and workflows.
          </p>
        </div>
      </div>
    </div>
  );
          }
