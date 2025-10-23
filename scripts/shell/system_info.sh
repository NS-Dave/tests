#!/bin/bash
# Script to display system information

echo "=== System Information ==="
echo "Hostname: $(hostname)"
echo "OS: $(uname -s)"
echo "Kernel: $(uname -r)"
echo "Architecture: $(uname -m)"
echo ""
echo "=== Current User ==="
echo "User: $(whoami)"
echo "Home: $HOME"
echo ""
echo "=== Date and Time ==="
echo "Date: $(date)"
echo ""
echo "=== Disk Usage ==="
df -h / | tail -n 1
