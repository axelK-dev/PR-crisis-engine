# Crisis Decision Matrix Tool

## Overview
The **Crisis Decision Matrix Tool** is a modular, secure, and scalable decision-support system designed to help organizations make better and faster decisions during high-pressure situations. It combines **AI tone optimization**, **sentiment analysis**, and a **decision matrix** to recommend actions based on structured insights.

This tool is **educational by design**—it guides decision-makers through structured reasoning rather than imposing rigid control. It promotes transparency and accountability while remaining fully customizable.

---

## Key Features
- **Customizable Architecture**
  - Modular design allows easy integration of new services (Azure OpenAI, Claude, Gemini, Slack, Brandwatch).
  - Clear separation of logic, UI, and configuration for maintainability.

- **Scalable & Deployable**
  - Lightweight SQLite backend for local use.
  - Ready for cloud deployment via Streamlit Cloud, Azure App Service, or Docker.
  - Future-ready for enterprise security with Azure Key Vault.

- **Secure Configuration**
  - Secrets managed via `.env` and `python-dotenv`.
  - Documentation for Azure Key Vault integration included.

- **Decision Matrix Logic**
  - Combines tone and sentiment → recommended action.
  - Testable and trainable for future machine learning enhancements.

- **Streamlit Dashboard**
  - Audit trail with filters.
  - Template management.
  - Real-time analysis sidebar.

---

## Ethical Framing
This tool is **not a surveillance mechanism**. It is a **decision-support and education platform**:
- Helps leaders arrive at better decisions faster.
- Provides transparency on recommendations without enforcing compliance.
- Logs actions for accountability, not punishment.

**Governance Principles**:
- Use for **support**, not control.
- Ensure **consent and clarity** in deployment.
- Avoid rigid enforcement—keep flexibility for human judgment.

---

## Risks & Mitigation
- **Risk**: Misuse as a rigid compliance tool.
  - **Mitigation**: Frame as advisory, not mandatory.
- **Risk**: Fear of accountability.
  - **Mitigation**: Communicate benefits of transparency for organizational resilience.

---

## Architecture Diagram
*(Insert diagram showing: Streamlit UI → Engine → Config Loader → APIs → SQLite DB)*

---

## Deployment Guide
### Local Setup
1. Clone repository.
2. Create `.env` file:
   ```bash
   AZURE_OPENAI_KEY=your-azure-key
   TEAMS_WEBHOOK_URL=your-teams-webhook-url
   BRANDWATCH_KEY=your-brandwatch-key

## Power of Choice & Brand Voice Alignment
One of the strongest advantages of this tool is its **flexibility in AI integration**. Organizations can choose the AI service that best reflects their brand voice and values—whether it’s Azure OpenAI, Claude, Gemini, or future models.

### Why This Matters
- **Personalization**: Crisis responses should sound authentic and aligned with organizational tone.
- **Vendor Freedom**: No lock-in. Swap or add AI services easily by updating configuration.
- **Future-Proof**: As new AI models emerge, they can be integrated without redesigning the system.

### Enhancements for Brand Voice
- **Tone Profile Manager**: Pre-set tone styles (empathetic, assertive, neutral) mapped to AI prompts.
- **Preview Mode**: Test tone outputs before sending.
- **Governance Controls**: Logs show which AI was used for which decision, reinforcing accountability.

**Pitch Angle**:
> “Our system ensures that every crisis response reflects your organization’s unique tone and values—powered by the AI you trust.”

---

## Brand-Specific AI Training & Secure Personalization
A key differentiator of this tool is its ability to reflect an organization’s unique voice and values—even under crisis conditions. By leveraging **custom AI training** and secure handling of sensitive information, the system ensures responses feel authentic and aligned with brand identity.

### Why This Matters
- **Authenticity**: Responses mirror the tone and language found in your organization’s literature, press releases, and guidelines.
- **Client Trust**: Personalized communication strengthens relationships during high-pressure situations.
- **Competitive Edge**: Moves beyond generic AI outputs to deliver brand-specific advisory.

### How It Works
- **Custom AI Training**:
  - Fine-tune or prompt-engineer models using internal documents and tone guidelines.
  - Dynamically apply tone profiles during analysis.
- **Secure Handling of Sensitive Data**:
  - Store tone profiles and proprietary content references in `.env` or encrypted vaults.
  - Use **Azure Key Vault** for enterprise-grade security.
- **Governance Controls**:
  - Logs show which AI and tone profile were used for each recommendation.
  - Ensures transparency without exposing sensitive content.

**Pitch Angle**:
> “Our system doesn’t just use AI—it uses *your AI*, trained on your literature and tone, for responses that feel authentic and aligned with your brand.”

### Why This Matters
- **Personalization**: Crisis responses should sound authentic and aligned with organizational tone.
- **Vendor Freedom**: No lock-in. Swap or add AI services easily by updating configuration.
- **Future-Proof**: As new AI models emerge, they can be integrated without redesigning the system.

### Enhancements for Brand Voice
- **Tone Profile Manager**: Pre-set tone styles (empathetic, assertive, neutral) mapped to AI prompts.
- **Preview Mode**: Test tone outputs before sending.
- **Governance Controls**: Logs show which AI was used for which decision, reinforcing accountability.

**Pitch Angle**:
> “Our system ensures that every crisis response reflects your organization’s unique tone and values—powered by the AI you trust.”