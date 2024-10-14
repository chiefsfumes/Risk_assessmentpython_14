# Step 2: Risk Categorization and Prioritization

After collecting our risk data, we move on to categorizing and prioritizing the risks. Let's continue following our example risk statement through this process.

## 2.1 Risk Categorization

Our risk statement "Increased frequency of extreme weather events" is already categorized as a "Physical Risk" in our data. However, the `categorize_risks` function in `src/risk_analysis/categorization.py` performs a multi-level categorization:

```python
categorized_risk = {
    "Physical Risk": {
        "Acute": [our_risk]
    }
}
```

This categorization helps in organizing and analyzing risks more effectively.

## 2.2 Risk Prioritization

Next, the `prioritize_risks` function assesses the likelihood and impact of each risk to assign a priority level. For our risk:

```python
likelihood = 0.8
impact = 0.9
```

Given these high values, our risk would likely be categorized as "High" priority:

```python
prioritized_risks = {
    "High": [our_risk],
    "Medium": [...],
    "Low": [...]
}
```

## 2.3 SASB Materiality Integration

The `integrate_sasb_materiality` function in `src/risk_analysis/sasb_integration.py` checks if our risk is material according to SASB standards for the company's industry. As an extreme weather event risk, it's likely to be considered material for most industries.

## 2.4 PESTEL Analysis

Finally, the `perform_pestel_analysis` function in `src/risk_analysis/pestel_analysis.py` categorizes our risk within the PESTEL framework. Our risk would be categorized under "Environmental":

```python
pestel_categories = {
    "Political": [...],
    "Economic": [...],
    "Social": [...],
    "Technological": [...],
    "Environmental": [our_risk],
    "Legal": [...]
}
```

At the end of this step, our risk has been thoroughly categorized and prioritized, providing a clear context for further analysis.