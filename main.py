import os

import uvicorn
from fastapi import FastAPI

from router.end import router as end_router
from router.root import router as root_router
from router.server import router as server_router
from router.start import router as start_router

app = FastAPI(
	title="Battlesnake Agent",
	description="HTTP endpoints used by the Battlesnake game engine.",
	version="1.0.0",
)

app.include_router(root_router)
app.include_router(server_router)
app.include_router(start_router)
app.include_router(end_router)


if __name__ == "__main__":
	uvicorn.run(
		app,
		host="localhost",
		port=int(os.environ.get("PORT", "8000")),
	)
