import "./Signup.css";
import ParticleBackground from "./ParticleBackground";

export default function Signup({ onSignupSuccess, goToLogin }) {
  return (
    <div className="signup-page">
      <ParticleBackground />

      <div className="signup-card">
        <h1 className="signup-title">Zen AI</h1>
        <p className="signup-desc">
          Create your account to get started.
        </p>

        <div className="signup-field">
          <label>Full Name</label>
          <input type="text" placeholder="Enter your name" />
        </div>

        <div className="signup-field">
          <label>Email Address</label>
          <input type="email" placeholder="Enter your email" />
        </div>

        <div className="signup-field">
          <label>Password</label>
          <input type="password" placeholder="Create a password" />
        </div>

        <div className="signup-field">
          <label>Confirm Password</label>
          <input type="password" placeholder="Confirm password" />
        </div>

        <button className="signup-btn" onClick={onSignupSuccess}>Create Account</button>

        <p className="login-link">
          Already have an account? <span onClick={goToLogin}>Login</span>
        </p>
      </div>
    </div>
  );
}
