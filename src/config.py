import os
import logging
from typing import Dict, NamedTuple
from src.models import Company

class Scenario(NamedTuple):
    name: str
    temp_increase: float
    carbon_price: float
    renewable_energy: float
    policy_stringency: float
    biodiversity_loss: float
    ecosystem_degradation: float
    financial_stability: float
    supply_chain_disruption: float
    biodiversity_index: float  # New parameter
    ecosystem_health: float  # New parameter
    financial_system_stability: float  # New parameter
    global_supply_chain_resilience: float  # New parameter

# Scenario definitions
SCENARIOS: Dict[str, Scenario] = {
    "Net Zero 2050": Scenario(
        name="Net Zero 2050",
        temp_increase=1.5,
        carbon_price=250,
        renewable_energy=0.75,
        policy_stringency=0.9,
        biodiversity_loss=0.1,
        ecosystem_degradation=0.2,
        financial_stability=0.8,
        supply_chain_disruption=0.3,
        biodiversity_index=0.9,
        ecosystem_health=0.8,
        financial_system_stability=0.85,
        global_supply_chain_resilience=0.7
    ),
    "Delayed Transition": Scenario(
        name="Delayed Transition",
        temp_increase=2.5,
        carbon_price=125,
        renewable_energy=0.55,
        policy_stringency=0.6,
        biodiversity_loss=0.3,
        ecosystem_degradation=0.4,
        financial_stability=0.6,
        supply_chain_disruption=0.5,
        biodiversity_index=0.7,
        ecosystem_health=0.6,
        financial_system_stability=0.7,
        global_supply_chain_resilience=0.6
    ),
    "Current Policies": Scenario(
        name="Current Policies",
        temp_increase=3.5,
        carbon_price=35,
        renewable_energy=0.35,
        policy_stringency=0.2,
        biodiversity_loss=0.5,
        ecosystem_degradation=0.6,
        financial_stability=0.4,
        supply_chain_disruption=0.7,
        biodiversity_index=0.5,
        ecosystem_health=0.4,
        financial_system_stability=0.5,
        global_supply_chain_resilience=0.4
    ),
    "Nature Positive": Scenario(
        name="Nature Positive",
        temp_increase=1.8,
        carbon_price=200,
        renewable_energy=0.7,
        policy_stringency=0.8,
        biodiversity_loss=-0.1,  # Net gain
        ecosystem_degradation=-0.2,  # Net restoration
        financial_stability=0.75,
        supply_chain_disruption=0.4,
        biodiversity_index=0.95,
        ecosystem_health=0.9,
        financial_system_stability=0.8,
        global_supply_chain_resilience=0.75
    ),
    "Systemic Crisis": Scenario(
        name="Systemic Crisis",
        temp_increase=4.0,
        carbon_price=50,
        renewable_energy=0.4,
        policy_stringency=0.3,
        biodiversity_loss=0.6,
        ecosystem_degradation=0.7,
        financial_stability=0.2,
        supply_chain_disruption=0.8,
        biodiversity_index=0.3,
        ecosystem_health=0.2,
        financial_system_stability=0.1,
        global_supply_chain_resilience=0.2
    ),
        "Cascading Failures": Scenario(
        name="Cascading Failures",
        temp_increase=3.5,
        carbon_price=75,
        renewable_energy=0.45,
        policy_stringency=0.4,
        biodiversity_loss=0.5,
        ecosystem_degradation=0.6,
        financial_stability=0.3,
        supply_chain_disruption=0.8
    ),
    "Global Instability": Scenario(
        name="Global Instability",
        temp_increase=4.0,
        carbon_price=50,
        renewable_energy=0.4,
        policy_stringency=0.3,
        biodiversity_loss=0.6,
        ecosystem_degradation=0.7,
        financial_stability=0.2,
        supply_chain_disruption=0.8
    )


}

# Monte Carlo simulation parameters
NUM_SIMULATIONS = 10000

# Clustering parameters
NUM_CLUSTERS = 3

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

# NLP model
NER_MODEL = "dbmdz/bert-large-cased-finetuned-conll03-english"

# LLM configuration
LLM_MODEL = "gpt-3.5-turbo"  # Replace with the actual model you're using
LLM_API_KEY = os.getenv("OPENAI_API_KEY")

if not LLM_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

# Visualization settings
VIZ_DPI = 300
HEATMAP_CMAP = 'YlOrRd'

# Time series analysis parameters
TIME_SERIES_HORIZON = 10  # years

# Sensitivity analysis parameters
SENSITIVITY_VARIABLES = ['temp_increase', 'carbon_price', 'renewable_energy', 'policy_stringency', 'biodiversity_loss', 'ecosystem_degradation', 'financial_stability', 'supply_chain_disruption']
SENSITIVITY_RANGE = 0.2  # +/- 20%

def setup_logging(log_level: str = "INFO") -> None:
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f'Invalid log level: {log_level}')
    
    logging.basicConfig(
        level=numeric_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename=os.path.join(OUTPUT_DIR, 'risk_assessment.log')
    )

COMPANY_INFO = Company(
    name="Example Corp",
    industry="Technology",
    region=["North America", "Europe"]
    key_products=["Software", "Cloud Services", "AI Solutions"]
)