# Lumos Server

Minimalist Flask server for managing my home automation tasks (Wake-on-LAN, Shutdown, Server Info, etc).

## Setup

1.  **Clone the repository** (if not already done).

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure environment:**
    -   Copy the `.env.example` (or create `.env` manually).
    -   Set all env in `.env` file by your own.

## Run

Start the server:
```bash
python server.py
```

The server will start at `http://localhost:5500`.
