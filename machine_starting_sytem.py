#how to start machine 
#if power supply is available=true
#safety door is closed=true
power=True
door=True
if power and door:
    print("machine is started")
else:
    print("machine is not started")