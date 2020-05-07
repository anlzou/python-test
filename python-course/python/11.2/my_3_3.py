g=float(input("请输入金额："))

if(g>5000):
    print("应付金额为%.2f"%(g*0.8))
elif(g>3000):
    print("应付金额为%.2f"%(g*0.85))
elif(g>2000):
    print("应付金额为%.2f"%(g*0.9))
elif(g>1000):
    print("应付金额为%.2f"%(g*0.95))    

