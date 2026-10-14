
FROM python:3.9-slim


WORKDIR /app


COPY requirements.txt .


RUN pip install -r requirements.txt


COPY . .


EXPOSE 5000

# 7. डबा चालू केल्यावर काय करायचं - Website चालू कर
CMD ["python", "app.py"]