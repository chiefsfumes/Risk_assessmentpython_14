# Climate Risk Assessment Prompts

from src.config import COMPANY_INFO

RISK_ASSESSMENT_PROMPT = """
<instruction>
As an expert in climate risk assessment for the {industry} sector, analyze the following risk statement for {company_name}:

<company_context>
Company: {company_name}
Industry: {industry}
Region: {company_region}
Key Products: {key_products}
</company_context>

<risk>
<description>{risk_description}</description>
<category>{risk_category}</category>
<subcategory>{risk_subcategory}</subcategory>
<current_likelihood>{risk_likelihood}</current_likelihood>
<current_impact>{risk_impact}</current_impact>
<time_horizon>{risk_time_horizon}</time_horizon>
</risk>

<scenario>
<name>{scenario_name}</name>
<temperature_increase>{temp_increase}</temperature_increase>
<carbon_price>{carbon_price}</carbon_price>
<renewable_energy>{renewable_energy}</renewable_energy>
<policy_stringency>{policy_stringency}</policy_stringency>
<biodiversity_loss>{biodiversity_loss}</biodiversity_loss>
<ecosystem_degradation>{ecosystem_degradation}</ecosystem_degradation>
<financial_stability>{financial_stability}</financial_stability>
<supply_chain_disruption>{supply_chain_disruption}</supply_chain_disruption>
</scenario>

Provide a detailed analysis addressing the following points:
1. How does this risk's likelihood and impact change under the given scenario, considering {company_name}'s specific context?
2. What are the potential financial implications for {company_name} over the next 5 years?
3. Are there any emerging opportunities related to this risk in this scenario, particularly for {company_name}'s products or services?
4. What additional challenges might arise from this risk in this specific context, considering {company_name}'s supply chain and operations?
5. Suggest 2-3 possible mitigation strategies tailored to this scenario and {company_name}'s sustainability goals.

Please structure your response in JSON format as follows:
</instruction>

<output_format>
{{
  "likelihood_impact_change": {{
    "likelihood_change": "string (choose one: ['Significant Decrease', 'Moderate Decrease', 'Slight Decrease', 'No Change', 'Slight Increase', 'Moderate Increase', 'Significant Increase'])",
    "impact_change": "string (choose one: ['Significant Decrease', 'Moderate Decrease', 'Slight Decrease', 'No Change', 'Slight Increase', 'Moderate Increase', 'Significant Increase'])",
    "explanation": "string"
  }},
  "financial_implications": {{
    "short_term": "string (choose one: ['Highly Negative', 'Moderately Negative', 'Slightly Negative', 'Neutral', 'Slightly Positive', 'Moderately Positive', 'Highly Positive'])",
    "medium_term": "string (choose one: ['Highly Negative', 'Moderately Negative', 'Slightly Negative', 'Neutral', 'Slightly Positive', 'Moderately Positive', 'Highly Positive'])",
    "long_term": "string (choose one: ['Highly Negative', 'Moderately Negative', 'Slightly Negative', 'Neutral', 'Slightly Positive', 'Moderately Positive', 'Highly Positive'])"
  }},
  "emerging_opportunities": [
    {{
      "opportunity": "string",
      "description": "string",
      "potential": "string (choose one: ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])"
    }}
  ],
  "additional_challenges": [
    {{
      "challenge": "string",
      "description": "string",
      "severity": "string (choose one: ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])"
    }}
  ],
  "mitigation_strategies": [
    {{
      "strategy": "string",
      "description": "string",
      "potential_impact": "string (choose one: ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])",
      "feasibility": "string (choose one: ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])"
    }}
  ]
}}
</output_format>
"""

RISK_NARRATIVE_PROMPT = """
<instruction>
As an expert in climate risk assessment, create a concise narrative summary for the following risk across different scenarios, specifically for {company_name}. Focus on key trends, variations in impact and likelihood, and overarching mitigation strategies.

<company_context>
Company: {company_name}
Industry: {industry}
Region: {company_region}
Key Products: {key_products}
</company_context>

<risk>
<description>{risk_description}</description>
<category>{risk_category}</category>
<subcategory>{risk_subcategory}</subcategory>
<current_likelihood>{risk_likelihood}</current_likelihood>
<current_impact>{risk_impact}</current_impact>
<time_horizon>{risk_time_horizon}</time_horizon>
</risk>

<scenario_analyses>
{scenario_analyses}
</scenario_analyses>

Provide a concise narrative summary (about 200 words) that synthesizes the insights from all scenarios, highlighting key trends and strategic implications for {company_name}. Structure your response in JSON format as follows:
</instruction>

<output_format>
{{
  "narrative_summary": "string",
  "key_trends": [
    {{
      "trend": "string",
      "description": "string",
      "significance": "string (choose one: ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])"
    }}
  ],
  "strategic_implications": [
    {{
      "implication": "string",
      "description": "string",
      "impact": "string (choose one: ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])"
    }}
  ],
  "overarching_mitigation_strategies": [
    {{
      "strategy": "string",
      "description": "string",
      "effectiveness": "string (choose one: ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])",
      "feasibility": "string (choose one: ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])"
    }}
  ]
}}
</output_format>
"""

EXECUTIVE_INSIGHTS_PROMPT = """
<instruction>
As a senior climate risk analyst, review the following comprehensive risk analyses across multiple scenarios for {company_name}. Provide high-level executive insights focusing on:

<company_context>
Company: {company_name}
Industry: {industry}
Region: {company_region}
Key Products: {key_products}
</company_context>

1. Key overarching trends across scenarios specific to {company_name}'s context
2. Most critical risks requiring immediate attention for {company_name}
3. Potential strategic opportunities arising from climate change for {company_name}'s products/services
4. Recommendations for enhancing {company_name}'s overall climate resilience

<analyses>
{all_analyses}
</analyses>

Provide a concise executive summary (about 400 words) with key insights and strategic recommendations tailored to {company_name}. Structure your response in JSON format as follows:
</instruction>

<output_format>
{{
  "executive_summary": "string",
  "key_trends": [
    {{
      "trend": "string",
      "description": "string",
      "implications": "string",
      "significance": "string (choose one: ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])"
    }}
  ],
  "critical_risks": [
    {{
      "risk": "string",
      "urgency": "string (choose one: ['Low', 'Medium', 'High', 'Very High', 'Critical'])",
      "potential_impact": "string (choose one: ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])"
    }}
  ],
  "strategic_opportunities": [
    {{
      "opportunity": "string",
      "description": "string",
      "potential_benefits": "string",
      "feasibility": "string (choose one: ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])"
    }}
  ],
  "resilience_recommendations": [
    {{
      "recommendation": "string",
      "description": "string",
      "expected_outcome": "string",
      "priority": "string (choose one: ['Low', 'Medium', 'High', 'Very High', 'Critical'])"
    }}
  ]
}}
</output_format>
"""

INTERACTION_ANALYSIS_PROMPT = """
<instruction>
As an expert in climate risk assessment, analyze the potential interaction between the following two risks for {company_name}:

<company_context>
Company: {company_name}
Industry: {industry}
Region: {company_region}
Key Products: {key_products}
</company_context>

<risk1>
<description>{risk1_description}</description>
<category>{risk1_category}</category>
<subcategory>{risk1_subcategory}</subcategory>
</risk1>

<risk2>
<description>{risk2_description}</description>
<category>{risk2_category}</category>
<subcategory>{risk2_subcategory}</subcategory>
</risk2>

Please provide:
1. A brief explanation of how these risks might interact or influence each other, considering {company_name}'s specific context.
2. An assessment of the potential compounding effects if both risks materialize simultaneously for {company_name}.
3. Any potential mitigating factors that could reduce the combined impact of these risks on {company_name}.
4. A suggested interaction score on a scale of 0 (no interaction) to 1 (strong interaction), with a brief justification.

Structure your response in JSON format as follows:
</instruction>

<output_format>
{{
  "interaction_explanation": "string",
  "compounding_effects": {{
    "description": "string",
    "severity": "string (choose one: ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])"
  }},
  "mitigating_factors": [
    {{
      "factor": "string",
      "description": "string",
      "effectiveness": "string (choose one: ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])"
    }}
  ],
  "interaction_score": {{
    "score": float,
    "justification": "string"
  }}
}}
</output_format>
"""

SYSTEMIC_RISK_PROMPT = """
<instruction>
As an expert in systemic risk analysis, evaluate the following risk in the context of broader systems, specifically for {company_name}:

<company_context>
Company: {company_name}
Industry: {industry}
Region: {company_region}
Key Products: {key_products}
</company_context>

<risk>
<description>{risk_description}</description>
<category>{risk_category}</category>
<subcategory>{risk_subcategory}</subcategory>
</risk>

<context>
<company_industry>{company_industry}</company_industry>
<key_dependencies>{key_dependencies}</key_dependencies>
</context>

Please provide an analysis addressing the following points:
1. How might this risk contribute to or be affected by systemic vulnerabilities in the {company_industry} sector, particularly for {company_name}?
2. Identify potential trigger points or critical thresholds related to this risk that could lead to cascading effects across systems, considering {company_name}'s position in the industry.
3. Assess {company_name}'s potential role in mitigating this systemic risk, considering its position in the industry and sustainability goals.
4. Suggest collaborative initiatives or policy engagements that could help address this risk at a systemic level, with {company_name} playing a key role.

Structure your response in JSON format as follows:
</instruction>

<output_format>
{{
  "systemic_vulnerabilities": {{
    "contribution": "string",
    "affected_by": "string",
    "significance": "string (choose one: ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])"
  }},
  "trigger_points": [
    {{
      "description": "string",
      "threshold": "string",
      "potential_cascading_effects": "string",
      "likelihood": "string (choose one: ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])"
    }}
  ],
  "company_mitigation_role": {{
    "potential_actions": "string",
    "industry_position_leverage": "string",
    "effectiveness": "string (choose one: ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])"
  }},
  "collaborative_initiatives": [
    {{
      "initiative": "string",
      "description": "string",
      "potential_impact": "string",
      "feasibility": "string (choose one: ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])"
    }}
  ],
  "policy_engagements": [
    {{
      "engagement": "string",
      "description": "string",
      "expected_outcome": "string",
      "importance": "string (choose one: ['Low', 'Medium', 'High', 'Very High', 'Critical'])"
    }}
  ]
}}
</output_format>
"""

MITIGATION_STRATEGY_PROMPT = """
<instruction>
As an expert in climate risk mitigation and adaptation strategies, analyze the following risk and its assessment across different scenarios for {company_name}:

<company_context>
Company: {company_name}
Industry: {industry}
Region: {company_region}
Key Products: {key_products}
</company_context>

<risk>
<description>{risk_description}</description>
<category>{risk_category}</category>
<subcategory>{risk_subcategory}</subcategory>
</risk>

<scenario_analyses>
{scenario_analyses}
</scenario_analyses>

Based on this information, please provide:

1. 3-5 concrete mitigation strategies that address this risk across multiple scenarios, tailored to {company_name}'s context and sustainability goals.
2. For each strategy, briefly explain its potential effectiveness and any challenges in implementation specific to {company_name}.
3. Prioritize these strategies based on their potential impact and feasibility for {company_name}.

Structure your response in JSON format as follows:
</instruction>

<output_format>
{{
  "mitigation_strategies": [
    {{
      "strategy": "string",
      "description": "string",
      "potential_effectiveness": "string (choose one: ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])",
      "implementation_challenges": "string",
      "challenge_level": "string (choose one: ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])",
      "priority": int,
      "impact": "string (choose one: ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])",
      "feasibility": "string (choose one: ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])"
    }}
  ],
  "overall_recommendation": "string"
}}
</output_format>
"""