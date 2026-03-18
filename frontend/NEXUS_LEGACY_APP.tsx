import React, { useState, useEffect } from "react";
import { SeniorFriendlyGeminiUI } from "./SeniorFriendlyGeminiUI";

// ============================================================
// Types
// ============================================================
type AppView = "DASHBOARD" | "INTERVIEW" | "WATCH" | "LIVE" | "CREATOR_MODE";

interface DocumentaryAsset {
  id: string;
  title: string;
  date: string;
  thumbnail: string;
  duration: string;
}

// ============================================================
// Main Application Container (NEXUS-LEGACY)
// ============================================================
export const NexusLegacyApp: React.FC = () => {
  const [currentView, setCurrentView] = useState<AppView>("DASHBOARD");
  const [isCreatorMode, setIsCreatorMode] = useState(false);

  // Simulated User Data
  const userName = "Grandpa Joe";
  const userAssets: DocumentaryAsset[] = [
    { id: "1", title: "My First Car (1965 Mustang)", date: "Oct 12, 2026", thumbnail: "https://images.unsplash.com/photo-1542468758-c923366050b1?w=800&auto=format&fit=crop", duration: "12:04" },
    { id: "2", title: "Meeting Grandma in Rome", date: "Nov 04, 2026", thumbnail: "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800&auto=format&fit=crop", duration: "28:15" },
  ];

  // ============================================================
  // Handlers
  // ============================================================
  const handleToggleMode = () => {
    setIsCreatorMode(!isCreatorMode);
    setCurrentView(isCreatorMode ? "DASHBOARD" : "CREATOR_MODE");
  };

  // ============================================================
  // Views
  // ============================================================

  // 1. The "Living History" Dashboard (Home)
  const renderDashboard = () => (
    <div style={{
      display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", minHeight: "100vh",
      backgroundImage: "url('https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?q=80&w=2000&auto=format&fit=crop')", // Nat Geo Cinematic
      backgroundSize: "cover", backgroundPosition: "center"
    }}>
      <div style={{ backgroundColor: "rgba(26,26,26,0.85)", backdropFilter: "blur(16px)", padding: "60px", borderRadius: "24px", textAlign: "center", maxWidth: "800px" }}>
        <h1 style={{ fontSize: "64px", color: "#FFD700", margin: "0 0 20px 0", fontFamily: "'Montserrat', sans-serif", fontWeight: 800 }}>Welcome back, {userName}.</h1>
        <p style={{ fontSize: "32px", color: "#e2e8f0", marginBottom: "60px" }}>What story shall we tell today?</p>

        <div style={{ display: "flex", flexDirection: "column", gap: "30px" }}>
          <button onClick={() => setCurrentView("INTERVIEW")} style={massiveButtonStyle("#22c55e")}>🎙️ Tell a Story</button>
          <button onClick={() => setCurrentView("WATCH")} style={massiveButtonStyle("#3b82f6")}>🍿 Watch My Life</button>
          <button onClick={() => setCurrentView("LIVE")} style={massiveButtonStyle("#ef4444")}>📡 Go Live (Family Stream)</button>
        </div>
      </div>
    </div>
  );

  // 2. The "Generational Bridge" (Youth View / Creator Mode)
  const renderCreatorMode = () => (
    <div style={{ backgroundColor: "#0f172a", minHeight: "100vh", color: "white", padding: "40px", fontFamily: "sans-serif" }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", borderBottom: "1px solid #334155", paddingBottom: "20px", marginBottom: "40px" }}>
        <h1 style={{ fontSize: "32px", fontWeight: "bold", color: "#38bdf8" }}>⚡ Studio Edit: {userName}'s Legacy</h1>
        <button onClick={() => alert("Exporting to TikTok/Instagram Reels...")} style={{ backgroundColor: "#ec4899", padding: "10px 20px", borderRadius: "8px", fontWeight: "bold", border: "none", cursor: "pointer" }}>Share to Socials</button>
      </div>

      <div style={{ display: "flex", gap: "40px" }}>
        {/* Assets Panel */}
        <div style={{ flex: 1, backgroundColor: "#1e293b", padding: "20px", borderRadius: "16px" }}>
          <h2 style={{ fontSize: "24px", color: "#94a3b8", marginBottom: "20px" }}>Raw Footage / Assets</h2>
          {userAssets.map(asset => (
            <div key={asset.id} style={{ display: "flex", gap: "15px", marginBottom: "15px", alignItems: "center", backgroundColor: "#0f172a", padding: "10px", borderRadius: "8px" }}>
              <img src={asset.thumbnail} alt={asset.title} style={{ width: "120px", height: "80px", objectFit: "cover", borderRadius: "4px" }} />
              <div>
                <h3 style={{ fontSize: "18px", margin: "0 0 5px 0" }}>{asset.title}</h3>
                <span style={{ fontSize: "14px", color: "#64748b" }}>{asset.duration} • AI Upscaled 4K</span>
              </div>
            </div>
          ))}
        </div>

        {/* Timeline Editor (Mock) */}
        <div style={{ flex: 2, display: "flex", flexDirection: "column", gap: "20px" }}>
          <div style={{ flex: 1, backgroundColor: "#000", borderRadius: "16px", display: "flex", alignItems: "center", justifyContent: "center", border: "2px dashed #334155" }}>
            <span style={{ fontSize: "24px", color: "#64748b" }}>Video Preview (16:9 or 9:16)</span>
          </div>
          <div style={{ height: "150px", backgroundColor: "#1e293b", borderRadius: "16px", padding: "20px" }}>
            <h3 style={{ fontSize: "16px", color: "#94a3b8", margin: "0 0 10px 0" }}>TikTok Style Timeline</h3>
            <div style={{ display: "flex", gap: "10px" }}>
               <div style={{ width: "30%", height: "60px", backgroundColor: "#3b82f6", borderRadius: "4px", display: "flex", alignItems: "center", justifyContent: "center", fontSize: "12px" }}>Clip 1 (A-Roll)</div>
               <div style={{ width: "20%", height: "60px", backgroundColor: "#8b5cf6", borderRadius: "4px", display: "flex", alignItems: "center", justifyContent: "center", fontSize: "12px" }}>B-Roll (Nat Geo)</div>
               <div style={{ width: "40%", height: "60px", backgroundColor: "#3b82f6", borderRadius: "4px", display: "flex", alignItems: "center", justifyContent: "center", fontSize: "12px" }}>Clip 2 (A-Roll)</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );

  // 3. Watch / Gallery View
  const renderWatchGallery = () => (
    <div style={{ backgroundColor: "#1a1a1a", minHeight: "100vh", padding: "40px", color: "white" }}>
      <button onClick={() => setCurrentView("DASHBOARD")} style={{ fontSize: "24px", background: "none", border: "none", color: "#FFD700", cursor: "pointer", marginBottom: "40px" }}>← Back to Dashboard</button>
      <h1 style={{ fontSize: "48px", color: "#FFD700", marginBottom: "40px" }}>Your Documentaries</h1>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(400px, 1fr))", gap: "40px" }}>
        {userAssets.map(asset => (
          <div key={asset.id} style={{ backgroundColor: "#262626", borderRadius: "16px", overflow: "hidden", cursor: "pointer", transition: "transform 0.2s" }}>
            <img src={asset.thumbnail} alt={asset.title} style={{ width: "100%", height: "250px", objectFit: "cover" }} />
            <div style={{ padding: "20px" }}>
              <h2 style={{ fontSize: "28px", margin: "0 0 10px 0" }}>{asset.title}</h2>
              <p style={{ fontSize: "18px", color: "#a3a3a3" }}>{asset.date} • {asset.duration}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );

  // ============================================================
  // Core Render
  // ============================================================
  return (
    <div style={{ position: "relative" }}>

      {/* Global Mode Toggle (Hidden for Seniors, Visible for Youth) */}
      <button
        onClick={handleToggleMode}
        style={{
          position: "absolute", top: "20px", right: "20px", zIndex: 1000,
          backgroundColor: isCreatorMode ? "#ec4899" : "rgba(255,255,255,0.1)",
          color: "white", border: "1px solid rgba(255,255,255,0.2)", borderRadius: "100px",
          padding: "10px 20px", fontSize: "16px", fontWeight: "bold", cursor: "pointer", backdropFilter: "blur(4px)"
        }}
      >
        {isCreatorMode ? "Exit Creator Mode" : "⚡ Enter Creator Mode"}
      </button>

      {/* View Router */}
      {currentView === "DASHBOARD" && renderDashboard()}
      {currentView === "INTERVIEW" && <SeniorFriendlyGeminiUI userId="user_123" />}
      {currentView === "WATCH" && renderWatchGallery()}
      {currentView === "LIVE" && <div style={{ color: "white", padding: "100px", fontSize: "48px", textAlign: "center" }}>📡 Connecting to Family Livestream...</div>}
      {currentView === "CREATOR_MODE" && renderCreatorMode()}

    </div>
  );
};

// Helper for massive accessibility buttons
const massiveButtonStyle = (bgColor: string) => ({
  backgroundColor: bgColor,
  color: "white",
  border: "none",
  borderRadius: "16px",
  padding: "30px 60px",
  fontSize: "40px",
  fontWeight: "bold",
  cursor: "pointer",
  width: "100%",
  boxShadow: `0 10px 30px ${bgColor}66`,
  transition: "transform 0.2s"
});
