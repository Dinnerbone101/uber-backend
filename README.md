# Ride Booking Backend (Uber-like System)

A backend system that simulates core functionalities of a ride-booking platform like Uber. Built using Django, this project focuses on ride creation, driver allocation, and ride lifecycle management.

---

## Features

* Rider creation
* Driver creation
* Ride booking (pickup and drop coordinates)
* Basic driver assignment
* Ride cancellation (if implemented)
* Backend APIs using Django views

---

## Tech Stack

* Backend: Django
* Database: SQLite
* Language: Python

---

## Project Structure

```
ride_booking/
│
├── manage.py
├── db.sqlite3
│
├── ride_app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── utils.py
│
└── ride_booking/
    ├── settings.py
    ├── urls.py
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/yourusername/ride-booking-backend.git
cd ride-booking-backend
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install django
```

### 4. Run migrations

```
python manage.py migrate
```

### 5. Start server

```
python manage.py runserver
```

---

## API Endpoints

| Method | Endpoint                  | Description                         |
| ------ | ------------------------- | ----------------------------------- |
| POST   | /create_ride/             | Create a new ride and assign driver |
| POST   | /start_ride/<ride_id>/    | Start an assigned ride              |
| POST   | /complete_ride/<ride_id>/ | Complete an ongoing ride            |
| POST   | /cancel_ride/<ride_id>/   | Cancel a ride                       |


## Example Request
---
POST /create_ride/

{
  "pickup_lat": 12.9,
  "pickup_lon": 77.5,
  "drop_lat": 13.0,
  "drop_lon": 77.6
}

---

## What I Learned

* Django backend fundamentals
* API handling using views
* Database modeling
* Structuring a real-world backend project
* 
---

## Author

Prajwal.Y.S
GitHub: https://github.com/Dinnerbone101
