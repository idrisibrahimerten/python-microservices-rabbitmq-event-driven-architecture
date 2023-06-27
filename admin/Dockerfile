FROM python:3.9
ENV PYTHONADMIN 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install Django==3.2.19
RUN pip install --index-url=https://pypi.python.org/simple/ djangorestframework
RUN pip install -r requirements.txt

COPY . /app