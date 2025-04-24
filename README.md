# 📘 SQL SRS — Spaced Repetition System for SQL Practice

Welcome to **SQL SRS**, an interactive web application designed to help you master SQL using the power of **spaced repetition**. Built with Streamlit and DuckDB, this tool lets you practice various SQL concepts like joins, window functions, groupings, and more — all through a structured review system that adapts to your learning.

---

## 🚀 Features

- 📚 **Spaced Repetition System**: Practice SQL exercises based on your review history.
- 🧠 **Concept Coverage**: Exercises on joins, CTEs, window functions, `GROUP BY`, and more.
- 🧪 **Query Validator**: Submit SQL queries and get real-time feedback compared to the correct solution.
- 📊 **Live Table Views**: See the relevant tables and expected solutions.
- 🛏️ **Intuitive UI**: Powered by Streamlit for a clean and interactive interface.

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/sql-srs.git
cd sql-srs
```

### 2. Set up a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```bash
sql-srs/
├── app.py                     # Main Streamlit app
├── init_db.py                 # Script to initialize the DuckDB database
├── init_db_case_when.py       # Modular DB creation scripts...
├── init_db_cross_join.py
├── ...                        # etc.
├── data/
│   └── exercises_sql_tables.duckdb  # DuckDB database file
├── questions/
│   └── <exercise>.txt         # Text descriptions for each SQL exercise
├── answers/
│   └── <exercise>.sql         # SQL solution for each exercise
├── logo/
│   └── SQL_SRS_logo.png       # App logo
├── requirements.txt           # Python dependencies
```

---

## 🧹 Usage

1. Launch the app in your browser using `streamlit run app.py`.
2. Choose a topic from the sidebar.
3. Read the exercise prompt.
4. Write your SQL in the provided editor and hit **Submit**.
5. Get instant feedback — balloons if you nailed it! 🎈
6. Use the buttons to schedule your next review (e.g., in 2, 7, or 21 days).

---

## 🔍 Example SQL Topics

- `INNER JOIN`, `LEFT JOIN`, `FULL OUTER JOIN`, `SELF JOIN`
- `GROUP BY`, `HAVING`, `CTE`
- `CASE WHEN`, `WINDOW FUNCTIONS`
- `GROUPING SETS`, `ROLLUP`, `CUBE`

---

## ⚙️ Configuration

The database is initialized automatically via `init_db.py`, which acts as a wrapper to execute individual setup scripts for each SQL topic:

```bash
python init_db.py
```

Each topic has its own file under the hood:

```bash
init_db_case_when.py
init_db_cross_join.py
init_db_full_outer_join.py
init_db_group_by.py
init_db_grouping_sets.py
init_db_inner_join.py
init_db_left_join.py
init_db_self_join.py
init_db_window_function.py
```

This modular design allows easy editing or expansion of the exercises per topic.

---

## 🧪 Development Notes

- Python 3.9+
- Streamlit app uses `duckdb` for local SQL execution
- Exercises are modular — just add a `.txt` and a `.sql` to include a new one
- Exercises and user progress are stored in `data/exercises_sql_tables.duckdb`

---

## 💡 Contributing

Contributions are welcome! Feel free to open issues or pull requests if you want to add new exercises, fix bugs, or improve functionality.

---


