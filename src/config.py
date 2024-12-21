import os
from dotenv import load_dotenv

# Load environment variables from a .env file (if it exists)
dotenv_path = os.getenv("DOTENV_PATH", ".env")  # Allow custom .env paths via a variable
load_dotenv(dotenv_path)

class Config:
    """
    Configuration class to manage environment variables.
    Supports local .env files and platform-provided environment variables.
    """
    # Model configuration
    MODEL_TYPE = os.getenv("MODEL_TYPE", "linear_regression")  # Default: linear regression
    OUTPUT_VARIABLE_NAME = os.getenv("OUTPUT_VARIABLE_NAME", "inferred_variable")

    # File paths
    DATA_FILE = os.getenv("DATA_FILE", "data.csv")  # Default: static data file
    DOTENV_PATH = dotenv_path  # Save the current .env file path for debugging.

    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    # Vercel environment variable example
    VERBOSE_LOGGING = os.getenv("VERBOSE_LOGGING", "false").lower() == "true"

    # Add more environment variables here as needed
