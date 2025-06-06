FROM python:3.12

WORKDIR /src

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
    
EXPOSE 8080

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8080"]
