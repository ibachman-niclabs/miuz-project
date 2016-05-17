# -*- coding: utf-8 -*-
import abc

__author__ = 'ivana'

from abc import *


class GraphAttack:
    __metaclass__ = ABCMeta

    @abc.abstractmethod
    def decide_attack(self, graph, edge_metric=False):
        return

    @abc.abstractmethod
    def get_element_to_remove(self):
        return

    @abc.abstractmethod
    def get_metric_value_element_to_remove(self):
        return
