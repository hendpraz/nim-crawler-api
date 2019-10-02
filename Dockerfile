FROM alpine:3.5
RUN apk upgrade --no-cache \
  && apk add --no-cache \
    python3 \
  && pip3 install --no-cache-dir --upgrade pip
COPY requirements.txt /src/requirements.txt
RUN pip3 install -r /src/requirements.txt
COPY database.db /
COPY app.py /src
COPY rest_api /src/rest_api
CMD python3 /src/app.py