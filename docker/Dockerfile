from ubuntu:22.04 as base

RUN apt-get update && apt-get install -y python3-pip gcc python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /repo

COPY requirements.txt /repo

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt
# Install the headless version of opencv in docker
RUN python3 -m pip uninstall -y opencv-python opencv-contrib-python
RUN python3 -m pip install --no-cache-dir opencv-python-headless opencv-contrib-python-headless


COPY . /repo

FROM base as lab

# Had some issues with psutil (needed by jupyter) on aarch64, so need to install it from source
RUN python3 -m pip install --no-cache-dir  psutil --no-binary=psutil
RUN python3 -m pip install --no-cache-dir jupyter

EXPOSE 8888/tcp
ENTRYPOINT [ "jupyter", "lab", "--ip", "0.0.0.0", "--port", "8888", "--no-browser", "--allow-root"]
