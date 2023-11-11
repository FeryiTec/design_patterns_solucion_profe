FROM python:3.9

# python
ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

#RUN apt-get update \
#    && apt-get install --no-install-recommends -y libpq5
#
## dev system utilities
#RUN apt-get update \
#    && apt-get install --no-install-recommends -y \
#	less htop inetutils-ping strace curl postgresql-client unzip

RUN pip install --upgrade pip
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /src

COPY src/ /src/
RUN pip install -e /src
COPY tests/ /tests/

WORKDIR /src
CMD python main.py
