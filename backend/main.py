from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from db.database import init_db
from routers import transactions, upload, summary
import os

app = FastAPI(title="Personal Finance Tracker")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Only needed during development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(transactions.router, prefix="/transactions", tags=["transactions"])
app.include_router(upload.router, prefix="/upload", tags=["upload"])
app.include_router(summary.router, prefix="/summary", tags=["summary"])

# Serve the React frontend in production
# Run "npm run build" in the frontend folder first to generate the dist folder
FRONTEND_DIST = os.path.join(os.path.dirname(__file__), "../frontend/dist")

if os.path.exists(FRONTEND_DIST):
    app.mount("/assets", StaticFiles(directory=os.path.join(FRONTEND_DIST, "assets")), name="assets")

    @app.get("/{full_path:path}")
    def serve_frontend(full_path: str):
        return FileResponse(os.path.join(FRONTEND_DIST, "index.html"))
else:
    @app.get("/")
    def root():
        return {"message": "Personal Finance Tracker API — run 'npm run build' in the frontend folder to serve the UI"}
