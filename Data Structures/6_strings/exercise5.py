str = 'X-DSPAM-Confidence:0.8475'

position_colon = str.find(':')
afterColon = float(str[position_colon+1:])

print(afterColon)