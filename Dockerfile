# Stage 1: Install Node.js and npm
FROM node:18 as node_stage

# Set the working directory inside the container
WORKDIR /app

# Copy the package.json and package-lock.json files into the container
COPY package*.json ./

# Install Node.js dependencies
RUN npm install

# Stage 2: Build your Python application using the official Python image
FROM python:3.10 as python_stage

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Copy the Node.js dependencies from the previous stage
COPY --from=node_stage /app/node_modules ./node_modules

EXPOSE 8080

# Start your application
CMD ["python", "app.py"]