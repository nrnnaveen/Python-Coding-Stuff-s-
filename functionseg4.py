#set s_user=emc, s_pass=123 and get input for uname and pass from the user
#and use function validate if uname and pass match correctly use return to print correct
#else return false 

s_username="EMC"
s_password=123

uname=input("ENTER YOUR NAME:")
password=int(input("ENTER YOUR PASS:"))

def validate():
    if(uname==s_username and password==s_password):
        return("CORRECT")
    else:
        return("WRONG")

print(validate())
