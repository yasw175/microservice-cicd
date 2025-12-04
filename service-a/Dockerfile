# Using a slim Python image to keep our container size down.
FROM python:3.10-slim

# Set the working directory inside the container.
# All our commands (like 'pip' and 'flask') will run from here.
WORKDIR /app

# Copy just the requirements file first.
# Docker caches this layer, so it won't re-install dependencies
# every time we change our app code, only when requirements.txt changes.
COPY requirements.txt .

# Install our Python dependencies.
# --no-cache-dir saves a bit of space.
RUN pip install --no-cache-dir -r requirements.txt

# Now, copy the rest of our application code (app.py, etc.) into the container.
COPY . .

# Tell Flask which file to run.
ENV FLASK_APP=app.py

# Expose port 5001. This tells Docker the container will listen on this port.
EXPOSE 5001

# The command to run when the container starts.
# This runs 'flask run' and binds it to all interfaces (0.0.0.0)
# on the port we specified.
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]