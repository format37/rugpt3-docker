FROM rocker/cuda:4.3.1
# FROM huggingface/transformers-pytorch-gpu:latest

WORKDIR /app

# Install git
RUN apt-get update \
    && apt-get install -y git \
    && rm -rf /var/lib/apt/lists/*

# Clone the repository and checkout the specific version
RUN git clone https://github.com/PanQiWei/AutoGPTQ.git \
    && cd AutoGPTQ \
    && git checkout v0.2.2 \
    && pip install .

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# EXPOSE 5000

COPY app.py ./

CMD ["python3", "./app.py"]
# Run perpetually
# CMD ["tail", "-f", "/dev/null"]
