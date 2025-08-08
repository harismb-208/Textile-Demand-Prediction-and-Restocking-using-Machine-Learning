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

## 🚀 How to Run

### 1️⃣ Run Locally
```bash
# Clone the repo
git clone https://github.com/YourUsername/Textile-Demand-Prediction.git
cd Textile-Demand-Prediction

# Install dependencies
pip install -r requirements.txt

# Start dashboard
streamlit run app.py
