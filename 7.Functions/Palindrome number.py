def checkPalindrome(num):
	rev=0
	digit=0
	while(num>0):
		digit=num%10
		rev=rev*10+digit
		num=num//10
	return rev

		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome ==num):
	print('true')
else:
	print('false')
