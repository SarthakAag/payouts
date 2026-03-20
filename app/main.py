from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base

# ROUTES
from app.routes import auth
from app.routes import admin_routes
from app.routes import policy_routes
from app.routes import enrollment_routes
from app.routes import premium_routes
from app.routes import earnings_routes
from app.routes import risk_map_routes

# MODELS
from app.models.user_model import DeliveryPartner
from app.models.admin_model import Admin
from app.models.policy_model import InsurancePolicy
from app.models.enrollment_model import PolicyEnrollment
from app.models.premium_model import PremiumPayment
from app.models.earnings_model import DeliveryEarnings
from app.models.payout_model import PayoutRecord, PredictionHistory

app = FastAPI(
    title="Gig Worker Insurance API",
    version="1.0",
    summary="API for managing insurance policies, enrollments, and payouts for gig workers"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# CREATE DATABASE TABLES
# Use a cross-process lock to avoid race in multi-worker gunicorn startup
import fcntl

def _create_all_tables():
    lock_path = "/tmp/db_init.lock"
    with open(lock_path, "w") as lock_file:
        fcntl.flock(lock_file, fcntl.LOCK_EX)
        try:
            Base.metadata.create_all(bind=engine)
        finally:
            fcntl.flock(lock_file, fcntl.LOCK_UN)

_create_all_tables()

# ROUTERS
app.include_router(auth.router,             prefix="/auth",       tags=["User Auth"])
app.include_router(admin_routes.router,     prefix="/admin",      tags=["Admin Auth"])
app.include_router(policy_routes.router,    prefix="/policy",     tags=["Policy"])
app.include_router(enrollment_routes.router,prefix="/enrollment", tags=["Enrollment"])
app.include_router(premium_routes.router,   prefix="/premium",    tags=["Premium"])
app.include_router(earnings_routes.router,  prefix="/earnings",   tags=["Earnings"])
app.include_router(risk_map_routes.router,                        tags=["Delivery Risk Map"])