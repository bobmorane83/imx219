FROM debian:bookworm-slim

COPY raspi.list /etc/apt/sources.list.d/raspi.list
COPY trusted.gpg /etc/apt/trusted.gpg.d/raspi.gpg
RUN apt update 

RUN apt install -y --no-install-recommends python3 python3-pip python3-picamera2 python3-numpy

COPY test.py .
CMD ["/usr/bin/python3", "test.py"]