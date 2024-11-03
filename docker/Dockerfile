# Start from the official ROS 2 Humble image
FROM ros:humble

# Install additional dependencies
RUN apt-get update && \
    apt-get install -y python3-colcon-common-extensions python3-rosdep python3-vcstool build-essential python3-pip && \
    pip3 install psutil && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip3 install psutil

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

ARG USER=ros
RUN useradd -m -s /bin/bash $USER && echo "$USER ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER $USER

RUN rosdep update

WORKDIR /home/$USER/ros2_ws/src
WORKDIR /home/$USER/ros2_ws

RUN echo "source /opt/ros/humble/setup.bash" >> /home/$USER/.bashrc
