# backend
# Django FAQ API with Redis Caching & Auto-Translation 🌍

A Django-based **FAQ API** that supports:

- **Multi-language translation** (Hindi, Bengali, etc.) using Google Translate
- **Redis caching** for faster responses
- **REST API** with Django REST Framework (DRF)
- **Automated testing** (Pytest for backend, Mocha/Chai for API tests)

---

## 📌 Features

👉 **CRUD operations** for FAQs\
👉 **Automatic translations** using `googletrans`\
👉 **Redis caching** for fast responses\
👉 **REST API endpoints** with Django REST Framework\
👉 **Comprehensive testing** (Pytest, Mocha/Chai)

---

## ⚡ Installation & Setup

### **1️⃣ Clone the Repository**

```sh
git clone https://github.com/yourusername/django-faq-api.git
cd django-faq-api
```

### **2️⃣ Create a Virtual Environme**i)&#xA;&#xA;python -m venv venv&#xA;source venv/bin/activate  # On Mac/Linux&#xA;venv\Scripts\activate  # On Windows

### **3️⃣ Install Dependencies**

```sh
pip install -r requirements.txt
```

### **4️⃣ Install & Start Redis**

Ensure Redis is installed and running:

```sh
# On Linux/macOS
sudo apt update && sudo apt install redis
redis-server

# On Windows (use WSL or Docker)
docker run -d --name redis -p 6379:6379 redis
```

### **5️⃣ Apply Migrations & Create a Superuser**

```sh
python manage.py migrate
python manage.py createsuperuser
```

### **6️⃣ Start the Django Server**

```sh
python manage.py runserver
```

---

## 🚀 API Usage Examples

### **Get All FAQs**

```sh
curl -X GET http://127.0.0.1:8000/api/faqs/
```

### **Get a Single FAQ**

```sh
curl -X GET http://127.0.0.1:8000/api/faqs/1/
```

### **Create a New FAQ**

```sh
curl -X POST http://127.0.0.1:8000/api/faqs/ \
     -H "Content-Type: application/json" \
     -d '{
           "question": "What is Django?",
           "answer": "Django is a web framework for Python."
         }'
```

### **Update an FAQ**

```sh
curl -X PUT http://127.0.0.1:8000/api/faqs/1/ \
     -H "Content-Type: application/json" \
     -d '{
           "question": "Updated Question",
           "answer": "Updated Answer"
         }'
```

### **Delete an FAQ**

```sh
curl -X DELETE http://127.0.0.1:8000/api/faqs/1/
```

---

## 🛠 Running Tests

### ** Run Backend Tests (Pytest)**

```sh
pytest
```


---

## 👥 Contribution Guidelines

Want to contribute? Follow these steps:

1️⃣ **Fork the repo** and clone it locally.\
2️⃣ Create a **new branch** (`git checkout -b feature-name`).\
3️⃣ **Commit changes** (`git commit -m "feat: Add new feature"`).\
4️⃣ **Push to GitHub** (`git push origin feature-name`).\
5️⃣ Open a **Pull Request (PR)** and describe your changes.

### **Commit Message Format (Conventional Commits)**

- `feat:` Add a new feature
- `fix:` Bug fix
- `docs:` Documentation updates
- `refactor:` Code improvements
- `test:` Adding tests
- `chore:` Dependencies or minor changes

Example:

```sh
git commit -m "feat: Implement automatic translation for FAQs"
```

---

## 🐝 License

This project is licensed under the **MIT License**. Feel free to use and modify! 🚀

---

## 📩 Contact & Support

For any issues or feature requests, open a GitHub issue or contact:\
📧 Email: `tejasvita1511@gmail.com`

