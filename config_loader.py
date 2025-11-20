
# config_loader.py
# Secure configuration loader using python-dotenv
# Future-ready for Azure Key Vault integration

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_config():
    return {
        "ai_service": "azure_openai",
        "workflow_service": "teams_webhook",
        "sentiment_service": "brandwatch",
        "api_keys": {
            "azure_openai": os.getenv("AZURE_OPENAI_KEY"),
            "teams": os.getenv("TEAMS_WEBHOOK_URL"),
            "brandwatch": os.getenv("BRANDWATCH_KEY")
        }
    }

# ------------------ Future Azure Key Vault Integration ------------------
# Steps:
# 1. Install Azure SDK: pip install azure-identity azure-keyvault-secrets
# 2. Authenticate using DefaultAzureCredential()
# 3. Create SecretClient with Key Vault URL
# 4. Replace os.getenv calls with client.get_secret("secret-name").value
