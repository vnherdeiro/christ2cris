FROM ubuntu:bionic
ENV DEBIAN_FRONTEND noninteractive

ENV TZ Europe/London

RUN     apt-get -y update
RUN     apt-get install -y python3-pip

ADD     .   .
RUN     pip3 install --upgrade pip
RUN     pip3 install -r requirements.txt

CMD     ["python3", "/bot/bot.py"]
