FROM ubuntu:22.04

ENV PIP_CACHE_DIR=/var/cache/buildkit/pip
RUN mkdir -p $PIP_CACHE_DIR
RUN rm -f /etc/apt/apt.conf.d/docker-clean
RUN --mount=type=cache,target=/var/cache/apt \
	apt-get update && apt-get install -yqq --no-install-recommends \
	python3 python3-pip && rm -rf /var/lib/apt/lists/*

# Changes working directory to `/app` within docker image
WORKDIR /app

# Copies everything in the local folder `./gesis-export/` into the container folder `/app`
COPY . . 

CMD ["python3", "./src/hello.py"]
