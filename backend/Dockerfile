FROM python:3.10-slim

WORKDIR /app

# psycopg2 / chromadb(hnswlib) 빌드에 필요한 컴파일러
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY backend/requirements.txt backend/requirements.txt

# torch는 CPU 전용 빌드로 설치 (CUDA 포함 버전 대비 이미지 용량 대폭 절감)
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu \
    && pip install --no-cache-dir -r backend/requirements.txt

# 챗봇 임베딩 모델을 빌드 타임에 캐싱 (런타임 콜드스타트 시 재다운로드 방지)
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')"

COPY backend/ backend/
COPY frontend/public/static/md/ frontend/public/static/md/

WORKDIR /app/backend

EXPOSE 8000

CMD ["sh", "-c", "alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]
