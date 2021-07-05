import re
str1='''

Hello sir, my name is Ravi singh chaunal and my email id is ravichaunal30900@gmail.com,
And I am learning programming on code with harry youtube channel and I have one more
email:"raviji@dt.com"
and some more
email id:<rc@codewithharry.com>

email:"ravi@dt.com.in" and I have one more harrybhai@codewithharry.com.

'''
list1=re.findall(r'\w+@\S+\w',str1)

op=open("email_store.txt","a")

j=1
for i in list1:
    op.write(f"Email{j}:{i}\n")
    j=j+1
op.close()

print(f"Email's are:{list1}")
print(f"Total Email's are:{j-1}")