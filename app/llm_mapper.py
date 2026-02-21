import json
from groq import Groq
from app.registry import PARAMETER_REGISTRY, ASSET_REGISTRY
from app.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def map_columns_with_llm(columns):

    prompt = f"""
You are an industrial data mapping AI agent.

Map Excel column headers to canonical parameter names and asset names.

Return ONLY valid JSON array. No explanation.

CRITICAL RULE:
You MUST return a mapping entry for EVERY column provided.
Do NOT skip any column.

Columns:
{columns}

Parameter Registry:
{PARAMETER_REGISTRY}

Asset Registry:
{ASSET_REGISTRY}

Return format:
[
  {{
    "column": "column_name",
    "param_name": "canonical_name_or_null",
    "asset_name": "asset_or_null",
    "confidence": "high|medium|low"
  }}
]
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",   # Fast & powerful
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    content = response.choices[0].message.content.strip()

    # Remove markdown if present
    if content.startswith("```"):
        content = content.split("```")[1]

    return json.loads(content)