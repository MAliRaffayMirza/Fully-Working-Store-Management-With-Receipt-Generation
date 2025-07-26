# 🧾 Store Management System with PDF Receipt Generator

This is a **fully functional Flask-based Store Management System** that allows users and administrators to manage product inventories, search by category, apply discounts, and generate **print-ready PDF receipts**. It includes user login, admin panel, dynamic form handling, session management, and beautifully styled HTML templates using pure inline CSS.

---

## 🚀 Features

### 👤 User System
- **Login System** with sessions
- Separate interfaces for **Admin** and **Customer**

### 🛍 Product Management (Admin Panel)
- Add, Read, Update, and Delete products
- Add new products dynamically through HTML forms
- Categorized product reading
- Category selection dropdown auto-updated from `categories.txt`
- Labels and field names dynamically read from `labels.txt`

### 🧾 Receipt System
- Add items by **Product ID**
- Items displayed in a styled HTML table
- Calculate **total dues**
- Apply **custom discounts**
- Auto-generate **PDF invoice** with discount applied using `WeasyPrint`

### 📄 File Handling & Storage
- Products stored in `items.txt`
- Product categories stored in `categories.txt`
- Labels in `labels.txt`
- Admin login stored securely in `admin.txt`
- Receipts rendered from `html.txt`
- Generated PDF is downloaded as `Invoice.pdf`

---

## 🛠 Tech Stack

- **Python 3** with **Flask**
- **WeasyPrint** for PDF rendering
- **HTML + CSS** (pure inline, no templates)
- Basic **file-based storage** (can be upgraded to SQLite or MongoDB)

---

## 📂 Folder Structure

```text
📦 Project Root
├── app.py              # Main Flask application
├── admin.txt           # Admin passwords (for login)
├── users.txt           # User login credentials
├── items.txt           # Stored product data
├── labels.txt          # Field labels for product display
├── categories.txt      # Product categories
├── html.txt            # HTML receipt body (used before rendering)
├── Invoice.pdf         # Final generated invoice
```
---

## ✅ How to Run Locally

1. Make sure Python 3 is installed.
2. Install dependencies:
    ```
    pip install flask weasyprint
    ```
3. Run the Flask server:
    ```
    python app.py
    ```
4. Navigate to `http://127.0.0.1:5000/` in your browser.

---

## 💡 Highlights

- Clean and consistent **user interface**
- Strong focus on **real-world use cases** like receipts and inventory
- Modular and **easily expandable**
- Styled for readability and user-friendliness
- Built using **pure logic, not external libraries or frameworks**
- **Session management**, **form handling**, and **PDF export** — all in one app!

---

## 🔐 Future Improvements

- Add password hashing (bcrypt or werkzeug)
- Upgrade to database (SQLite or PostgreSQL)
- Add product image support
- Add “Add Label” and “Add Category” through the UI
- Login validation improvements
- REST API support for external integrations

---

## 🤝 About the Developer

This project was built **from scratch** in just a few days with **over 750 lines of clean Python code**, fully designed and executed by an aspiring Computer Science student preparing for a **Werkstudent (IT) job in Germany**.  
Every line represents hard work, learning, and determination to become job-ready — not in theory, but with *real, working systems*.

---

## 📌 Live Demo

Deployed on **Render**:  
🔗 [Try it Live](https://crud-flask-app-v01o.onrender.com/)  
(Note: Load times may vary based on server wake-up time.)

---

## 📫 Contact

If you'd like to collaborate, hire, or give feedback:

**Developer:** Muhammad Ali Raffay  
📧 Email: [Your Email Here]  
📍 Open to Werkstudent roles in Germany (IT | Python | Web Dev)
