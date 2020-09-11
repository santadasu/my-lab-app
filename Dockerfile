FROM python:2

WORKDIR /Users/sandasu/k8sapp/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./ping.py" ]
