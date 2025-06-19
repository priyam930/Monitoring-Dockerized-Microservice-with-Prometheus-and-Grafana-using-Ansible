FROM ubuntu:22.04

# Install dependencies first
RUN apt update && \
    apt install -y wget libfontconfig1 adduser libx11-dev gnupg2 software-properties-common

# Download and install Grafana OSS instead of Enterprise (safer, more stable)
RUN wget https://dl.grafana.com/oss/release/grafana_10.4.2_amd64.deb && \
    dpkg -i grafana_10.4.2_amd64.deb || apt-get install -f -y

EXPOSE 3000

CMD ["/usr/sbin/grafana-server", "--homepath=/usr/share/grafana", "--config=/etc/grafana/grafana.ini"]
