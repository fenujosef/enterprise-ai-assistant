from app.settings import settings


print("Environment:", settings.environment)
print("Model:", settings.model_name)
print(
    "Groq key loaded:",
    bool(settings.groq_api_key),
)