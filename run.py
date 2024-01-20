import base64
from time import sleep

coded_string = 'dG9vIGVhc3k/='
decoded = base64.b64decode(coded_string)

print('=========================')
sleep(5)
print('CybSec Decoding . . .')
sleep(5)
print('Flag: ',decoded)
sleep(5)
print('Program completed.')