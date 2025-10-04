Air Quality Insights — Fullstack Scaffold

This repository contains a React + TypeScript frontend (Vite) with Tailwind CSS and a Python FastAPI backend scaffold.

Goals
- Clean, modular architecture
- Pluggable adapters for external APIs (TEMPO, PurpleAir, NOAA, AirNow)
- Forecasting engine separated (can be implemented with TensorFlow/PyTorch or scikit-learn)

Quick start (frontend)

```bash
# from project root
npm install
npm run dev
```

Quick start (backend)

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn backend.app.main:app --reload --port 8000
```

Notes
- Frontend expects backend at `http://localhost:8000` by default. Change the URL in `src/App.tsx` or provide an env-based wrapper.
- Add adapter implementations in `backend/app/adapters/` and wire into `backend/app/api/airquality.py` for production use.
