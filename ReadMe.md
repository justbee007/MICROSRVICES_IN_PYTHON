# README

This repository contains a Flask-based microservice application for video and audio file management, including conversion, upload, and download functionalities. It utilizes Flask, MongoDB, RabbitMQ, and JWT for authentication and authorization.

## Setup

1. **Dependencies Installation**:
   - Install required Python packages using pip:
     ```bash
     pip install -r requirements.txt
     ```

2. **Database Setup**:
   - MySQL is used for authentication info, and MongoDB for storing files.

3. **Environment Variables**:
   - Set:
     - `AUTH_SVC_ADDRESS`: Address of the auth service.
     - `VIDEO_QUEUE`: Name of the RabbitMQ queue for video processing.
     - `JWT_SECRET`: Secret key for JWT token.

4. **Running the Application**:
   - Start the Flask application: `python server.py`.

## Components

1. **Authentication Service** (`auth_service.py`):
   - Provides user authentication and token generation using JWT.

2. **Video to MP3 Conversion Service** (`convert.py`):
   - Asynchronously converts videos to MP3 using RabbitMQ and MongoDB.

3. **File Upload and Download Service** (`server.py`):
   - Provides endpoints for uploading videos and downloading MP3 files.

## Endpoints

- **/login** (POST): User authentication.
- **/upload** (POST): Uploads videos and triggers MP3 conversion.
- **/download** (GET): Downloads converted MP3 files.

## Kubernetes Deployment

- Follow instructions in the `kubernetes` directory for deployment.

## Contributing

- Contributions welcome via pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
