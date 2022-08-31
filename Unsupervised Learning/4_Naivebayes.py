'''
===========================================================================================================
			*---*---*---*---*---*---*---*
			|   Naivebayes Algorithm    |	
			*---*---*---*---*---*---*---*	
==========================================================================================================='''

import pandas as pd
df=pd.read_csv("example.csv")
total_count=0
Mamal_count=0
Non_Mamal_count=0

Mgive_brith=0
Mcan_fly=0
Mlive_in_water=0
Mhave_leg=0

Ngive_brith=0
Ncan_fly=0
Nlive_in_water=0
Nhave_leg=0

for i in df.index:
    total_count+=1
    if(df['Class'][i]=='m'):
        Mamal_count+=1
        if(df['GiveBirth'][i]=='yes'):
            Mgive_brith+=1
        if(df['CanFly'][i]=='no'):
            Mcan_fly+=1
        if(df['LiveInWater'][i]=='yes'):
            Mlive_in_water+=1
        if(df['HaveLegs'][i]=='no'):
            Mhave_leg+=1
        
    else:
        Non_Mamal_count+=1
        if(df['GiveBirth'][i]=='yes'):
            Ngive_brith+=1
        if(df['CanFly'][i]=='no'):
            Ncan_fly+=1
        if(df['LiveInWater'][i]=='yes'):
            Nlive_in_water+=1
        if(df['HaveLegs'][i]=='no'):
            Nhave_leg+=1
        
        
probablity_Mamal=(Mgive_brith/Mamal_count)*(Mcan_fly/Mamal_count)*(Mlive_in_water/Mamal_count)*(Mhave_leg/Mamal_count)
print(probablity_Mamal)

probablity_Non_Mamal=(Ngive_brith/Non_Mamal_count)*(Ncan_fly/Non_Mamal_count)*(Nlive_in_water/Non_Mamal_count)*(Nhave_leg/Non_Mamal_count)
print(probablity_Non_Mamal)

probabilityMammel=(probablity_Mamal*Mamal_count)/total_count
probabilityNonMammel=(probablity_Non_Mamal*Non_Mamal_count)/total_count

if(probabilityMammel>probabilityNonMammel):
    print("Mammels")
else:
    print("Non-Mammels")
'''
===========================================================================================================
Output:
===========================================================================================================

0.05997501041232819
0.00420153355974931
Mammels
'''