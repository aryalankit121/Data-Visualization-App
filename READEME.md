# 📊 2025 311 Service Requests Dashboard

An interactive Streamlit web application for analyzing municipal 311 service request data submitted between January and June 2025.

## 🚀 Key Features

* **Date Range Filtering:** Dynamically select a start and end date within the available 2025 data.
* **Multi-Select Filters:** Filter requests by responsible agency and request status.
* **Summary Metrics:** View total requests, unique service types, percentage of closed requests, and average resolution time.
* **Visualizations:**

  * Top responsible agencies by request volume.
  * Average resolution time for the top service types.
  * Daily request volume over time.

## 📁 Repository Structure

```text
Data-Visualization-App/
├── app.py
├── 311_2025_dashboard.csv
├── requirements.txt
├── README.md
├── Notebook_1.ipynb
└── Notebook_2.ipynb
```

* `app.py` — Streamlit dashboard application.
* `311_2025_dashboard.csv` — Reduced 2025 dataset used by the dashboard.
* `requirements.txt` — Python packages required to run the application.
* `README.md` — Project documentation.
* `Notebook_1_Prepare_2025_311_Dashboard_Data.ipynb` — Data preparation and analysis.
* `Notebook_2_Prototype_311_Dashboard_(1).ipynb` — Analysis and visualizations used to develop the dashboard.

## 📊 Dataset

The dashboard uses a reduced 2025 311 service request dataset created for this project.

The original large dataset is **not** included in this repository. Only the reduced dataset used by the dashboard is included.

## 🛠️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/aryalankit121/Data-Visualization-App.git
cd Data-Visualization-App
```

### 2. Install the required packages

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
streamlit run app.py
```

The dashboard will open in your web browser.
