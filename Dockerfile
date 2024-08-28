# running app with tailwind
# npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch

# PYTHON FOR THE PROJECT
FROM python:3.12.3



# SETTING UP ENV VARIABLES
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

#SETTING UP WORKING DIRECTORY
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/