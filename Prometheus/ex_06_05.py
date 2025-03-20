text = "X-DSPAM-Confidence:    0.8475"
specific_search = text.find('0.8475')
print(float(text[specific_search: len(text)]))
# improved version
double_dot = text.find(':')
print(float(text[double_dot+1: len(text)]))