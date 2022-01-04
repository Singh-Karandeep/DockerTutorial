FROM python:3.9.6

WORKDIR /usr/src/app
COPY . .

ENTRYPOINT ["python", "./table_volume.py"]

# Volume Location on Windows with WSL Installed : \\wsl$\docker-desktop-data\version-pack-data\community\docker\volumes\
# Paste above in Windows File Explorer

# Build : docker build -t table-volume .
# Run (Without Volume)  : docker run -it table-volume 5 10
# Run (With Volume) : docker run -it -v my-table-vol:/usr/src/app/Artifacts table-volume 5 10

# View Container : $ docker ps -a
# To Gain Shell Access : $ docker exec -it <container_id> bash
