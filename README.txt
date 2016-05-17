
To simulate an attack over a graph run DecayGenerator.py

DecayGenerator.py -h will display the necessary information about it.

usage: decayGenerator.py [-h] [-e] [-m metric [metric ...]] [-i INPUT]
                         [-o OUTPUT_FOLDER] [-g A A A A]

DecayGenerator calculates the decay of a graph when it is under attack. The
attack consists on removing vertices or edges with a high metric value for
some metric. Attacks by default are preformed over nodes. DecayGenerator
receives a metric list, for each metric and each graph a result is obtained
and put into an output file on csv format. Graphs might be generated or
received from the input.

optional arguments:
  -h, --help            show this help message and exit
  -e, --edge            Attack is performed over edges, therefore metrics are
                        calculated for edges. Only betweenness and miuz can be
                        used as edge metrics.
  -m metric [metric ...], --metrics metric [metric ...]
                        Set of metrics that will be used to calculate decays
                        on input graph or generated graph. Available metrics:
                            - betweenness [node edge]
                            - degree [node]
                            - harmonic [node]
                            - miuz [node edge]
                            - clustering [node]
                            - eigenvector [node]
                            - coreness [node]
  -i INPUT, --input INPUT
                        Calculations will be made over the input graph. Must
                        contain a csv file with the following format: Every
                        line must contain an edge, this edge is represented by
                        the node_a and node_b it connects as 'node_a,node_b'.
                            - For more information look at graph_example.csv

  -o OUTPUT_FOLDER, --output OUTPUT_FOLDER
                        Path to the folder where results of the calculations
                        will be stored. Defaults to current working directory.
  -g A A A A, --generate A A A A
                        Receives (N, alpha, number_of_nodes, destiny_folder)
                        to generate N power law graphs with number_of_nodes
                        nodes, coefficient alpha and saves the graph on
                        destiny_folder. Note that the results will be saved on
                        the path specified on --output. Decay calculations
                        will be made over these power law graphs.


Examples:

$ python DecayGenerator.py -i graph_example.csv -m betweenness

This will read graph_example and calculate its decay under a betweenness attack over the nodes. Results will be stored on the current location.

$ python DecayGenerator.py -i graph_example.csv -m betweenness -o decay/results/ -e

This will read graph_example and calculate its decay under a betweenness attack over the edges. Results will be saved on the folder results that is located on the folder named decay. Note that these folders must already exist.

$ python DecayGenerator.py -g 3 2.1 100 powerLaw/graphs/ -o powerLaw/results/ -m betweenness degree

This will generate 3 power law graphs with coefficient 2.1 and 100 nodes, the graphs will be saved on 'powerLaw/graphs/'.
The results of the attacks will be saved on 'powerLaw/results/'. For each type of attack, and each graph there will be a csv file with the results.