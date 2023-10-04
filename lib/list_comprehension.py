#!/usr/bin/env python3

def return_evens(sequence):
    even_numbers = [x for x in sequence if x % 2 == 0]
    return even_numbers


def make_exclamation(sentences):
    excited_sentences = [s + '!' for s in sentences]
    return excited_sentences
