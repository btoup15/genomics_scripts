# Calculating pairwise tree-to-tree distances for a given dataset and writing out the results to csv

import dendropy

genes = ["ATP6","ATP8","COX1","COX2","COX3","CYTB","ND1","ND2","ND3","ND4","ND4L","ND5","ND6"]

with open("C:/Users/ben/Desktop/covarion/results/amph/partition/part_amph_95_con_tree_distances.csv", "a") as fp:
    for i in range(len(genes)-1):
        tns = dendropy.TaxonNamespace()
        in_tree = dendropy.Tree.get_from_path("C:/Users/ben/Desktop/covarion/results/amph/partition/{}/part_amph_{}_95_con.tree".format(genes[i], genes[i]), "nexus", taxon_namespace=tns)
        in_tree.encode_bipartitions()
        ls = range(i+1, len(genes))
        for j in ls:
            comp_tree = dendropy.Tree.get_from_path("C:/Users/ben/Desktop/covarion/results/amph/partition/{}/part_amph_{}_95_con.tree".format(genes[j], genes[j]), "nexus", taxon_namespace=tns)
            comp_tree.encode_bipartitions()
            distance = dendropy.calculate.treecompare.symmetric_difference(in_tree, comp_tree)    
            fp.write(str(distance))
            fp.write("\n")




