''''steed feed seed recipe = (5 * fertilizer + 35 * bulb)
fertilizer = (3 * shroom 13 * glim 1 * water) / 5
water = 2 * shroom + 3 * glim
mushroom = (((3 * shroom 13 * glim 1 * water) / 5) * 3 + 15 bulb) / 10
steed_feed_recipe = 'steed feed seed recipe = (5 * fertilizer + 35 * bulb)'
steed_feed_recipe = steed_feed_recipe.replace('fertilizer' ,'((3 * shroom 13 * glim 1 * water) / 5)').replace('water', '(2 * shroom + 3 * glim)')
print(steed_feed_recipe)
'(5 * ((3 * shroom + 13 * glim +(2 * shroom + 3 * glim) / 5) + 35 * bulb)'''
#5 shrooms = one recipe of steed feed(10 steed feed seeds)
#35 bulb = one recipe of teed feed(10 steed feed)
#16 glim
#1 water
#5 fertilizer

def calculate_sporeling_amounts(bulb=0, shroom=0, glim=0, water=0, fertilizer=0, target=0):
    # decomposiçao dos recrusos compostos
    if (water + shroom + glim + bulb + fertilizer) == 0:
        while True:
            try:
                bulb = int(input('How many sunlight bulbs do you have?'))
                shroom = int(input('How many mushrooms do you have?'))
                water = int(input('How many water blocks or sponges do you have?'))
                glim = int(input('How much glim do you have?'))
                fertilizer = int(input('How many fertilizers do you have?'))
                break
            except:
                print('Input only numbers please')
    shroom_from_fert = fertilizer * 1
    glim_from_fert = fertilizer * 16/5
    shroom_from_water = water * 2
    glim_from_water = water * 3
    glim_per_sporeling = 160
    bulb_per_sporeling = 350
    shroom_per_sporeling = 505
    water_per_sporeling = fertilizer_per_sporeling = 50
    # Soma total dos recursos atomicos
    total_shroom = shroom + shroom_from_fert + shroom_from_water
    total_glim = glim + glim_from_fert + glim_from_water
    #
    weighted_atomic_glim =total_glim/glim_per_sporeling
    weighted_atomic_bulb = bulb/bulb_per_sporeling
    weighted_atomic_shroom =(total_shroom/shroom_per_sporeling)
    most = max(weighted_atomic_bulb, weighted_atomic_shroom, weighted_atomic_glim)


    if target != 0:
        sporelings_final_ammount = target
        glim_target = sporelings_final_ammount*glim_per_sporeling
        bulb_target = sporelings_final_ammount * bulb_per_sporeling
        shroom_target = sporelings_final_ammount * shroom_per_sporeling
        water_target = (sporelings_final_ammount * water_per_sporeling) - fertilizer
        lacking_bulb = bulb_target - bulb
        lacking_shroom = shroom_target - total_shroom
        lacking_glim = glim_target - total_glim
        water_to_craft = water_target - water
        print('''You want to make {sporeling} sporelings.
        You to do that you will need to gather {fbulb} additional sunlight bulbs, {fshroom} additional mushrooms, {fglim} additional glim. You also need to craft {fwater} sponges'''.format(
            sporeling=sporelings_final_ammount, fbulb=lacking_bulb,fglim=lacking_glim, fshroom=lacking_shroom, fwater=water_to_craft))
        pass
    else:
        ################################################################MECHER NO MOST, PRA CONSIDERAR MELHOR O FERTILIZER###############################################
        if most == weighted_atomic_glim:
            sporelings_final_ammount = total_glim//glim_per_sporeling
            bulb_target = sporelings_final_ammount*bulb_per_sporeling
            shroom_target = sporelings_final_ammount   *shroom_per_sporeling
            water_target = (sporelings_final_ammount *water_per_sporeling) - fertilizer
            lacking_bulb = bulb_target - bulb
            lacking_shroom = shroom_target - total_shroom
            water_to_craft = water_target - water
            print('''You have enough glim to make {sporeling} sporelings.
            You lack {fbulb} sunlight bulbs, {fshroom} mushrooms. You also need to craft {fwater} sponges'''.format(sporeling= sporelings_final_ammount, fbulb= lacking_bulb, fshroom=lacking_shroom,fwater=water_to_craft ))

        elif most == weighted_atomic_bulb:
            sporelings_final_ammount = bulb // bulb_per_sporeling
            glim_target = sporelings_final_ammount * glim_per_sporeling
            shroom_target = sporelings_final_ammount * shroom_per_sporeling
            water_target = (sporelings_final_ammount * water_per_sporeling) - fertilizer
            lacking_glim = glim_target - glim
            lacking_shroom = shroom_target - total_shroom
            water_to_craft = water_target - water
            print('''You have enough sunlight bulbs to make {sporeling} sporelings.
                    You lack {fglim} glim, {fshroom} mushrooms. You also need to craft {fwater} sponges'''.format(
                sporeling=sporelings_final_ammount, fbulb=lacking_glim, fshroom=lacking_shroom, fwater=water_to_craft))

        else:
            sporelings_final_ammount = total_shroom // shroom_per_sporeling
            glim_target = sporelings_final_ammount * glim_per_sporeling
            bulb_target = sporelings_final_ammount * bulb_per_sporeling
            water_target = (sporelings_final_ammount * water_per_sporeling) - fertilizer
            lacking_glim = glim_target - glim
            lacking_bulb = bulb_target - bulb
            water_to_craft = water_target - water
            print('''You have enough mushrooms to make {sporeling} sporelings.
                            You lack {fglim} glim, {fbulb} sunlight bulbs. You also need to craft {fwater} sponges'''.format(
                sporeling=sporelings_final_ammount, fbulb=lacking_glim, fshroom=lacking_shroom, fwater=water_to_craft))
calculate_sporeling_amounts()




