""" A simulation of the first Model of Ernesto Carrella's paper: Zero-Knowledge Traders,
journal of artificial societies and social simulation, december 2013

This is a partial 'equilibrium' model. A firm has a fixed production of 4 it offers
this to a fixed population of 10 household. The household willingness to pay is
household id * 10 (10, 20, 30 ... 90).
The firms sets the prices using a PID controller.
"""
from __future__ import division
from firm import Firm
from household import Household
from abce import Simulation, gui


simulation_parameters = {'name':'name',
                         'random_seed': None,
                         'rounds': 300}

@gui(simulation_parameters)
def main(simulation_parameters):
    s = Simulation(rounds=simulation_parameters['rounds'])
    action_list = [

        ('firm', 'production'),
        ('firm', 'panel'),
        ('firm', 'quote'),
        ('household', 'buying'),
        ('firm', 'selling'),
        ('household', 'panel'),
        ('household', 'consumption')
    ]

    s.add_action_list(action_list)

    s.panel('household', possessions=['cookies'])
    s.panel('firm', possessions=['cookies'])

    s.build_agents(Firm, 'firm', 1)
    s.build_agents(Household, 'household', 10)

    s.run()

if __name__ == '__main__':
    main(simulation_parameters)
