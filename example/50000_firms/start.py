from __future__ import division
from myagent import MyAgent
from youragent import YourAgent
from abce import Simulation


def main():
    parameters = {
    'name': 'name',
    'rounds': 300
    }

    s = Simulation(rounds=parameters['rounds'], cores=8)
    action_list = [#(('myagent', 'youragent'), 'compute'),
                   ('youragent', 's'),
                   ('myagent', 'g')]
    s.add_action_list(action_list)

    s.build_agents(MyAgent, 'myagent', 50000)
    s.build_agents(YourAgent, 'youragent', 50000)

    s.run()

if __name__ == '__main__':
    main()
