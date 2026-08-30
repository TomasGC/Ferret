# Commands - Ferret Build & Test

---

## Backend (Python)

```bash
# Setup (one-time)
cd backend
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
cp .env.example .env          # then edit DATABASE_URL/JWT_SECRET

# Local Postgres for dev
docker compose -f docker-compose.dev.yml up -d

# Run the API
uvicorn app.main:app --reload

# Run tests
pytest

# Run the scraper manually (same entrypoint as the daily GitHub Actions job)
python scripts/run_scrape.py
```

## Android (Kotlin)

Open `app/` in Android Studio — it syncs the Gradle wrapper automatically on first open (see `contexts/architecture.md` note on the missing wrapper jar). After that:

```bash
# From app/ directory
gradlew assembleDebug
gradlew testDebugUnitTest
```

(`gradlew`/`gradlew.bat` appear after the first Android Studio sync — don't expect them before that.)
