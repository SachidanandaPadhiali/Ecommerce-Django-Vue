# 🛍️ VueCommerce — Full-Stack E-commerce Platform

VueCommerce is a modern, responsive e-commerce web application built with Django (backend) and Vue.js (frontend). It supports product listings, dynamic cart functionality, user authentication, and admin management with a RESTful API at its core.

---

## 🚀 Features

- 🧾 User registration & JWT-based login/logout
- 📦 Product catalog with pagination, filtering & search
- 🛒 Shopping cart with quantity updates & checkout
- ✅ Order history & payment confirmation
- 🔒 Admin dashboard for product & order management
- 🌟 Dynamic star ratings & reviews
- 📸 Image upload support
- ⚡ Frontend powered by Vue 3 with component-based architecture

---

## 📁 Tech Stack

| Layer       | Technology     |
|-------------|----------------|
| Frontend    | Vue.js 3, Pinia, Vue Router, Axios |
| Backend     | Django, Django REST Framework      |
| Database    | SQLite3 (dev), PostgreSQL (prod)   |
| Auth        | JWT via `djangorestframework-simplejwt` |
| Deployment  | Docker, Gunicorn, Nginx (optional), Heroku/Railway-ready |

---

## 📦 Installation

### 🔧 Backend Setup

```bash
# Clone the project
git clone https://github.com/yourusername/vuecommerce.git
cd vuecommerce/backend

# Create virtual environment & install dependencies
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run migrations & start server
python manage.py migrate
python manage.py runserver
