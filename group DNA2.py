############# select the exon from a seq
# find an exon
# store it and cut
# continue
# import the initial DNA
amino_acid_table = dict(A="alanine", C="cystine", D="aspartic acid", E="glutamic acid", F="phenylalanine", G="glycine",
                        H="histidine", I="isoleucine", K="lysine", L="leucine", M="methionine/start", N="asparagine",
                        P="proline", Q="glutamine", R="arginine", S="serine", T="threonine", V="valine", W="tryptophan",
                        Y="tyrosine", _="") # the table shows the relation between aa name and abbreviation
codon_table = dict(ATA='I', ATC='I', ATT='I', ATG='M', ACA='T', ACC='T', ACG='T', ACT='T', AAC='N', AAT='N',
                   AAA='K', AAG='K', AGC='S', AGT='S', AGA='R', AGG='R', CTA='L', CTC='L', CTG='L', CTT='L',
                   CCA='P', CCC='P', CCG='P', CCT='P', CAC='H', CAT='H', CAA='Q', CAG='Q', CGA='R', CGC='R',
                   CGG='R', CGT='R', GTA='V', GTC='V', GTG='V', GTT='V', GCA='A', GCC='A', GCG='A', GCT='A',
                   GAC='D', GAT='D', GAA='E', GAG='E', GGA='G', GGC='G', GGG='G', GGT='G', TCA='S', TCC='S',
                   TCG='S', TCT='S', TTC='F', TTT='F', TTA='L', TTG='L', TAC='Y', TAT='Y', TAA='_', TAG='_',
                   TGC='C', TGT='C', TGA='_', TGG='W',_='TGA'or'TAA'or'TAG')  # the table gives the relation between codons and aa

def w():
    S0 = input('Please type the initial DNA sequence:')
    S0=S0.upper()
    global S1
    S1=S0
    # find the position of the start codon
    global exon
    exon = []
    def g(v):
        start_codon='start_codon';end_codon='end_codon'
        p0 = v.find('ATG')  # find the position of start codon
        if p0 == -1:
            return start_codon
        else:
            global G # G: one of the exons of the initial sequence
            G = ''
            for t in range(len(v)):
                code0 = v[p0:p0 + 3]  # from the position of "ATG", read the triplets
                G+= code0
                p0 += 3
                if codon_table[code0] == '_' or p0+3>len(v):  # G is the expressed sequence of initial DNA
                    break
            if codon_table[G[len(G)-3:len(G)]]!='_':
                return end_codon
        exon.append(G)  # collect exons in a list
        return p0
    for i in range(len(S0)):
        p1=g(S0)
        if (p1=='end_codon'or p1=='start_codon') and i>0 :
            break
        elif i==0 and p1=='start_codon':
            print('\nno start codon was found in the initial DNA.')
            break
        elif i == 0 and p1 == 'end_codon':
            print('\nno end codon was found in the initial DNA.')
            break
        else:
            S0=S0[p1:]
    print('initial exons:',exon)

w()