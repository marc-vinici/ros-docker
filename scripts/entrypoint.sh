#!/bin/bash
set -e

# Build the workspace if needed
if [ ! -d "build" ]; then
    echo "Building ROS 2 workspace..."
    colcon build
fi

# Source the setup script
source install/setup.bash

exec /bin/bash
