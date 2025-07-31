# 🧑‍🎓 PFA Management Platform

A web-based application designed to streamline the management of *Projets de Fin d'Année (PFA)* in academic institutions. Built using Django and modern front-end tools, this platform facilitates collaboration between students, supervisors, and administrators.

## 📌 Features

### 🔐 Authentication & User Roles
- Secure login/signup system
- Role-based access (Student, Professor, Admin)

### 👨‍🎓 Student Features
- Form binômes (project pairs)
- Browse and request project subjects
- Send/receive requests
- Messaging system with professors
- Personal profile management

### 👨‍🏫 Professor Features
- Propose and manage project subjects
- Validate/refuse binôme requests
- Track student project progress
- Messaging with students

### 🛠️ General Features
- Notifications for all important events
- Profile editing
- Responsive and intuitive interface
- Admin dashboard for user and data management

## 🧰 Technologies Used             
 Backend        :   Django (Python)     
 Frontend       :   HTML, CSS, Bootstrap, JavaScript 
 Database       :   SQLite              
 Modeling Tools :   StarUML (Use Case, Class, Sequence Diagrams) 


## ⚙️ Installation Guide

### Prerequisites
- Python 3.10+
- Virtualenv (recommended)

### Steps

```bash
# Clone the repository
git clone https://github.com/your-username/pfa_project.git
cd pfa-management

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
