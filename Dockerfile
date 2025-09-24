FROM python:3.10-slim-bullseye

WORKDIR /app
COPY . /app

# Install AWS CLI using pip
RUN pip install awscli --upgrade

# Install other dependencies
RUN pip install -r requirements.txt

# Run your app
CMD ["python3", "app.py"]
