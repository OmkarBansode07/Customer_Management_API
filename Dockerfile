# build
# Use the official Python image as base
FROM python:3.11-slim


# Set working directory in the container
WORKDIR /api
# Copy the application code into the container
COPY . .

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/venv

RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir wheel

# Copy requirements.txt and install Python dependencies
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

# run
# Expose port 5000 for Flask app
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]