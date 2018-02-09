import random
from math import fabs
import matplotlib.pyplot as plt
import numpy as np

Iterations = 0

#Servers
Free = 0; Busy = 1

Server_R_1      = Free;   Server_R_2    = Free;   Server_R_List         = [];      Server_R_List_Counter     = 0
Server_Beta     = Free;                           Server_Beta_List      = [];      Server_Beta_List_Counter  = 0
Server_D_1      = Free;   Server_D_2    = Free;   Server_D_List         = [];      Server_D_List_Counter     = 0
Server_Beta_II  = Free;                           Server_Beta_II_List   = [];      Server_Beta_List_Counter  = 0
Server_Ray_1    = Free;   Server_Ray_2  = Free;   Server_Ray_List       = [];      Server_Ray_List_Counter   = 0


#Time
System_Time  = 0.0

Time_R_A        = 0.0;           Time_R_A_List       = [];         Time_R_A_List_Counter = 0
Time_R_B        = 0.0;           Time_R_B_List       = [];         Time_R_B_List_Counter = 0      
Waiting_Time_R  = 0.0;           Waiting_Time_List_R = []
Queue_R_List    = []

Beta_Const = 0.1
Time_Beta_A         = 0.0;       Time_Beta_A_List       = [];      Time_Beta_A_List_Counter = 0
Time_Beta_B         = 0.0;       Time_Beta_B_List       = [];      Time_Beta_B_List_Counter = 0      
Waiting_Time_Beta   = 0.0;       Waiting_Time_List_Beta = []
Queue_Beta_List     = []

D_Const = 0.1
Time_D_A        = 0.0;           Time_D_A_List       = [];         Time_D_A_List_Counter = 0    
Time_D_B        = 0.0;           Time_D_B_List       = [];         Time_D_B_List_Counter = 0  
Waiting_Time_D  = 0.0;           Waiting_Time_List_D = []
Queue_D_List    = []

Beta_II_Const = 0.1
Time_Beta_II_A       = 0.0;      Time_Beta_II_A_List       = [];   Time_Beta_II_A_List_Counter = 0
Time_Beta_II_B       = 0.0;      Time_Beta_II_B_List       = [];   Time_Beta_II_B_List_Counter = 0      
Waiting_Time_Beta_II = 0.0;      Waiting_Time_List_Beta_II = []
Queue_Beta_II_List   = []

Ray_Const = 0.1
Time_Ray_A        = 0.0;         Time_Ray_A_List       = [];        Time_Ray_A_List_Counter = 0      
Time_Ray_B        = 0.0;         Time_Ray_B_List       = [];        Time_Ray_B_List_Counter = 0
Waiting_Time_Ray  = 0.0;         Waiting_Time_List_Ray = []
Queue_Ray_List    = []


#Event indicators
Sort = 0;

R_A         = 0;    R_B         = 1
Beta_A      = 2;    Beta_B      = 3
D_A         = 4;    D_B         = 5 
Beta_II_A   = 6;    Beta_II_B   = 7
Ray_A       = 8;    Ray_B       = 9


#====================================

def Exp_Generation():       return random.expovariate(0.1)
def Uniform_Generation():   return random.uniform(0,10.0)
def Beta_Generation():      return random.betavariate(0.5, 0.5) 
def Distr_Generation():     return 1 
def Ray_Generation():       return random.uniform(0,10.0)


def Random_Generation():
    if  (Sort == R_A       or Sort == R_B):       rand = Uniform_Generation(); print("     Uniform_Generation() = %f"%rand)
    elif(Sort == D_A       or Sort == D_B):       rand = Distr_Generation();   print("     Distr_Generation() = %f"%rand)
    elif(Sort == Ray_A     or Sort == Ray_B):     rand = Ray_Generation();     print("     Ray_Generation() = %f"%rand)
    elif(Sort == Beta_A    or Sort == Beta_B 
      or Sort == Beta_II_A or Sort == Beta_II_B): rand = Ray_Generation();     print("     Beta_Generation() = %f"%rand)

    return rand

def Start():
    global  Sort, R_A,\
            System_Time,\
            Time_R_A, Time_R_A_List, Time_R_A_List_Counter,\
            Main_List

    Time_R_A = Exp_Generation()
    Time_R_A_List.append(Time_R_A)
    System_Time = Time_R_A
    print("System_Time = %f"%(System_Time))
    Sort = R_A
#====================================

def Two_Servers_A_event():
    global  System_Time,\
            Time_Beta_A,    Time_Beta_A_List,       Time_Beta_A_List_Counter,\
            Time_Beta_B,    Time_Beta_B_List,       Time_Beta_B_List_Counter,\
            Time_Beta_II_A, Time_Beta_II_A_List,    Time_Beta_II_A_List_Counter,\
            Time_Beta_II_B, Time_Beta_II_B_List,    Time_Beta_II_B_List_Counter,\
            Time_D_A,       Time_D_A_List,          Time_D_A_List_Counter,\
            Time_D_B,       Time_D_B_List,          Time_D_B_List_Counter,\
            Time_R_A,       Time_R_A_List,          Time_R_A_List_Counter, \
            Time_R_B,       Time_R_B_List,          Time_R_B_List_Counter,\
            Time_Ray_A,     Time_Ray_A_List,        Time_Ray_A_List_Counter, \
            Time_Ray_B,     Time_Ray_B_List,        Time_Ray_B_List_Counter,\
            \
            Beta_Const, Beta_II_Const, D_Const, Ray_Const,\
            \
            Waiting_Time_D,         Waiting_Time_List_D,\
            Waiting_Time_R,         Waiting_Time_List_R,\
            Waiting_Time_Ray,       Waiting_Time_List_Ray,\
            Waiting_Time_Beta,      Waiting_Time_List_Beta,\
            Waiting_Time_Beta_II,   Waiting_Time_List_Beta_II,\
            \
            Queue_D_List,\
            Queue_R_List,\
            Queue_Ray_List,\
            Queue_Beta_List,\
            Queue_Beta_II_List,\
            \
            Server_Beta,    Server_Beta_List,\
            Server_Beta_II, Server_Beta_II_List,\
            Server_D_1,     Server_D_2,     Server_D_List,\
            Server_R_1,     Server_R_2,     Server_R_List,\
            Server_Ray_1,   Server_Ray_2,   Server_Ray_List
            
    if (Sort == R_A):
        print("R_A_event\n")

        Server_1            = Server_R_1
        Server_2            = Server_R_2
        Server_List         = Server_R_List

        Time_1_A            = Time_R_A
        Time_1_B            = Time_R_B
        Time_1_A_List       = Time_R_A_List
        Time_1_B_List       = Time_R_B_List

        Const               = Beta_Const
        Time_2_A            = Time_Beta_A
        Time_2_A_List       = Time_Beta_A_List

        Queue_List          = Queue_R_List
        Waiting_Time_List   = Waiting_Time_List_R

    elif(Sort == D_A):
        print("D_A_event\n")

        Server_1            = Server_D_1
        Server_2            = Server_D_2
        Server_List         = Server_D_List

        Time_1_A            = Time_D_A
        Time_1_B            = Time_D_B
        Time_1_A_List       = Time_D_A_List
        Time_1_B_List       = Time_D_B_List

        Const               = Beta_II_Const
        Time_2_A            = Time_Beta_II_A
        Time_2_A_List       = Time_Beta_II_A_List

        Queue_List          = Queue_D_List
        Waiting_Time_List   = Waiting_Time_List_D

    elif(Sort == Ray_A):
        print("Ray_A_event\n")

        Server_1            = Server_Ray_1
        Server_2            = Server_Ray_2
        Server_List         = Server_Ray_List

        Time_1_A            = Time_Ray_A
        Time_1_B            = Time_Ray_B
        Time_1_A_List       = Time_Ray_A_List
        Time_1_B_List       = Time_Ray_B_List

        Queue_List          = Queue_Ray_List
        Waiting_Time_List   = Waiting_Time_List_Ray
#=============================

    if  (Server_1 == Busy and Server_2 == Busy):
        print("     Server_1 = Busy\n     Server_2 = Busy")
        Queue_List.append(System_Time)
        print("     len(Queue_List) + 1=> %i"%len(Queue_List))   
    else:
        if  (Server_1 == Free and Server_2 == Free):
            print("     Server_1 = 0\n     Server_2 = 0")
            Server_1 = Busy
            Server_List.append(0)

            if   len(Time_1_B_List) == 0: Time_1_B = Time_1_A + Random_Generation()
            elif len(Time_1_B_List)  > 0: 
                 while Time_1_B <= System_Time:
                       if Time_1_B <= System_Time: Time_1_B = Time_1_B + Random_Generation()#max(Time_1_B_List)
                       else: break
        else:
            if  (Server_1 == Busy and Server_2 == Free):
                print("     Server_1 = 1\n     Server_2 = 0")
                Server_2 = Busy
                Server_List.append(1)
            elif (Server_1 == Free and Server_2 == Busy):
                print("     Server_1 = 0\n     Server_2 = 1")
                Server_1 = Busy
                Server_List.append(0)
            
            while Time_1_B <= System_Time:
                  if Time_1_B <= System_Time: Time_1_B = Time_1_B + Random_Generation()
                  else: break

        Time_1_B_List.append(Time_1_B)
        print("     Time_1_B = %f"%(Time_1_B))
        Waiting_Time_List.append(0)     
 

    if (Sort == R_A):
        while Time_R_A <= System_Time:
            Time_R_A = Time_R_A + Random_Generation()

        Time_R_A_List.append(Time_R_A)
        print("     Time_R_A = %f"%(Time_R_A))

#=============================
    if (Sort == R_A):

        Server_R_1          = Server_1
        Server_R_2          = Server_2
        Server_R_List       = Server_List

        Time_R_A            = Time_1_A
        Time_R_B            = Time_1_B   
        Time_R_A_List       = Time_1_A_List
        Time_R_B_List       = Time_1_B_List

        Const               = Beta_Const
        Time_Beta_A         = Time_2_A
        Time_Beta_A_List    = Time_2_A_List
        
        Queue_R_List        = Queue_List
        Waiting_Time_List_R = Waiting_Time_List

    elif(Sort == D_A):

        Server_D_1          = Server_1
        Server_D_2          = Server_2
        Server_D_List       = Server_List

        Time_D_A            = Time_1_A
        Time_D_B            = Time_1_B   
        Time_D_A_List       = Time_1_A_List
        Time_D_B_List       = Time_1_B_List

        Const               = Beta_Const
        Time_Beta_II_A      = Time_2_A
        Time_Beta_II_A_List = Time_2_A_List

        Queue_D_List        = Queue_List
        Waiting_Time_List_D = Waiting_Time_List

    elif(Sort == Ray_A):

        Server_Ray_1          = Server_1
        Server_Ray_2          = Server_2
        Server_Ray_List       = Server_List

        Time_Ray_A            = Time_1_A
        Time_Ray_A_List       = Time_1_A_List

        Time_Ray_B           = Time_1_B
        Time_Ray_B_List      = Time_1_B_List

        Queue_Ray_List        = Queue_List
        Waiting_Time_List_Ray = Waiting_Time_List


def Two_Servers_B_event():

    global  Iterations,\
            Kostil,\
            System_Time,\
            Time_Beta_A,    Time_Beta_A_List,       Time_Beta_A_List_Counter,\
            Time_Beta_B,    Time_Beta_B_List,       Time_Beta_B_List_Counter,\
            Time_Beta_II_A, Time_Beta_II_A_List,    Time_Beta_II_A_List_Counter,\
            Time_Beta_II_B, Time_Beta_II_B_List,    Time_Beta_II_B_List_Counter,\
            Time_D_A,       Time_D_A_List,          Time_D_A_List_Counter,\
            Time_D_B,       Time_D_B_List,          Time_D_B_List_Counter,\
            Time_R_A,       Time_R_A_List,          Time_R_A_List_Counter, \
            Time_R_B,       Time_R_B_List,          Time_R_B_List_Counter,\
            Time_Ray_A,     Time_Ray_A_List,        Time_Ray_A_List_Counter, \
            Time_Ray_B,     Time_Ray_B_List,        Time_Ray_B_List_Counter,\
            \
            Waiting_Time_D,         Waiting_Time_List_D,\
            Waiting_Time_R,         Waiting_Time_List_R,\
            Waiting_Time_Ray,       Waiting_Time_List_Ray,\
            Waiting_Time_Beta,      Waiting_Time_List_Beta,\
            Waiting_Time_Beta_II,   Waiting_Time_List_Beta_II,\
            \
            Queue_D_List,\
            Queue_R_List,\
            Queue_Ray_List,\
            Queue_Beta_List,\
            Queue_Beta_II_List,\
            \
            Server_Beta,    Server_Beta_List,\
            Server_Beta_II, Server_Beta_II_List,\
            Server_D_1,     Server_D_2,     Server_D_List,      Server_D_List_Counter,\
            Server_R_1,     Server_R_2,     Server_R_List,      Server_R_List_Counter,\
            Server_Ray_1,   Server_Ray_2,   Server_Ray_List,    Server_Ray_List_Counter
            

    if (Sort == R_B):
        print("R_B_event\n")

        Server_1                = Server_R_1
        Server_2                = Server_R_2
        Server_List             = Server_R_List
        Server_List_Counter     = Server_R_List_Counter

        Time_1_A                = Time_R_A
        Time_1_B                = Time_R_B
        Time_1_A_List           = Time_R_A_List
        Time_1_B_List           = Time_R_B_List
        Time_1_B_List_Counter   = Time_R_B_List_Counter

        Const                   = Beta_Const
        Time_2_A                = Time_Beta_A
        Time_2_A_List           = Time_Beta_A_List
        Time_2_A_List_Counter   = Time_Beta_A_List_Counter

        Queue_List              = Queue_R_List
        Waiting_Time            = Waiting_Time_R
        Waiting_Time_List       = Waiting_Time_List_R

    elif(Sort == D_B):
        print("D_B_event\n")

        Server_1                = Server_D_1
        Server_2                = Server_D_2
        Server_List             = Server_D_List
        Server_List_Counter     = Server_D_List_Counter

        Time_1_A                = Time_D_A
        Time_1_B                = Time_D_B
        Time_1_A_List           = Time_D_A_List
        Time_1_B_List           = Time_D_B_List
        Time_1_B_List_Counter   = Time_D_B_List_Counter

        Const                   = Beta_II_Const
        Time_2_A                = Time_Beta_II_A
        Time_2_A_List           = Time_Beta_II_A_List
        Time_2_A_List_Counter   = Time_Beta_II_A_List_Counter

        Queue_List              = Queue_D_List
        Waiting_Time            = Waiting_Time_D
        Waiting_Time_List       = Waiting_Time_List_D

    elif(Sort == Ray_B):
        print("Ray_B_event\n")

        Server_1                = Server_Ray_1
        Server_2                = Server_Ray_2
        Server_List             = Server_Ray_List
        Server_List_Counter     = Server_Ray_List_Counter

        Time_1_A                = Time_Ray_A
        Time_1_B                = Time_Ray_B
        Time_1_A_List           = Time_Ray_A_List
        Time_1_B_List           = Time_Ray_B_List
        Time_1_B_List_Counter   = Time_Ray_B_List_Counter

        Queue_List              = Queue_Ray_List
        Waiting_Time            = Waiting_Time_Ray
        Waiting_Time_List       = Waiting_Time_List_Ray
#=============================

    if      Server_List[Server_List_Counter] == 0: Server_1 = Free
    elif    Server_List[Server_List_Counter] == 1: Server_2 = Free
    Server_List_Counter += 1

    if not Queue_List:
        print("     Очередь пуста")

        if  (Server_1 == Server_2 == Free and Sort == R_B): 
            Time_1_A = Time_1_A + Random_Generation()

    else:
        print("     Очередь не пуста")

        Waiting_Time = System_Time - Queue_List[0]
        print("     %f = %f - %f"%(Waiting_Time, System_Time, Queue_List[0]))
        print("     Waitin_R = Sys_Time - Queue[0]")
        Waiting_Time_List.append(Waiting_Time)
        Queue_List.pop(0)
        print("     len(Queue_List) - 1 => %i"%len(Queue_List))

        while Time_1_B <= System_Time:
              if Time_1_B <= System_Time: Time_1_B = Time_1_B + Random_Generation()
              else: break

        Time_1_B_List.append(Time_1_B)
        print("     Time_1_B = %f"%(Time_1_B))
        

        if ((Server_1 == Server_2 == Free) or (Server_1 == Free and Server_2 == Busy)):
            Server_1 = Busy
            Server_List.append(0)
        elif(Server_1 == Busy and Server_2 == Free):
            Server_2 = Busy
            Server_List.append(1)

    if (Sort != Ray_B):
        Time_2_A = Time_1_B + Const
        Time_2_A_List.append(Time_2_A)
        print("     Time_2_A = %f"%(Time_2_A))

#=============================
    if (Sort == R_B):

        Server_R_1            = Server_1
        Server_R_2            = Server_2
        Server_R_List         = Server_List
        Server_R_List_Counter = Server_List_Counter

        Time_R_A            = Time_1_A
        Time_R_B            = Time_1_B   
        Time_R_A_List       = Time_1_A_List
        Time_R_B_List       = Time_1_B_List

        Time_Beta_A         = Time_2_A
        Time_Beta_A_List    = Time_2_A_List

        Queue_R_List        = Queue_List
        Waiting_Time_R      = Waiting_Time
        Waiting_Time_List_R = Waiting_Time_List

    elif(Sort == D_B):

        Server_D_1            = Server_1
        Server_D_2            = Server_2
        Server_D_List         = Server_List
        Server_D_List_Counter = Server_List_Counter

        Time_D_A              = Time_1_A
        Time_D_B              = Time_1_B   
        Time_D_A_List         = Time_1_A_List
        Time_D_B_List         = Time_1_B_List

        Time_Beta_II_A        = Time_2_A
        Time_Beta_II_A_List   = Time_2_A_List

        Queue_D_List          = Queue_List
        Waiting_Time_D        = Waiting_Time
        Waiting_Time_List_D   = Waiting_Time_List

    elif(Sort == Ray_B):

        Server_Ray_1            = Server_1
        Server_Ray_2            = Server_2
        Server_Ray_List         = Server_List
        Server_Ray_List_Counter = Server_List_Counter

        Time_Ray_A              = Time_1_A
        Time_Ray_B              = Time_1_B   
        Time_Ray_A_List         = Time_1_A_List
        Time_Ray_B_List         = Time_1_B_List

        Queue_Ray_List          = Queue_List
        Waiting_Time_Ray        = Waiting_Time
        Waiting_Time_List_Ray   = Waiting_Time_List

#------------------------

def One_Server_A_event():
    global  Iterations,\
            Kostil,\
            System_Time,\
            Time_Beta_A,    Time_Beta_A_List,       Time_Beta_A_List_Counter,\
            Time_Beta_B,    Time_Beta_B_List,       Time_Beta_B_List_Counter,\
            Time_Beta_II_A, Time_Beta_II_A_List,    Time_Beta_II_A_List_Counter,\
            Time_Beta_II_B, Time_Beta_II_B_List,    Time_Beta_II_B_List_Counter,\
            Time_D_A,       Time_D_A_List,          Time_D_A_List_Counter,\
            Time_D_B,       Time_D_B_List,          Time_D_B_List_Counter,\
            Time_R_A,       Time_R_A_List,          Time_R_A_List_Counter, \
            Time_R_B,       Time_R_B_List,          Time_R_B_List_Counter,\
            Time_Ray_A,     Time_Ray_A_List,        Time_Ray_A_List_Counter, \
            Time_Ray_B,     Time_Ray_B_List,        Time_Ray_B_List_Counter,\
            \
            Waiting_Time_D,         Waiting_Time_List_D,\
            Waiting_Time_R,         Waiting_Time_List_R,\
            Waiting_Time_Ray,       Waiting_Time_List_Ray,\
            Waiting_Time_Beta,      Waiting_Time_List_Beta,\
            Waiting_Time_Beta_II,   Waiting_Time_List_Beta_II,\
            \
            Queue_D_List,\
            Queue_R_List,\
            Queue_Ray_List,\
            Queue_Beta_List,\
            Queue_Beta_II_List,\
            \
            Server_Beta,    Server_Beta_List,\
            Server_Beta_II, Server_Beta_II_List,\
            Server_D_1,     Server_D_2,     Server_D_List,      Server_D_List_Counter,\
            Server_R_1,     Server_R_2,     Server_R_List,      Server_R_List_Counter,\
            Server_Ray_1,   Server_Ray_2,   Server_Ray_List,    Server_Ray_List_Counter

    if (Sort == Beta_A):
        print("Beta_A_event\n")

        Server              = Server_Beta

        Time_1_A            = Time_Beta_A
        Time_1_B            = Time_Beta_B
        Time_1_A_List       = Time_Beta_A_List
        Time_1_B_List       = Time_Beta_B_List

        Const               = D_Const
        Time_2_A            = Time_D_A
        Time_2_A_List       = Time_D_A_List


        Queue_List          = Queue_Beta_List
        Waiting_Time        = Waiting_Time_Beta
        Waiting_Time_List   = Waiting_Time_List_Beta

    elif (Sort == Beta_II_A):
        print("Beta_II_A_event\n")

        Server            = Server_Beta_II

        Time_1_A            = Time_Beta_II_A
        Time_1_B            = Time_Beta_II_B
        Time_1_A_List       = Time_Beta_II_A_List
        Time_1_B_List       = Time_Beta_II_B_List

        Const               = Ray_Const
        Time_2_A            = Time_Ray_A
        Time_2_A_List       = Time_Ray_A_List

        Queue_List          = Queue_Beta_II_List
        Waiting_Time        = Waiting_Time_Beta_II
        Waiting_Time_List   = Waiting_Time_List_Beta_II
#=============================

    if  (Server == Free):
        print("     Server = Free")
        Server = Busy

        if   len(Time_1_B_List) == 0:  Time_1_B = Time_1_A + Random_Generation()
        elif len(Time_1_B_List)  > 0:  
             while Time_1_B <= System_Time:
                if Time_1_B <= System_Time: Time_1_B = Time_1_B + Random_Generation()
                else: break

        Time_1_B_List.append(Time_1_B)     
        print("     Time_1_B = %f"%(Time_1_B))
        Waiting_Time_List.append(0) 

    elif(Server == Busy):
         print("     Server = Busy")
         Queue_List.append(System_Time)
         print("     len(Queue_List) + 1=> %i"%len(Queue_List))

#=============================
    if (Sort == Beta_A):

        Server_Beta                 = Server

        Time_Beta_A                 = Time_1_A
        Time_Beta_B                 = Time_1_B
        Time_Beta_A_List            = Time_1_A_List
        Time_Beta_B_List            = Time_1_B_List

        Time_D_A                    = Time_2_A
        Time_D_A_List               = Time_2_A_List

        Queue_Beta_List             = Queue_List
        Waiting_Time_Beta           = Waiting_Time
        Waiting_Time_List_Beta      = Waiting_Time_List

    elif (Sort == Beta_II_A):

        Server_Beta_II              = Server

        Time_Beta_II_A              = Time_1_A
        Time_Beta_II_B              = Time_1_B
        Time_Beta_II_A_List         = Time_1_A_List
        Time_Beta_II_B_List         = Time_1_B_List

        Time_Ray_A                  = Time_2_A
        Time_Ray_A_List             = Time_2_A_List

        Queue_Beta_II_List          = Queue_List
        Waiting_Time_Beta_II        = Waiting_Time
        Waiting_Time_List_Beta_II   = Waiting_Time_List

def One_Server_B_event():
    global  Iterations,\
            Kostil,\
            System_Time,\
            Time_Beta_A,    Time_Beta_A_List,       Time_Beta_A_List_Counter,\
            Time_Beta_B,    Time_Beta_B_List,       Time_Beta_B_List_Counter,\
            Time_Beta_II_A, Time_Beta_II_A_List,    Time_Beta_II_A_List_Counter,\
            Time_Beta_II_B, Time_Beta_II_B_List,    Time_Beta_II_B_List_Counter,\
            Time_D_A,       Time_D_A_List,          Time_D_A_List_Counter,\
            Time_D_B,       Time_D_B_List,          Time_D_B_List_Counter,\
            Time_R_A,       Time_R_A_List,          Time_R_A_List_Counter, \
            Time_R_B,       Time_R_B_List,          Time_R_B_List_Counter,\
            Time_Ray_A,     Time_Ray_A_List,        Time_Ray_A_List_Counter, \
            Time_Ray_B,     Time_Ray_B_List,        Time_Ray_B_List_Counter,\
            \
            Waiting_Time_D,         Waiting_Time_List_D,\
            Waiting_Time_R,         Waiting_Time_List_R,\
            Waiting_Time_Ray,       Waiting_Time_List_Ray,\
            Waiting_Time_Beta,      Waiting_Time_List_Beta,\
            Waiting_Time_Beta_II,   Waiting_Time_List_Beta_II,\
            \
            Queue_D_List,\
            Queue_R_List,\
            Queue_Ray_List,\
            Queue_Beta_List,\
            Queue_Beta_II_List,\
            \
            Server_Beta,    Server_Beta_List,\
            Server_Beta_II, Server_Beta_II_List,\
            Server_D_1,     Server_D_2,     Server_D_List,      Server_D_List_Counter,\
            Server_R_1,     Server_R_2,     Server_R_List,      Server_R_List_Counter,\
            Server_Ray_1,   Server_Ray_2,   Server_Ray_List,    Server_Ray_List_Counter

    if (Sort == Beta_B):
        print("Beta_B_event\n")

        Server            = Server_Beta#

        Time_1_A            = Time_Beta_A#
        Time_1_B            = Time_Beta_B#
        Time_1_B_List       = Time_Beta_B_List#

        Const               = D_Const
        Time_2_A            = Time_D_A
        Time_2_A_List       = Time_D_A_List

        Queue_List          = Queue_Beta_List#
        Waiting_Time        = Waiting_Time_Beta#
        Waiting_Time_List   = Waiting_Time_List_Beta

    elif (Sort == Beta_II_B):
        print("Beta_II_B_event\n")

        Server              = Server_Beta_II

        Time_1_A              = Time_Beta_II_A
        Time_1_B              = Time_Beta_II_B
        Time_1_B_List         = Time_Beta_II_B_List

        Const               = Ray_Const
        Time_2_A            = Time_Ray_A
        Time_2_A_List       = Time_Ray_A_List

        Queue_List          = Queue_Beta_II_List
        Waiting_Time        = Waiting_Time_Beta_II
        Waiting_Time_List   = Waiting_Time_List_Beta_II
#=============================
    Server = Free

    if not Queue_List:
       print("     Очередь пуста")
       Time_1_B = 0

    else:
        print("     Очередь не пуста")

        Waiting_Time = System_Time - Queue_List[0]
        print("     %f = %f - %f"%(Waiting_Time,System_Time, Queue_List[0]))
        print("     Wait_Beta = Sys_Time - Que_Beta[0]")
        Waiting_Time_List.append(Waiting_Time)
        Queue_List.pop(0)
        print("     len(Queue_List) - 1 => %i"%len(Queue_List))

        while Time_1_B <= System_Time:
           if Time_1_B <= System_Time:
                Time_1_B = Time_1_B + Random_Generation()
                print("     Time_1_B = %f"%Time_1_B)
           else: break



        Time_1_B_List.append(Time_1_B)
        print("     Time_1_B = %f"%(Time_1_B))

    Time_2_A = System_Time + Const
    Time_2_A_List.append(Time_2_A)
    print("     Time_2_A = %f"%(Time_2_A))


#=============================

    if (Sort == Beta_B):

        Server_Beta            = Server

        Time_Beta_A            = Time_1_A
        Time_Beta_B            = Time_1_B
        Time_Beta_B_List       = Time_1_B_List

        Time_D_A               = Time_2_A
        Time_D_A_List          = Time_2_A_List

        Queue_Beta_List        = Queue_List
        Waiting_Time_Beta      = Waiting_Time
        Waiting_Time_List_Beta = Waiting_Time_List

    elif (Sort == Beta_II_B):

        Server_Beta_II              = Server

        Time_Beta_II_A              = Time_1_A
        Time_Beta_II_B              = Time_1_B
        Time_Beta_II_B_List         = Time_1_B_List

        Time_Ray_A                  = Time_2_A
        Time_Ray_A_List             = Time_2_A_List

        Queue_Beta_II_List          = Queue_List
        Waiting_Time_Beta_II        = Waiting_Time
        Waiting_Time_List_Beta_II   = Waiting_Time_List

#====================================
def Table():
    print("\n     Time_R_A   S   Time_R_B   C   Waitin_R   T_Beta_A   T_Beta_B   C   Wai_Beta   Time_D_A   S   Time_D_B   C   Waitin_D   T_Bet2_A   T_Bet2_B   C   Wai_Bet2   Ti_Ray_A   S   Ti_Ray_B   C   Wait_Ray")  

    for n in range(0, len(Time_R_A_List)):
        print ("#%i"%n, end = "   ")

        print ("%f"%Time_R_A_List[n], end = "   ")

        if n < len(Server_R_List): print ("%i"%Server_R_List[n], end = "   ")
        else: print (" ", end = "   ")

        if n < len(Time_R_B_List): print ("%f"%Time_R_B_List[n], end = "   ")
        else: print ("        ", end = "   ")

        if n < Time_R_B_List_Counter : print ("#", end = "   ")
        else: print (" ", end = "   ")

        if n < len(Waiting_Time_List_R): print ("%f"%(Waiting_Time_List_R[n]), end = "   ")
        else: print ("        ", end = "   ")

        #==============================

        if n < len(Time_Beta_A_List): print ("%f"%Time_Beta_A_List[n], end = "   ")
        else: print ("        ", end = "   ")

        if n < len(Time_Beta_B_List): print ("%f"%Time_Beta_B_List[n], end = "   ")
        else: print ("        ", end = "   ")

        if n < Time_Beta_B_List_Counter: print ("#", end = "   ")
        else: print (" ", end = "   ")
   
        if n < len(Waiting_Time_List_Beta): print ("%f"%(Waiting_Time_List_Beta[n]), end = "   ")
        else: print ("        ", end = "   ")

        #==============================

        if n < len(Time_D_A_List): print ("%f"%Time_D_A_List[n], end = "   ")
        else: print ("        ", end = "   ")

        if n < len(Server_D_List): print ("%i"%Server_D_List[n], end = "   ")
        else: print (" ", end = "   ")

        if n < len(Time_D_B_List): print ("%f"%Time_D_B_List[n], end = "   ")
        else: print ("        ", end = "   ")

        if n < Time_D_B_List_Counter: print ("#", end = "   ")
        else: print (" ", end = "   ")

        if n < len(Waiting_Time_List_D): print ("%f"%(Waiting_Time_List_D[n]), end = "   ")
        else: print ("        ", end = "   ")

        #==============================

        if n < len(Time_Beta_II_A_List): print ("%f"%Time_Beta_II_A_List[n], end = "   ")
        else: print ("        ", end = "   ")

        if n < len(Time_Beta_II_B_List): print ("%f"%Time_Beta_II_B_List[n], end = "   ")
        else: print ("        ", end = "   ")

        if n < Time_Beta_II_B_List_Counter: print ("#", end = "   ")
        else: print (" ", end = "   ")
   
        if n < len(Waiting_Time_List_Beta_II): print ("%f"%(Waiting_Time_List_Beta_II[n]), end = "   ")
        else: print ("        ", end = "   ")

        #==============================

        if n < len(Time_Ray_A_List): print ("%f"%Time_Ray_A_List[n], end = "   ")
        else: print ("        ", end = "   ")

        if n < len(Server_Ray_List): print ("%i"%Server_Ray_List[n], end = "   ")
        else: print (" ", end = "   ")

        if n < len(Time_Ray_B_List): print ("%f"%Time_Ray_B_List[n], end = "   ")
        else: print ("        ", end = "   ")

        if n < Time_Ray_B_List_Counter: print ("#", end = "   ")
        else: print (" ", end = "   ")

        if n < len(Waiting_Time_List_Ray): print ("%f"%(Waiting_Time_List_Ray[n]), end = "   ")
        else: print ("        ", end = "   ")

        print ("")

def Finish():
    global  Sort,  Iterations,   Kostil,\
            \
            System_Time,\
            Time_Beta_A,    Time_Beta_A_List,       Time_Beta_A_List_Counter,\
            Time_Beta_B,    Time_Beta_B_List,       Time_Beta_B_List_Counter,\
            Time_Beta_II_A, Time_Beta_II_A_List,    Time_Beta_II_A_List_Counter,\
            Time_Beta_II_B, Time_Beta_II_B_List,    Time_Beta_II_B_List_Counter,\
            Time_D_A,       Time_D_A_List,          Time_D_A_List_Counter,\
            Time_D_B,       Time_D_B_List,          Time_D_B_List_Counter,\
            Time_R_A,       Time_R_A_List,          Time_R_A_List_Counter, \
            Time_R_B,       Time_R_B_List,          Time_R_B_List_Counter,\
            Time_Ray_A,     Time_Ray_A_List,        Time_Ray_A_List_Counter, \
            Time_Ray_B,     Time_Ray_B_List,        Time_Ray_B_List_Counter,\
            \
            Waiting_Time_D,         Waiting_Time_List_D,\
            Waiting_Time_R,         Waiting_Time_List_R,\
            Waiting_Time_Ray,       Waiting_Time_List_Ray,\
            Waiting_Time_Beta,      Waiting_Time_List_Beta,\
            Waiting_Time_Beta_II,   Waiting_Time_List_Beta_II,\
            \
            Queue_D_List,\
            Queue_R_List,\
            Queue_Ray_List,\
            Queue_Beta_List,\
            Queue_Beta_II_List,\
            \
            Server_Beta,    Server_Beta_List,\
            Server_Beta_II, Server_Beta_II_List,\
            Server_D_1,     Server_D_2,     Server_D_List,      Server_D_List_Counter,\
            Server_R_1,     Server_R_2,     Server_R_List,      Server_R_List_Counter,\
            Server_Ray_1,   Server_Ray_2,   Server_Ray_List,    Server_Ray_List_Counter
    
#===================================

    Table()
    
    #====================================
    print("\n")
    '''
    Time_printing_list_Lists    = [ Time_R_A_List[Time_R_A_List_Counter], Time_R_B_List[Time_R_B_List_Counter], Time_Beta_A_List[Time_Beta_A_List_Counter], Time_Beta_B_List[Time_Beta_B_List_Counter], Time_D_A_List[Time_D_A_List_Counter], Time_D_B_List[Time_D_B_List_Counter], Time_Beta_II_A_List[Time_Beta_II_A_List_Counter], Time_Beta_II_A_List[Time_Beta_II_A_List_Counter], Time_Ray_A_List[Time_Ray_A_List_Counter], Time_Ray_B_List[Time_Ray_B_List_Counter] ]
    Time_printing_list_J_Lists  = [ Time_R_A_List,                        Time_R_B_List,                        Time_Beta_A_List,                           Time_Beta_B_List,                           Time_D_A_List,                        Time_D_B_List,                        Time_Beta_II_A_List,                              Time_Beta_II_A_List,                              Time_Ray_A_List,                          Time_Ray_B_List ]        
    Time_printing_list_Counters = [ Time_R_A_List_Counter,                Time_R_B_List_Counter,                Time_Beta_A_List_Counter,                   Time_Beta_B_List_Counter,                   Time_D_A_List_Counter,                Time_D_B_List_Counter,                Time_Beta_II_A_List_Counter,                      Time_Beta_II_A_List_Counter,                      Time_Ray_A_List_Counter,                  Time_Ray_B_List_Counter ]
    Comparing_List              = [ El_R_A,                               El_R_B,                               El_Beta_A,                                  El_Beta_B,                                  El_D_A,                               El_D_B,                               El_Beta_II_A,                                     El_Beta_II_B,                                     El_Ray_A,                                 El_Ray_B] 
 

    for Time_printing in range(0,10):             
        while Time_printing_list_Lists[n] <= System_Time + 1:
           if Time_printing_list_Lists[n] <= System_Time:
              if Time_R_A_List_Counter < (len(Time_printing_list_J_Lists[n]) - 1):
                 Time_R_A_List_Counter += 1
              else: 
                   Compaing_List[n] = 0
                   break    
           else:
               Compaing_List[n] = Time_printing_list_Lists[n]
               break
    ''' 


    for n in range (1, 3):
        if Time_R_A_List[Time_R_A_List_Counter] <= System_Time: 
            if Time_R_A_List_Counter < (len(Time_R_A_List) - 1):
                Time_R_A_List_Counter += 1
                n -= 1
            else: 
                El_R_A = 0
                break         
        else: 
            El_R_A = Time_R_A_List[Time_R_A_List_Counter]
            break
    print ("      Time_R_A = %f" % El_R_A)

    for n in range (1, 3):
        if Time_R_B_List[Time_R_B_List_Counter] <= System_Time: 
            if Time_R_B_List_Counter < (len(Time_R_B_List) - 1):
                Time_R_B_List_Counter += 1
                n -= 1
            else: 
                El_R_B = 0       
                break  
        else: 
            El_R_B = Time_R_B_List[Time_R_B_List_Counter]
            break
    print ("      Time_R_B = %f" % El_R_B)

    if len(Time_Beta_A_List) > 0: 
       for n in range (1, 3):
            if Time_Beta_A_List[Time_Beta_A_List_Counter] <= System_Time: 
                if Time_Beta_A_List_Counter < (len(Time_Beta_A_List) - 1):
                    Time_Beta_A_List_Counter += 1
                    n -= 1
                else: 
                    El_Beta_A  = 0
                    break         
            else: 
                El_Beta_A = Time_Beta_A_List[Time_Beta_A_List_Counter]
                break
    else:  El_Beta_A = 0
    print ("   Time_Beta_A = %f" % El_Beta_A)

    if len(Time_Beta_B_List) > 0: 
       for n in range (1, 3):
            if Time_Beta_B_List[Time_Beta_B_List_Counter] <= System_Time: 
                if Time_Beta_B_List_Counter < (len(Time_Beta_B_List) - 1):
                    Time_Beta_B_List_Counter += 1
                    n -= 1
                elif Time_Beta_B_List_Counter >= (len(Time_Beta_B_List) - 1): 
                    El_Beta_B  = 0 
                    break        
            else:  
                El_Beta_B = Time_Beta_B_List[Time_Beta_B_List_Counter]
                break
    else: El_Beta_B = 0
    print ("   Time_Beta_B = %f" % El_Beta_B)

    if len(Time_D_A_List) > 0: 
       for n in range (1, 3):
            if Time_D_A_List[Time_D_A_List_Counter] <= System_Time: 
                if Time_D_A_List_Counter < (len(Time_D_A_List) - 1):
                    Time_D_A_List_Counter += 1
                    n -= 1
                else: 
                    El_D_A  = 0
                    break         
            else: 
                El_D_A = Time_D_A_List[Time_D_A_List_Counter]
                break
    else:  El_D_A = 0
    print ("      Time_D_A = %f" % El_D_A)

    if len(Time_D_B_List) > 0: 
       for n in range (1, 3):
            if Time_D_B_List[Time_D_B_List_Counter] <= System_Time: 
                if Time_D_B_List_Counter < (len(Time_D_B_List) - 1):
                    Time_D_B_List_Counter += 1
                    n -= 1
                elif Time_D_B_List_Counter >= (len(Time_D_B_List) - 1): 
                    El_D_B  = 0 
                    break        
            else:  
                El_D_B = Time_D_B_List[Time_D_B_List_Counter]
                break
    else:  El_D_B = 0
    print ("      Time_D_B = %f" % El_D_B)


    if len(Time_Beta_II_A_List) > 0: 
       for n in range (1, 3):
            if Time_Beta_II_A_List[Time_Beta_II_A_List_Counter] <= System_Time: 
                if Time_Beta_II_A_List_Counter < (len(Time_Beta_II_A_List) - 1):
                    Time_Beta_II_A_List_Counter += 1
                    n -= 1
                else: 
                    El_Beta_II_A  = 0
                    break         
            else: 
                El_Beta_II_A = Time_Beta_II_A_List[Time_Beta_II_A_List_Counter]
                break
    else: El_Beta_II_A = 0
    print ("Time_Beta_II_A = %f" % El_Beta_II_A)

    if len(Time_Beta_II_B_List) > 0: 
       for n in range (1, 3):
            if Time_Beta_II_B_List[Time_Beta_II_B_List_Counter] <= System_Time: 
                if Time_Beta_II_B_List_Counter < (len(Time_Beta_II_B_List) - 1):
                    Time_Beta_II_B_List_Counter += 1
                    n -= 1
                elif Time_Beta_II_B_List_Counter >= (len(Time_Beta_II_B_List) - 1): 
                    El_Beta_II_B  = 0 
                    break        
            else:  
                El_Beta_II_B = Time_Beta_II_B_List[Time_Beta_II_B_List_Counter]
                break
    else: El_Beta_II_B = 0
    print ("Time_Beta_II_B = %f" % El_Beta_II_B)

    
    if len(Time_Ray_A_List) > 0: 
       for n in range (1, 3):
            if Time_Ray_A_List[Time_Ray_A_List_Counter] <= System_Time: 
                if Time_Ray_A_List_Counter < (len(Time_Ray_A_List) - 1):
                    Time_Ray_A_List_Counter += 1
                    n -= 1
                else: 
                    El_Ray_A  = 0
                    break         
            else: 
                El_Ray_A = Time_Ray_A_List[Time_Ray_A_List_Counter]
                break
    else: El_Ray_A = 0
    print ("    Time_Ray_A = %f" % El_Ray_A)

    if len(Time_Ray_B_List) > 0: 
       for n in range (1, 3):
            if Time_Ray_B_List[Time_Ray_B_List_Counter] <= System_Time: 
                if Time_Ray_B_List_Counter < (len(Time_Ray_B_List) - 1):
                    Time_Ray_B_List_Counter += 1
                    n -= 1
                elif Time_Ray_B_List_Counter >= (len(Time_Ray_B_List) - 1): 
                    El_Ray_B  = 0 
                    break        
            else:  
                El_Ray_B = Time_Ray_B_List[Time_Ray_B_List_Counter]
                break
    else: El_Ray_B = 0
    print ("    Time_Ray_B = %f" % El_Ray_B)

    print("\n")


    if (El_R_A == El_R_B == El_Beta_A == El_Beta_B == El_D_A == El_D_B == El_Beta_II_A == El_Beta_II_B == El_Ray_A == El_Ray_B == 0):

        while Time_R_A < System_Time:  Time_R_A = Time_R_A + Random_Generation()

        Time_R_A_List.append(Time_R_A)
        print("     Time_R_A = %f"%(Time_R_A))
        System_Time = Time_R_A
        print("System_Time = Time_R_A= %f"%(System_Time))
        Sort = R_A 
        
    else:

        Comparing_List           = [El_R_A, El_R_B, El_Beta_A, El_Beta_B, El_D_A, El_D_B, El_Beta_II_A, El_Beta_II_B, El_Ray_A, El_Ray_B] 
        Comparing_List_Dublicate = [El_R_A, El_R_B, El_Beta_A, El_Beta_B, El_D_A, El_D_B, El_Beta_II_A, El_Beta_II_B, El_Ray_A, El_Ray_B] 

        Comparing_List.sort()

        #не учитывает нулевые элементы
        variable = 0
        for n in range (0,10):
            if Comparing_List[variable] == 0: 
                variable += 1 

        #if variable == 9:
        #    print("", end = "")
    
        if   Comparing_List_Dublicate[0] == Comparing_List[variable]:   

            System_Time = El_R_A     
            print("System_Time = Time_R_A = %f"%El_R_A)

            if Time_R_A_List_Counter < (len(Time_R_A_List)-1):
                Time_R_A_List_Counter += 1

            Sort = R_A
            print("Sort = R_A")

        elif Comparing_List_Dublicate[1] == Comparing_List[variable]:   

            System_Time = El_R_B;    
            print("System_Time = Time_R_B = %f"%El_R_B)

            if Time_R_B_List_Counter < (len(Time_R_B_List)-1):
                Time_R_B_List_Counter += 1
            Sort = R_B
            print("Sort = R_B")

        elif Comparing_List_Dublicate[2] == Comparing_List[variable]:   

            System_Time = El_Beta_A;    
            print("System_Time = Time_Beta_A = %f"%El_Beta_A)

            if Time_Beta_A_List_Counter < (len(Time_Beta_A_List)-1):
                Time_Beta_A_List_Counter += 1

            Sort = Beta_A
            print("Sort = Beta_A")

        elif Comparing_List_Dublicate[3] == Comparing_List[variable]:   

            System_Time = El_Beta_B    
            print("System_Time = Time_Beta_B = %f"%El_Beta_B)

            if Time_Beta_B_List_Counter < (len(Time_Beta_B_List)-1):
                Time_Beta_B_List_Counter += 1

            Sort = Beta_B
            print("Sort = Beta_B")

        elif Comparing_List_Dublicate[4] == Comparing_List[variable]:   

            System_Time = El_D_A   
            print("System_Time = Time_D_A = %f"%El_D_A)

            if Time_D_A_List_Counter < (len(Time_D_A_List)-1):
                Time_D_A_List_Counter += 1

            Sort = D_A
            print("Sort = D_A")

        elif Comparing_List_Dublicate[5] == Comparing_List[variable]:   

            System_Time = El_D_B  
            print("System_Time = Time_D_B = %f"%El_D_B)

            if Time_D_B_List_Counter < (len(Time_D_B_List)-1):
                Time_D_B_List_Counter += 1

            Sort = D_B
            print("Sort = D_B")

        elif Comparing_List_Dublicate[6] == Comparing_List[variable]:   

            System_Time = El_Beta_II_A;    
            print("System_Time = Time_Beta_II_A = %f"%El_Beta_II_A)

            if Time_Beta_II_A_List_Counter < (len(Time_Beta_II_A_List)-1):
                Time_Beta_II_A_List_Counter += 1

            Sort = Beta_II_A
            print("Sort = Beta_II_A")

        elif Comparing_List_Dublicate[7] == Comparing_List[variable]:   

            System_Time = El_Beta_II_B    
            print("System_Time = Time_Beta_II_B = %f"%El_Beta_II_B)

            if Time_Beta_II_B_List_Counter < (len(Time_Beta_II_B_List)-1):
                Time_Beta_II_B_List_Counter += 1

            Sort = Beta_II_B
            print("Sort = Beta_II_B")

        elif Comparing_List_Dublicate[8] == Comparing_List[variable]:   

            System_Time = El_Ray_A     
            print("System_Time = Time_Ray_A = %f"%El_Ray_A)

            if Time_Ray_A_List_Counter < (len(Time_Ray_A_List)-1):
                Time_Ray_A_List_Counter += 1
            Sort = Ray_A
            print("Sort = Ray_A")

        elif Comparing_List_Dublicate[9] == Comparing_List[variable]:   

            System_Time = El_Ray_B;    
            print("System_Time = Time_Ray_B = %f"%El_Ray_B)

            if Time_Ray_B_List_Counter < (len(Time_Ray_B_List)-1):
                Time_Ray_B_List_Counter += 1

            Sort = Ray_B
            print("Sort = Ray_B")
    #====================================
        
    print("\nServer_R_1     = %i"%Server_R_1)   
    print(  "Server_R_2     = %i"%Server_R_2)
    print(  "Server_Beta    = %i"%Server_Beta)
    print(  "Server_D_1     = %i"%Server_D_1)
    print(  "Server_D_2     = %i"%Server_D_2)
    print(  "Server_Beta_II = %i"%Server_Beta_II)
    print(  "Server_Ray_1   = %i"%Server_Ray_1)
    print(  "Server_Ray_2   = %i"%Server_Ray_2)


    #Очереди
    print ("\nlen(Queue_R_List)       = %i"%len(Queue_R_List))
    for n in range(0, len(Queue_R_List)):
        print(" #%i - %f"%(n,Queue_R_List[n]))

    print ("len(Queue_Beta_List)    = %i"%len(Queue_Beta_List))
    for n in range(0, len(Queue_Beta_List)):
        print(" #%i - %f"%(n,Queue_Beta_List[n]))

    print ("len(Queue_D_List)       = %i"%len(Queue_D_List))
    for n in range(0, len(Queue_D_List)):
        print(" #%i - %f"%(n,Queue_D_List[n]))

    print ("len(Queue_Beta_II_List) = %i"%len(Queue_Beta_II_List))
    for n in range(0, len(Queue_Beta_II_List)):
        print(" #%i - %f"%(n,Queue_Beta_II_List[n]))

    print ("len(Queue_Ray_List)     = %i"%len(Queue_Ray_List))
    for n in range(0, len(Queue_Ray_List)):
        print(" #%i - %f"%(n,Queue_Ray_List[n]))

#====================================

Requet_Time = input("Request time is: ")
Start()

while float (Time_Ray_B) < float (Requet_Time):

    print("====================================")
    print("\n#%i = %f"%(Iterations, System_Time), end = " - ")
    
    if  (Sort == R_A or Sort == D_A or Sort == Ray_A):      Two_Servers_A_event()
    elif(Sort == R_B or Sort == D_B or Sort == Ray_B):      Two_Servers_B_event()
    elif(Sort == Beta_A or Sort == Beta_II_A):              One_Server_A_event()
    elif(Sort == Beta_B or Sort == Beta_II_B):              One_Server_B_event()

    Finish()

    Iterations += 1 

    if len(Time_Ray_B_List) == 0:
        print("\n==================================== Output list = 0")
    else:
        print("\n==================================== Output list = %f" % Time_Ray_B)



print("\nСистемное время  = %f"%(System_Time))
print("====================================")

Table()

Task_iterations_val = 0
Task_List=[]

while Task_iterations_val < len(Time_Ray_B_List):
        w = fabs( Waiting_Time_List_R[Task_iterations_val] + Waiting_Time_List_Beta[Task_iterations_val] + Waiting_Time_List_D[Task_iterations_val] + Waiting_Time_List_Beta_II[Task_iterations_val] + Waiting_Time_List_Ray[Task_iterations_val])

        q = fabs(Time_R_B_List[Task_iterations_val] + Time_Beta_B_List[Task_iterations_val] + Time_D_B_List[Task_iterations_val] + Time_Beta_II_B_List[Task_iterations_val] + Time_Ray_B_List[Task_iterations_val])

        z = w / q
        Task_List.append(z)

        Task_iterations_val += 1


print("\nСистемное время  = %f"%(System_Time))
print("====================================")

Table()

Task_iterations_val = 0
Task_List=[]

while Task_iterations_val < len(Time_Ray_B_List):
        w = fabs( Waiting_Time_List_R[Task_iterations_val] + Waiting_Time_List_Beta[Task_iterations_val] + Waiting_Time_List_D[Task_iterations_val] + Waiting_Time_List_Beta_II[Task_iterations_val] + Waiting_Time_List_Ray[Task_iterations_val])

        q = fabs(Time_R_B_List[Task_iterations_val] + Time_Beta_B_List[Task_iterations_val] + Time_D_B_List[Task_iterations_val] + Time_Beta_II_B_List[Task_iterations_val] + Time_Ray_B_List[Task_iterations_val])

        z = w / q

        Task_List.append(z)
        Task_iterations_val += 1

Graphic_List = [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0]

Graph_val = 0
while Graph_val < len(Task_List):
    if      Task_List[Graph_val] <= ((max(Task_List))/20):                                                          Graphic_List[0]  += 1
    elif    Task_List[Graph_val] >  ((max(Task_List))/20)    and Task_List[Graph_val] <= (2*(max(Task_List))/20):   Graphic_List[1]  += 1
    elif    Task_List[Graph_val] >  (2*(max(Task_List))/20)  and Task_List[Graph_val] <= (3*(max(Task_List))/20):   Graphic_List[2]  += 1
    elif    Task_List[Graph_val] >  (3*(max(Task_List))/20)  and Task_List[Graph_val] <= (4*(max(Task_List))/20):   Graphic_List[3]  += 1
    elif    Task_List[Graph_val] >  (4*(max(Task_List))/20)  and Task_List[Graph_val] <= (5*(max(Task_List))/20):   Graphic_List[4]  += 1
    elif    Task_List[Graph_val] >  (5*(max(Task_List))/20)  and Task_List[Graph_val] <= (6*(max(Task_List))/20):   Graphic_List[5]  += 1
    elif    Task_List[Graph_val] >  (6*(max(Task_List))/20)  and Task_List[Graph_val] <= (7*(max(Task_List))/20):   Graphic_List[6]  += 1
    elif    Task_List[Graph_val] >  (7*(max(Task_List))/20)  and Task_List[Graph_val] <= (8*(max(Task_List))/20):   Graphic_List[7]  += 1
    elif    Task_List[Graph_val] >  (8*(max(Task_List))/20)  and Task_List[Graph_val] <= (9*(max(Task_List))/20):   Graphic_List[8]  += 1
    elif    Task_List[Graph_val] >  (9*(max(Task_List))/20)  and Task_List[Graph_val] <= (10*(max(Task_List))/20):  Graphic_List[9]  += 1
    elif    Task_List[Graph_val] >  (10*(max(Task_List))/20) and Task_List[Graph_val] <= (11*(max(Task_List))/20):  Graphic_List[10] += 1
    elif    Task_List[Graph_val] >  (11*(max(Task_List))/20) and Task_List[Graph_val] <= (12*(max(Task_List))/20):  Graphic_List[11] += 1
    elif    Task_List[Graph_val] >  (12*(max(Task_List))/20) and Task_List[Graph_val] <= (13*(max(Task_List))/20):  Graphic_List[12] += 1
    elif    Task_List[Graph_val] >  (13*(max(Task_List))/20) and Task_List[Graph_val] <= (14*(max(Task_List))/20):  Graphic_List[13] += 1
    elif    Task_List[Graph_val] >  (14*(max(Task_List))/20) and Task_List[Graph_val] <= (15*(max(Task_List))/20):  Graphic_List[14] += 1
    elif    Task_List[Graph_val] >  (15*(max(Task_List))/20) and Task_List[Graph_val] <= (16*(max(Task_List))/20):  Graphic_List[15] += 1
    elif    Task_List[Graph_val] >  (16*(max(Task_List))/20) and Task_List[Graph_val] <= (17*(max(Task_List))/20):  Graphic_List[16] += 1
    elif    Task_List[Graph_val] >  (17*(max(Task_List))/20) and Task_List[Graph_val] <= (18*(max(Task_List))/20):  Graphic_List[17] += 1
    elif    Task_List[Graph_val] >  (18*(max(Task_List))/20) and Task_List[Graph_val] <= (19*(max(Task_List))/20):  Graphic_List[18] += 1
    elif    Task_List[Graph_val] >  (19*(max(Task_List))/20) and Task_List[Graph_val] <= ((max(Task_List))):        Graphic_List[19] += 1
    elif    Task_List[Graph_val] >  ((max(Task_List)))       and Task_List[Graph_val] <= (21*(max(Task_List))/20):  Graphic_List[20] += 1

    Graph_val += 1 
    


plt.figure()

x = range(0, 105, 5)
y = Graphic_List
plt.plot(x, y)

plt.title('Распределение вероятностей величины\nCумма периодов ожидания/Сумма периодов времени, затраченных на решение задачи')
plt.xlabel('Спектр значений случайной величины')
plt.ylabel('Количество попаданий значения распределения в определённый сегмент диапазона')
plt.grid(True)
plt.show()

