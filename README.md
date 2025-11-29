# PR Crisis Engine

![Engine Header](/engine_header.png)

> A modular platform for managing public relations crises with decision matrices, AI-driven insights, and secure configuration practices.

---

## Quick Start
1. **Clone the repo**
   ```bash
   git clone https://github.com/axelK-dev/PR-crisis-engine.git
   cd PR-crisis-engine
---

## Documentation Index

Navigate through the key resources and templates:

### Wiki Templates

This project includes a set of structured wiki templates for documentation and knowledge management:

- **Architecture.md** – System architecture overview.
- **Brand_Voice_AI.md** – Guidelines for AI-driven brand voice.
- **Compliance_Governance.md** – Compliance and governance standards.
- **Configuration_Customization.md** – Configuration and customization instructions.
- **Crisis_Typology.md** – Classification of crisis types.
- **Deployment_Guide.md** – Steps for deploying the engine.
- **Ethical_Risk.md** – Ethical risk considerations.
- **FAQ.md** – Frequently asked questions.
- **Home.md** – Main wiki landing page.
- **Key_Features.md** – Highlights of core features.
- **Roadmap.md** – Planned development roadmap.
- **Testing_Validation.md** – Testing and validation procedures.
- **Use_Cases.md** – Practical use cases and examples.

![Crisis Alert](/crisis_alert.png)
---

## Crisis Decision Matrix Tool - Secure Setup Guide

### 1. Environment Variables Setup
To keep your API keys secure, use a `.env` file instead of hardcoding them.

**Steps:**
1. Create a file named `.env` in your project root.
2. Add your keys:
    ```env
    AZURE_OPENAI_KEY=your-azure-openai-key
    TEAMS_WEBHOOK_URL=your-teams-webhook-url
    BRANDWATCH_KEY=your-brandwatch-api-key
    ```
3. Install `python-dotenv`:
    ```bash
    pip install python-dotenv
    ```
4. The system will automatically load these keys using `config_loader.py`.

---

### 2. Azure Key Vault Integration (Enterprise Security)
For production deployments, use Azure Key Vault instead of `.env`.

**Steps:**
1. Install Azure SDK:
    ```bash
    pip install azure-identity azure-keyvault-secrets
    ```
2. Authenticate using DefaultAzureCredential:
    ```python
    from azure.identity import DefaultAzureCredential
    from azure.keyvault.secrets import SecretClient

    credential = DefaultAzureCredential()
    client = SecretClient(vault_url="https://<your-keyvault-name>.vault.azure.net/", credential=credential)
    secret = client.get_secret("AZURE_OPENAI_KEY").value
    ```
3. Replace `os.getenv()` calls in `config_loader.py` with `client.get_secret("secret-name").value`.
4. Ensure your app has proper Azure RBAC permissions to access Key Vault.

![Modular Engine](/mod_engine.png)
---

### 3. Security Best Practices
- Never commit `.env` to GitHub. Add it to `.gitignore`.
- Rotate keys regularly.
- Use least privilege principles for Azure Key Vault access.

---
![Python Badge](/python_badge.png)

### 4. Running the Tool
Launch the dashboard:
```bash
streamlit run dashboard_modular.py
