import sys
input = sys.stdin.readline
n = int(input()) # target channel
m = int(input()) # number of broken buttons
cnt = abs(100-n) # case of pressing buttons maximum times
broken_buttons = list(map(str,input().split()))

for num in range(1000001):
    for digits in str(num): 
        if digits in broken_buttons: # if button is broken
            break
    else: # if none of the buttons are broken
        cnt = min(cnt, len(str(num)) + abs(num-n))

print(cnt)
