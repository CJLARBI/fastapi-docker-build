# FROM python:3.10-slim

# WORKDIR /src

# COPY src/requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt

# COPY src/ .

# COPY models /app/models

# COPY data /src/data

# EXPOSE 8000

# CMD ["uvicorn", "src.mlapi:app", "--host", "0.0.0.0", "--port", "8000"]FROM python:3.10-slim

FROM python:3.10-slim

WORKDIR /src

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ .

# Fix path to data folder
COPY src/data /src/data

# Remove or adjust the following if the models directory doesn't exist
# COPY models /app/models 

# Expose port
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "src.mlapi:app", "--host", "0.0.0.0", "--port", "8000"]
