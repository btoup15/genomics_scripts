# Script for collating the results of a BLAST genomic search
# One species may have multiple entries, so takes these, combines them, and orders them by their position in the genome

from collections import OrderedDict

in_file = "C:/Users/ben/Desktop/redpanda/seqdump.txt" #Input file
out_file = "C:/Users/ben/Desktop/redpanda/seqdump_sorted.txt" #Output file

with open(out_file, "a") as out: #Opening output file for writing
    with open(in_file) as inp: #Opening input file to read
        seqs = {} #Defining empty dictionary to add values to
        for i, line in enumerate(inp, 1): #Iterating over lines in the input file
            if line[0] == ">": #Detects start of fasta name block by searching for ">" character
                seqs[line[:-1]] = "" #Adds blank key named after name block to dictionary
                curr_name = line[:-1] #Sets the name block found as the current name
            elif line[0] != ">":
                seqs[curr_name] = seqs[curr_name] + line[:-1] #If line does not begin with ">" (indicating sequence block), adds the line to the dictionary key of the current name
    ordered_seqs = OrderedDict(sorted(seqs.items())) #Creates a new dictionary using the items of the previous dictionary ordered by key name (Effectively orders them based on genome start position)
    for key, value in ordered_seqs.items(): #For each item in the ordered dictionary, prints the value of the key to an output file
        out.write(value)