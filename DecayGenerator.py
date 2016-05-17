# -*- coding: utf-8 -*-
__author__ = 'ivana'
from Library import *
import argparse
import ntpath
from MetricGraphAttack import *

parser = argparse.ArgumentParser(description="DecayGenerator calculates the decay of a graph when it is under attack."
                                             " The attack consists on removing vertices or edges with a high metric "
                                             "value for some metric. Attacks by default are preformed over nodes."
                                             " DecayGenerator receives a metric list, for each "
                                             "metric and each graph a result is obtained and put into an output file on"
                                             " csv format. Graphs might be generated or received from the input.")

parser.add_argument('-e', '--edge', action="store_true",
                    help='Attack is performed over edges, therefore metrics are calculated for edges. Only betweenness'
                         ' and miuz can be used '
                         'as edge metrics.')
parser.add_argument('-m', '--metrics', metavar='metric', type=str, nargs='+',
                    help='Set of metrics that will be used to calculate decays on input graph or generated graph.\n'
                         ' Available metrics:\n'
                         '- betweenness [node edge]\n'
                         '- degree [node]\n'
                         '- harmonic [node]\n'
                         '- miuz [node edge]\n'
                         '- clustering [node]\n'
                         '- eigenvector [node]\n'
                         '- coreness [node]\n'
                         '- lcc [node edge] -')

parser.add_argument('-i', '--input', type=str, default='',
                    help='Calculations will be made over the input graph. Must contain a csv file with the following'
                         ' format: Every line must contain an edge, this edge is represented by the node_a and node_b'
                         ' '
                         'it connects as \'node_a,node_b\'.')

parser.add_argument('-o', '--output',metavar='OUTPUT_FOLDER', type=str, default='',
                    help='Path to the folder where results of the calculations will be stored. Defaults to current'
                         ' working directory.')
parser.add_argument('-g', '--generate', metavar='A', type=str, nargs=4,
                    help='Receives (N, alpha, number_of_nodes, destiny_folder) to generate N power law graphs with'
                         ' number_of_nodes nodes, coefficient alpha and saves the graph '
                         'on destiny_folder. Note that the results will be saved on the path specified on --output.'
                         ' Decay calculations will be made over these power law graphs.\n'
                    , default=[str(0), str(0), str(0), str(0)])


args = parser.parse_args()
ho,to = ntpath.split(args.output)
output_path = ho + '/'
edge = args.edge
input_path = args.input

if args.metrics is None or not Library.is_on_available_metrics(args.metrics):
    print >> sys.stderr, "--metrics received wrong input, it won't run."
else:
    if args.generate != [str(0), str(0), str(0), str(0)]:

        amount = int(args.generate[0])
        start_number = 1
        alfa = float(args.generate[1])
        alfaname = str(int(alfa * 10))
        folder_name = args.generate[3]
        number_of_nodes = int(args.generate[2])
        err = False

        if amount < 1:
            print >> sys.stderr, "The number of graphs to generate must be at least 1"
            err = True
        if alfa <= 0:
            print >> sys.stderr, "Power law coefficient must be > 0"
            err = True
        if number_of_nodes < 1:
            print >> sys.stderr, "Number of nodes must be at least 1"
            err = True
        if err:
            print >> sys.stderr, "--generate received wrong input, it won't run."
        elif not err:
            print "GENERATING POWERLAW", alfa

            for i in range(amount):

                graph_name = 'PL' + alfaname + 'v' + str(i + start_number)
                title_graph = folder_name + graph_name

                title_edge = folder_name + graph_name

                g = generate_power_law_graph(number_of_nodes, alfa, 0.01)

                write_graph(g, title_graph)
                for metric in args.metrics:
                    if edge:
                        metric_name = metric + '_edge'
                    else:
                        metric_name = metric
                    attack = MetricGraphAttack(metric)

                    write_decay_by(g, output_path + graph_name + "_", metric_name, attack, is_seq=True,
                                   edge_metric=edge)

            print "DONE! :D"

    if input_path != '':
        g = Library.generate_graph_from_file(input_path)
        for metric in args.metrics:
            head, tail = ntpath.split(input_path)
            pos = len(tail) - 4
            graph_name = tail[0:pos] + "_"
            if edge:
                metric_name = metric + '_edge'
            else:
                metric_name = metric
            attack = MetricGraphAttack(metric)
            write_decay_by(g, output_path + graph_name, metric_name, attack, is_seq=True, edge_metric=edge)
