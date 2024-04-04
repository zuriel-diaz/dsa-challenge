"""
Mission: You have a bowl of letters. Please write a method
that outputs how many times you would be able to spell 
"PENNYMAC" from the letters in the bowl.

If you are unable to spell it, please return 0.
"""

from collections import Counter
from typing import Union


def solution(word: str, letters: Union[list, str]) -> int:
    if len(letters) == 0:
        return 0

    letter_frequency, occurrence_number = Counter(word), 0

    for letter in letter_frequency:
        if letter in letters:
            if letter_frequency[letter] != letters.count(letter):
                return occurrence_number
        else:
            return occurrence_number

    occurrence_number += 1
    return occurrence_number
