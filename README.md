🚀 AI-Powered Predictive Maintenance for IoT Devices

📌 Overview
This project focuses on Predictive Maintenance (PdM) for industrial equipment. By utilizing Machine Learning algorithms and simulated IoT sensor data (Temperature, Vibration, and Current), the system can predict whether a machine is likely to fail before the breakdown actually occurs.

❗ Problem Statement
Unscheduled downtime in industries leads to massive production losses and high repair costs. Traditional maintenance is either:
*Reactive: Fix it when it breaks (expensive and disruptive).
Preventative: Fix it on a schedule (can be wasteful if parts are still good).

This project implements Predictive Maintenance, which uses data to fix machines only when a failure is imminent.

🏭 Industry Relevance
This technology is a core pillar of Industry 4.0 and is used by global leaders such as:
Siemens & GE:For monitoring gas turbines and power plants.
*Tesla: For predictive diagnostics in automated manufacturing lines.
*Aviation: To monitor engine health and prevent mid-flight issues.

🛠 Tech Stack
Language: Python
Libraries:`Pandas` & `NumPy` (Data Manipulation)
    `Scikit-learn` (Machine Learning: Random Forest, Logistic Regression)
    `Matplotlib` & `Seaborn` (Data Visualization)

📊 Dataset
The project uses a simulated dataset representing typical IoT sensor readings from a manufacturing cell:
Features: `Temperature (°C)`: Thermal state of the motor.
    `Vibration (mm/s)`: Mechanical stability.
    `Current (A)`: Electrical load and health.
Target:** `Failure` (0 = Healthy, 1 = Fail).

🏗 Architecture
The workflow follows a standard data science pipeline integrated with Mechatronics principles:

1.  Data Acquisition: Simulated sensor streams.
2.  Preprocessing: Normalization and feature scaling.
3.  Model Training: Training Random Forest and Logistic Regression.
4.  Inference:Predicting failure state based on real-time inputs.
5.  Visualization: Confusion Matrix to evaluate performance.

⚙ Installation
1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/predictive-maintenance-iot.git
    ```
2.  Navigate to the folder:
    ```bash
    cd predictive-maintenance-iot
    
3.  Install dependencies:
    ```bash
    pip install pandas numpy scikit-learn matplotlib seaborn
    ```
# 🚀 AI Project – Beginner Friendly Guide

## 📌 Project Overview

This project uses Python and machine learning libraries to process data and generate results/graphs.

---

🧑‍💻 HOW TO RUN THIS PROJECT (STEP-BY-STEP FOR BEGINNERS)
 🔹 STEP 1: Create a Project Folder

1. Go to your Desktop
2. Right click → Click **New → Folder**
3. Name it: `AI_Project` (or anything you like)

---

🔹 STEP 2: Download / Copy Project Files

* Copy all project files (`main.py`, `requirements.txt`, etc.)
* Paste them inside your folder

---

🔹 STEP 3: Open Command Prompt in this Folder

1. Open your project folder
2. Click on the **address bar (top where path is shown)**
3. Type:

   ```
   cmd
   ```
4. Press **Enter**

👉 A black window (Command Prompt) will open
👉 It will already be inside your project folder ✅

---

🔹 STEP 4: Create Virtual Environment

In Command Prompt, type:

```
python -m venv venv
```

👉 This creates a folder named `venv`

---

🔹 STEP 5: Activate Virtual Environment

Type this command:

```
venv\Scripts\activate
```

👉 If successful, you will see:

```
(venv) C:\...
```

---

🔹 STEP 6: Install Required Libraries

Type:

```
pip install -r requirements.txt
```

👉 This installs all required packages automatically

---

🔹 STEP 7: Run the Project

Type:

```
python main.py
```

---

📊 OUTPUT

* If program prints something → it will show in Command Prompt
* If graphs are used → a graph window will open 📈
* If files are generated → check project folder

---

❗ TROUBLESHOOTING

🔸 Python not recognized

* Install Python from official website
* During install, tick **“Add Python to PATH”**

---

🔸 pip not working

Run:

```
python -m pip install --upgrade pip
```

---

🔸 Module not found error

Run again:

```
pip install -r requirements.txt
```

---

📦 REQUIREMENTS

Make sure you have:

Python installed (version 3.x)

---
 🧠 SIMPLE SUMMARY

1. Open folder
2. Type `cmd`
3. Create venv
4. Activate venv
5. Install requirements
6. Run project

---
🎯 Done!

Now your project should run successfully 🚀
🚀 Usage
Run the main script to train the model and see the prediction results:
```bash
python main.py
```

📈 Results
Accuracy:Achieved 100% accuracy on the simulated dataset.
Confusion Matrix:True Positives: Successfully identified all failure states.
    True Negatives:Corrected identified all healthy states.
    *(See screenshot below for the visualization)*

📸 Screenshots
 1. Confusion Matrix
This chart shows that the model correctly predicted every single failure and healthy state.
![Confusion Matrix](images/Figure_1.png)

2. Terminal Output
This screenshot confirms the training process and the final accuracy score.
![Model Training Output](images/figure2.png)

3. Project Structure
A look at the professional organization of the repository.
![Folder Structure](images/images/figure3.png)

## 💡 Learning Outcomes
* Understood the integration of **Mechatronics sensors** with **Artificial Intelligence**.
* Mastered the use of **Random Forest** for binary classification tasks.
* Evaluated model performance using **Confusion Matrices** and accuracy scores.
* Applied **Low-Cost Automation (LCA)** logic to software-based predictive systems.

---

Author
Atharv Vishnudas Bunde | ss Mechatronics Engineering Student | DBATU*
