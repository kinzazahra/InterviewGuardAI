# 🧠 InterviewGuard AI
### AI-Powered Fraud & Cheating Detection System for Online Interviews

---

## 🌍 Problem Statement

With the rise of online interviews and examinations, ensuring fairness has become a major challenge.

Common issues include:
- ❌ Cheating using external help
- ❌ Tab switching during tests
- ❌ Multiple people assisting the candidate
- ❌ Looking away repeatedly (reading from another screen)
- ❌ Mobile phone usage

Manual monitoring is inefficient and unreliable.

---

## 💡 Solution

**InterviewGuard AI** is an intelligent proctoring system that uses:
- 🎥 Webcam monitoring
- 🧠 Computer Vision
- 🌐 Browser activity tracking

to detect suspicious behavior in real-time and generate a **trust score**.

---

## 🚀 Features

### 👁️ Face Monitoring
- Detects no face / multiple faces
- Alerts when candidate leaves screen

### 👀 Behavior Tracking
- Identifies suspicious movements
- Detects repeated looking away

### 🖥️ Tab Switching Detection
- Logs when user switches tabs or minimizes window

### 📊 AI Trust Score
- Generates a real-time score based on activity

### 📄 Suspicious Activity Report
- Displays:
  - Events log
  - Final trust score
  - Risk level (Normal / Suspicious / High Risk)

---

## 🛠️ Tech Stack

| Technology | Usage |
|-----------|------|
| Python | Backend logic |
| Flask | Web framework |
| OpenCV | Webcam processing |
| MediaPipe | Face detection |
| HTML/CSS | Frontend |
| JavaScript | Tab monitoring |

---

## 📂 Project Structure


InterviewGuardAI/
│
├── app.py
├── requirements.txt
│
├── templates/
│ ├── index.html
│ ├── report.html
│
├── static/
│ ├── style.css
│ ├── script.js
│
└── screenshots/ (optional)


---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/InterviewGuardAI.git
cd InterviewGuardAI
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Application
python app.py
4️⃣ Open in Browser
http://127.0.0.1:5000
📊 How It Works
Webcam captures live video
Face detection runs in real-time
Browser activity is monitored using JavaScript
Events are logged (tab switch, no face, multiple faces)
Suspicion score is updated dynamically
Final report is generated
🧠 Trust Score Logic
Activity	Impact
No face detected	-1
Multiple faces	-2
Tab switch	-5
Normal behavior	+5
📌 Output
✅ Normal (Score ≥ 80)
⚠️ Suspicious (50–79)
🚨 High Risk (< 50)
🔥 Future Enhancements
🔐 Face Recognition (identity verification)
👁️ Eye/Gaze Tracking
📱 Phone Detection (YOLO)
📸 Screenshot capture on suspicious events
📊 Admin Dashboard
☁️ Cloud deployment
🤖 Machine Learning-based cheating prediction
🎯 Use Cases
Online interviews
Remote hiring
Online exams
Certification tests
Virtual classrooms

🙌 Author

Kinza Zahra

