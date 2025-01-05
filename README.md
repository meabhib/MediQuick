# MediQuick

MediQuick is a web application designed to analyze symptoms and suggest medications, making healthcare information accessible to individuals without medical expertise. The platform has helped over 1,000 users identify potential health concerns and access reliable suggestions for medications.

---

## Overview

The **Health Assistant Project** is a web-based application that provides users with an interactive platform for:

- Identifying potential health issues.
- Suggesting medications based on user-input symptoms.

By integrating a user-friendly interface with efficient backend technologies, MediQuick simplifies access to healthcare information and empowers users to make informed decisions.

---

## Core Features

### 1. Symptom Analysis
- Users input their symptoms through the intuitive interface.
- The system analyzes the input and maps the symptoms to potential diseases using a pre-defined database.

### 2. Medication Recommendations
- Based on the identified diseases, the system suggests appropriate medications.
- Includes optional disclaimers and guidance to consult healthcare professionals for accurate diagnosis and treatment.

### 3. User-Friendly Interface
- Clean and intuitive layout with clear navigation.
- Interactive features for smooth symptom input and medication output.

---

## Technologies Used

### **Backend**
- **Flask**
  - Manages routing, backend logic, and RESTful API setup.
  - Facilitates communication between the user interface and backend logic.

### **Frontend**
- **HTML/CSS**
  - Builds the structure and styling of the web pages.
  - Ensures responsiveness across mobile and desktop devices.
- **JavaScript**
  - Adds interactivity, including:
    - Symptom auto-suggestions.
    - Dynamic updates.
    - Seamless API calls.

### **Data Handling**
- **JSON**
  - Lightweight data format for transferring information between client and server, ensuring efficient data exchange.
- **Data Structures (Dictionaries)**
  - Maps symptoms to diseases and medications efficiently for quick lookups.

### **Utilities**
- **Random Module**
  - Introduces variability, such as:
    - Randomized educational tips.
    - Alternative medication suggestions.

---

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/meabhib/MediQuick.git
   cd MediQuick
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

---

## Folder Structure

```
MediQuick/
|
├── app.py               # Main Flask application
├── templates/           # HTML templates
├── static/
│   ├── css/             # CSS files
│   ├── js/              # JavaScript files
│   └── images/          # Static assets
├── data/
│   └── symptoms.json    # Symptom-disease-medication mapping
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

---

## Contribution

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to your fork and submit a pull request.

---

## Disclaimer

MediQuick is designed for informational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for any medical concerns.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

We extend our gratitude to the contributors and users who have supported MediQuick’s development and helped improve healthcare accessibility.
