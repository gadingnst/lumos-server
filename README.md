# Lumos Server

Minimalist Flask server for managing my home automation tasks (Wake-on-LAN, Server Info, etc).

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
    -   Set `AI_SERVER_MAC_ADDR` to the target machine's MAC address.
    ```bash
    echo "AI_SERVER_MAC_ADDR=00:11:22:33:44:55" > .env
    ```

## Run

Start the server:
```bash
python server.py
```

The server will start at `http://localhost:5500`.
