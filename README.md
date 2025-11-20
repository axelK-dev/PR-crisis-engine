# PR Crisis Engine

A modular platform for managing public relations crises with decision matrices, AI-driven insights, and secure configuration practices.

---

## 📚 Documentation Index

Navigate through the key resources and templates:

### Wiki Templates
- Home
- Architecture Overview
- Brand Voice AI
- [Compliance & Governance](wiki_templates/Compliance_Governancesis Typology](wiki_templates/Crisis_Typemplates/DeploymentFeatures
- Roadmap
- Testing & Validation
- [Use Cases](wiki_templates/Use_Cces
- Crisis Decision Matrix Tool Overview
- BBC Crisis Case Study

---

## 🔐 Crisis Decision Matrix Tool - Secure Setup Guide

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

---

### 3. Security Best Practices
- Never commit `.env` to GitHub. Add it to `.gitignore`.
- Rotate keys regularly.
- Use least privilege principles for Azure Key Vault access.

---

### 4. Running the Tool
Launch the dashboard:
```bash
streamlit run dashboard_modular.py
