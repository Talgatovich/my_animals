FROM python:3.7-slim
WORKDIR /app
COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip3 install -r ./requirements.txt --no-cache-dir

COPY ./ ./
CMD ["gunicorn", "my_animals.wsgi:application", "--bind", "0:8000"]