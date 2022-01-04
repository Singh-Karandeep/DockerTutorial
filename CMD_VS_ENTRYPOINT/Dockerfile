FROM python:3.9.6-alpine

WORKDIR /usr/src/app
COPY . .

CMD ["python", "./table.py"]
# CMD ["python", "./table.py", "3", "5"]
# CMD ["python", "./table.py", "2", "5", "10"]

# ENTRYPOINT ["python", "./table.py"]
# ENTRYPOINT ["python", "./table.py", "3"]
# CMD ["4", "8"]
# CMD ["5", "7"]

# Build : docker build -t cmd-ep .
# Run   : docker run -it cmd-ep
# Run   : docker run -it cmd-ep 4 7
# Run   : docker run -it cmd-ep ls

# Que : How to achieve the same in CMD ?
# Ans : $ docker run -it cmd-ep python ./table.py 2 5
