FROM python:3.9.6-alpine

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python", "./main.py" ]

# Build : docker build -t docker-flask .
# Run   : docker run -it -p 5000:5000 docker-flask
