from __future__ import division
import abce
from tools import *


class ContractSeller(abce.Agent, abce.Contracting):
    def init(self, simulation_parameters, agent_parameters):
        self.last_round = simulation_parameters['rounds'] - 1
        if self.id == 0:
            self.create('labor_endowment', 1)

    def make_offer(self):
        if self.id == 0:
            if self.round % 10 == 0:
                self.given_contract = self.offer_good_contract('contractseller', 1,
                                                               'labor',
                                                               quantity=5,
                                                               price=10,
                                                               duration=9)

    def accept_offer(self):
        if self.id == 1:
            contracts = self.get_contract_offers('labor')
            for contract in contracts:
                self.accepted_contract = self.accept_contract(contract)

    def deliver(self):
        for contract in self.contracts_to_deliver('labor'):
            self.deliver_contract(contract)
            assert self.possession('labor') == 0

    def pay(self):
        for contract in self.contracts_to_receive('labor'):
            if self.was_delivered_this_round(contract):
                self.create('money', 50)
                self.pay_contract(contract)
                assert self.possession('money') == 0

    def control(self):
        if self.id == 0:
            assert self.was_paid_this_round(self.given_contract), self._contracts_payed
            assert self.possession('labor') == 0, (self.id, self.possession('labor'))
            assert self.possession('money') == 50, self.possession('money')
            self.destroy('money')
        else:
            assert self.was_delivered_this_round(self.accepted_contract), self.contracts_to_receive('labor')
            assert self.possession('labor') == 5, self.possession('labor')
            assert self.possession('money') == 0, self.possession('money')

    def clean_up(self):
        pass

    def all_tests_completed(self):
        if self.round == self.last_round and self.id == 0:
            print('Test make_offer         \t\t\tOK')

