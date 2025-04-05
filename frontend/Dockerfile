FROM python:3.9-slim

WORKDIR /app

COPY frontend.py .

RUN pip install streamlit requests

EXPOSE 8501

CMD ["streamlit", "run", "frontend.py", "--server.port=8501", "--server.enableCORS=false"]

