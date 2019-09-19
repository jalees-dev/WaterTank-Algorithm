
import math
def trackFlow(f_in, f_out, r, H, h, t_max, t_open):      #Function with input values
    t = 0
    pi = math.pi
    Volume = []                                          #Making list for volumes
    Heights = []                                         #Making list for heights
    Times = []                                           #Making list for times
    v_old = round(pi*r**2*h,10)                          #Defining the start volume of water.
    Heights.append(h)
    Volume.append(v_old)
    Times.append(0)
     
    while t < t_max and h < H and h >= 0:                    #Make a loop for filling up the tank
                                                    
        t += 0.1
                 
                                                     
        if round(t, 2) <= t_open:                           #When out_flow is not open
            v_new = round(v_old + (f_in*(0.1)),10)           #New Volume after inflow of 0.1sec
            v_old = v_new                                    #present volume becomes new vloume for the next iteration
            h_new = round(h + ((f_in*(0.1))/(pi*r**2)),10)     #The height after the time
            h = h_new                                       #present height becomes new height for the next iteration
            Heights.append(round(h_new,2))                   #Adding heights before tank is filled
            Times.append(round(t,2))                         #Adding time-stamps
            Volume.append(round(v_new,2))                    #Adding the volume in the list Volume
            
         
        else:                                                           #Now the tap is open and there is out flow
            v_new = round(v_old + ((f_in - f_out)*(0.1)),10)            #Equation for water volume after tap is open and f_out has been taken into consideration.
            v_old = v_new
            h_new = round(h + (((f_in - f_out)*(0.1))/(pi*r**2)),10)    #Equation for water height after tap is open and f_out has been taken into consideration
            h = h_new
            if h < 0:                                                   #to eleminate error if calculating even when h < 0
                break
            Volume.append(round(v_new,2))                                   #Adding heights after the outward flow has started
            Heights.append(round(h_new,2))                                  #Adding heights after the outward flow has started
            Times.append(round(t,2))                                        #Adding time-stamps, still supposed to still add 0.1        
     
     
    print(Volume)                                 #Print list with volumes
    print(Heights)                                #Print list with heights
    print(Times)                                  #Print list with time-stamps



print("result of: trackFlow(1, 1, 1, 10, 0, 3, 1): ")
trackFlow(1, 1, 1, 10, 0, 3, 1)

print("\n")
print("result of: trackFlow(1, 5, 1, 10, 0, 5, 2): ")
trackFlow(1, 5, 1, 10, 0, 5, 2)


print("\n")
print("result of trackFlow(1, 0.5, 1, 10, 0, 3, 1): ")
trackFlow(1, 0.5, 1, 10, 0, 3, 1)


