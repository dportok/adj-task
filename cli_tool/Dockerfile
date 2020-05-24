FROM python:3.7.6-slim-buster
ADD . /opt/adjust
WORKDIR /opt/adjust
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3.7", "adjust.py"]