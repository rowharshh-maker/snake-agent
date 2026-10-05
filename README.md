# Battlesnake Agent

FastAPI application with the four HTTP endpoints used by the Battlesnake agent.

## Windows setup

Create and activate the virtual environment, then install the project dependencies:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the server

```powershell
python main.py
```

The server listens on `http://localhost:8000` by default. To select another port in PowerShell, set `PORT` before starting the app:

```powershell
$env:PORT = "8080"
python main.py
```

## Endpoints

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/` | Returns Battlesnake metadata |
| GET | `/server` | Returns server health |
| POST | `/start` | Receives the game start payload |
| POST | `/end` | Receives the game end payload |

FastAPI's interactive API documentation is available at `
