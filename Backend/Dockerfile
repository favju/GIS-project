FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN apt-get update && \
    apt-get install -y libproj-dev libfreexl-dev libgdal-dev gdal-bin 
COPY . /code/
