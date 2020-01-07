FROM raspbian/stretch

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3 -y
RUN pwd
RUN whoami

ADD docker/launchscript.sh .

ADD src /client

ENTRYPOINT ["sh", "./launchscript.sh"]
