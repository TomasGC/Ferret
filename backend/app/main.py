from fastapi import FastAPI

from app.routers import auth, companies, follows, criteria, offers

app = FastAPI(title="Ferret API")

app.include_router(auth.router)
app.include_router(companies.router)
app.include_router(follows.router)
app.include_router(criteria.router)
app.include_router(offers.router)
