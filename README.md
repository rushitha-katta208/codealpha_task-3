# 📈 Stock Portfolio Tracker

A simple and customizable *Stock Portfolio Tracker* built with Python. This tool helps users track their stock investments, current market value, and overall performance using real-time or historical data.

## 🚀 Features

- Add and manage your stock portfolio
- Fetch real-time stock prices using external APIs (e.g., Yahoo Finance or Alpha Vantage)
- Calculate profit/loss, average cost, and total investment
- Visualize portfolio performance using matplotlib or Plotly
- Export reports to CSV

## 🛠 Tech Stack

- *Python 3.8+*
- *pandas* for data management
- *yfinance* or *Alpha Vantage API* for fetching stock data
- *matplotlib / Plotly* for visualization (optional)
- *SQLite / CSV* for data storage (optional)

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/rushitha-katta208/stock-portfolio-tracker.git
cd stock-portfolio-tracker

2. Create a virtual environment and activate it:



python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:



pip install -r requirements.txt

📝 Usage

Update your portfolio file (e.g., portfolio.csv) with your stock symbols, quantities, and purchase prices.

Example format:

Symbol	Shares	Purchase Price

AAPL	10	150.00
TSLA	5	700.00


Run the tracker:

python tracker.py

This will display current portfolio value, gain/loss, and optional charts.

📊 Sample Output

-----------------------------------------------------
| SYMBOL | SHARES | COST BASIS | CURRENT | P/L (%) |
-----------------------------------------------------
| AAPL   | 10     | $1,500.00  | $1,750  | +16.67% |
| TSLA   | 5      | $3,500.00  | $4,200  | +20.00% |
-----------------------------------------------------
| TOTAL  |        | $5,000.00  | $5,950  | +19.00% |
-----------------------------------------------------

🖼 Charts (Optional)

If enabled, the script can generate:

Portfolio distribution pie chart

Performance over time line chart


✅ To-Do

[ ] Add GUI with Tkinter or Streamlit

[ ] Add support for dividends and splits

[ ] Implement multi-currency support

[ ] Add alerts or notifications


🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

📜 License

This project is licensed under the MIT License.


---

Happy tracking! 📉📈

---

Let me know if you'd like this customized for a *web app, **GUI version*, or if you want the actual Python code scaffold too.
