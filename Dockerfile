FROM langchain/langchain

WORKDIR /app

# Install pip requirements
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY main.py .
COPY helper.py .
COPY codebasics_faqs.csv .

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]
