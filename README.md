# SQL Injection Attack Detection and Prevention Using Secure Login System

## 📋 Project Overview

An educational web application demonstrating SQL Injection vulnerabilities and their prevention using parameterized queries. Built with Flask and SQLite.

**Developer:** Mohd Yasin Kazi  
**Class:** TYBSc Computer Science  
**College:** SIWS College  
**Theme:** Leadership in the Age of AI / Cyber Security Education

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Navigate to the project directory**
   ```bash
   cd sql-injection-project
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   ```
   - On Windows: `venv\Scripts\activate`
   - On Linux/Mac: `source venv/bin/activate`

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**
   ```bash
   python init_db.py
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

---

## 🎯 How to Use

### Demo Users

| Username | Password |
|----------|----------|
| admin | admin123 |
| user1 | pass123 |
| user2 | test456 |
| demo | demo123 |
| student | project2024 |
| test | test123 |

### Demonstration Steps

1. **Visit the Insecure Login page**
2. **Try normal login** with valid credentials (e.g., admin/admin123)
3. **Try SQL Injection** - Enter `' OR '1'='1` as username and password
4. **Observe** how the login is bypassed
5. **Visit the Secure Login page**
6. **Try the same SQL Injection payload** - It will fail because parameterized queries prevent injection

### SQL Injection Payloads to Try

| Payload | Effect |
|---------|--------|
| `admin' --` | Comments out password check |
| `' OR '1'='1` | Always-true condition |
| `admin' /*` | Multi-line comment bypass |
| `' OR 1=1 --` | Numeric always-true condition |

---

## 📁 Project Structure

```
sql-injection-project/
├── app.py              # Flask application with routes
├── database.py         # Database connection and initialization
├── init_db.py          # Database setup script
├── requirements.txt    # Python dependencies
├── README.md           # This file
├── database.db         # SQLite database (auto-generated)
├── templates/
│   ├── index.html      # Landing page
│   ├── login.html      # Insecure login page
│   ├── secure_login.html # Secure login page
│   └── dashboard.html  # User dashboard
├── static/
│   ├── css/
│   │   └── style.css   # Main stylesheet
│   └── js/
│       └── script.js   # Main JavaScript
├── screenshots/        # Screenshots directory
└── docs/
    ├── REPORT.md       # Full project report
    ├── PPT.md          # Presentation outline
    ├── Viva.md         # Viva questions and answers
    └── Bibliography.md # References
```

---

## 🧪 Features

- **Two Login Systems:** Insecure (string concatenation) and Secure (parameterized queries)
- **Live SQL Injection Demo:** See the vulnerability in action
- **SQL Query Display:** View the actual SQL query executed
- **One-Click Payload Copy:** Pre-built SQL injection payloads
- **Session Management:** Login/logout with session tracking
- **Flash Messages:** User-friendly notifications
- **Responsive Design:** Works on desktop, tablet, and mobile
- **Dark Theme:** Professional dark + blue interface

---

## ⚠️ Educational Purpose Only

This application is created **solely for educational purposes** to demonstrate:
1. How SQL Injection attacks work
2. Why string concatenation in SQL queries is dangerous
3. How parameterized queries prevent SQL Injection

**DO NOT** use the vulnerable login system in any real-world application.

---

## 🔧 Technologies Used

- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Backend:** Python with Flask framework
- **Database:** SQLite
- **Security:** Parameterized Queries / Prepared Statements

---

## 📄 License

This project is for educational use only.
