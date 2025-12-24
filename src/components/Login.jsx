import "./Login.css";
import ParticleBackground from "./ParticleBackground";

export default function Login({ onLoginSuccess, goToSignup, goToForgot }) {
  return (
    <div className="login-page">
      <ParticleBackground />

      <div className="login-card">
        <h1 className="login-title">Zen AI</h1>
        <p className="login-desc">
          Welcome back! Please login to your account.
        </p>

        <div className="login-field">
          <label>Email Address</label>
          <input type="email" placeholder="Enter your email" />
        </div>

        <div className="login-field">
          <label>Password</label>
          <input type="password" placeholder="Enter your password" />
        </div>

        <a className="forgot" onClick={goToForgot}>Forgot password?</a>

        <button className="login-btn" onClick={onLoginSuccess}>Login</button>

        <p className="signup">
  Don’t have an account?{" "}
  <span onClick={goToSignup}>Sign up</span>
</p>
      </div>
    </div>
  );
}
