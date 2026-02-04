# 🚀 Two-Tier Flask Application

A modern, containerized two-tier web application built with Flask and MySQL, featuring Docker deployment and CI/CD integration with Jenkins.

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [CI/CD Pipeline](#cicd-pipeline)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)

## 🔍 Overview

This is a two-tier web application that demonstrates a simple message board system. Users can submit messages through a web interface, which are then stored in a MySQL database. The application is fully containerized using Docker and can be deployed with a single command.

The project showcases:
- Modern web application development with Flask
- Database integration with MySQL
- Containerization with Docker
- Multi-container orchestration with Docker Compose
- CI/CD automation with Jenkins

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Two-Tier Architecture                    │
└─────────────────────────────────────────────────────────────┘

    ┌──────────────────────────────────────────────┐
    │              Client Layer                     │
    │         (Web Browser / User)                  │
    └──────────────┬───────────────────────────────┘
                   │
                   │ HTTP Requests (Port 5000)
                   │
    ┌──────────────▼───────────────────────────────┐
    │          Presentation Tier                    │
    │        (Flask Web Application)                │
    │                                               │
    │  ┌─────────────────────────────────────┐     │
    │  │  app.py (Main Application)          │     │
    │  │  - Routes & Controllers             │     │
    │  │  - Request Handling                 │     │
    │  └─────────────────────────────────────┘     │
    │                                               │
    │  ┌─────────────────────────────────────┐     │
    │  │  Templates (HTML) + Static (CSS)    │     │
    │  │  - User Interface                   │     │
    │  └─────────────────────────────────────┘     │
    │                                               │
    │  ┌─────────────────────────────────────┐     │
    │  │  config.py (Configuration)          │     │
    │  │  - Environment Variables            │     │
    │  └─────────────────────────────────────┘     │
    │                                               │
    │  ┌─────────────────────────────────────┐     │
    │  │  db.py (Database Connection)        │     │
    │  │  - MySQL Connector                  │     │
    │  └─────────────────────────────────────┘     │
    └──────────────┬───────────────────────────────┘
                   │
                   │ MySQL Protocol (Port 3306)
                   │
    ┌──────────────▼───────────────────────────────┐
    │            Data Tier                          │
    │       (MySQL Database Server)                 │
    │                                               │
    │  ┌─────────────────────────────────────┐     │
    │  │  Database: twotierdb                │     │
    │  │                                     │     │
    │  │  Table: messages                    │     │
    │  │  - id (INT, PRIMARY KEY)            │     │
    │  │  - content (VARCHAR)                │     │
    │  │  - created_at (TIMESTAMP)           │     │
    │  └─────────────────────────────────────┘     │
    │                                               │
    │  ┌─────────────────────────────────────┐     │
    │  │  Persistent Storage Volume          │     │
    │  │  (mysql_data)                       │     │
    │  └─────────────────────────────────────┘     │
    └───────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│              Containerization Layer                           │
│                                                               │
│  ┌──────────────────────┐  ┌──────────────────────┐          │
│  │  Flask Container     │  │  MySQL Container     │          │
│  │  (web)               │  │  (db)                │          │
│  │  Port: 5000          │  │  Port: 3307→3306     │          │
│  └──────────────────────┘  └──────────────────────┘          │
│                                                               │
│          Docker Compose Orchestration                         │
└───────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│                   CI/CD Pipeline                              │
│                   (Jenkins)                                   │
│                                                               │
│  Stage 1: Clean → Stage 2: Build & Deploy                    │
└───────────────────────────────────────────────────────────────┘
```

### Architecture Components

#### **Tier 1: Presentation Layer (Flask Application)**
- **Purpose**: Handles HTTP requests, business logic, and renders HTML templates
- **Components**:
  - Flask web framework for routing and request handling
  - Jinja2 templates for dynamic HTML rendering
  - Static CSS files for styling
  - Environment-based configuration management
  - MySQL database connection management

#### **Tier 2: Data Layer (MySQL Database)**
- **Purpose**: Stores and manages application data persistently
- **Components**:
  - MySQL 8 database server
  - Persistent volume for data storage
  - Automatic schema initialization
  - Connection pooling through mysql-connector-python

## ✨ Features

- **Message Board System**: Submit and view messages in real-time
- **Persistent Storage**: All messages are stored in MySQL database
- **Health Check Endpoint**: Monitor application status
- **Responsive UI**: Modern, gradient-based design with clean interface
- **Automatic Database Initialization**: Schema created on first run
- **Environment Configuration**: Flexible configuration through environment variables
- **Containerized Deployment**: Complete Docker setup with docker-compose
- **CI/CD Ready**: Jenkins pipeline for automated deployment
- **Data Persistence**: MySQL data persists across container restarts

## 🛠️ Tech Stack

### Backend
- **Flask** - Lightweight Python web framework
- **Python 3.10** - Programming language
- **mysql-connector-python** - MySQL database driver

### Database
- **MySQL 8** - Relational database management system

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with gradients and modern design
- **Jinja2** - Template engine

### DevOps
- **Docker** - Containerization platform
- **Docker Compose** - Multi-container orchestration
- **Jenkins** - CI/CD automation

## 📦 Prerequisites

Before running this application, ensure you have the following installed:

- **Docker** (version 20.10 or higher)
- **Docker Compose** (version 1.29 or higher)
- **Git** (for cloning the repository)

Optional (for local development without Docker):
- Python 3.10+
- MySQL 8+
- pip (Python package manager)

## 🚀 Installation

### Option 1: Using Docker Compose (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/Shreyyy07/Two-Tier-Flask-App.git
   cd Two-Tier-Flask-App
   ```

2. **Start the application**
   ```bash
   docker compose up -d --build
   ```

3. **Access the application**
   - Open your browser and navigate to: `http://localhost:5000`
   - The database will be available at: `localhost:3307`

4. **Stop the application**
   ```bash
   docker compose down
   ```

5. **Clean up (including volumes)**
   ```bash
   docker compose down -v
   ```

### Option 2: Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Shreyyy07/Two-Tier-Flask-App.git
   cd Two-Tier-Flask-App
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up MySQL database**
   ```bash
   mysql -u root -p
   CREATE DATABASE twotierdb;
   ```

4. **Configure environment variables**
   ```bash
   export DB_HOST=localhost
   export DB_USER=root
   export DB_PASSWORD=your_password
   export DB_NAME=twotierdb
   export DB_PORT=3306
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   - Open your browser and navigate to: `http://localhost:5000`

## 💻 Usage

### Submitting Messages

1. Navigate to `http://localhost:5000`
2. Enter your message in the text input field
3. Click "Save Message" button
4. Your message will appear in the "Stored Messages" section below

### Viewing Messages

All submitted messages are displayed on the homepage in reverse chronological order (newest first), showing:
- Message content
- Timestamp of submission

### Health Check

Monitor the application status:
```bash
curl http://localhost:5000/health
```

Response:
```json
{
  "status": "UP"
}
```

## 📁 Project Structure

```
Two-Tier-Flask-App/
│
├── app.py                  # Main Flask application
├── config.py               # Configuration management
├── db.py                   # Database connection handler
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker image definition
├── docker-compose.yml     # Multi-container orchestration
├── Jenkinsfile            # CI/CD pipeline definition
├── .gitignore             # Git ignore rules
│
├── templates/             # HTML templates
│   └── index.html         # Main page template
│
└── static/                # Static assets
    └── style.css          # Application styles
```

### File Descriptions

- **app.py**: Main application file containing Flask routes, database initialization, and business logic
- **config.py**: Configuration class that loads settings from environment variables
- **db.py**: Database connection factory using mysql-connector-python
- **requirements.txt**: Python package dependencies
- **Dockerfile**: Instructions for building the Flask application Docker image
- **docker-compose.yml**: Defines and configures both web and database services
- **Jenkinsfile**: Jenkins pipeline for automated deployment
- **templates/index.html**: Jinja2 template for the main web interface
- **static/style.css**: CSS styles with gradient background and modern design

## 🔄 CI/CD Pipeline

The project includes a Jenkins pipeline with the following stages:

### Stage 1: Clean Old Containers
- Removes any existing containers and orphaned resources
- Ensures clean slate for new deployment

### Stage 2: Build & Deploy
- Builds Docker images from Dockerfile
- Starts containers in detached mode
- Automatically applies any configuration changes

### Pipeline Configuration

The Jenkinsfile is configured for Windows agents and uses:
- `docker compose down --remove-orphans` for cleanup
- `docker compose up -d --build` for deployment

To use the pipeline:
1. Set up Jenkins with Docker support
2. Create a new Pipeline job
3. Point it to this repository
4. Run the pipeline

## 🔧 Environment Variables

### Application Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `APP_NAME` | Two-Tier Flask App | Application name displayed in UI |
| `ENV` | development | Environment (development/production) |

### Database Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `DB_HOST` | localhost | MySQL server hostname |
| `DB_USER` | root | Database user |
| `DB_PASSWORD` | root | Database password |
| `DB_NAME` | twotierdb | Database name |
| `DB_PORT` | 3307 | Database port (3306 inside container) |

### Docker Compose Override

When using Docker Compose, environment variables are automatically set:
- `DB_HOST=db` (uses service name for internal networking)
- `DB_PORT=3306` (internal container port)

## 🌐 API Endpoints

### Web Routes

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Display the message board interface |
| `/` | POST | Submit a new message |
| `/health` | GET | Application health check |

### Request/Response Examples

**Submit a Message (POST /)**
```html
Content-Type: application/x-www-form-urlencoded

message=Hello World
```

**Health Check (GET /health)**
```bash
curl http://localhost:5000/health
```
Response:
```json
{
  "status": "UP"
}
```

## 🐛 Troubleshooting

### Database Connection Issues

If you encounter database connection errors:

1. **Check if containers are running**
   ```bash
   docker ps
   ```

2. **Check database logs**
   ```bash
   docker logs two-tier-flask-app-db-1
   ```

3. **Verify network connectivity**
   ```bash
   docker exec -it two-tier-flask-app-web-1 ping db
   ```

### Port Already in Use

If port 5000 or 3307 is already in use:

1. **Find the process using the port**
   ```bash
   # On Linux/Mac
   lsof -i :5000
   
   # On Windows
   netstat -ano | findstr :5000
   ```

2. **Modify ports in docker-compose.yml**
   ```yaml
   ports:
     - "5001:5000"  # Change external port
   ```

### Database Data Persistence

To reset the database:
```bash
docker compose down -v  # Removes volumes
docker compose up -d --build
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available for educational purposes.

## 👤 Author

**Shreyyy07**

- GitHub: [@Shreyyy07](https://github.com/Shreyyy07)

## 🙏 Acknowledgments

- Flask framework for the simple and elegant web framework
- MySQL for robust database management
- Docker for containerization technology
- Jenkins for CI/CD automation

---

Made with ❤️ by Shreyyy07
