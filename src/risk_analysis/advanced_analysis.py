from typing import List, Dict, Any
from src.models import Risk, Scenario, PESTELAnalysis, SystemicRisk
from src.config import LLM_MODEL, LLM_API_KEY, SCENARIOS, COMPANY_INFO
from src.prompts import (RISK_NARRATIVE_PROMPT, EXECUTIVE_INSIGHTS_PROMPT, 
                         SYSTEMIC_RISK_PROMPT, MITIGATION_STRATEGY_PROMPT, 
                         PESTEL_ANALYSIS_PROMPT)
import openai
import numpy as np
import re
from src.risk_analysis.pestel_analysis import perform_pestel_analysis
from src.risk_analysis.sasb_integration import integrate_sasb_materiality
from src.risk_analysis.systemic_risk_analysis import analyze_systemic_risks, identify_trigger_points, assess_resilience
from src.risk_analysis.interaction_analysis import analyze_risk_interactions, build_risk_network, create_risk_interaction_matrix, simulate_risk_interactions

openai.api_key = LLM_API_KEY

def conduct_advanced_risk_analysis(risks: List[Risk], scenarios: Dict[str, Scenario], key_dependencies: List[str], external_data: Dict) -> Dict:
    comprehensive_analysis = {}
    for scenario_name, scenario in scenarios.items():
        scenario_analysis = {}
        for risk in risks:
            scenario_analysis[risk.id] = llm_risk_assessment(risk, scenario, COMPANY_INFO)
        comprehensive_analysis[scenario_name] = scenario_analysis
    
    risk_narratives = generate_risk_narratives(risks, comprehensive_analysis)
    executive_insights = generate_executive_insights(comprehensive_analysis, risks)
    systemic_risks = analyze_systemic_risks(risks, COMPANY_INFO.industry, key_dependencies)
    risk_interactions = analyze_risk_interactions(risks)
    risk_network = build_risk_network(risks, risk_interactions)
    cross_scenario_results = perform_cross_scenario_analysis(comprehensive_analysis)
    key_uncertainties = identify_key_uncertainties(cross_scenario_results)
    mitigation_strategies = generate_mitigation_strategies(risks, comprehensive_analysis)
    
    pestel_analysis = perform_pestel_analysis(risks, external_data)
    sasb_material_risks = integrate_sasb_materiality(risks, COMPANY_INFO.industry)
    
    trigger_points = identify_trigger_points(risks, risk_network, external_data)
    resilience_assessment = assess_resilience(risks, comprehensive_analysis, cross_scenario_results)
    
    return {
        "comprehensive_analysis": comprehensive_analysis,
        "risk_narratives": risk_narratives,
        "executive_insights": executive_insights,
        "systemic_risks": systemic_risks,
        "cross_scenario_results": cross_scenario_results,
        "key_uncertainties": key_uncertainties,
        "mitigation_strategies": mitigation_strategies,
        "pestel_analysis": pestel_analysis,
        "sasb_material_risks": sasb_material_risks,
        "trigger_points": trigger_points,
        "resilience_assessment": resilience_assessment
    }

def llm_risk_assessment(risk: Risk, scenario: Scenario, company_info: Any) -> Dict[str, Any]:
    prompt = f"""
    As an expert in climate risk assessment for the {company_info.industry} industry, analyze the following risk under the given scenario for {company_info.name}:

    Company: {company_info.name}
    Industry: {company_info.industry}
    Region: {company_info.region}
    Key Products: {', '.join(company_info.key_products)}

    Risk: {risk.description}
    Category: {risk.category}
    Subcategory: {risk.subcategory}
    Current likelihood: {risk.likelihood}
    Current impact: {risk.impact}

    Scenario: {scenario.name}
    - Temperature increase: {scenario.temp_increase}°C
    - Carbon price: ${scenario.carbon_price}/ton
    - Renewable energy share: {scenario.renewable_energy * 100}%
    - Policy stringency: {scenario.policy_stringency * 100}%
    - Biodiversity loss: {scenario.biodiversity_loss * 100}%
    - Ecosystem degradation: {scenario.ecosystem_degradation * 100}%
    - Financial stability: {scenario.financial_stability * 100}%
    - Supply chain disruption: {scenario.supply_chain_disruption * 100}%

    Provide a detailed analysis addressing:
    1. How does this risk's likelihood and impact change under the given scenario, considering {company_info.name}'s specific context?
    2. What are the potential financial implications for {company_info.name} over the next 5 years?
    3. Are there any emerging opportunities related to this risk in this scenario, particularly for {company_info.name}'s products or services?
    4. What additional challenges might arise from this risk in this specific context, considering {company_info.name}'s supply chain and operations?
    5. Suggest 2-3 possible mitigation strategies tailored to this scenario and {company_info.name}'s sustainability goals.

    Structure your response with clear headings for each point.
    """

    response = openai.ChatCompletion.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": "You are an expert in climate risk assessment."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1000
    )

    return parse_llm_response(response.choices[0].message['content'])

def parse_llm_response(content: str) -> Dict[str, Any]:
    sections = content.split('\n\n')
    parsed_response = {}
    current_section = ""
    for section in sections:
        if ':' in section:
            title, text = section.split(':', 1)
            current_section = title.strip().lower().replace(' ', '_')
            parsed_response[current_section] = text.strip()
        else:
            parsed_response[current_section] += '\n' + section.strip()
    return parsed_response

def assess_aggregate_impact(risks: List[Risk], interaction_matrix: np.ndarray, num_simulations: int = 1000) -> Dict[str, float]:
    n = len(risks)
    base_impacts = np.array([risk.impact for risk in risks])
    
    aggregate_impacts = []
    for _ in range(num_simulations):
        risk_levels = np.random.beta(2, 2, n) * base_impacts
        for _ in range(10):  # Simulate interactions for 10 time steps
            influence = interaction_matrix @ risk_levels
            risk_levels = np.clip(risk_levels + 0.1 * influence, 0, 1)
        aggregate_impacts.append(np.sum(risk_levels))
    
    return {
        "mean": np.mean(aggregate_impacts),
        "median": np.median(aggregate_impacts),
        "95th_percentile": np.percentile(aggregate_impacts, 95),
        "max": np.max(aggregate_impacts)
    }

def identify_tipping_points(risks: List[Risk], interaction_matrix: np.ndarray) -> List[Dict[str, Any]]:
    n = len(risks)
    base_impacts = np.array([risk.impact for risk in risks])
    tipping_points = []

    for i in range(n):
        impact_levels = np.linspace(0, 1, 100)
        aggregate_impacts = []
        for level in impact_levels:
            risk_levels = base_impacts.copy()
            risk_levels[i] = level
            for _ in range(10):  # Simulate interactions for 10 time steps
                influence = interaction_matrix @ risk_levels
                risk_levels = np.clip(risk_levels + 0.1 * influence, 0, 1)
            aggregate_impacts.append(np.sum(risk_levels))
        
        # Detect sudden changes in the rate of change
        rate_of_change = np.diff(aggregate_impacts)
        threshold = np.mean(rate_of_change) + 2 * np.std(rate_of_change)
        tipping_point_indices = np.where(rate_of_change > threshold)[0]
        
        if len(tipping_point_indices) > 0:
            tipping_points.append({
                "risk_id": risks[i].id,
                "risk_description": risks[i].description,
                "tipping_point_level": impact_levels[tipping_point_indices[0]],
                "aggregate_impact": aggregate_impacts[tipping_point_indices[0]]
            })
    
    return tipping_points

def generate_risk_narratives(risks: List[Risk], comprehensive_analysis: Dict[str, Dict[int, str]]) -> Dict[int, str]:
    risk_narratives = {}
    for risk in risks:
        scenario_analyses = {scenario: analyses[risk.id] for scenario, analyses in comprehensive_analysis.items()}
        prompt = RISK_NARRATIVE_PROMPT.format(
            company_name=COMPANY_INFO.name,
            industry=COMPANY_INFO.industry,
            company_region=COMPANY_INFO.region,
            key_products=', '.join(COMPANY_INFO.key_products),
            risk_description=risk.description,
            risk_category=risk.category,
            risk_subcategory=risk.subcategory,
            risk_likelihood=risk.likelihood,
            risk_impact=risk.impact,
            scenario_analyses="\n".join([f"{scenario}: {analysis}" for scenario, analysis in scenario_analyses.items()])
        )

        response = openai.ChatCompletion.create(
            model=LLM_MODEL,
            messages=[
                {"role": "system", "content": "You are an expert in climate risk assessment and scenario analysis."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        risk_narratives[risk.id] = response.choices[0].message['content']
    
    return risk_narratives

def generate_executive_insights(comprehensive_analysis: Dict[str, Dict[int, str]], risks: List[Risk]) -> str:
    all_analyses = "\n\n".join([f"Risk: {risk.description}\n" + "\n".join([f"{scenario}: {analysis}" for scenario, analyses in comprehensive_analysis.items() for r_id, analysis in analyses.items() if r_id == risk.id]) for risk in risks])

    prompt = EXECUTIVE_INSIGHTS_PROMPT.format(
        company_name=COMPANY_INFO.name,
        industry=COMPANY_INFO.industry,
        company_region=COMPANY_INFO.region,
        key_products=', '.join(COMPANY_INFO.key_products),
        all_analyses=all_analyses
    )

    response = openai.ChatCompletion.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": "You are a senior climate risk analyst providing insights to top executives."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=800
    )

    return response.choices[0].message['content']

def perform_cross_scenario_analysis(comprehensive_analysis: Dict[str, Dict[int, str]]) -> Dict[int, Dict[str, Dict[str, float]]]:
    cross_scenario_results = {}
    for risk_id in comprehensive_analysis[next(iter(comprehensive_analysis))].keys():
        risk_results = {}
        for scenario, analyses in comprehensive_analysis.items():
            analysis = analyses[risk_id]
            impact_score = extract_impact_score(analysis)
            likelihood_score = extract_likelihood_score(analysis)
            adaptability_score = extract_adaptability_score(analysis)
            
            risk_results[scenario] = {
                "impact": impact_score,
                "likelihood": likelihood_score,
                "adaptability": adaptability_score
            }
        cross_scenario_results[risk_id] = risk_results
    return cross_scenario_results

def identify_key_uncertainties(cross_scenario_results: Dict[int, Dict[str, Dict[str, float]]]) -> List[int]:
    uncertainties = []
    for risk_id, scenarios in cross_scenario_results.items():
        impact_variance = np.var([s['impact'] for s in scenarios.values()])
        likelihood_variance = np.var([s['likelihood'] for s in scenarios.values()])
        if impact_variance > 0.1 or likelihood_variance > 0.1:  # Threshold for high uncertainty
            uncertainties.append(risk_id)
    return uncertainties

def generate_mitigation_strategies(risks: List[Risk], comprehensive_analysis: Dict[str, Dict[int, str]]) -> Dict[int, List[str]]:
    mitigation_strategies = {}
    for risk in risks:
        prompt = MITIGATION_STRATEGY_PROMPT.format(
            risk_description=risk.description,
            risk_category=risk.category,
            risk_subcategory=risk.subcategory,
            scenario_analyses="\n".join([f"Scenario: {scenario}\nAnalysis: {analyses[risk.id]}" for scenario, analyses in comprehensive_analysis.items()])
        )
        
        response = openai.ChatCompletion.create(
            model=LLM_MODEL,
            messages=[
                {"role": "system", "content": "You are an expert in climate risk mitigation and adaptation strategies."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=600
        )
        
        strategies = parse_mitigation_strategies(response.choices[0].message['content'])
        mitigation_strategies[risk.id] = strategies
    
    return mitigation_strategies

def extract_impact_score(analysis: str) -> float:
    impact_pattern = r"impact.*?(\d+(?:\.\d+)?)"
    match = re.search(impact_pattern, analysis, re.IGNORECASE)
    return float(match.group(1)) if match else 0.5

def extract_likelihood_score(analysis: str) -> float:
    likelihood_pattern = r"likelihood.*?(\d+(?:\.\d+)?)"
    match = re.search(likelihood_pattern, analysis, re.IGNORECASE)
    return float(match.group(1)) if match else 0.5

def extract_adaptability_score(analysis: str) -> float:
    adaptability_pattern = r"adaptability.*?(\d+(?:\.\d+)?)"
    match = re.search(adaptability_pattern, analysis, re.IGNORECASE)
    return float(match.group(1)) if match else 0.5

def parse_mitigation_strategies(content: str) -> List[str]:
    strategies = re.findall(r'\d+\.\s*(.*?)(?=\n\d+\.|\Z)', content, re.DOTALL)
    return [strategy.strip() for strategy in strategies if strategy.strip()]