pyg = 'ay'
original_response = raw_input ("Which word would you like translated?")
word = original_response.lower()
p = word[0]
if len(p) > 0:
new_word = word + p + pyg
new_word = new_word[1:len(new_word)]

if len(original_response) > 0 and original_response.isalpha():
  print new_word
else:
  print "this isn't a word"
