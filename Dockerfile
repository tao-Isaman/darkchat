FROM python:3.9

COPY . ./server

WORKDIR /server

RUN pip install -r requirements.txt

# RUN ./init_env.sh

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]