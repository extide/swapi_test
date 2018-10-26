FROM alpine

RUN apk add --no-cache \
    python python-dev python2-dev gcc linux-headers libc-dev py-pip \
   && pip install swapi 

WORKDIR /home

COPY james_code.py /home

CMD ["/usr/bin/python", "/home/james_code.py"]
