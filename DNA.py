
def analyze_data_sequence(dna_sequence):
    
    nucleo_cnt = {}
    for nucleotide in dna_sequence:
        nucleo_cnt[nucleotide] = nucleo_cnt.get(nucleotide, 0) + 1
    return nucleo_cnt
        

dna_sequence = "ATGCTGAT"
result = analyze_data_sequence(dna_sequence)
print(result)
    