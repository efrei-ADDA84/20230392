FROM python:3.8

# Setting working dir
WORKDIR /TP1code

COPY requirements.txt /TP1code/

RUN pip install -r requirements.txt

# Install fu gettingWeather.py
COPY src/ /TP1code/

# Final configuration
ENV lat=-22.82
ENV lon=-47.27

CMD [ "python", "./gettingWeather.py" ]