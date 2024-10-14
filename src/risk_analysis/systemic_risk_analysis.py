from typing import List, Dict, Tuple
import networkx as nx
import numpy as np
from src.models import Risk, ExternalData, SimulationResult

# Keep existing functions

def identify_trigger_points(risks: List[Risk], risk_network: nx.Graph, external_data: Dict[str, ExternalData]) -> Dict[int, Dict]:
    trigger_points = {}
    centrality = nx.betweenness_centrality(risk_network, weight='weight')
    
    for risk in risks:
        if centrality[risk.id] > np.mean(list(centrality.values())):
            neighbors = list(risk_network.neighbors(risk.id))
            total_weight = sum(risk_network[risk.id][neighbor]['weight'] for neighbor in neighbors)
            
            if total_weight > 0.5 * len(neighbors):  # More than half of max possible weight
                trigger_points[risk.id] = {
                    "description": risk.description,
                    "centrality": centrality[risk.id],
                    "connected_risks": neighbors,
                    "total_interaction_weight": total_weight,
                    "external_factors": identify_relevant_external_factors(risk, external_data)
                }
    
    return trigger_points

def assess_system_resilience(risks: List[Risk], risk_network: nx.Graph, scenario_impacts: Dict[str, List[Tuple[Risk, float]]]) -> Dict[str, float]:
    resilience_metrics = {}
    
    # Network-based resilience metrics
    resilience_metrics["network_density"] = nx.density(risk_network)
    resilience_metrics["average_clustering"] = nx.average_clustering(risk_network, weight='weight')
    resilience_metrics["assortativity"] = nx.degree_assortativity_coefficient(risk_network, weight='weight')
    
    # Impact-based resilience metrics
    for scenario, impacts in scenario_impacts.items():
        impact_values = [impact for _, impact in impacts]
        resilience_metrics[f"{scenario}_impact_dispersion"] = np.std(impact_values) / np.mean(impact_values)
        resilience_metrics[f"{scenario}_max_impact"] = max(impact_values)
    
    # Adaptive capacity metric (placeholder - this should be refined based on specific company data)
    resilience_metrics["adaptive_capacity"] = 1 - np.mean([risk.impact for risk in risks])
    
    return resilience_metrics

# Keep existing code below this line



def analyze_systemic_risks(risks: List[Risk], company_industry: str, key_dependencies: List[str]) -> Dict[str, Dict]:
    systemic_risks = {}
    for risk in risks:
        if is_systemic_risk(risk, company_industry, key_dependencies):
            systemic_risks[risk.id] = {
                "description": risk.description,
                "impact": risk.impact,
                "systemic_factor": identify_systemic_factor(risk)
            }
    return systemic_risks


def assess_resilience(risks: List[Risk], scenario_impacts: Dict[str, List[Tuple[Risk, float]]], simulation_results: Dict[str, Dict[int, SimulationResult]]) -> Dict[str, float]:
    resilience_scores = {}
    for scenario, impacts in scenario_impacts.items():
        scenario_resilience = calculate_scenario_resilience(impacts, simulation_results[scenario])
        resilience_scores[scenario] = scenario_resilience
    return resilience_scores

def is_systemic_risk(risk: Risk, company_industry: str, key_dependencies: List[str]) -> bool:
    systemic_keywords = ["market-wide", "industry-wide", "global", "systemic", "interconnected"]
    return any(keyword in risk.description.lower() for keyword in systemic_keywords) or \
           any(dep.lower() in risk.description.lower() for dep in key_dependencies)

def identify_systemic_factor(risk: Risk) -> str:
    if "financial" in risk.description.lower():
        return "Financial System"
    elif "supply chain" in risk.description.lower():
        return "Supply Chain"
    elif "geopolitical" in risk.description.lower():
        return "Geopolitical"
    else:
        return "Other"

def identify_relevant_external_factors(risk: Risk, external_data: Dict[str, ExternalData]) -> List[str]:
    relevant_factors = []
    latest_year = max(external_data.keys())
    if "economic" in risk.description.lower():
        relevant_factors.append(f"GDP Growth: {external_data[latest_year].gdp_growth}%")
    if "population" in risk.description.lower():
        relevant_factors.append(f"Population: {external_data[latest_year].population}")
    return relevant_factors

def calculate_scenario_resilience(impacts: List[Tuple[Risk, float]], simulation_results: Dict[int, SimulationResult]) -> float:
    total_impact = sum(impact for _, impact in impacts)
    variance = sum(np.var(result.impact_distribution) for result in simulation_results.values())
    return 1 / (total_impact * (1 + variance))  # Higher resilience for lower impact and lower variance

def analyze_risk_cascades(risk_network: nx.Graph, initial_risks: List[int], threshold: float = 0.5, max_steps: int = 10) -> Dict[int, List[float]]:
    cascade_progression = {risk: [1.0] for risk in initial_risks}
    for _ in range(max_steps):
        new_activations = {}
        for node in risk_network.nodes():
            if node not in cascade_progression:
                neighbor_influence = sum(cascade_progression.get(neighbor, [0])[-1] * risk_network[node][neighbor]['weight']
                                         for neighbor in risk_network.neighbors(node))
                if neighbor_influence > threshold:
                    new_activations[node] = neighbor_influence
        
        if not new_activations:
            break
        
        for node, activation in new_activations.items():
            cascade_progression[node] = [0.0] * (len(next(iter(cascade_progression.values()))) - 1) + [activation]
        
        for progression in cascade_progression.values():
            progression.append(progression[-1])
    
    return cascade_progression

def identify_risk_feedback_loops(risk_network: nx.Graph) -> List[List[int]]:
    feedback_loops = list(nx.simple_cycles(risk_network))
    return [loop for loop in feedback_loops if len(loop) > 2]

def assess_network_resilience(risk_network: nx.Graph) -> Dict[str, float]:
    resilience_metrics = {
        "average_clustering": nx.average_clustering(risk_network),
        "average_shortest_path_length": nx.average_shortest_path_length(risk_network, weight='weight'),
        "graph_density": nx.density(risk_network),
        "assortativity": nx.degree_assortativity_coefficient(risk_network)
    }
    return resilience_metrics