import "./ForgetPassword.css";
import ParticleBackground from "./ParticleBackground";

export default function ForgotPassword({ goToLogin }) {
  return (
    <div className="forgot-page">
      <ParticleBackground />

      <div className="forgot-card">
        <h1 className="forgot-title">Zen AI</h1>
        <p className="forgot-desc">
          Enter your email and we’ll send you a reset link.
        </p>

        <div className="forgot-field">
          <label>Email Address</label>
          <input type="email" placeholder="Enter your email" />
        </div>

        <button className="forgot-btn">Send Reset Link</button>

        <p className="back-login">
          Remembered your password?{" "}
          <span onClick={goToLogin}>Login</span>
        </p>
      </div>
    </div>
  );
}
