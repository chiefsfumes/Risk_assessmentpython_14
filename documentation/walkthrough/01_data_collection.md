# Step 1: Data Collection and Preprocessing

In this initial step, we collect and preprocess the data necessary for our climate risk assessment. Let's follow the journey of a single risk statement through this process.

## 1.1 Loading Risk Data

Our risk statement is initially stored in a CSV file (`data/risk_data.csv`). The `load_risk_data` function in `src/data_loader.py` reads this file and creates a `Risk` object for each entry.

Example risk statement:
```
id: 1
description: "Increased frequency of extreme weather events"
category: "Physical Risk"
likelihood: 0.8
impact: 0.9
```

This risk is loaded into our system as a `Risk` object with attributes corresponding to each field in the CSV.

## 1.2 Loading External Data

Simultaneously, we load external data (e.g., GDP growth, population, energy demand) from `data/external_data.csv` using the `load_external_data` function. This data provides context for our risk assessment.

## 1.3 Extracting Risk Statements from 10-K Filings

While our example risk is already in our system, we also use NLP techniques to extract additional risk statements from 10-K filings. The `extract_risk_statements_from_10k` function in `src/data_collection/nlp_extraction.py` processes these documents and identifies potential climate-related risks.

For instance, if our 10-K filing contained the sentence:
"The company faces potential disruptions due to increased frequency of extreme weather events."

Our NLP model would identify this as a relevant risk statement, extract it, and create a new `Risk` object to be included in our analysis.

At the end of this step, our risk statement is now a `Risk` object in our system, ready for categorization and further analysis.