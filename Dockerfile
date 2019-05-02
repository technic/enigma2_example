FROM technic93/e2xvfb:latest

RUN apt-get install -y bash-completion command-not-found psmisc htop vim

RUN pip install ptvsd
EXPOSE 5678
COPY mytest-ptvsd.py /opt/mytest-ptvsd.py
CMD [ "x11vnc", "-forever" ]
