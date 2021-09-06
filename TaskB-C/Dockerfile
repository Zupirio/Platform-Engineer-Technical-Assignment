FROM python:3

RUN mkdir /app
ADD . /app
WORKDIR /app
# ENV MAX_SIZE=10000
RUN pip3 install -r requirements.txt
CMD ["python", "bubbleSort.py"]
