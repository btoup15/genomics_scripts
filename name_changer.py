# Reading in a genomic alignment and reformatting the species names to a common format
# with or without user I/O

import re
import os
import glob

#User input of current gene name
#gene = input("Enter the gene name: ")

#List of taxon names being added, as they appear in the files
new_names = ["Mellivora capensis", "Neogale vison", "Spilogale interrupta", "Spilogale gracilis", "Meles meles", "Gulo gulo", "Potos flavus", "Procyon lotor", "Martes zibellina", "Eira barbara", "Ailurus styani"]
#List of taxon names currently in the files
old_names = ["Ictidomys_tridecemlineatus", "Ailurus_styani", "Mustela_putorius", "Enhydra_lutris_kenyoni", "Ailuropoda_melanoleuca", "Mellivora_capensis", "Neogale_vison", "Spilogale_interrupta", "Spilogale_gracilis", "Meles_meles", "Gulo_gulo", "Potos_flavus", "Procyon_lotor", "Martes_zibellina", "Eira_barbara"]

#Name of the temporary file we're going to create to hold our renamed sequences
out_file = "C:/Users/ben/Downloads/temp.fasta"
#Name of the gene file we're currently looking at
in_files = "C:/Users/ben/Downloads/orig"
in_file_suffix = ".fasta"

for in_file in glob.glob(in_files + in_file_suffix):
    with open(out_file, "a") as out: #Opening the temporary output file to append to
        with open(in_file, "r") as inp: #Opening the current gene file to read 
            for i, line in enumerate(inp): #Reading our input file line by line
                if line[0] == ">": #Checking if the current line starts with ">", denoting a taxon name
                    old = False #Flag indicating whether or not the taxon name is old or new
                    for j in old_names: 
                        if re.search(j, line): #Searching for an old taxon name in the line
                            old = True #If an old taxon name is found, flips old flag to true
                    if old: #If old flag is true (taxon name is an old one), writes the line as is
                        out.write(line)
                    else: #If old flag is false (taxon name is a new one), proceeds
                        for k in new_names: #Iterating over our list of new names
                            if re.search(k, line): #If we find a match of one of the new names in the line, writes our the correct name with an underscore and a newline
                                out.write(">" + k.replace(" ", "_"))
                                out.write("\n")
                else: #If the line is not a taxon name, writes as is
                    out.write(line)

    os.replace(out_file, in_file) #Replaces the old gene file with our temporary file