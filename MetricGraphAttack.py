# -*- coding: utf-8 -*-
import Library

__author__ = 'ivana'
from GraphAttack import *


class MetricGraphAttack(GraphAttack):
    def __init__(self, metric):
        super(MetricGraphAttack, self).__init__()
        self.metric = metric
        self.metric_list = []
        self.dict = {}

    def decide_attack(self, graph, edge_metric=False):
        Library.set_one_metric(graph, self.metric, edge_metric)
        if edge_metric:
            lst = graph.es[self.metric]
        else:
            lst = graph.vs[self.metric]
        metric_list = Library.order_list_of_metric(lst, dict=self.dict)
        self.metric_list = metric_list

    def get_element_to_remove(self, element_id=0):
        return self.metric_list[element_id][0]

    def get_metric_value_element_to_remove(self, element_id=0):
        return self.metric_list[element_id][1]

    def get_dict_value_from_element_id(self, element_id):
        return self.dict[element_id]

    def filtered_list_of_elements(self, value):
        return [i[0] for i in self.metric_list if i[1] == value]