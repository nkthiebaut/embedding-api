FROM nvcr.io/nvidia/tritonserver:22.12-py3

WORKDIR /models

# Copy model repository
COPY models /models

# Install Python backend requirements
RUN pip install -r ./requirements.txt

# Expose Triton ports
EXPOSE 8000 8001 8002

# Start Triton Inference Server
CMD ["tritonserver", "--model-repository=/models"]