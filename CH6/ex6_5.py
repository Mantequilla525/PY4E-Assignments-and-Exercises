str = 'X-DSPAM-Confidence:0.8475'

pos1 = str.find(':')

afterColon = str[pos1+1:]
slice(afterColon)
float(afterColon)


print(afterColon)