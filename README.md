# 🩸 BLOOD CARE – Full Stack Blood Donation App (Flutter + Django REST)

BLOOD CARE is a user-friendly mobile application that enables real-time blood request and donation services. Built with **Flutter** for the frontend and **Django REST Framework** for the backend, it connects blood donors and patients efficiently with geolocation features, blood group/city filtering, and helpful health tools like BMI calculation and many other features.

---

## 📦 Project Structure

BLOODCARE-application/
├── BLOOD CARE/ # 🌐 Backend root folder (Django project)
│ ├── api/ # Django app for REST APIs
│ ├── users/ # Django app for user authentication
│ ├── blood_requests/ # App to handle blood requests
│ ├── hospitals/ # Hospital management
│ ├── manage.py # Django management script
│ └── ... # Other Django files
├── bloodcare_flutter/ # 📱 Flutter frontend root folder
│ ├── lib/
│ │ ├── screens/ # Screens like Home, Login, Blood Request
│ │ ├── services/ # API integration
│ │ ├── utils/ # Reusable widgets, constants
│ │ └── main.dart # Flutter app entry point
│ └── pubspec.yaml # Flutter dependencies
└── README.md


---

## 🚀 Key Features

### 🔴 User Features (Mobile App – Flutter)
- 🩸 **Request & Receive Blood** with a few taps
- 📍 **Search Donors** by city and blood group
- 🗺️ **Google Maps Integration** for location-based donor lookup
- 📊 **BMI Calculator** integrated for health tracking
- 🧾 **Registration/Login** system for both donors and receivers
- 🔔 User-friendly UI for seamless interaction

### ⚙️ Backend Features (Django REST)
- 🔐 Token-based authentication
- 📑 CRUD APIs for user management, blood requests, hospitals
- 🏥 Role-based permissions (Donor, Hospital, Admin)
- 🌐 Django Admin for backend data control
- 📦 API ready for integration with any frontend/mobile client

---

## 🛠️ Tech Stack

| Layer        | Technology                        |
|--------------|-----------------------------------|
| Frontend     | Flutter (Dart)                    |
| Backend      | Django + Django REST Framework    |
| Geolocation  | Google Maps API                   |
| Database     | SQLite (development)              |
| Auth         | Token-based Authentication (DRF)  |
|              |                                   |

---

## 📱 Screenshots

> Add these inside a `screenshots/` folder in the repo.

- ![Login](screenshots/login.png)
- ![Map View](screenshots/map_view.png)
- ![Request Blood](screenshots/request_blood.png)
- ![BMI Calculator](screenshots/bmi.png)

---

## ⚙️ Getting Started

### 🔧 Backend (Django)

```bash
cd BLOODCARE-application-backend/BLOOD\ CARE

# Create virtual environment
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start development server
python manage.py runserver


