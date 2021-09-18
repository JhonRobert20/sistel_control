def hammer_difference(string1: str, string2: str):
  """
  Given two strings s and t of different length, you have to find the Hamming distance between s
  and t, denoted dH(s,t). Hamming distance is the number of corresponding symbols that differ in
  s and t.
  """
  string1 = string1.upper()
  string2 = string2.upper()
  length1 = len(string1)
  length2 = len(string2)
  length = min(length1, length2)
  word_difference = abs(length1 - len(string2))
  hammer_difference = 0
  for i in range(length):
    if string1[i] != string2[i]:
      hammer_difference += 1
  hammer_difference_and_word_difference = hammer_difference  + word_difference
  result =  {"string_1": string1, "string_2": string2, "hammer_difference": hammer_difference}
  if hammer_difference_and_word_difference != hammer_difference:
    result["hammer_difference_and_word_difference"] = hammer_difference_and_word_difference
  return result

def get_dictionary_to_compare(string1: str, string2: str, hammer_difference: int, hammer_difference_and_word_difference=False):
  string1 = string1.upper()
  string2 = string2.upper()
  if hammer_difference_and_word_difference:
    return  {"string_1": string1, "string_2": string2, "hammer_difference": hammer_difference, "hammer_difference_and_word_difference": hammer_difference_and_word_difference}
  return {"string_1": string1, "string_2": string2, "hammer_difference": hammer_difference}