# Dockerfile

FROM ubuntu:20.04 as website-common

SHELL ["/bin/bash", "-c"]

ENV USER=website
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        build-essential \
        cargo \
        curl \
        libffi-dev \
        libssl-dev \
        python3-dev \
        python3-pip \
        python3-venv \
        rustc && \
    useradd -m -s /bin/bash $USER

USER $USER
WORKDIR /home/${USER}

ENV VENV=/home/${USER}/.venv
ENV PATH=${VENV}/bin:$PATH

# Create virtual env and install common package.
COPY --chown=$USER ./common/ ./common/
COPY --chown=$USER ./certs/ ./certs/
RUN python3 -m venv $VENV && \
    pip3 install -U pip && \
    cd common && \
    python3 setup.py install

CMD ["python3"]

################################################################################

FROM website-common as website-index

COPY --chown=$USER ./index/ ./index

USER $USER
WORKDIR /home/${USER}/index

RUN pip3 install -r requirements.txt

CMD ["gunicorn"]

################################################################################

FROM website-common as website-apps

USER root
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get update && \
    apt-get install -y nodejs

COPY --chown=$USER ./apps/ ./apps

USER $USER
WORKDIR /home/${USER}/apps

RUN pip3 install -r requirements.txt && \
    npm install && \
    npm run build

CMD ["gunicorn"]
