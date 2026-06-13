FROM python:3.10-slim

WORKDIR /app

# psycopg2 / chromadb(hnswlib) 빌드에 필요한 컴파일러
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY backend/requirements.txt backend/requirements.txt

RUN pip install --no-cache-dir -r backend/requirements.txt

COPY backend/ backend/
COPY frontend/public/static/md/ frontend/public/static/md/

WORKDIR /app/backend

EXPOSE 8000

CMD ["sh", "-c", "alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]
