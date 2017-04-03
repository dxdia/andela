import unittest
a=float(input("enter amount"))
t=float(input("enter time"))
r=12
def amtpayable(a,t,r):
	amt=(a*(r*0.01)*(t/12))+a
	return amt
print(amtpayable(a,t,r))



class test1(unittest.TestCase):
	def calculate(self):
		self.assertEqual(amtpayable(100000,12,12),(112000))
	
