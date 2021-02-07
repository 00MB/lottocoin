FROM python:3.7-slim

WORKDIR lottocoin

EXPOSE 5000

RUN pip install flask pycryptodome jsonpickle flask_sqlalchemy requests flask_bcrypt flask_login flask_wtf email_validator gunicorn

COPY . .

CMD ["gunicorn", "lottocoin:app", "-b", "0.0.0.0:5000", "-w", "6"]