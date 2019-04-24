FROM python:3.6.5
MAINTAINER Han <kumpenghan@gmail.com>

ENV INSTALL_PATH /snakeeyes
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install --editable .

CMD gunicorn -b 128.199.164.229:8000 --access-logfile - "snakeeyes.app:create_app()"
