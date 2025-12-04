# This Dockerfile is almost identical to Service A's.
# The only real difference is the port we expose and run on.
FROM python:3.10-slim

WORKDIR /app

# Cache the dependency layer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Set the app entrypoint
ENV FLASK_APP=app.py

# Expose the port for Service B
EXPOSE 5002

# Run the service on its specific port
CMD ["flask", "run", "--host=0.0.0.0", "--port=5002"]