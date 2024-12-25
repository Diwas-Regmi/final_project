# final_project

This project uses face recognition technology to automate attendance marking. It leverages OpenCV, Dlib, and Face_Recognition libraries for real-time detection and recognition.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- Detects faces from live webcam feed.
- Compares detected faces against a database of student images.
- Marks attendance in a CSV file with name, date, and time.

## Requirements
Make sure you have the following installed on your system:
- Python 3.7 or above
- Libraries:
  - OpenCV
  - face_recognition
  - dlib
  - numpy

## Installation

### Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/Diwas-Regmi/final_project.git
cd final_project
```

### Install Required Libraries
Install all dependencies using the provided `requirements.txt` file:
```bash
pip install -r requirements.txt
```
If `requirements.txt` is not available, manually install the required libraries:
```bash
pip install opencv-python face_recognition dlib numpy
```

## Usage

### 1. Add Student Images
- Place all student images inside the `Students` folder.
- Name each image with the student’s name (e.g., `John_Doe.jpg`).

### 2. Run the Project
Execute the main Python file to start the face recognition attendance system:
```bash
python final_project.py
```

### 3. Mark Attendance
- The program will detect faces from the webcam.
- It will compare detected faces with the stored images in the `Students` folder.
- If a match is found, the student's attendance will be marked in the `attendance.csv` file with the current date and time.

## How It Works
1. **Face Encoding**:
   - The program reads images from the `Students` folder and encodes their facial features using the `face_recognition` library.
2. **Live Detection**:
   - It uses the webcam to capture video frames.
   - Detects faces in real-time and encodes them for comparison.
3. **Comparison**:
   - Compares the encoded faces with stored encodings to find matches.
4. **Attendance Marking**:
   - If a match is found, the student's name is written to `attendance.csv` along with the current date and time.

## File Structure
```
final_project/
├── Students/        # Folder containing student images
├── final_project.py # Main Python script
├── attendance.csv   # Output file for attendance logs
├── README.md        # Project documentation
```

## Contributing
Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to explore, modify, and enhance the project as needed. For any issues or suggestions, open an issue in the GitHub repository!

