from __future__ import division
import abce


class Household(abce.Agent, abce.Household):
    def init(self, simulation_parameters, agent_parameters):
        """ self.employer is the _number_ of the agent that receives his
        labor offer.
        """
        self.create('labor_endowment', 1)
        self.set_cobb_douglas_utility_function({"consumption_good": 1})
        self.accumulated_utility = 0
        self.employer = self.id

    def sell_labor(self):
        """ offers one unit of labor to firm self.employer, for the price of 1 "money" """
        self.sell('firm', self.employer, "labor", quantity=1, price=1)

    def buy_intermediary_goods(self):
        """ recieves the offers and accepts them one by one """
        oo = self.get_offers("consumption_good")
        for offer in oo:
            self.accept(offer)

    def consumption(self):
        """ consumes_everything and logs the aggregate utility. current_utiliy
        """
        current_utiliy = self.consume_everything()
        self.accumulated_utility += current_utiliy
        self.log('HH', {'': self.accumulated_utility})
