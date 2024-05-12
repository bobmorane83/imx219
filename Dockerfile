FROM debian:bookworm-slim

COPY raspi.list /etc/apt/sources.list.d/raspi.list
COPY trusted.gpg /etc/apt/trusted.gpg.d/raspi.gpg
RUN apt update 

RUN apt install -y --no-install-recommends python3 python3-pip python3-picamera2
COPY requirements.txt requirements.txt
RUN pip install --break-system-packages -r requirements.txt

COPY . .
CMD ["/usr/bin/python3", "main.py"]