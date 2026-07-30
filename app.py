from flask import (
    Flask, render_template, request,
    session, redirect, url_for, flash
)
import sqlite3
import os
from functools import wraps
from database import get_db

app = Flask(__name__)
app.secret_key = 'sql-injection-demo-secret-key-2024'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login first', 'warning')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return render_template('index.html')

# ============================================================
# INSECURE LOGIN
# Uses string concatenation — VULNERABLE to SQL Injection
# ============================================================
@app.route('/insecure', methods=['GET', 'POST'])
def insecure_login():
    query_tried = None
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()

        if not username or not password:
            flash('Please fill all fields', 'error')
            return render_template('login.html')

        conn = get_db()
        cursor = conn.cursor()

        try:
            query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
            query_tried = query
            cursor.execute(query)
            user = cursor.fetchone()

            if user:
                session['user_id'] = user['id']
                session['username'] = user['username']
                session['login_type'] = 'insecure'
                flash('Insecure login successful! (This is UNSAFE)', 'warning')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid credentials', 'error')

        except Exception as e:
            flash(f'SQL Error: {str(e)}', 'error')

        finally:
            conn.close()

    return render_template('login.html', query_tried=query_tried)

# ============================================================
# SECURE LOGIN
# Uses parameterized query — SAFE from SQL Injection
# ============================================================
@app.route('/secure', methods=['GET', 'POST'])
def secure_login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()

        if not username or not password:
            flash('Please fill all fields', 'error')
            return render_template('secure_login.html')

        conn = get_db()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT * FROM users WHERE username=? AND password=?",
                (username, password)
            )
            user = cursor.fetchone()

            if user:
                session['user_id'] = user['id']
                session['username'] = user['username']
                session['login_type'] = 'secure'
                flash('Secure login successful! (This is SAFE)', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid credentials', 'error')

        except Exception as e:
            flash(f'Error: {str(e)}', 'error')

        finally:
            conn.close()

    return render_template('secure_login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template(
        'dashboard.html',
        username=session.get('username'),
        login_type=session.get('login_type')
    )

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    if not os.path.exists('database.db'):
        print("Database not found. Initializing...")
        from database import init_db
        init_db()
    app.run(debug=True, host='127.0.0.1', port=5000)
