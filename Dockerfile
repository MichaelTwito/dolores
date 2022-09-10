FROM alpine:latest

RUN apk add build-base py3-pip python3-dev
COPY . /opt/app
WORKDIR /opt/app
EXPOSE 8080

ADD requirements.txt /srv/requirements.txt
RUN pip install -r requirements.txt
RUN chmod u+x boot.sh

ENTRYPOINT ["sh", "boot.sh"]

