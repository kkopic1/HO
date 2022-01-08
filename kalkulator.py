import random 

"""
ma - malo aktivan
sa - srednje aktivan
a - aktivan
"""

# računanje količine kalorija
# izvor : https://www.urmc.rochester.edu/encyclopedia/content.aspx?contenttypeid=85&contentid=P00221&fbclid=IwAR3weSUxx6W_N-9nu8zsgl7TaqpwKpXpDAhMmP1O0KHMilOL5O9DqUfAyj8
# izvor : https://www.heart.org/en/healthy-living/healthy-eating/eat-smart/nutrition-basics/dietary-recommendations-for-healthy-children
def calc_kalorije(ma,sa,a, smanjenje, povecanje, odrzavanje, spol, dob):
    kalorije = 0
    
    if (smanjenje == True or odrzavanje == True):
        if (spol == "F"): 
            if (0 < dob <= 2): 
                kalorije = 900
            
            if (2 < dob <= 3): 
                kalorije = 1000
            
            if (3 < dob <= 8):
                kalorije = 1200
                
            if (8 < dob <= 13):
                kalorije = 1600
                
            if (13 < dob <= 18):
                kalorije = 1800
                
            if (ma == True):
                if (18 < dob <= 30):
                    kalorije = random.uniform(1800, 2000)
                    
                if (30 < dob <= 50):
                    kalorije = 1800
                    
                if (dob > 50): 
                    kalorije = 1600
            
            if (sa == True):
                if (18 < dob <= 30):
                    kalorije = random.uniform(2000, 2200)
                    
                if (30 < dob <= 50):
                    kalorije = 2000
                    
                if (dob > 50): 
                    kalorije = 1800
                    
            if (a == True):
                if (18 < dob <= 30):
                    kalorije = 2400
                    
                if (30 < dob <= 50):
                    kalorije = 2200
                    
                if (dob > 50): 
                    kalorije = random.uniform(2000, 2200)
         
        if (spol == "M"): 
            if (0 < dob <= 2): 
                kalorije = 900
            
            if (2 < dob <= 3): 
                kalorije = 1000
            
            if (3 < dob <= 8):
                kalorije = 1400
                
            if (8 < dob <= 13):
                kalorije = 1800
                
            if (13 < dob <= 18):
                kalorije = 2200
                
            if (ma == True):
                if (18 < dob <= 30):
                    kalorije = random.uniform(2400, 2600)
                    
                if (30 < dob <= 50):
                    kalorije = random.uniform(2200, 2400)
                    
                if (dob > 50): 
                    kalorije = random.uniform(2000, 2200)
            
            if (sa == True):
                if (18 < dob <= 30):
                    kalorije = random.uniform(2600, 2800)
                    
                if (30 < dob <= 50):
                    kalorije = random.uniform(2600, 2800)
                    
                if (dob > 50): 
                    kalorije = random.uniform(2200, 2400)
                    
            if (a == True):
                if (18 < dob <= 30):
                    kalorije = 3000
                    
                if (30 < dob <= 50):
                    kalorije = random.uniform(2800, 3000)
                    
                if (dob > 50): 
                    kalorije = random.uniform(2400, 2800)
    
    if (povecanje == True):
        if (spol == "F"): 
            if (0 < dob <= 2): 
                kalorije = 900 
            
            if (2 < dob <= 3): 
                kalorije = 1000
            
            if (3 < dob <= 8):
                kalorije = 1200
                
            if (8 < dob <= 13):
                kalorije = 1600
                
            if (13 < dob <= 18):
                kalorije = 1800
                
            if (ma == True):
                if (18 < dob <= 30):
                    kalorije = random.uniform(1800, 2000) + + random.uniform(300,500)
                    
                if (30 < dob <= 50):
                    kalorije = 1800 + random.uniform(300,500)
                    
                if (dob > 50): 
                    kalorije = 1600 + random.uniform(300,500)
            
            if (sa == True):
                if (18 < dob <= 30):
                    kalorije = random.uniform(2000, 2200) + random.uniform(300,500)
                    
                if (30 < dob <= 50):
                    kalorije = 2000 + random.uniform(300,500)
                    
                if (dob > 50): 
                    kalorije = 1800 + random.uniform(300,500)
                    
            if (a == True):
                if (18 < dob <= 30):
                    kalorije = 2400 + random.uniform(300,500)
                    
                if (30 < dob <= 50):
                    kalorije = 2200 + random.uniform(300,500)
                    
                if (dob > 50): 
                    kalorije = random.uniform(2000, 2200) + random.uniform(300,500)
         
    if (spol == "M"): 
            if (0 < dob <= 2): 
                kalorije = 900 + random.uniform(300,500)
            
            if (2 < dob <= 3): 
                kalorije = 1000 + random.uniform(300,500)
            
            if (3 < dob <= 8):
                kalorije = 1400 + random.uniform(300,500)
                
            if (8 < dob <= 13):
                kalorije = 1800 + random.uniform(300,500)
                
            if (13 < dob <= 18):
                kalorije = 2200 + random.uniform(300,500)
                
            if (ma == True):
                if (18 < dob <= 30):
                    kalorije = random.uniform(2400, 2600) + random.uniform(300,500)
                    
                if (30 < dob <= 50):
                    kalorije = random.uniform(2200, 2400) + random.uniform(300,500)
                    
                if (dob > 50): 
                    kalorije = random.uniform(2000, 2200) + random.uniform(300,500)
            
            if (sa == True):
                if (18 < dob <= 30):
                    kalorije = random.uniform(2600, 2800) + random.uniform(300,500)
                    
                if (30 < dob <= 50):
                    kalorije = random.uniform(2600, 2800) + random.uniform(300,500)
                    
                if (dob > 50): 
                    kalorije = random.uniform(2200, 2400) + random.uniform(300,500)
                    
            if (a == True):
                if (18 < dob <= 30):
                    kalorije = 3000 + random.uniform(300,500)
                    
                if (30 < dob <= 50):
                    kalorije = random.uniform(2800, 3000) + random.uniform(300,500)
                    
                if (dob > 50): 
                    kalorije = random.uniform(2400, 2800) + random.uniform(300,500)
                    
    return round(kalorije)

# računanje količine proteina 
# izvor : https://blog.nasm.org/nutrition/how-much-protein-should-you-eat-per-day-for-weight-loss?fbclid=IwAR32HGP7hxIzAiYIbGonARPZMRVQrAePTEvOuCU9b-Xgex0l1dlzQ3ebY1I
def calc_proteini(ma, sa, a, smanjenje, povecanje, odrzavanje, tjelesna_masa):
    proteini = 0
    
    if (smanjenje == True): 
        if(ma == True or sa == True):
            proteini = random.uniform(1.6, 2.2) * tjelesna_masa
            
        if(a == True):
            proteini = random.uniform(2.2,3.4) * tjelesna_masa
            
    if (povecanje == True):
        proteini = 1.6 * tjelesna_masa
        
    if (odrzavanje == True):
        proteini = 0.8 * tjelesna_masa
    
    return round(proteini)

#računanje količine ugljikohidrata
# izvor : https://www.healthline.com/nutrition/how-many-carbs-per-day-to-lose-weight#why-eat-fewer-carbs
def calc_ugljikohidrati(smanjenje, povecanje, odrzavanje, kalorije):
    ugljikohidrati = 0
    
    if (smanjenje == True):
        ugljikohidrati = random.uniform(50,150)
        
    if (povecanje == True or odrzavanje == True): 
        ugljikohidrati = (300/2000)*kalorije
        
    return round(ugljikohidrati)

#računanje količine masti
# izvor : https://www.urmc.rochester.edu/encyclopedia/content.aspx?contenttypeid=85&contentid=P00221
def calc_masti(smanjenje, povecanje, odrzavanje, tjelesna_masa, kalorije):
    masti = 0
    
    if (smanjenje == True):
        masti = 0.5* tjelesna_masa
        
    if(povecanje == True or odrzavanje == True):
        masti = (0.3*kalorije)/9 # najviše 30% kalorija ide na masti i 1 gram masti ima 9 kalorija
    
    return round(masti)

#računanje količine kalija 
# izvor : https://www.medicalnewstoday.com/articles/287212#benefits
def calc_kalij(dob,spol):
    kalij = 0
    
    if (spol == "F"):
        if (dob <= 0.5):
            kalij = 400
            
        if(0.5 < dob <=1):
            kalij = 860
            
        if (1 < dob <= 3):
            kalij = 2000
            
        if (3 < dob <= 18):
            kalij = 2300
            
        if ( dob > 19):
            kalij = 2600
            
    if (spol == "M"):
        if (dob <= 0.5):
            kalij = 400
            
        if(0.5 < dob <=1):
            kalij = 860
            
        if (1 < dob <= 3):
            kalij = 2000
            
        if (3 < dob <= 8):
            kalij = 2300
            
        if (8 < dob <= 13):
            kalij = 2500
            
        if (13 < dob <= 18):
            kalij = 3000
            
        if ( dob > 19):
            kalij = 3400
    
    return kalij 

#računanje količine vitamina C 
# izvor : https://ods.od.nih.gov/factsheets/VitaminC-Consumer/
def calc_vitaminC(dob, spol):
    vitaminC = 0
    
    if (spol == "F"):
        if(14 <= dob <=18):
            vitaminC = 65
            
        if ( dob > 19):
            vitaminC = 75
            
    if (spol == "M"):
        if(14 <= dob <=18):
            vitaminC = 75
            
        if ( dob > 19):
            vitaminC = 90
            
    if (0 < dob <=0.5):
        vitaminC = 40
        
    if (0.5 < dob <= 1): 
        vitaminC = 50
        
    if (1 < dob <= 3):
        vitaminC = 15
        
    if (3 < dob <= 8):
        vitaminC = 25
        
    if (8 < dob <= 13):
        vitaminC = 45
        
    return vitaminC

#računanje količine magnezija 
# izvor : https://www.healthline.com/nutrition/magnesium-dosage#types
def calc_magnezij(ma,sa,a, dob, spol):
    magnezij = 0 
    
    if (ma == True or sa == True):
        if (spol == "F"): 
            if (0 < dob <= 0.5):
                magnezij = 30
                
            if (0.5 < dob <= 1):
                magnezij = 75
                
            if (1 < dob <= 3):
                magnezij = 80
                
            if (3 < dob <= 8):
                magnezij = 130
                
            if (8 < dob <=13):
                magnezij = 240
                
            if (13 < dob <= 18): 
                magnezij = 360
                
            if (18 < dob <= 30):
                magnezij = 310
                
            if (30 < dob <= 50):
                magnezij = 320
                
            if (dob > 50):
                magnezij = 320
                
        if (spol == "M"): 
            if (0 < dob <= 0.5):
                magnezij = 30
                
            if (0.5 < dob <= 1):
                magnezij = 75
                
            if (1 < dob <= 3):
                magnezij = 80
                
            if (3 < dob <= 8):
                magnezij = 130
                
            if (8 < dob <=13):
                magnezij = 240
                
            if (13 < dob <= 18): 
                magnezij = 410
                
            if (18 < dob <= 30):
                magnezij = 400
                
            if (30 < dob <= 50):
                magnezij = 420
                
            if (dob > 50):
                magnezij = 420
                
    if (a == True):
        magnezij = 350
        
    return magnezij
    

#račnanje količine kolesterola 
# izvor : https://perks.optum.com/blog/how-much-cholesterol-should-i-be-having-each-day-to-be-healthy/
def calc_kolesterol(smanjenje, povecanje, odrzavanje):
    kolesterol = 0
    
    if(povecanje == True or odrzavanje == True):
        kolesterol = 300
        
    if (smanjenje == True):
        kolesterol = 200
        
    return kolesterol

#računanje količine natrija 
# izvor : https://www.livestrong.com/article/399295-how-to-raise-sodium-levels-in-the-blood/ 
def calc_natrij(smanjenje, povecanje, odrzavanje):
    natrij = 0
    
    if (smanjenje == True or odrzavanje == True): 
        natrij = 1500
        
    if (povecanje == True):
        natrij = 2300
    
    return natrij 
    
# računanje količine željeza
# izvor : https://ods.od.nih.gov/factsheets/Iron-HealthProfessional/
def calc_zeljezo(dob, spol):
    zeljezo = 0
    
    if (spol == "F"): 
        if (0 < dob <= 0.5):
            zeljezo = 0.27
            
        if (0.5 < dob <= 1):
            zeljezo = 11
            
        if (1 < dob <= 3):
            zeljezo = 7
            
        if (3 < dob <= 8):
            zeljezo = 10
            
        if (8 < dob <=13):
            zeljezo = 8
            
        if (13 < dob <= 18): 
            zeljezo = 15
            
        if (18 < dob <= 50):
            zeljezo = 18
            
        if (dob > 50):
            zeljezo = 8
            
    if (spol == "M"): 
        if (0 < dob <= 0.5):
            zeljezo = 0.27
            
        if (0.5 < dob <= 1):
            zeljezo = 11
            
        if (1 < dob <= 3):
            zeljezo = 7
            
        if (3 < dob <= 8):
            zeljezo = 10
            
        if (8 < dob <=13):
            zeljezo = 8
            
        if (13 < dob <= 18): 
            zeljezo = 11
            
        if (18 < dob <= 50):
            zeljezo = 8
            
        if (dob > 50):
            zeljezo = 8
        
    return zeljezo

# računanje količine kalcija
# izvor : https://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/in-depth/calcium-supplements/art-20047097
# izvor : https://www.verywellfamily.com/childrens-calcium-requirements-2633314
def calc_kalcij(dob, spol):
    kalcij = 0
    
    if (spol == "F"):
        if(18 <= dob <= 50):
            kalcij = 1000
            
        if ( dob > 50):
            kalcij = 1200
            
    if (spol == "M"):
        if(18 <= dob <= 70):
            kalcij = 1000
            
        if ( dob > 70):
            kalcij = 1200
            
    if (0 < dob <= 3):
        kalcij = 700
        
    if (3 < dob <= 8):
        kalcij = 1000
        
    if (8 < dob <= 18):
        kalcij = 1300
    
    return kalcij


def kalkulator (aktivnost, tjMasa, spol, dob, tjelesna_masa):
        
    if aktivnost == "1":
        ma = True
        sa = False
        a = False
    elif aktivnost == "2":
        ma = False
        sa = True
        a = False
    else:
        ma = False
        sa = False
        a = True

    if tjMasa == "1":
        smanjenje = True
        odrzavanje = False
        povecanje = False
    elif tjMasa == "2":
        smanjenje = False
        odrzavanje = True
        povecanje = False
    else:
        smanjenje = False
        odrzavanje = False
        povecanje = True

    dob = float(dob)
    tjelesna_masa = float(tjelesna_masa)

    #print(aktivnost, ma, sa, a)
    #print(tjMasa, smanjenje, odrzavanje, povecanje)

    kalorije = calc_kalorije(ma,sa, a, smanjenje, povecanje, odrzavanje, spol, dob)
    
    proteini = calc_proteini(ma, sa, a, smanjenje, povecanje, odrzavanje, tjelesna_masa)
    
    ugljikohidrati = calc_ugljikohidrati(smanjenje, povecanje, odrzavanje, kalorije)
    
    masti = calc_masti(smanjenje, povecanje, odrzavanje, tjelesna_masa, kalorije)
    
    kalij = calc_kalij(dob,spol)
    
    vitaminC = calc_vitaminC(dob, spol)
    
    magnezij = calc_magnezij(ma,sa,a, dob, spol)
    
    kolesterol = calc_kolesterol(smanjenje, povecanje, odrzavanje)
    
    natrij = calc_natrij(smanjenje, povecanje, odrzavanje)
    
    zeljezo = calc_zeljezo(dob, spol)
    
    kalcij = calc_kalcij(dob, spol)
    
    return kalorije, proteini, ugljikohidrati, masti, kalij, vitaminC, magnezij, kolesterol, natrij, zeljezo, kalcij
    

"""if __name__ == "__main__":
    kolicine = kalkulator(False, False, True, False, False, True, "Z", 20, 60)
    print("Kalorije :", kolicine[0])
    print("Proteini :", kolicine[1])
    print("Ugljikohidrati :", kolicine[2])
    print("Masti :", kolicine[3])
    print("Kalij :", kolicine[4])
    print("Vitamin C :", kolicine[5])
    print("Magnezij :", kolicine[6])
    print("Kolesterol :", kolicine[7])
    print("Natrij :", kolicine[8])
    print("Zeljezo :", kolicine[9])
    print("Kalcij :", kolicine[10])"""
    
    
    
    
