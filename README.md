# 🧵 Textile Demand Prediction & Smart Restocking with Machine Learning

This project predicts **which fabrics will sell in the next 3 months** and tells you **which ones to restock first**.  
It’s like having a smart inventory assistant that looks at your past sales and says:  
> “Hey, this fabric is running low and will sell out soon — better restock it now!”  

Built with:
- **XGBoost** for super-accurate demand prediction
- **Streamlit** for an easy-to-use, interactive dashboard

---

## ✨ What This Project Does
- **Predicts upcoming sales** for each fabric/material based on history  
- **Labels stock** as:
  - 🛑 **Urgent** (stock < 20)
  - ⚠ **Soon** (stock 20–40)
  - ✅ **OK** (stock > 40)
- Shows **beautiful graphs & tables** so you can see exactly what’s happening
- Helps **avoid stockouts** and **reduce overstock waste**
- Works even if you’re **not a tech person** — the dashboard does the heavy lifting

---

## 🎯 Why We Built It
Running a textile business means guessing demand — and guessing wrong costs money.  
Too little stock = **lost sales**.  
Too much stock = **money stuck in shelves**.  

This tool turns sales data into **clear, actionable insights** so you can:
- Order the right products at the right time
- Save money and storage space
- Keep customers happy

---

## 🛠 How It Works
1. **We feed in your sales history** (month, year, fabric type, supplier, stock, etc.)
2. **The ML model predicts** the next 3 months of sales
3. **We tag each item** as Urgent, Soon, or OK
4. **You view it all** on the Streamlit dashboard

---

 Tech Behind the Scenes
Python for the whole project

pandas, numpy for data wrangling

XGBoost for prediction

matplotlib, seaborn for charts

Streamlit for the dashboard

---

🚀 How to Run the Project
This project consists of two key components:

Data Processing & Forecast Generation – Performed in finalinternproject.ipynb

Interactive Visualization Dashboard – Implemented in app.py using Streamlit

Step 1 – Generate Forecast Outputs
Run the Jupyter Notebook finalinternproject.ipynb in Jupyter, VS Code, or any compatible environment.
Executing all cells will produce the following output files required by the Streamlit application:

Images (.png) – Visualization charts (e.g., cell2_total_sales_year.png, cell11_forecast_xgboost.png)

Excel Files (.xlsx) – Forecast tables and recommendations (e.g., forecast_materials.xlsx, top5_items_by_period.xlsx)

These files are automatically saved to the project directory.

Step 2 – Launch the Streamlit Dashboard
Once the notebook has been executed and the output files have been generated:

Open a terminal in the project directory.

Run the following command:

bash
Copy
Edit
streamlit run app.py
The dashboard will launch in your default web browser, displaying:

Historical sales trends

Predicted demand for the next three months

Restocking priority recommendations

Note: Running app.py without first executing the notebook will result in missing file errors, as the necessary PNG and Excel outputs will not exist.
