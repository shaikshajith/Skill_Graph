import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

COGNODB_URI = os.getenv("COGNODB_URI")
COGNODB_USERNAME = os.getenv("COGNODB_USERNAME")
COGNODB_PASSWORD = os.getenv("COGNODB_PASSWORD")


def validate_config():
    """Check whether all required CognoDB credentials are available."""

    missing = []

    if not COGNODB_URI:
        missing.append("COGNODB_URI")

    if not COGNODB_USERNAME:
        missing.append("COGNODB_USERNAME")

    if not COGNODB_PASSWORD:
        missing.append("COGNODB_PASSWORD")

    if missing:
        raise ValueError(
            f"Missing environment variables: {', '.join(missing)}"
        )