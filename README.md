Excel Agent

AI-powered Excel parsing backend that converts messy spreadsheet data into clean, validated, structured JSON using LLM-based column mapping.

🔗 Live API Docs:
https://excel-agent-s1ca.onrender.com/docs

📌 Overview

Excel Agent is a FastAPI-based backend service that:

📄 Accepts Excel file uploads

🧠 Uses an LLM to intelligently map column headers

🔎 Detects headers automatically (even with title rows)

🔢 Parses messy numeric formats (%, commas, mixed text)

⚠ Validates suspicious values

🔁 Detects duplicate parameter mappings

📦 Returns structured, production-ready JSON

It is built to handle both clean and messy industrial reports.

✨ Features
1️⃣ Smart Header Detection

Scans first 10 rows

Skips title rows

Detects first valid header row automatically

2️⃣ LLM-Based Column Mapping

Maps messy headers like:

Excel Header	Mapped Parameter
Coal Used	coal_consumption
Steam Gen (T/hr)	steam_generation
Boiler Eff %	efficiency

Each mapping includes:

param_name

asset_name

confidence

3️⃣ Value Parsing

Handles:

1,000 → 1000

85% → 0.85

Empty cells

Mixed numeric formats

4️⃣ Validation Rules

Flags suspicious values:

❌ Coal consumption < 0

❌ Steam generation < 0

❌ Efficiency outside 0–100%

Example output:

{
  "row": 7,
  "parameter": "coal_consumption",
  "issue": "negative_value",
  "message": "Coal consumption cannot be negative"
}
5️⃣ Duplicate Detection

Detects duplicate parameter + asset combinations across columns.

{
  "param_name": "coal_consumption",
  "asset_name": "AFBC-1",
  "column": "Coal Used Copy",
  "reason": "Duplicate parameter+asset combination detected"
}
6️⃣ Unmapped Column Detection

If LLM cannot map a column:

{
  "col": 5,
  "header": "Comments",
  "reason": "No matching parameter found"
}
🛠 API Endpoint
POST /parse

Upload Excel file using multipart/form-data.

Response Format
{
  "status": "success",
  "header_row": 2,
  "parsed_data": [...],
  "unmapped_columns": [...],
  "warnings": [...],
  "validation_issues": [...],
  "duplicates": [...]
}
🏗 Project Structure
excel-agent/
│
├── app/
│   ├── main.py
│   ├── parser.py
│   ├── llm_mapper.py
│   ├── value_parser.py
│   ├── models.py
│   └── __init__.py
│
├── requirements.txt
└── README.md
⚙ Tech Stack

FastAPI

Uvicorn

OpenPyXL

Groq LLM API

Pydantic

🚀 Deployment

Hosted on Render

Start command:

uvicorn app.main:app --host 0.0.0.0 --port 10000
