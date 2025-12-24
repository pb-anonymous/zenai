import { useState } from "react";
import "./App.css";
import ParticleBackground from "./components/ParticleBackground";
import Login from "./components/Login";
import Signup from "./components/Signup";
import ForgotPassword from "./components/ForgetPassword";
import MainPage from "./components/MainPage";

function App() {
  const [page, setPage] = useState("landing");
  // landing | login | signup | forgot | main

  // LOGIN PAGE
  if (page === "login") {
    return (
      <Login
        onLoginSuccess={() => setPage("main")}
        goToSignup={() => setPage("signup")}
        goToForgot={() => setPage("forgot")}
      />
    );
  }

  // SIGNUP PAGE
  if (page === "signup") {
    return (
      <Signup
        onSignupSuccess={() => setPage("main")}
        goToLogin={() => setPage("login")}
      />
    );
  }

  // FORGOT PASSWORD
  if (page === "forgot") {
    return <ForgotPassword goToLogin={() => setPage("login")} />;
  }

  // MAIN WORKING PAGE
  if (page === "main") {
    return <MainPage onLogout={() => setPage("login")} />;
  }

  // LANDING PAGE
  return (
    <>
      <ParticleBackground />

      <div className="hero">
        <h1 className="title">Zen AI</h1>
        <p>Built to Listen. Built to Execute.</p>

        <div className="cta">
          <button className="primary" onClick={() => setPage("login")}>
            Open AI Modal
          </button>
        </div>
      </div>
    </>
  );
}

export default App;
