import React, { useState, useEffect } from "react";
import { SeniorFriendlyGeminiUI } from "./SeniorFriendlyGeminiUI";

// ============================================================
// Types
// ============================================================
type AppView = "STUDIO_SELECTOR" | "DASHBOARD" | "INTERVIEW" | "WATCH" | "LIVE" | "CREATOR_MODE";
type Theme = "NAT_GEO" | "AEROSPACE" | "CREATOR";

// ============================================================
// GUCE Edge-Compute Module: Parallel L5 WebGPU Offloading
// ============================================================
export const applyLocalKenBurns = async (imageBlob: Blob): Promise<Blob | string> => {
  if ('gpu' in navigator) {
    // User has a modern GPU (Chrome L5 Standard)
    console.log("[Parallel L5] OFFLOADING TO LOCAL WEBGPU - SAVING CLOUD TOKENS");

    try {
      const adapter = await navigator.gpu.requestAdapter();
      if (!adapter) throw new Error("No WebGPU adapter found.");

      const device = await adapter.requestDevice();
      console.log("[Parallel L5] WebGPU Device acquired. Rendering 8-second clip LOCALLY.");

      // [Simulated WebGPU Shader Execution for 2D Pan/Zoom]
      // In production, WGSL shaders compile here to apply the Ken Burns matrix math.

      return imageBlob; // Returns locally rendered video blob
    } catch (e) {
      console.warn("[Parallel L5] Local WebGPU failed. Falling back to CSS or Cloud.", e);
      return "FALLBACK_CSS_OR_CLOUD";
    }
  } else {
    // Fallback to Cloud (Costs Tokens)
    console.warn("[Parallel L5] WebGPU not supported. Routing to Cloud VEO...");
    return "ROUTE_TO_VEO";
  }
};

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
  const [currentView, setCurrentView] = useState<AppView>("STUDIO_SELECTOR");
  const [activeTheme, setActiveTheme] = useState<Theme>("NAT_GEO");
  const [isCreatorMode, setIsCreatorMode] = useState(false);
  const [isVoiceOnlyMode, setIsVoiceOnlyMode] = useState(false);

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
    setActiveTheme(isCreatorMode ? "NAT_GEO" : "CREATOR");
    setCurrentView(isCreatorMode ? "DASHBOARD" : "CREATOR_MODE");
  };

  const handleSelectTheme = (theme: Theme) => {
    setActiveTheme(theme);
    setCurrentView("DASHBOARD");
  };

  // ============================================================
  // Theme Engine Styling Handlers
  // ============================================================
  const getThemeStyles = () => {
    switch(activeTheme) {
      case "AEROSPACE":
        return {
          bgUrl: "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2000&auto=format&fit=crop", // Space/Earth view
          panelBg: "rgba(15, 23, 42, 0.6)", // Frosted Sapphire
          textColor: "#ffffff",
          headerColor: "#38bdf8", // Neon Blue
          fontFamily: "'Space Grotesk', sans-serif"
        };
      case "NAT_GEO":
      default:
        return {
          bgUrl: "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?q=80&w=2000&auto=format&fit=crop", // Golden Hour
          panelBg: "rgba(26, 26, 26, 0.85)", // Deep Charcoal
          textColor: "#e2e8f0",
          headerColor: "#FFD700", // Rich Gold
          fontFamily: "'Montserrat', sans-serif"
        };
    }
  };

  const themeStyles = getThemeStyles();

  // ============================================================
  // Views
  // ============================================================

  // 0. The Studio Selector (Theme Engine Root)
  const renderStudioSelector = () => (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", minHeight: "100vh", backgroundColor: "#000", color: "#fff", fontFamily: "'Montserrat', sans-serif" }}>
      <h1 style={{ fontSize: "56px", fontWeight: "900", marginBottom: "60px", textShadow: "0 4px 20px rgba(255,255,255,0.2)" }}>Select Your Studio</h1>
      <div style={{ display: "flex", gap: "40px" }}>
        {/* Nat Geo Studio Button */}
        <div
          onClick={() => handleSelectTheme("NAT_GEO")}
          style={{ width: "400px", height: "500px", backgroundImage: "url('https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?q=80&w=800&auto=format&fit=crop')", backgroundSize: "cover", borderRadius: "32px", cursor: "pointer", position: "relative", overflow: "hidden", transition: "transform 0.3s" }}
          onMouseOver={(e) => e.currentTarget.style.transform = "scale(1.05)"}
          onMouseOut={(e) => e.currentTarget.style.transform = "scale(1)"}
        >
          <div style={{ position: "absolute", bottom: 0, left: 0, right: 0, padding: "40px", background: "linear-gradient(to top, rgba(0,0,0,0.9), transparent)" }}>
            <h2 style={{ fontSize: "36px", color: "#FFD700", margin: 0 }}>Heritage Studio</h2>
            <p style={{ fontSize: "20px", color: "#e2e8f0", marginTop: "10px" }}>Warm. Cinematic. Family History.</p>
          </div>
        </div>

        {/* Aerospace Museum Studio Button */}
        <div
          onClick={() => handleSelectTheme("AEROSPACE")}
          style={{ width: "400px", height: "500px", backgroundImage: "url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=800&auto=format&fit=crop')", backgroundSize: "cover", borderRadius: "32px", cursor: "pointer", position: "relative", overflow: "hidden", transition: "transform 0.3s" }}
          onMouseOver={(e) => e.currentTarget.style.transform = "scale(1.05)"}
          onMouseOut={(e) => e.currentTarget.style.transform = "scale(1)"}
        >
          <div style={{ position: "absolute", bottom: 0, left: 0, right: 0, padding: "40px", background: "linear-gradient(to top, rgba(0,0,0,0.9), transparent)" }}>
            <h2 style={{ fontSize: "36px", color: "#38bdf8", margin: 0 }}>Aerospace Studio</h2>
            <p style={{ fontSize: "20px", color: "#e2e8f0", marginTop: "10px" }}>NASA-Grade Futurism. Veterans & Museums.</p>
          </div>
        </div>
      </div>
    </div>
  );

  // 1. The "Living History" Dashboard (Home)
  const renderDashboard = () => (
    <div style={{
      display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", minHeight: "100vh",
      position: "relative", overflow: "hidden", fontFamily: themeStyles.fontFamily
    }}>
      {/* Cinematic Ken Burns Background */}
      <img src={themeStyles.bgUrl}
           className="documentary-image"
           style={{ position: "absolute", zIndex: 0, width: "100%", height: "100%", objectFit: "cover" }}
      />

      {/* Anti-Gravity Glow & Frosted Sapphire / Deep Charcoal Panels */}
      <div style={{
        backgroundColor: themeStyles.panelBg, backdropFilter: "blur(16px)", padding: "60px", borderRadius: "24px",
        textAlign: "center", maxWidth: "800px", zIndex: 1, boxShadow: "0 50px 100px rgba(0,0,0,0.5)", border: "1px solid rgba(255,255,255,0.1)"
      }}>
        <h1 style={{ fontSize: "64px", color: themeStyles.headerColor, margin: "0 0 20px 0", fontWeight: 800, textShadow: `0 0 20px ${themeStyles.headerColor}66` }}>Welcome back, {userName}.</h1>
        <p style={{ fontSize: "32px", color: themeStyles.textColor, marginBottom: "60px" }}>What story shall we tell today?</p>

        <div style={{ display: "flex", flexDirection: "column", gap: "30px" }}>
          <button onClick={() => setCurrentView("INTERVIEW")} style={massiveButtonStyle("#22c55e")}>🎙️ Tell a Story (Video Call)</button>
          <button onClick={() => setIsVoiceOnlyMode(true)} style={massiveButtonStyle("#8b5cf6")}>🔮 Tell a Story (Voice Only)</button>
          <button onClick={() => setCurrentView("WATCH")} style={massiveButtonStyle("#3b82f6")}>🍿 Watch My Life</button>
          <button onClick={() => setCurrentView("LIVE")} style={massiveButtonStyle("#ef4444")}>📡 Go Live (Family Stream)</button>
        </div>
      </div>
    </div>
  );

  // 1.5 The "Voice Glow" Mode (Living Interface)
  const renderVoiceOnlyMode = () => (
    <div style={{
      display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", minHeight: "100vh",
      backgroundColor: "#0f172a", // Dimmed, deep-charcoal background
    }}>
      <style>
        {`
          @keyframes pulseGlow {
            0% { box-shadow: 0 0 40px #FFD700, 0 0 80px #FFD700; transform: scale(1); }
            50% { box-shadow: 0 0 80px #FFD700, 0 0 120px #FFD700; transform: scale(1.05); }
            100% { box-shadow: 0 0 40px #FFD700, 0 0 80px #FFD700; transform: scale(1); }
          }
          .glowing-orb {
            width: 250px;
            height: 250px;
            border-radius: 50%;
            background: radial-gradient(circle, #fff 0%, #FFD700 40%, #d97706 100%);
            animation: pulseGlow 2s infinite ease-in-out;
            margin-bottom: 80px;
          }
        `}
      </style>

      <div className="glowing-orb"></div>

      <h2 style={{ color: "#FFD700", fontSize: "48px", fontWeight: "bold", fontFamily: "'Montserrat', sans-serif", textShadow: "0 4px 20px rgba(255, 215, 0, 0.5)", marginBottom: "20px" }}>I am listening, {userName}.</h2>
      <p style={{ color: "#94a3b8", fontSize: "28px", fontStyle: "italic", marginBottom: "60px" }}>Tell me about your first car...</p>

      <button
        onClick={() => setIsVoiceOnlyMode(false)}
        style={{ fontSize: "32px", padding: "20px 60px", backgroundColor: "rgba(239, 68, 68, 0.2)", color: "#ef4444", border: "2px solid #ef4444", borderRadius: "100px", fontWeight: "bold", cursor: "pointer", transition: "all 0.2s" }}
        onMouseOver={(e) => e.currentTarget.style.backgroundColor = "#ef4444"}
        onMouseOut={(e) => e.currentTarget.style.backgroundColor = "rgba(239, 68, 68, 0.2)"}
      >
        🛑 End Session
      </button>
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

  // 3. Watch / Gallery View (The "Bento Box" Grid)
  const renderWatchGallery = () => (
    <div style={{
      backgroundColor: "#1a1a1a",
      backgroundImage: "url('https://images.unsplash.com/photo-1493606278519-11aa9f86e40a?q=80&w=2000&auto=format&fit=crop')", // Film grain / old parchment texture
      backgroundBlendMode: "overlay",
      minHeight: "100vh",
      padding: "60px",
      color: "white"
    }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "60px" }}>
        <button onClick={() => setCurrentView("DASHBOARD")} style={{ fontSize: "28px", background: "rgba(255,215,0,0.1)", border: "2px solid #FFD700", color: "#FFD700", borderRadius: "100px", padding: "10px 30px", cursor: "pointer", fontWeight: "bold" }}>
          ← Return Home
        </button>
        <h1 style={{ fontSize: "64px", color: "#FFD700", margin: 0, fontFamily: "'Montserrat', sans-serif", fontWeight: "900", textShadow: "0 4px 20px rgba(0,0,0,0.8)" }}>Family Archive</h1>
      </div>

      {/* Bento Box Layout */}
      <div style={{
        display: "grid",
        gridTemplateColumns: "repeat(3, 1fr)",
        gridAutoRows: "350px",
        gap: "30px",
        maxWidth: "1400px",
        margin: "0 auto"
      }}>
        {userAssets.map((asset, index) => (
          <div key={asset.id} style={{
            backgroundColor: "rgba(26,26,26,0.6)",
            backdropFilter: "blur(12px)",
            borderRadius: "32px",
            overflow: "hidden",
            cursor: "pointer",
            position: "relative",
            border: "1px solid rgba(255,255,255,0.1)",
            gridColumn: index === 0 ? "span 2" : "span 1", // First item spans 2 columns for the trendy Bento look
            boxShadow: "0 20px 40px rgba(0,0,0,0.5)",
            transition: "transform 0.3s cubic-bezier(0.4, 0, 0.2, 1)"
          }}
          onMouseOver={(e) => e.currentTarget.style.transform = "scale(1.02) translateY(-10px)"}
          onMouseOut={(e) => e.currentTarget.style.transform = "scale(1) translateY(0)"}
          >
            <img src={asset.thumbnail} alt={asset.title} className="documentary-image" style={{ width: "100%", height: "100%", objectFit: "cover", position: "absolute", zIndex: 0, opacity: 0.6 }} />
            <div style={{ position: "absolute", bottom: 0, left: 0, right: 0, padding: "40px", background: "linear-gradient(to top, rgba(0,0,0,0.9), transparent)", zIndex: 1 }}>
              <h2 style={{ fontSize: index === 0 ? "48px" : "32px", margin: "0 0 10px 0", fontWeight: "bold", textShadow: "0 2px 10px rgba(0,0,0,1)" }}>{asset.title}</h2>
              <p style={{ fontSize: "24px", color: "#FFD700", fontWeight: "bold", textShadow: "0 2px 10px rgba(0,0,0,1)" }}>{asset.date} • {asset.duration}</p>
            </div>

            {/* Play Button Icon overlay */}
            <div style={{ position: "absolute", top: "40px", right: "40px", zIndex: 1, backgroundColor: "rgba(255,215,0,0.8)", borderRadius: "50%", width: "80px", height: "80px", display: "flex", alignItems: "center", justifyContent: "center" }}>
              <span style={{ fontSize: "36px", marginLeft: "10px" }}>▶</span>
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
      <style>
        {`
          /* World-Class Ken Burns Animation for Documentaries */
          @keyframes kenburns-effect {
            0% { transform: scale(1.0) translate(0, 0); }
            100% { transform: scale(1.2) translate(-20px, -10px); }
          }
          .documentary-image {
            animation: kenburns-effect 12s ease-in-out infinite alternate;
          }
        `}
      </style>

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
      {isVoiceOnlyMode ? renderVoiceOnlyMode() : (
        <>
          {currentView === "STUDIO_SELECTOR" && renderStudioSelector()}
          {currentView === "DASHBOARD" && renderDashboard()}
          {currentView === "INTERVIEW" && <SeniorFriendlyGeminiUI userId="user_123" />}
          {currentView === "WATCH" && renderWatchGallery()}
          {currentView === "LIVE" && <div style={{ color: "white", padding: "100px", fontSize: "48px", textAlign: "center" }}>📡 Connecting to Family Livestream...</div>}
          {currentView === "CREATOR_MODE" && renderCreatorMode()}
        </>
      )}

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
