FROM python:3.9-slim
COPY . /
WORKDIR /
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python /MasterFilter.py
