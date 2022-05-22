FROM python:3-slim-buster
ENV PYTHONUNBUFFERED 1

WORKDIR /web_app
ADD . /web_app
COPY requirements.txt /web_app/
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "/web_app/manage.py", "runserver", "0.0.0.0:8000", "--insecure"]
