// SeniorFriendlyGeminiUI.tsx
import React, { useState, useEffect, useRef } from "react";
// Mock websocket to prevent Vite bundler from dying since 'websocket' module might not work directly in browser without shims.
// We are only testing UI visualization.
const W3CWebSocket = globalThis.WebSocket;

// ============================================================
// Types
// ============================================================
interface GeminiMessage {
  timestamp: string;
  role: "user" | "gemini";
  content: string;
  suggestedClips?: Array<{ title: string; url: string }>;
}

// ============================================================
// Component: The "Cinematic Legacy" Engine (NEXUS-LEGACY)
// ============================================================
export const SeniorFriendlyGeminiUI: React.FC<{ userId: string }> = ({ userId }) => {
  const [messages, setMessages] = useState<GeminiMessage[]>([]);
  const [isCalling, setIsCalling] = useState(false);
  const [language, setLanguage] = useState("English");
  const videoRef = useRef<HTMLVideoElement>(null);

  // Translations & Cultural Voice Personas
  const translations = {
    "English": { greeting: "Tell me about your first car.", btnCall: "ANSWER CALL", btnEnd: "END SESSION", tone: "Respectful narrator" },
    "Español": { greeting: "Cuéntame sobre tu primer auto.", btnCall: "CONTESTAR", btnEnd: "TERMINAR", tone: "Warm, friendly abuela" },
    "中文": { greeting: "告诉我你的第一辆车。", btnCall: "接听", btnEnd: "结束", tone: "Wise elder" },
    "Tagalog": { greeting: "Sabihin mo sa akin ang tungkol sa iyong unang kotse.", btnCall: "SAGUTIN", btnEnd: "BABAAN", tone: "Warm and familial" },
    "Tiếng Việt": { greeting: "Kể cho tôi nghe về chiếc xe đầu tiên của bạn.", btnCall: "TRẢ LỜI", btnEnd: "KẾT THÚC", tone: "Respectful and gentle" },
    "العربية": { greeting: "أخبرني عن سيارتك الأولى.", btnCall: "إجابة", btnEnd: "إنهاء", tone: "Storyteller" }
  };

  // WebSocket for Gemini live conversation
  const clientRef = useRef<W3CWebSocket | null>(null);

  useEffect(() => {
    // Only connect WebSocket when the "Call" is answered
    if (!isCalling) {
        if (clientRef.current) clientRef.current.close();
        return;
    }

    // Append the cultural persona instructions to the WebSocket payload
    const culturalTone = translations[language].tone;
    const client = new W3CWebSocket(`wss://your-gemini-server.com/live?userId=${userId}&lang=${language}&tone=${culturalTone}`);
    clientRef.current = client;

    client.onopen = () => console.log(`[GeminiUI] Connected to live server. Mode: ${culturalTone}`);
    client.onmessage = (message) => {
      try {
        const data: GeminiMessage = JSON.parse(message.data as string);
        setMessages((prev) => [...prev, data]);
      } catch (err) {
        console.error(err);
      }
    };

    return () => client.close();
  }, [userId, isCalling, language]);

  // ============================================================
  // Camera + Microphone (Voice-to-Docu Engine)
  // ============================================================
  useEffect(() => {
    async function setupCamera() {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
        if (videoRef.current) {
          videoRef.current.srcObject = stream;
        }
      } catch (err) {
        console.error("[GeminiUI] Camera/mic error. Ensure HTTPS.", err);
      }
    }
    setupCamera();
  }, []);

  const handleCallToggle = () => {
    setIsCalling(!isCalling);
    if (!isCalling) {
        setMessages([{ timestamp: new Date().toISOString(), role: "gemini", content: translations[language].greeting }]);
    } else {
        setMessages([]);
    }
  };

  // ============================================================
  // "National Geographic Meets Apple" Cinematic Aesthetic
  // ============================================================
  return (
    <div style={{
        backgroundColor: "#1a1a1a", // Deep Charcoal
        color: "#ffffff",
        fontFamily: "'Montserrat', 'Proxima Nova', sans-serif", // Geometric Sans-Serif
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        backgroundImage: "url('https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?q=80&w=2000&auto=format&fit=crop')", // Cinematic Golden Hour Background
        backgroundSize: "cover",
        backgroundPosition: "center"
    }}>

      {/* Frosted Glass UI Container */}
      <div style={{
          backgroundColor: "rgba(26, 26, 26, 0.75)",
          backdropFilter: "blur(12px)",
          flex: 1,
          display: "flex",
          flexDirection: "column",
          padding: "40px"
      }}>

          {/* Header & Multilingual Toggle */}
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "40px" }}>
              <h1 style={{ color: "#FFD700", fontSize: "48px", fontWeight: "bold", margin: 0 }}>
                  <span style={{ fontSize: "56px" }}>🎥</span> AI Director
              </h1>
              <select
                  value={language}
                  onChange={(e) => setLanguage(e.target.value)}
                  style={{ fontSize: "24px", padding: "10px", backgroundColor: "#005f73", color: "#fff", border: "none", borderRadius: "8px", cursor: "pointer" }}
              >
                  {Object.keys(translations).map(lang => (
                      <option key={lang} value={lang}>{lang}</option>
                  ))}
              </select>
          </div>

          {/* Cinematic Video Feed (The "Interview" Interface) */}
          <div style={{ display: "flex", flex: 1, gap: "40px" }}>

              <div style={{ flex: 1, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center" }}>
                  <video
                    ref={videoRef}
                    autoPlay
                    muted
                    style={{
                        width: "100%",
                        maxWidth: "800px",
                        border: "8px solid #FFD700", // Rich Gold Border
                        borderRadius: "24px",
                        boxShadow: "0 20px 40px rgba(0,0,0,0.5)",
                        objectFit: "cover",
                        backgroundColor: "#000"
                    }}
                  ></video>

                  {/* Massive Action Buttons */}
                  <div style={{ marginTop: "40px", display: "flex", gap: "20px" }}>
                      {!isCalling ? (
                          <button onClick={handleCallToggle} style={{ fontSize: "36px", padding: "20px 60px", backgroundColor: "#22c55e", color: "white", border: "none", borderRadius: "100px", fontWeight: "bold", cursor: "pointer", boxShadow: "0 0 30px rgba(34, 197, 94, 0.6)", transition: "transform 0.2s" }}>
                              📞 {translations[language].btnCall}
                          </button>
                      ) : (
                          <button onClick={handleCallToggle} style={{ fontSize: "36px", padding: "20px 60px", backgroundColor: "#ef4444", color: "white", border: "none", borderRadius: "100px", fontWeight: "bold", cursor: "pointer", boxShadow: "0 0 30px rgba(239, 68, 68, 0.6)" }}>
                              ☎️ {translations[language].btnEnd}
                          </button>
                      )}
                  </div>
              </div>

              {/* Subtitles & AI Voice Output (Massive Legible Text) */}
              <div style={{ flex: 1, display: "flex", flexDirection: "column", justifyContent: "flex-end", paddingBottom: "100px" }}>
                  {messages.map((msg, idx) => (
                      <div key={idx} style={{ marginBottom: "20px", fontSize: "32px", lineHeight: "1.4" }}>
                          <strong style={{ color: msg.role === "user" ? "#4fd1c5" : "#FFD700" }}> {/* Deep Teal User vs Gold AI */}
                              {msg.role === "user" ? "You:" : "Director:"}
                          </strong>{" "}
                          <span style={{ textShadow: "2px 2px 4px rgba(0,0,0,0.8)" }}>{msg.content}</span>
                      </div>
                  ))}
                  {!isCalling && <p style={{ fontSize: "32px", color: "rgba(255,255,255,0.5)", fontStyle: "italic" }}>Awaiting connection...</p>}
              </div>

          </div>
      </div>
    </div>
  );
};
