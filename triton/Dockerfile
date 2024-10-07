FROM nvcr.io/nvidia/tritonserver:24.06-py3

WORKDIR /models

# Copy model repository
COPY models /models

# Install Python backend requirements
COPY requirements.txt /models/requirements.txt
RUN pip install -r /models/requirements.txt

# Expose Triton ports
EXPOSE 8000 8001 8002

# Start Triton Inference Server
CMD ["tritonserver", "--model-repository=/models"]