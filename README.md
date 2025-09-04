# 🏫 IIT Gandhinagar Campus Navigation App

- Welcome to the **IITGN Campus Navigation** web application — your one-stop solution to easily find facilities and navigate across the IIT Gandhinagar campus!

- This app is designed to help students, visitors, and faculty members locate classrooms, hostels, food courts, ATMs, sports areas, washrooms, and more — all from a clean, accessible interface.

---

## 🔍 Features

### 🧭 Where Do You Want to Go?
Easily choose from categorized facilities and discover locations instantly.

### 🏷️ Categories Available:
- 🎓 **Academic** – Classrooms, departments, and labs  
- 🎤 **Auditorium and OAT** – Seminar halls, OATs  
- 🏦 **Bank & ATM** – ATM and banking services  
- 🍽️ **Food** – Mess, canteens, food courts  
- 🏥 **Health Center** – Medical and emergency rooms  
- 🏠 **Hostels** – Hostel blocks, washrooms, water points  
- 📚 **Library** – Central library and reading rooms  
- 🅿️ **Parking Area** – Campus vehicle parking locations  
- 🛒 **Shops** – Stationery, printing, and campus stores  
- 🏸 **Sports** – Fields, courts, and sport complexes  
- 🚻 **Washrooms** – Bathrooms across blocks  
- 💧 **Water Points** – Water coolers across campus  

---
## 📸 Screenshots
<img width="1876" height="910" alt="image" src="https://github.com/user-attachments/assets/776cdf9e-5acd-4ff6-af21-ae68a37efabb" />
<img width="1486" height="940" alt="image" src="https://github.com/user-attachments/assets/1c91bf47-9ea1-4d03-ae0e-3f9ea5ab4c82" />


---

## 💻 Tech Stack

- **Frontend**: HTML, CSS, Bootstrap 5
- **Backend**: Django (Python)
- **Templating**: Django Templates
- **Deployment**: Render / Vercel *(planned)*  
- **Counter**: JavaScript + Django (in-memory or localStorage-based)

---

## 📥 Feedback & Inquiries

- Have suggestions, spotted an issue, or want to contribute?  
- 📬 Fill out this form: [Google Form Link](https://forms.gle/nfYMX1LCb4v2nKJu6)
- Feel free to reach out for collaboration or queries!
---

## 📂 Setup Instructions (For Local Development)

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Sreejaan/IIT-GN-Campus-Guide.git
   cd iitgn-campus-navigation
   
   python -m venv env
   source env/bin/activate  # or env\Scripts\activate on Windows
   pip install -r requirements.txt

   python manage.py migrate
   
   python manage.py runserver
   ```
