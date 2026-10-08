# 📊 311 Service Request Dashboard

An interactive Streamlit web application for analyzing municipal 311 service request data submitted between January and June 2025.

---

## 📌 Project Overview

This project uses real-world 311 service request data to explore patterns in requests for city services.

The project began with a large dataset that required data preparation before it could be used in an interactive application. Using Python and Pandas, I cleaned and reduced the original dataset, selected the attributes needed for analysis, created useful date variables, and prepared a smaller dataset containing 2025 service requests.

I then performed exploratory data analysis (EDA) to identify important patterns and trends in the data. Based on this analysis, I selected information and visualizations that would be useful in an interactive dashboard.

---

## 🌐 Live Dashboard

**Streamlit Application:**

👉 [2025 311 Service Requests Dashboard](https://data-visualization-app-npc2qrxf5wgrhyonlswtpu.streamlit.app/)

---

## 🚀 Interactive Dashboard

I developed an interactive web application using Streamlit. The dashboard allows users to:

* **Select a start and end date** within the available 2025 data.
* **Filter the data interactively** by responsible agency and request status.
* **View summary metrics**, including total requests, unique service types, percentage of closed requests, and average resolution time.
* **Explore service request categories and trends** through interactive visualizations.
* **View charts and visualizations** based on the selected data.
* **Explore available geographic information**, including latitude and longitude data.

### Visualizations

The dashboard includes visualizations such as:

1. Top responsible agencies by request volume.
2. Average resolution time (days) for top service types.
3. Daily service request volume over time.

The dashboard updates automatically whenever the user changes the selected options.

---

## 🔄 Project Workflow

The project followed an end-to-end data application workflow:

**Raw Data → Data Preparation → Exploratory Data Analysis → Visualization → Streamlit Application → GitHub → Cloud Deployment**

This project demonstrates how Python analysis can be transformed from a Jupyter Notebook into an interactive application that can be used by others.

---

## 📁 Repository Structure

```text
Data-Visualization-App/
├── app.py
├── 311_2025_dashboard.csv
├── requirements.txt
├── README.md
├── Notebook_1_Prepare_2025_311_Dashboard_Data.ipynb
└── Notebook_2_Prototype_311_Dashboard_(1).ipynb
```

* `app.py` — Streamlit application script
* `311_2025_dashboard.csv` — Reduced 2025 dataset used by the dashboard
* `requirements.txt` — Python package dependencies
* `README.md` — Project documentation
* `Notebook_1_Prepare_2025_311_Dashboard_Data.ipynb` — Data preparation and cleaning
* `Notebook_2_Prototype_311_Dashboard_(1).ipynb` — Exploratory data analysis and visualization prototyping

**Note:** The original large dataset is intentionally excluded from this repository because of its size. Only the reduced 2025 dataset required by the dashboard is included.

---

## 🛠️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/aryalankit121/Data-Visualization-App.git
cd Data-Visualization-App
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
streamlit run app.py
```

---

## 💻 Technologies Used

* Python
* Pandas
* Matplotlib
* Jupyter Notebook / Google Colab
* Streamlit
* GitHub
* Streamlit Community Cloud

---

## 🌟 Skills Demonstrated

This project demonstrates experience with:

* Data cleaning and preparation
* Exploratory data analysis (EDA)
* Python programming
* Data visualization
* Interactive application development
* Streamlit
* GitHub and version control
* Cloud application deployment
