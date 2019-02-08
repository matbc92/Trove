''''steed feed seed recipe = (5 * fertilizer + 35 * bulb)
fertilizer = (3 * shroom 13 * glim 1 * water) / 5
water = 2 * shroom + 3 * glim
mushroom = (((3 * shroom 13 * glim 1 * water) / 5) * 3 + 15 bulb) / 10 '''
steed_feed_recipe = 'steed feed seed recipe = (5 * fertilizer + 35 * bulb)'
steed_feed_recipe = steed_feed_recipe.replace('fertilizer' ,'((3 * shroom 13 * glim 1 * water) / 5)').replace('water', '(2 * shroom + 3 * glim)')
print(steed_feed_recipe)
'(5 * ((3 * shroom + 13 * glim +(2 * shroom + 3 * glim) / 5) + 35 * bulb)'
#5 shrooms = one recipe of steed feed(10 steed feed seeds)
#35 bulb = one recipe of teed feed(10 steed feed)
#16 glim
#1 water
#5 fertilizer

def calcular_quantidade_steed_feed(bulb=0, shroom=0, glim=0, water=0, fertilizer=0):
    # decomposiçao dos recrusos compostos
    shroom_from_fert = fertilizer * 1
    glim_from_fert = fertilizer * 16/5
    shroom_from_water = water * 2
    glim_from_water = water * 3
    # Soma total dos recursos atomicos
    total_shroom = shroom + shroom_from_fert + shroom_from_water
    total_glim = glim + glim_from_fert + glim_from_water
    #
    weighted_atomic_glim =total_glim/16
    weighted_atomic_bulb = bulb/35
    weighted_atomic_shroom =total_shroom/5
    most = max(weighted_atomic_bulb, weighted_atomic_shroom, weighted_atomic_glim)
    if most == weighted_atomic_glim:
        
        pass
    elif most == weighted_atomic_bulb:
        pass
    else:
        pass



