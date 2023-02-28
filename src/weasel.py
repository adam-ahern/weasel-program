import random
import string

# Set the length of the string
length: int = 28
probability: float = 0.99
pool_size: int = 100


class Weasel:
    def __init__(self) -> None:
        self.current_gene: str = "".join(
            random.choices(string.ascii_uppercase, k=length)
        )
        self.alphabet: list = self.define_alphabet()
        self.current_gene_score: int = 0
        self.gene_target: str = "METHINKS IT IS LIKE A WEASEL"

    @staticmethod
    def define_alphabet() -> list:
        alphabet: list = [chr(i) for i in range(65, 91)]
        alphabet.append(chr(32))
        return alphabet

    def mutate_sequence(self, start_seq: str) -> str:
        return "".join(
            [
                self.alphabet[random.randint(0, 26)]
                if round(random.random(), 2) >= probability
                else x
                for x in list(start_seq)
            ]
        )

    def count_string_score(self, mutated_seq: str) -> int:
        score: int = 0
        for i in range(0, (length - 1)):
            if list(mutated_seq)[i] == list(self.gene_target)[i]:
                score += 1
        return score

    def create_mutated_list(self, current_sequence: str) -> list:
        return [self.mutate_sequence(current_sequence) for i in range(pool_size)]

    def choose_highest_string(self, mutations: list) -> None:
        for sequence in mutations:
            seq_score = self.count_string_score(sequence)
            if seq_score > self.current_gene_score:
                self.current_gene = sequence
                self.current_gene_score = seq_score
                print(self.current_gene, self.current_gene_score)


w: Weasel = Weasel()
count = 0
while w.current_gene_score < length:
    count += 1
    w.choose_highest_string(w.create_mutated_list(w.current_gene))

print(count)
