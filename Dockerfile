FROM python:3.12
LABEL version=1 
WORKDIR /usr/src/app
#RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD "./app.py" "PyUser" "2024-08-30 00:00:00" 
