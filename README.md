# Attendance System with Excel Logging

A real-time attendance system that tracks attendance using facial recognition or RFID technology. The system records attendance in an Excel file along with the date and time when a person is marked present.

## ✨ Features

- Real-time attendance tracking using facial recognition or RFID cards
- Records attendance in an Excel file (including name, date, and time)
- Easy to use with an intuitive interface
- Tracks attendance for students or employees
- Simple and customizable to suit specific needs

## 🛠️ Tech Stack

- Python 3.x
- OpenCV (for face detection)
- dlib or face_recognition (for face recognition)
- Pandas (for Excel file handling)
- Tkinter or Flask (for user interface)

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/attendance-system.git
cd attendance-system
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Set Up the Excel File
Make sure the Excel file is set up to log the attendance with columns: Name, Date, and Time. The system will create this file automatically, or you can use an existing template.

Example:


Name	Date	Time
John Doe	2025-04-21	08:45 AM
Jane Smith	2025-04-21	09:00 AM
4. Run the Application
To start the attendance system, run:

bash
Copy
Edit
python attendance_system.py
The application will detect faces or read RFID cards, and it will record the name along with the current time in the Excel file.

📁 Project Structure
perl
Copy
Edit
attendance-system/
│
├── attendance_system.py   # Main script for attendance tracking
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── attendees.xlsx         # Excel file to store attendance data
└── images/                # Folder for storing images for facial recognition (if applicable)


🤖 How It Works
Facial Recognition/RFID Detection: The system detects the face or RFID card when a person is in front of the camera or scans their card.

Attendance Logging: Once a match is detected, the system logs the person's name, the current date, and the time in the Excel file (attendees.xlsx).

Excel File Update: The data is saved in real-time, allowing for easy export or analysis of attendance data.
