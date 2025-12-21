#!/bin/bash

# Script to setup autorun for Lumos Server using systemd user service
# This ensures the server starts automatically when the user logs in.

# Get the absolute path of the current directory
PROJECT_DIR=$(pwd)
SERVICE_NAME="lumos-server"
SERVICE_DIR="$HOME/.config/systemd/user"
SERVICE_FILE="$SERVICE_DIR/$SERVICE_NAME.service"

# Check for virtual environment
if [ -d "$PROJECT_DIR/venv" ]; then
    PYTHON_EXEC="$PROJECT_DIR/venv/bin/python"
    echo "Using virtual environment: $PROJECT_DIR/venv"
elif [ -d "$PROJECT_DIR/.venv" ]; then
    PYTHON_EXEC="$PROJECT_DIR/.venv/bin/python"
    echo "Using virtual environment: $PROJECT_DIR/.venv"
else
    PYTHON_EXEC=$(which python3)
    echo "Using system python: $PYTHON_EXEC"
fi

# Check for .env file and read PORT
PORT=5000 # Default
if [ -f "$PROJECT_DIR/.env" ]; then
    echo "Reading configuration from .env..."
    # Extract PORT from .env (handling potential comments or whitespace)
    # This grep looks for PORT=... and handles optional quotes
    ENV_PORT=$(grep "^PORT=" "$PROJECT_DIR/.env" | cut -d '=' -f2 | tr -d '[:space:]"' | tr -d "'")
    if [ ! -z "$ENV_PORT" ]; then
        PORT=$ENV_PORT
        echo "Found PORT in .env: $PORT"
    fi
fi

if [ -z "$PYTHON_EXEC" ]; then
    echo "Error: python3 not found. Please install python3 first."
    exit 1
fi

echo "Setting up autorun for Lumos Server..."
echo "Project Directory: $PROJECT_DIR"
echo "Python Executable: $PYTHON_EXEC"

# Create systemd user directory if it doesn't exist
mkdir -p "$SERVICE_DIR"

# Create the service file
cat <<EOF > "$SERVICE_FILE"
[Unit]
Description=Lumos Server
After=network.target

[Service]
Type=simple
WorkingDirectory=$PROJECT_DIR
ExecStart=$PYTHON_EXEC $PROJECT_DIR/server.py
Restart=on-failure
Environment=PORT=$PORT
# Add environment variables from .env if needed, or load them in python

[Install]
WantedBy=default.target
EOF

echo "Created service file at $SERVICE_FILE"

# Reload systemd user daemon
echo "Reloading systemd user daemon..."
systemctl --user daemon-reload

# Enable the service to start on login
echo "Enabling service $SERVICE_NAME..."
systemctl --user enable $SERVICE_NAME

# Start the service now
echo "Starting service $SERVICE_NAME..."
systemctl --user start $SERVICE_NAME

echo "---------------------------------------------------"
echo "✅ Setup complete!"
echo "The Lumos Server is now running and will start automatically on login."
echo ""
echo "To check status:    systemctl --user status $SERVICE_NAME"
echo "To view logs:       journalctl --user -u $SERVICE_NAME -f"
echo "To stop:            systemctl --user stop $SERVICE_NAME"
echo "To disable autorun: systemctl --user disable $SERVICE_NAME"
echo "---------------------------------------------------"

# Enable linger to keep the service running after logout
echo "Enabling linger for $USER..."
loginctl enable-linger $USER

echo "---------------------------------------------------"
echo "✅ Setup complete!"
