# TORVAK Configuration
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "gemini")
LLM_MODEL = os.getenv("LLM_MODEL", "gemini-2.5-flash")
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.2"))
MEMORY_DB_PATH = os.getenv("MEMORY_DB_PATH", "memory/memory.json")
MEMORY_BACKUP_PATH = os.getenv("MEMORY_BACKUP_PATH", "memory/backup.json")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")