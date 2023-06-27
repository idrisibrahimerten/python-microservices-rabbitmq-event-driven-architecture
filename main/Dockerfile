FROM python:3.9
ENV PYTHONADMIN 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN Flask==2.0.2
RUN pip install -r requirements.txt

COPY . /app
