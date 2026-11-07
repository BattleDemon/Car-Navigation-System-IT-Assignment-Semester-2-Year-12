
#!/bin/bash

# Stop if a command fails
set -e

# Create a virtual environment if one does not exist
if [ ! -d "venv" ]; then
    python -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Update pip
python -m pip install --upgrade pip setuptools wheel

# Install external dependencies
python -m pip install \
    pyrosm \
    pynmea2 \
    pandas \
    numpy \
    PyQt5 \
    PyQtWebEngine \
    folium \
    networkx \
    shapely

echo "All dependencies installed successfully."
