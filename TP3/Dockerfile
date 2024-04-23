FROM python:3.12-alpine

# Setting working dir
WORKDIR /TP2app

# Install system dependencies
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install fu gettingWeather.py
COPY src/ ./

EXPOSE 5000
CMD [ "python", "./gettingWeather.py" ]