import { useState, useRef,useEffect } from "react";
import ParticleBackground from "./ParticleBackground";
import "./MainPage.css";


export default function MainPage({ onLogout }) {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);
  const recognitionRef = useRef(null);
  const [isTyping, setIsTyping] = useState(false);
const [showScrollBtn, setShowScrollBtn] = useState(false);
const chatEndRef = useRef(null);
const chatLayerRef = useRef(null);
const [isListening, setIsListening] = useState(false);
const listeningRef = useRef(false);
  // SEND MESSAGE
  const handleSend = async () => {
    if (message.trim() === "") return;
    
    // show user message
    setMessages(prev => [
      ...prev,
      { from: "user", text: message }
    ]);
    
    const userMessage = message;
    setMessage("");
    setIsTyping(true);
    
    try {
      // Call backend /agent endpoint
      const response = await fetch("http://localhost:5000/agent", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: userMessage }),
      });
      
      const data = await response.json();
      const aiReply = data.reply || "I couldn't process that request.";
      
      setIsTyping(false);
      setMessages((prev) => [
        ...prev,
        { from: "ai", text: aiReply },
      ]);
    } catch (error) {
      console.error("Error calling backend:", error);
      setIsTyping(false);
      setMessages((prev) => [
        ...prev,
        { from: "ai", text: "Error: Could not reach the backend server." },
      ]);
    }
  };// 2 seconds typing

const handleCopy = (text) => {
  navigator.clipboard.writeText(text);
};

const handleShare = (text) => {
  if (navigator.share) {
    navigator.share({text });
  } else {
    alert("Sharing not supported on this device");
  }
};


  // ENTER KEY SEND
  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      handleSend();
    }
  };
  // 🔓 LOGOUT
const handleLogout = () => {
  // clear stored user data (if any)
  alert("Logout clicked"); // TEMP PROOF
  localStorage.clear();

  // close dropdown
  setShowProfile(false);

  // go back to login / refresh
  onLogout();
};

  // 🎙️ MIC LOGIC - Auto-send after recognition
  const startContinuousListening = () => {
    if (!("webkitSpeechRecognition" in window && "SpeechRecognition" in window)) {
      alert("Speech Recognition not supported in this browser. Please use Chrome, Edge, or similar.");
      return;
    }

    const recognition = new window.webkitSpeechRecognition() || new window.SpeechRecognition();
    recognitionRef.current = recognition;

    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.lang = "en-US";

    let interimTranscript = "";

    recognition.onstart = () => {
      console.log("🎤 Listening started...");
      setIsListening(true);
      listeningRef.current = true;
    };

    recognition.onresult = (event) => {
      interimTranscript = "";
      let finalTranscript = "";

      for (let i = event.resultIndex; i < event.results.length; i++) {
        const transcript = event.results[i][0].transcript;

        if (event.results[i].isFinal) {
          finalTranscript += transcript + " ";
        } else {
          interimTranscript += transcript;
        }
      }

      // Show interim results in input
      if (interimTranscript) {
        setMessage(interimTranscript);
      } else if (finalTranscript) {
        setMessage((prev) => prev + finalTranscript);
      }

      // Auto-send when speech ends (final result detected)
      if (finalTranscript) {
        setTimeout(() => {
          handleSend();
        }, 500);
      }
    };

    recognition.onerror = (event) => {
      console.error("🔴 Speech error:", event.error);
    };

    recognition.onend = () => {
      console.log("🎤 Listening stopped");
      setIsListening(false);
      listeningRef.current = false;
      // Restart listening if it was manually enabled
      if (listeningRef.current) {
        recognition.start();
      }
    };

    recognition.start();
  };

  const stopListening = () => {
    if (recognitionRef.current) {
      recognitionRef.current.stop();
      setIsListening(false);
      listeningRef.current = false;
    }
  };

  // 🎙️ OLD MIC LOGIC - On-demand listening
  const handleMic = () => {
    if (isListening) {
      stopListening();
    } else {
      startContinuousListening();
    }
  };

  // Auto-start listening on mount
  useEffect(() => {
    startContinuousListening();
    // Load chat history on mount
    loadChatHistory();
    return () => {
      if (recognitionRef.current) {
        recognitionRef.current.stop();
      }
    };
  }, []);

  const loadChatHistory = async () => {
    try {
      const response = await fetch("http://localhost:5000/history");
      const data = await response.json();
      const msgs = data.messages || [];
      
      // Convert history format to display format
      const formattedMessages = msgs.map(msg => [
        { from: "user", text: msg.user_request },
        { from: "ai", text: msg.response_summary }
      ]).flat();
      
      setMessages(formattedMessages);
    } catch (error) {
      console.error("Error loading chat history:", error);
    }
  };
// 👤 CLOSE PROFILE ON OUTSIDE CLICK
const [showProfile, setShowProfile] = useState(false);
  const profileRef = useRef(null);
  useEffect(() => {
    const handleClickOutside = (e) => {
      if (profileRef.current && !profileRef.current.contains(e.target)) {
        setShowProfile(false);
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  // detect scroll
  useEffect(() => {
    const chat = chatLayerRef.current;
    if (!chat) return;

    const handleScroll = () => {
      const atBottom =
        chat.scrollHeight - chat.scrollTop <= chat.clientHeight + 20;

      setShowScrollBtn(!atBottom);
    };

    chat.addEventListener("scroll", handleScroll);
    return () => chat.removeEventListener("scroll", handleScroll);
  }, []);
////////////////..........................////////////////////////////
  return (
    <div className="main-page">
      <ParticleBackground />

      {/* Top Navigation */}
      <header className="top-bar">
        <div className="logo">Zen AI</div>

        <div className="profile" ref={profileRef}>
  <div
    className="avatar"
    onClick={() => setShowProfile(!showProfile)}
  >
    👤
  </div>

  {showProfile && (
  <div className="profile-dropdown">
    <div className="profile-name">Pavani Rathore</div>
    <div className="profile-email">pavani@email.com</div>

    <div className="profile-divider"></div>

    <button
  className="logout-btn"
  onClick={() => handleLogout()}
>
  Logout
</button>

  </div>
)}

</div>

      </header>
<div className="workspace">

  {/* Welcome state */}
  <div className="welcome-layer">
  {messages.length === 0 && (
    <div className="welcome-container">
      <h1 className="welcome-title">Welcome to Zen AI</h1>
      <p className="welcome-subtitle">
        Your personal AI assistant for all your needs.
      </p>
    </div>
  )}
</div>

  {/* Chat Area */}

 <div className="chat-layer">
  {!showProfile && messages.length > 0 && (
    <div className="chat-container"  ref={chatLayerRef}>
     {messages.map((msg, index) => (
  <div
    key={index}
    className={`chat-bubble ${msg.from}`}
  >
    {/* MESSAGE TEXT */}
    <div className="bubble-text">
      {msg.text}
    </div>
<div ref={chatEndRef} />
    {/* BUTTONS BELOW (AI ONLY) */}
    {msg.from === "ai" && (
      <div className="message-actions">
        <button onClick={() => handleCopy(msg.text)}>
          📋 Copy
        </button>

        <button onClick={() => handleShare(msg.text)}>
  🔗 Share
</button>

      </div>
    )}
  </div>
))}


      {isTyping && (
        <div className="chat-bubble ai typing">
          Zen AI is typing<span className="dots">...</span>
        </div>
      )}
    </div>
  )}
</div>
</div>
{showScrollBtn && (
  <button
    className="scroll-bottom-btn"
    onClick={() =>
      chatEndRef.current?.scrollIntoView({ behavior: "smooth" })
    }
  >
    ⬇
  </button>
)}

      {/* Input Bar */}
      <div className="input-bar">
        <label className="upload-btn">
          📎
          <input type="file" hidden />
        </label>

        <input
          type="text"
          className="text-input"
          placeholder="Type or speak..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={handleKeyPress}
        />
        <button className="mic-btn" onClick={handleMic} title={isListening ? "Click to stop listening" : "Click to toggle listening"}>
          {isListening ? "🎤🔴" : "🎙️"}
        </button>

        <button className="send-btn" onClick={handleSend}>
          ➤
        </button>
      </div>
    </div>
  );
}
