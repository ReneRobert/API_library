FROM alpine-python3 
ARG http_proxy
ARG https_proxy
COPY . /app
WORKDIR /app
RUN pip3 install --user -r requirements.txt
CMD python3 -u app.py
