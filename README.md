# Electronic Gadget Sales Dashboard

A modern, interactive sales analytics dashboard built with Streamlit and Plotly. This project enables data-driven insights into electronic gadget sales, empowering business leaders and analysts to make informed decisions with ease.

## 🚀 Features
- **Dynamic Filtering:** Instantly filter sales data by city, sales person, and product using an intuitive sidebar.
- **Interactive Visualizations:** Explore monthly and weekly sales trends, product performance, and city-level revenue with beautiful Plotly charts.
- **Key Performance Indicators (KPIs):** Real-time metrics for total products, cities, quantity ordered, and revenue.
- **Data Cleaning & Preprocessing:** Robust pipeline ensures accurate, reliable analytics from raw CSV files.
- **Expandable Raw Data View:** Inspect the underlying data directly in the dashboard.

## 📊 Dashboard Preview
![Dashboard Screenshot](dashboard_screenshot.png)

## 🏗️ Project Structure
```
├── dashboard.py              # Streamlit dashboard app
├── Sales_*.csv               # Monthly sales data files
├── report.ipynb              # Data exploration and analysis notebook
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## ⚡ Getting Started
1. **Clone the repository:**
   ```bash
   git clone https://github.com/MrBhumzie/electronic-gadget-sales-dashboard.git
   cd electronic-gadget-sales-dashboard
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Add your sales CSV files:**
   Place your `Sales_*.csv` files in the project root directory.
4. **Run the dashboard:**
   ```bash
   streamlit run dashboard.py
   ```

## 🧑‍💻 Technologies Used
- [Streamlit](https://streamlit.io/) for rapid dashboard development
- [Plotly](https://plotly.com/python/) for interactive charts
- [Pandas](https://pandas.pydata.org/) & [NumPy](https://numpy.org/) for data manipulation

## 💡 Why This Project Stands Out
- **Production-Ready:** Clean, modular code with robust error handling and data validation.
- **User-Centric Design:** Focused on usability, clarity, and actionable insights.
- **Scalable:** Easily extendable for new KPIs, charts, or data sources.
- **Impressive Visuals:** Modern, publication-quality charts and responsive layout.

## 📬 Contact
For questions, suggestions, or collaboration, please reach out via [LinkedIn](https://www.linkedin.com/) or open an issue.

---

> "Data is the new oil. This dashboard helps you refine it."
