#
#nodes: 5  max x = 1000.0, max y: 1000.0
#
#$node_(0) set X_ 0.6642883828044
#$node_(0) set Y_ 0.2309939067026
#$node_(0) set Z_ 0.0
#$node_(1) set X_ 50.6642883828044
#$node_(1) set Y_ 50.2309939067026
#$node_(1) set Z_ 0.0
#$node_(2) set X_ 100.1527892303775
#$node_(2) set Y_ 100.0017151661647
#$node_(2) set Z_ 0.0
#$node_(3) set X_ 150.3207048718017
#$node_(3) set Y_ 150.7817679768309
#$node_(3) set Z_ 0.0
#$node_(4) set X_ 200.6792971281983
#$node_(4) set Y_ 200.2182340231691
#$node_(4) set Z_ 0.0
#$time 0.0 "$node_(0) 0.00 0.00 0.00"
#$time 0.0 "$node_(1) 50.0 50.0 0.0"
#$time 0.0 "$node_(2) 100 100 0"
#$time 0.0 "$node_(3) 150 150 0"
#$time 0.0 "$node_(4) 200 200 0"
#$time 0.05 "$node_(0) 50 0 0"
#$time 0.05 "$node_(1) 100 50 0"

###############################################################


array=[]
a=int(raw_input("Enter number of UE performing file based mobility \n"))
x=float(raw_input("Enter max x value in grid length\n"))
y=float(raw_input("Enter max y value in grid length\n"))
print("Enter details for each UE \n");
for i in range(0,a):
  node=int(raw_input("Enter UE device number in scenario \n"))
  node_x=float(raw_input("Enter device initial x position\n"))
  node_y=float(raw_input("Enter device initial y position\n"))
  node_z=float(raw_input("Enter device initial z position\n"))
  array.append("$node_(%d) set X_ %.1f"%(node-1,node_x))
  array.append("$node_(%d) set Y_ %.1f"%(node-1,node_y))
  array.append("$node_(%d) set Z_ %.1f"%(node-1,node_z))
  k=node_x
  for i in range(0,501):
      if(i%5==0):
        p=i/10.0
        array.append("$time %.1f \"$node_(%d) %.1f %.1f %.1f\""%(p,node-1,k,node_y,node_z))
        k=k+50.0
      i=i+1

    
print(array)
f= open("C:\\Program Files\\NetSim Standard\\bin\\mobility.txt","w")
for line in array:
    f.writelines(line)
    f.writelines('\n')
f.close()
#<MOBILITY CALCULATION_INTERVAL="1.0" GROUP_ID="1" MODEL="FILE_BASED_MOBILITY" PAUSE_TIME="1" VELOCITY="20"/>
