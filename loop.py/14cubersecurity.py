print("Welcome to the CyberSecurity Mission")
ques = input("Do you want to 'track the hacker' as 'h' or 'secure the system' as 's' : ").lower()
if ques == 'h':
    choose = input("Do you want to 'track their IP' as 'i' or 'decode their message' as 'm' : ")
    if choose == 'i':
        print("You caught the hacker. You Win!")
    elif choose == 'm':
        print("The message was a trap. Game Over.")
    else:
        pass
elif ques == 's':
    choose = input("Do you want to 'shut down the server' as 'd' or 'upgrade the firewall' as 'f' : ")
    if choose == 'd':
        print("The atttack was stopped. You Win!")
    elif choose == 'f':
        print("The hacker bypassed it. Game Over.")
    else:
        pass
else:
    pass