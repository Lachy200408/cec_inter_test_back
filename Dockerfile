FROM python:3.9-slim-buster

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt-get update \
		&& apt-get install -y --no-install-recommends \
			gcc \
			libpq-dev \
		&& pip install --no-cache-dir -r requirements.txt 

COPY . .

EXPOSE 8000

CMD ["fastapi", "run", "./app/main.py"]