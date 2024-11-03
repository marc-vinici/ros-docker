CONTAINER="ros-docker"
CONTAINER_VERSION="latest"

docker run --rm -it \
    -v "$(pwd)/ros2_ws/src:/home/ros/ros2_ws/src" \
    "${CONTAINER}:${CONTAINER_VERSION}" bash