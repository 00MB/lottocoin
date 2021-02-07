FROM python:3.7-slim

WORKDIR lottocoin

EXPOSE 5000

RUN pip install flask pycryptodome jsonpickle flask_sqlalchemy requests flask_bcrypt flask_login flask_wtf email_validator expiringdict

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]