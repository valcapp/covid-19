"""
Python model "community corona 8.py"
Translated using PySD version 0.10.0
"""
from __future__ import division
import numpy as np
from pysd import utils
import xarray as xr

from pysd.py_backend.functions import cache
from pysd.py_backend import functions

_subscript_dict = {}

_namespace = {
    'TIME': 'time',
    'Time': 'time',
    'Initial Population': 'initial_population',
    'Seasonal Period': 'seasonal_period',
    'Effect of Season': 'effect_of_season',
    'Peak Season': 'peak_season',
    'Infecting': 'infecting',
    'Seasonal Amplitude': 'seasonal_amplitude',
    'Contact Density Decline': 'contact_density_decline',
    'Relative Contact Density': 'relative_contact_density',
    'Transmission Rate': 'transmission_rate',
    'Active Infected': 'active_infected',
    'Potential Isolation Effectiveness': 'potential_isolation_effectiveness',
    'Isolation Effectiveness': 'isolation_effectiveness',
    'Hospital Strain': 'hospital_strain',
    'Relative Behavioral Risk': 'relative_behavioral_risk',
    'Public Health Capacity Sensitivity': 'public_health_capacity_sensitivity',
    'Public Health Capacity': 'public_health_capacity',
    'Fatality Rate': 'fatality_rate',
    'Public Health Strain': 'public_health_strain',
    'Hospital Capacity Sensitivity': 'hospital_capacity_sensitivity',
    'Importing Infected': 'importing_infected',
    'Fraction Susceptible': 'fraction_susceptible',
    'Hospital Capacity': 'hospital_capacity',
    'Serious Cases': 'serious_cases',
    'Deaths': 'deaths',
    'Dying': 'dying',
    'Exposed': 'exposed',
    'Fraction Requiring Hospitalization': 'fraction_requiring_hospitalization',
    'Recovered': 'recovered',
    'Recovering': 'recovering',
    'Untreated Fatality Rate': 'untreated_fatality_rate',
    'Infected': 'infected',
    'Treated Fatality Rate': 'treated_fatality_rate',
    'Advancing': 'advancing',
    'Behavior Reaction Time': 'behavior_reaction_time',
    'Behavioral Risk Reduction': 'behavioral_risk_reduction',
    'Incubation Time': 'incubation_time',
    'N Imported Infections': 'n_imported_infections',
    'Infection Duration': 'infection_duration',
    'Isolation Reaction Time': 'isolation_reaction_time',
    'R0': 'r0',
    'Susceptible': 'susceptible',
    'Initial Uncontrolled Transmission Rate': 'initial_uncontrolled_transmission_rate',
    'Import Time': 'import_time',
    'FINAL TIME': 'final_time',
    'INITIAL TIME': 'initial_time',
    'SAVEPER': 'saveper',
    'TIME STEP': 'time_step'
}

__pysd_version__ = "0.10.0"

__data = {'scope': None, 'time': lambda: 0}


def _init_outer_references(data):
    for key in data:
        __data[key] = data[key]


def time():
    return __data['time']()


@cache('run')
def initial_population():
    """
    Real Name: b'Initial Population'
    Original Eqn: b'100000'
    Units: b'people'
    Limits: (1.0, 200000.0)
    Type: constant

    b''
    """
    return 100000


@cache('run')
def seasonal_period():
    """
    Real Name: b'Seasonal Period'
    Original Eqn: b'365'
    Units: b'days'
    Limits: (None, None)
    Type: constant

    b'One year'
    """
    return 365


@cache('step')
def effect_of_season():
    """
    Real Name: b'Effect of Season'
    Original Eqn: b'1-Seasonal Amplitude+Seasonal Amplitude*(1+COS( 2*3.14159*(Time-Peak Season)/Seasonal Period\\\\ ))/2'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b'Effect of season on transmission - peak transmission occurs in winter; \\n    \\t\\ttransmission in trough = (1-amplitude)'
    """
    return 1 - seasonal_amplitude() + seasonal_amplitude() * (
        1 + np.cos(2 * 3.14159 * (time() - peak_season()) / seasonal_period())) / 2


@cache('run')
def peak_season():
    """
    Real Name: b'Peak Season'
    Original Eqn: b'0'
    Units: b'day'
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0


@cache('step')
def infecting():
    """
    Real Name: b'Infecting'
    Original Eqn: b'Active Infected*Transmission Rate*Effect of Season'
    Units: b'people/day'
    Limits: (None, None)
    Type: component

    b''
    """
    return active_infected() * transmission_rate() * effect_of_season()


@cache('run')
def seasonal_amplitude():
    """
    Real Name: b'Seasonal Amplitude'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (0.0, 1.0)
    Type: constant

    b'Amplitude of seasonal swings in transmission.'
    """
    return 0


@cache('run')
def contact_density_decline():
    """
    Real Name: b'Contact Density Decline'
    Original Eqn: b'0'
    Units: b'dmnl'
    Limits: (0.0, 4.0)
    Type: constant

    b'Slope of decline in contacts as the infection penetrates to less-connected \\n    \\t\\tportions of the social network.'
    """
    return 0


@cache('step')
def relative_contact_density():
    """
    Real Name: b'Relative Contact Density'
    Original Eqn: b'1/(1+Contact Density Decline*(1-Fraction Susceptible))'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b'Decline in contacts as the infection penetrates to less-connected portions \\n    \\t\\tof the social network. The effect is real, but the functional form is \\n    \\t\\tnotional here. This would be a good focus for improvement.'
    """
    return 1 / (1 + contact_density_decline() * (1 - fraction_susceptible()))


@cache('step')
def transmission_rate():
    """
    Real Name: b'Transmission Rate'
    Original Eqn: b'Initial Uncontrolled Transmission Rate*Relative Behavioral Risk*Fraction Susceptible\\\\ *Relative Contact Density'
    Units: b'fraction/day'
    Limits: (None, None)
    Type: component

    b'Fractional rate of transmission from non-isolated infected to the \\n    \\t\\tsusceptible population.'
    """
    return initial_uncontrolled_transmission_rate() * relative_behavioral_risk(
    ) * fraction_susceptible() * relative_contact_density()


@cache('step')
def active_infected():
    """
    Real Name: b'Active Infected'
    Original Eqn: b'Infected*(1-Isolation Effectiveness)'
    Units: b'people'
    Limits: (None, None)
    Type: component

    b'Effective number of infected people, after adjusting for reduction in \\n    \\t\\tinfectiousness from isolation, quarantine, and monitoring.'
    """
    return infected() * (1 - isolation_effectiveness())


@cache('run')
def potential_isolation_effectiveness():
    """
    Real Name: b'Potential Isolation Effectiveness'
    Original Eqn: b'0'
    Units: b'fraction'
    Limits: (0.0, 1.0)
    Type: constant

    b'Effect of isolation and monitoring measures, absent strain on the system.'
    """
    return 0


@cache('step')
def isolation_effectiveness():
    """
    Real Name: b'Isolation Effectiveness'
    Original Eqn: b'SMOOTH3(STEP(Potential Isolation Effectiveness,Import Time),Isolation Reaction Time) /(1+Public Health Strain^Public Health Capacity Sensitivity)'
    Units: b'fraction'
    Limits: (0.0, 1.0)
    Type: component

    b'Fractional reduction in infections gained by isolating infected persons.'
    """
    return _smooth_functionsstep__datatime_potential_isolation_effectiveness_import_time_isolation_reaction_time_functionsstep__datatime_potential_isolation_effectiveness_import_time_3(
    ) / (1 + public_health_strain()**public_health_capacity_sensitivity())


@cache('step')
def hospital_strain():
    """
    Real Name: b'Hospital Strain'
    Original Eqn: b'Serious Cases/Hospital Capacity'
    Units: b'Index'
    Limits: (None, None)
    Type: component

    b'Strain on hospital capacity, from ratio of serious cases to capacity.'
    """
    return serious_cases() / hospital_capacity()


@cache('step')
def relative_behavioral_risk():
    """
    Real Name: b'Relative Behavioral Risk'
    Original Eqn: b'SMOOTH3(1-STEP(Behavioral Risk Reduction,Import Time),Behavior Reaction Time)'
    Units: b'dmnl'
    Limits: (None, None)
    Type: component

    b''
    """
    return _smooth_1functionsstep__datatime_behavioral_risk_reduction_import_time_behavior_reaction_time_1functionsstep__datatime_behavioral_risk_reduction_import_time_3(
    )


@cache('run')
def public_health_capacity_sensitivity():
    """
    Real Name: b'Public Health Capacity Sensitivity'
    Original Eqn: b'2'
    Units: b'dmnl'
    Limits: (1.0, 5.0)
    Type: constant

    b'Sensitivity of public health performance to capacity constraint.'
    """
    return 2


@cache('run')
def public_health_capacity():
    """
    Real Name: b'Public Health Capacity'
    Original Eqn: b'1000'
    Units: b'people'
    Limits: (None, None)
    Type: constant

    b'Capacity of the public health system to monitor, quarantine, and trace \\n    \\t\\tcontacts. Expressed as number of infected people that can be managed.'
    """
    return 1000


@cache('step')
def fatality_rate():
    """
    Real Name: b'Fatality Rate'
    Original Eqn: b'Untreated Fatality Rate+(Treated Fatality Rate-Untreated Fatality Rate)/(1+Hospital Strain\\\\ ^Hospital Capacity Sensitivity)'
    Units: b'fraction'
    Limits: (None, None)
    Type: component

    b''
    """
    return untreated_fatality_rate() + (treated_fatality_rate() - untreated_fatality_rate()) / (
        1 + hospital_strain()**hospital_capacity_sensitivity())


@cache('step')
def public_health_strain():
    """
    Real Name: b'Public Health Strain'
    Original Eqn: b'Infected/Public Health Capacity'
    Units: b'Index'
    Limits: (None, None)
    Type: component

    b'Strain on the public health system, expressed as the burden of infected \\n    \\t\\trelative to capacity.'
    """
    return infected() / public_health_capacity()


@cache('run')
def hospital_capacity_sensitivity():
    """
    Real Name: b'Hospital Capacity Sensitivity'
    Original Eqn: b'2'
    Units: b'dmnl'
    Limits: (1.0, 5.0)
    Type: constant

    b'Sensitivity of care quality to capacity.'
    """
    return 2


@cache('step')
def importing_infected():
    """
    Real Name: b'Importing Infected'
    Original Eqn: b'N Imported Infections*PULSE(Import Time,TIME STEP)/TIME STEP'
    Units: b'people/day'
    Limits: (None, None)
    Type: component

    b'Import of infections into the region. This is a one-time introduction; \\n    \\t\\tthere is no repeated challenge from an outside reservoir.'
    """
    return n_imported_infections() * functions.pulse(__data['time'], import_time(),
                                                     time_step()) / time_step()


@cache('step')
def fraction_susceptible():
    """
    Real Name: b'Fraction Susceptible'
    Original Eqn: b'Susceptible/Initial Population'
    Units: b'fraction'
    Limits: (None, None)
    Type: component

    b'Fraction of initial population remaining susceptible.'
    """
    return susceptible() / initial_population()


@cache('run')
def hospital_capacity():
    """
    Real Name: b'Hospital Capacity'
    Original Eqn: b'100'
    Units: b'people'
    Limits: (0.0, 1000.0)
    Type: constant

    b'Hospital capacity, expressed as number of serious infected cases that can \\n    \\t\\tbe handled given beds, staff, etc.'
    """
    return 100


@cache('step')
def serious_cases():
    """
    Real Name: b'Serious Cases'
    Original Eqn: b'Infected*Fraction Requiring Hospitalization'
    Units: b'people'
    Limits: (None, None)
    Type: component

    b'Serious cases, requiring hospitalization.'
    """
    return infected() * fraction_requiring_hospitalization()


@cache('step')
def deaths():
    """
    Real Name: b'Deaths'
    Original Eqn: b'INTEG ( Dying, 0)'
    Units: b'people'
    Limits: (None, None)
    Type: component

    b'Cumulative infections resolving to death.'
    """
    return _integ_deaths()


@cache('step')
def dying():
    """
    Real Name: b'Dying'
    Original Eqn: b'Infected*Fatality Rate/Infection Duration'
    Units: b'people/day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected() * fatality_rate() / infection_duration()


@cache('step')
def exposed():
    """
    Real Name: b'Exposed'
    Original Eqn: b'INTEG ( Infecting-Advancing, 0)'
    Units: b'people'
    Limits: (None, None)
    Type: component

    b'Exposed, asymptomatic population. As a simplification, assumed to be \\n    \\t\\tnon-infectious, though there appears to be some infectivity for \\n    \\t\\tcoronavirus in reality.'
    """
    return _integ_exposed()


@cache('run')
def fraction_requiring_hospitalization():
    """
    Real Name: b'Fraction Requiring Hospitalization'
    Original Eqn: b'0.1'
    Units: b'fraction'
    Limits: (0.0, 1.0, 0.01)
    Type: constant

    b'Fraction of infected who require hospitalization.'
    """
    return 0.1


@cache('step')
def recovered():
    """
    Real Name: b'Recovered'
    Original Eqn: b'INTEG ( Recovering, 0)'
    Units: b'people'
    Limits: (None, None)
    Type: component

    b'Cumulative recovered people. As a simplification, these are assumed immune \\n    \\t\\t- there is no reinfection.'
    """
    return _integ_recovered()


@cache('step')
def recovering():
    """
    Real Name: b'Recovering'
    Original Eqn: b'Infected/Infection Duration*(1-Fatality Rate)'
    Units: b'people/day'
    Limits: (None, None)
    Type: component

    b''
    """
    return infected() / infection_duration() * (1 - fatality_rate())


@cache('run')
def untreated_fatality_rate():
    """
    Real Name: b'Untreated Fatality Rate'
    Original Eqn: b'0.04'
    Units: b'fraction'
    Limits: (0.0, 0.1)
    Type: constant

    b'Fatality rate when minimally treated due to overwhelmed, chaotic health \\n    \\t\\tcare.'
    """
    return 0.04


@cache('step')
def infected():
    """
    Real Name: b'Infected'
    Original Eqn: b'INTEG ( Advancing+Importing Infected-Dying-Recovering, 0)'
    Units: b'people'
    Limits: (None, None)
    Type: component

    b'Infected, symptomatic, infectious people.'
    """
    return _integ_infected()


@cache('run')
def treated_fatality_rate():
    """
    Real Name: b'Treated Fatality Rate'
    Original Eqn: b'0.01'
    Units: b'fraction'
    Limits: (0.0, 0.1)
    Type: constant

    b'Fatality rate with good health care.'
    """
    return 0.01


@cache('step')
def advancing():
    """
    Real Name: b'Advancing'
    Original Eqn: b'Exposed/Incubation Time'
    Units: b'people/day'
    Limits: (None, None)
    Type: component

    b''
    """
    return exposed() / incubation_time()


@cache('run')
def behavior_reaction_time():
    """
    Real Name: b'Behavior Reaction Time'
    Original Eqn: b'20'
    Units: b'day'
    Limits: (1.0, 60.0)
    Type: constant

    b'Time from first infection for behavioral risk reductions to be fully \\n    \\t\\timplemented.'
    """
    return 20


@cache('run')
def behavioral_risk_reduction():
    """
    Real Name: b'Behavioral Risk Reduction'
    Original Eqn: b'0'
    Units: b'fraction'
    Limits: (0.0, 1.0)
    Type: constant

    b'Fractional reduction in risk from social distancing, increased \\n    \\t\\thandwashing, and other behavioral measures.'
    """
    return 0


@cache('run')
def incubation_time():
    """
    Real Name: b'Incubation Time'
    Original Eqn: b'5'
    Units: b'day'
    Limits: (1.0, 10.0)
    Type: constant

    b'Time to onset of symptoms among exposed people.'
    """
    return 5


@cache('run')
def n_imported_infections():
    """
    Real Name: b'N Imported Infections'
    Original Eqn: b'3'
    Units: b'people'
    Limits: (0.0, 100.0)
    Type: constant

    b'Number of infections initially imported into the region.'
    """
    return 3


@cache('run')
def infection_duration():
    """
    Real Name: b'Infection Duration'
    Original Eqn: b'7'
    Units: b'day'
    Limits: (1.0, 10.0)
    Type: constant

    b'Duration of infection. As a simplification, this is the same for cases \\n    \\t\\tresulting in recovery and death, though in reality serious cases have \\n    \\t\\tlonger duration.'
    """
    return 7


@cache('run')
def isolation_reaction_time():
    """
    Real Name: b'Isolation Reaction Time'
    Original Eqn: b'2'
    Units: b'day'
    Limits: (1.0, 30.0)
    Type: constant

    b'Time from first infected person needed to ramp up public health measures.'
    """
    return 2


@cache('run')
def r0():
    """
    Real Name: b'R0'
    Original Eqn: b'3.3'
    Units: b'dmnl'
    Limits: (1.0, 4.0)
    Type: constant

    b'Base reproduction ratio for the disease. Plausible range reported for \\n    \\t\\tcoronavirus is about 2.2-3.9.'
    """
    return 3.3


@cache('step')
def susceptible():
    """
    Real Name: b'Susceptible'
    Original Eqn: b'INTEG ( -Infecting, Initial Population)'
    Units: b'people'
    Limits: (None, None)
    Type: component

    b'Susceptible population.'
    """
    return _integ_susceptible()


@cache('step')
def initial_uncontrolled_transmission_rate():
    """
    Real Name: b'Initial Uncontrolled Transmission Rate'
    Original Eqn: b'R0/Infection Duration'
    Units: b'people/person/day'
    Limits: (None, None)
    Type: component

    b'Initial transmission rate, with 100% susceptibles and no controls.'
    """
    return r0() / infection_duration()


@cache('run')
def import_time():
    """
    Real Name: b'Import Time'
    Original Eqn: b'10'
    Units: b'day'
    Limits: (1.0, 100.0)
    Type: constant

    b'Time of first infection.'
    """
    return 10


@cache('run')
def final_time():
    """
    Real Name: b'FINAL TIME'
    Original Eqn: b'300'
    Units: b'day'
    Limits: (None, None)
    Type: constant

    b'The final time for the simulation.'
    """
    return 300


@cache('run')
def initial_time():
    """
    Real Name: b'INITIAL TIME'
    Original Eqn: b'0'
    Units: b'day'
    Limits: (None, None)
    Type: constant

    b'The initial time for the simulation.'
    """
    return 0


@cache('step')
def saveper():
    """
    Real Name: b'SAVEPER'
    Original Eqn: b'TIME STEP'
    Units: b'day'
    Limits: (0.0, None)
    Type: component

    b'The frequency with which output is stored.'
    """
    return time_step()


@cache('run')
def time_step():
    """
    Real Name: b'TIME STEP'
    Original Eqn: b'0.125'
    Units: b'day'
    Limits: (0.0, None)
    Type: constant

    b'The time step for the simulation.'
    """
    return 0.125


_smooth_functionsstep__datatime_potential_isolation_effectiveness_import_time_isolation_reaction_time_functionsstep__datatime_potential_isolation_effectiveness_import_time_3 = functions.Smooth(
    lambda: functions.step(__data['time'], potential_isolation_effectiveness(), import_time(
    )), lambda: isolation_reaction_time(), lambda: functions.step(
        __data['time'], potential_isolation_effectiveness(), import_time()), lambda: 3)

_smooth_1functionsstep__datatime_behavioral_risk_reduction_import_time_behavior_reaction_time_1functionsstep__datatime_behavioral_risk_reduction_import_time_3 = functions.Smooth(
    lambda: 1 - functions.step(__data['time'], behavioral_risk_reduction(), import_time()), lambda:
    behavior_reaction_time(), lambda: 1 - functions.step(__data['time'], behavioral_risk_reduction(
    ), import_time()), lambda: 3)

_integ_deaths = functions.Integ(lambda: dying(), lambda: 0)

_integ_exposed = functions.Integ(lambda: infecting() - advancing(), lambda: 0)

_integ_recovered = functions.Integ(lambda: recovering(), lambda: 0)

_integ_infected = functions.Integ(
    lambda: advancing() + importing_infected() - dying() - recovering(), lambda: 0)

_integ_susceptible = functions.Integ(lambda: -infecting(), lambda: initial_population())
