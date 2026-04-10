# 🚀 AI-Powered Predictive Maintenance for IoT Devices

---

## 📌 Overview

This project focuses on **Predictive Maintenance (PdM)** for industrial equipment.
By using **Machine Learning algorithms** and simulated IoT sensor data (Temperature, Vibration, and Current), the system predicts machine failure **before breakdown occurs**.

---

## ❗ Problem Statement

Unscheduled downtime in industries leads to:

* High production losses
* Expensive repairs

Traditional maintenance methods:

* **Reactive** → Fix after failure (costly)
* **Preventative** → Fix on schedule (wasteful)

✅ This project implements **Predictive Maintenance**, which uses data to fix machines only when failure is likely.

---

## 🏭 Industry Relevance

This technology is a core part of **Industry 4.0** and is used by:

* **Siemens & GE** → Monitoring turbines & power plants
* **Tesla** → Automated manufacturing diagnostics
* **Aviation Industry** → Engine health monitoring

---

## 🛠 Tech Stack

* **Language:** Python
* **Libraries:**

  * Pandas & NumPy → Data handling
  * Scikit-learn → Machine Learning
  * Matplotlib & Seaborn → Visualization

---

## 📊 Dataset

Simulated IoT sensor dataset:

* **Temperature (°C)** → Thermal condition
* **Vibration (mm/s)** → Mechanical stability
* **Current (A)** → Electrical load
* **Target:**

  * `0` = Healthy
  * `1` = Failure

---

## 🏗 Architecture

1. Data Acquisition → Simulated sensor data
2. Preprocessing → Cleaning & scaling
3. Model Training → Random Forest & Logistic Regression
4. Prediction → Failure detection
5. Visualization → Confusion Matrix

---

## ⚙ Installation

```bash
git clone https://github.com/your-username/predictive-maintenance-iot.git
cd predictive-maintenance-iot
pip install -r requirements.txt
```

---

# 🧑‍💻 HOW TO RUN THIS PROJECT (FOR BEGINNERS)

## 🔹 STEP 1: Create Folder

1. Go to Desktop
2. Right click → New → Folder
3. Name it: `AI_Project`

---

## 🔹 STEP 2: Add Project Files

* Copy all project files (`main.py`, `requirements.txt`, etc.)
* Paste them inside the folder

---

## 🔹 STEP 3: Open Command Prompt

1. Open the folder
2. Click address bar
3. Type:

```
cmd
```

4. Press Enter

---

## 🔹 STEP 4: Create Virtual Environment

```
python -m venv venv
```

---

## 🔹 STEP 5: Activate Virtual Environment

```
venv\Scripts\activate
```

👉 You should see `(venv)` in terminal

---

## 🔹 STEP 6: Install Dependencies

```
pip install -r requirements.txt
```

---

## 🔹 STEP 7: Run Project

```
python main.py
```

---

## 📊 Output

* Text output → shown in terminal
* Graphs → open in new window 📈
* Files → saved in project folder

---

## 🚀 Usage

Run:

```bash
python main.py
```

---

## 📈 Results

* **Accuracy:** 100% (on simulated dataset)
* **Confusion Matrix:**

  * True Positives → Correct failure prediction
  * True Negatives → Correct healthy prediction

---

## 📸 Screenshots

### 1. Confusion Matrix

![Confusion Matrix](images/Figure_1.png)

### 2. Terminal Output

![Model Output](images/figure2.png)

### 3. Project Structure

![Folder Structure](images/figure3.png)

---

## 📦 Requirements

Create a file `requirements.txt`:

```
pandas
numpy
scikit-learn
matplotlib
seaborn
```

---

## ❗ Troubleshooting

### Python not recognized

Install Python and enable **“Add to PATH”**

### pip not working

```
python -m pip install --upgrade pip
```

### Module not found

```
pip install -r requirements.txt
```

---

## 💡 Learning Outcomes

* Integration of **IoT Sensors + AI**
* Understanding **Predictive Maintenance systems**
* Using **Random Forest for classification**
* Evaluating model using **Confusion Matrix**
* Applying **Low-Cost Automation concepts**

---

## 👨‍💻 Author

**Atharv Vishnudas Bunde**
Diploma in Mechatronics Engineering
DBATU

---

## 🎯 Conclusion

This project demonstrates how **AI + IoT** can reduce downtime and improve industrial efficiency.

🚀 Future Scope:

* Real-time IoT integration
* Mobile dashboard
* Edge AI deployment
