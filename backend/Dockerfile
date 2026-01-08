FROM python:3.10-slim

# --------------------
# Environment settings
# --------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=backend.settings

# --------------------
# Set working directory
# --------------------
WORKDIR /app/backend

# --------------------
# System dependencies
# --------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# --------------------
# Python dependencies
# --------------------
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# --------------------
# Copy project source
# --------------------
COPY . /app/

# --------------------
# Expose port
# --------------------
EXPOSE 8000

# --------------------
# Run Django with Gunicorn
# --------------------
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]


