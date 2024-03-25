FROM python:3.9.18-slim

ARG UID
ARG GID
ARG USERNAME

RUN groupadd -g ${GID} ${USERNAME} \
  && useradd -u ${UID} -g ${GID} -s /bin/bash -m ${USERNAME}

RUN apt-get update && \
    apt-get upgrade && \
    apt-get install -y \
    vim \
    python3-dev \
    default-mysql-client \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config

RUN mkdir -p /opt/python
WORKDIR /opt/python

USER ${UID}

RUN echo 'alias ll="ls -la"' >> ~/.bashrc

RUN python -m pip install --upgrade pip
RUN python -m pip install --upgrade setuptools
