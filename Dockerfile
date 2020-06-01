FROM alpine

RUN apk add git python3 curl
RUN pip3 install flask flask-wtf email-validator flask-sqlalchemy

ADD . hangman

WORKDIR hangman

CMD python3 script.py
