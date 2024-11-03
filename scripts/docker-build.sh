CONTAINER="ros-docker"
DOCKERFILE="docker/Dockerfile"

docker build -t ${CONTAINER} -f ${DOCKERFILE} .