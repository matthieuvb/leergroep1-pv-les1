def one_dna_to_rna(c):
    """Converts a single-character c from DNA nucleotide
       to complementary RNA nucleotide
    """
    if c == 'A':
        return 'U'
    elif c == 'C':
        return 'G'
    elif c== 'G':
        return 'C'
    elif c== 'T':
        return 'A'
    else:
        return ''

transcribe (s)