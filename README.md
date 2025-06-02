# 🩸 BLOOD CARE – Full Stack Blood Donation App (Flutter + Django REST)

BLOOD CARE is a user-friendly mobile application that enables real-time blood request and donation services. Built with **Flutter** for the frontend and **Django REST Framework** for the backend, it connects blood donors and patients efficiently with geolocation features, blood group/city filtering, and helpful health tools like BMI calculation and many other features.

---

## 📦 Project Structure

```

BLOOD CARE/                   # 🌐 Backend root folder (Django project)
├── api/                      # Django app managing:
│   ├── user authentication(JWT)
│   ├── user profile management (view/update)
│   ├── password reset/forget password
│   └── other user-related APIs
├── care/                     # Core Django project folder containing:
│   ├── settings.py           # Project settings
│   ├── urls.py               # URL routing
│   ├── wsgi.py               # WSGI config
│   └── other Django core files
├── users/                    # Django app handling user models and related logic
├── manage.py                 # Django management script
├── media/                    # Folder for user-uploaded images (e.g., profile pictures,documents uplaoded for verification)
└── static/                   # Static files such as system images used in the app
```


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
- 🔐 Token-based authentication (JWT)
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





- ![Login](BLOOD%20CARE/screenshots/screenshots/1.png)  
  **Login Screen:** Users can securely log into the BloodCare application.

- ![Signup](BLOOD%20CARE/screenshots/screenshots/2.png)  
  **Signup Screen:** New users can register to access the app features.

- ![Dashboard](BLOOD%20CARE/screenshots/screenshots/3.jpg)  
  **Dashboard:** Overview of user activities and quick access to main features.

- ![Donors Nearby](BLOOD%20CARE/screenshots/screenshots/5.jpg)  
  **Donors Nearby:** Shows nearby blood donors based on user location markers seen on map.

- ![Donors List](BLOOD%20CARE/screenshots/screenshots/7.jpg)  
  **Donors List:** A detailed list of blood donors filtered by blood group and city.

- ![Request List](BLOOD%20CARE/screenshots/screenshots/8.jpg)  
  **Request List:** Displays blood requests made by users in the community.

- ![Request Form](BLOOD%20CARE/screenshots/screenshots/9.jpg)  
  **Request Form:** Allows users to submit a request for blood donation.

- ![BMI Calculator](BLOOD%20CARE/screenshots/screenshots/12.jpg)  
  **BMI Calculator:** Calculates and displays Body Mass Index for health monitoring.

- ![Other Features](BLOOD%20CARE/screenshots/screenshots/6.jpg)  
  **Additional Features:** Various other helpful utilities integrated into the app.

---

For more detailed views and additional screenshots, please refer to the `screenshots` folder in the repository.



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


