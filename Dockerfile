FROM python:3-slim
COPY . /app
RUN pip3 install requests
CMD python /app/hello.py