FROM python:3.13.2 AS builder

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Create virtual environment and install dependencies
RUN python -m venv .venv
COPY requirements.txt ./
RUN .venv/bin/pip install -r requirements.txt

# --- Final Slim Image ---
FROM python:3.13.2-slim

WORKDIR /app

# Copy installed venv and source files
COPY --from=builder /app/.venv .venv/
COPY . .

# Expose the port Fly expects
EXPOSE 8080

# Run using Gunicorn instead of Flask's dev server
CMD ["/app/.venv/bin/gunicorn", "app:app", "--bind", "0.0.0.0:8080"]

