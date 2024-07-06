FROM python:3.9-slim

RUN apt-get update && apt-get install -y

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate -q
RUN pip uninstall -y transformers accelerate -q
RUN pip install transformers[torch] accelerate -q

CMD ["python3","application.py"]
