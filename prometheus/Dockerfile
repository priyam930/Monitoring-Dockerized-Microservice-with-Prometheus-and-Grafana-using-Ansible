FROM ubuntu:22.04
RUN apt update && apt install -y wget tar
RUN useradd -rs /bin/false prometheus

RUN wget https://github.com/prometheus/prometheus/releases/download/v2.51.1/prometheus-2.51.1.linux-amd64.tar.gz && \
    tar -xvf prometheus-2.51.1.linux-amd64.tar.gz && \
    mv prometheus-2.51.1.linux-amd64 /etc/prometheus

COPY prometheus.yml /etc/prometheus/prometheus.yml
EXPOSE 9090
CMD ["/etc/prometheus/prometheus", "--config.file=/etc/prometheus/prometheus.yml"]
