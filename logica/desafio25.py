def hamming_distance(seq1, seq2):
        if len(seq1) != len(seq2): # VErifica se asa sequência tem o mesmo comprimento
                raise ValueError("As sequências devem ter o mesmo comprimento.")
        return sum(c1 != c2 for c1, c2 in zip(seq1, seq2)) 

seq1 = "1011101"
seq2 = "1001001"
print("Distância de hamming: ", hamming_distance(seq1, seq2))