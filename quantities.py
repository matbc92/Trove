''''steed feed seed recipe = (5 * fertilizer + 35 * bulb)
fertilizer = (3 * shroom 13 * glim 1 * water) / 5
water = 2 * shroom + 3 * glim
mushroom = (((3 * shroom 13 * glim 1 * water) / 5) * 3 + 15 bulb) / 10
steed_feed_recipe = 'steed feed seed recipe = (5 * fertilizer + 35 * bulb)'
steed_feed_recipe = steed_feed_recipe.replace('fertilizer' ,'((3 * shroom 13 * glim 1 * water) / 5)').replace('water', '(2 * shroom + 3 * glim)')
print(steed_feed_recipe)
'(5 * ((3 * shroom + 13 * glim +(2 * shroom + 3 * glim) / 5) + 35 * bulb)'''
# drafts of the ammounts of things I was going to use, mostly a reference card
#5 shrooms = one recipe of steed feed(10 steed feed seeds)
#35 bulb = one recipe of teed feed(10 steed feed)
#16 glim
#1 water
#5 fertilizer
def calculate_sporeling_amounts(bulb=0, shroom=0, glim=0, water=0, fertilizer=0,sfeed=0,ichor = 0, target=0):
    # If no ammounts are supllied to the function, the function will ask for them in the form of inputs
    if (water + shroom + glim + bulb + fertilizer) == 0:
        while True:
            try:
                bulb = int(input('How many sunlight bulbs do you have?'))
                shroom = int(input('How many mushrooms do you have?'))
                water = int(input('How many water blocks or sponges do you have?'))
                glim = int(input('How much glim do you have?'))
                fertilizer = int(input('How many fertilizers do you have?'))
                sfeed = int(input('How many steed feed or steed feed seeds do you have?'))
                ichor = int(input('How many sticky ichor do you have?'))
                break
            except:
                print('Input only numbers please')
    # Decomposition of composite resources
    fertilizer_from_sfeed = sfeed * 5/10
    total_fert = fertilizer + fertilizer_from_sfeed
    water_from_fert = total_fert//5
    shroom_from_fert = total_fert * 1
    shroom_from_water = water * 2
    glim_from_fert = total_fert * 16/5
    bulb_from_sfeed = sfeed * 35/10
    glim_from_water = water * 3
    glim_per_sporeling = 160
    bulb_per_sporeling = 350
    shroom_per_sporeling = 505
    water_per_sporeling = 10
    fertilizer_per_sporeling = 50
    sfeed_per_sporeling = 100
    ichor_per_sporeling = 50
    # Sum of the actual ammount of the resources with the quantity resluting of the decompostion
    total_shroom = shroom + shroom_from_fert + shroom_from_water
    total_glim = glim + glim_from_fert + glim_from_water
    total_bulb = bulb + bulb_from_sfeed
    total_water = water_from_fert + water
    # Weighting of the amounts based on the quantity required for the complete recipe
    weighted_glim = glim/glim_per_sporeling
    weighted_bulb = bulb/bulb_per_sporeling
    weighted_shroom = shroom/shroom_per_sporeling
    weighted_fertilizer = fertilizer/fertilizer_per_sporeling
    weighted_sfeed = sfeed/sfeed_per_sporeling
    weighted_water = water/water_per_sporeling
    weighted_ichor = ichor/ichor_per_sporeling
    most = max(weighted_bulb, weighted_shroom, weighted_glim, weighted_fertilizer,weighted_sfeed,weighted_water,weighted_ichor)


    # Optional mode of the function, if the target parameter is set to anything,
    # the function will not calculate how much resources you will need to exhaust
    # your most abundant one, instead it will calculate how much resources will
    # will be required to produce the ammout of steed feed equal to the number
    # supllied on the target parameter.
    # If all the parameters refering to the resources are empty they will still
    # be asked as inputs.
    if target != 0:
        sporelings_final_ammount = target
        glim_target = sporelings_final_ammount*glim_per_sporeling
        bulb_target = sporelings_final_ammount * bulb_per_sporeling
        shroom_target = sporelings_final_ammount * shroom_per_sporeling
        water_target = sporelings_final_ammount * water_per_sporeling
        fertilizer_target = sporelings_final_ammount * fertilizer_per_sporeling
        sfeed_target = sporelings_final_ammount * sfeed_per_sporeling
        lacking_bulb = bulb_target - total_bulb
        lacking_shroom = shroom_target - total_shroom
        lacking_glim = glim_target - total_glim
        water_to_craft = water_target - total_water
        fertilizer_to_craft = fertilizer_target - fertilizer
        sfeed_to_craft = sfeed_target - sfeed
        print('''You want to make {sporeling} sporelings.
You to do that you will need to gather {fbulb} additional sunlight bulbs, {fshroom} additional mushrooms, {fglim} additional glim and {fichor} aditional sticky ichors.
You also need to craft {fsfeed} steed feed seeds, for which will require {ffertilizer} to be craft, which will also require {fwater} aditional sponges to be craft'''.format(sporeling=sporelings_final_ammount, fbulb=lacking_bulb,fglim=lacking_glim,\
fshroom=lacking_shroom, fwater=water_to_craft,fsfeed = sfeed_to_craft,ffertilizer =fertilizer_to_craft, fichor = lacking_ichor))
# After the weighting is done and the (relative to the recipe requirements)
# most abundant resource is established the ammount required of the remaining
# ones will be calculated and printed
    else:
        if most == weighted_glim:
            sporelings_final_ammount = total_glim//glim_per_sporeling
            glim_target = sporelings_final_ammount * glim_per_sporeling
            bulb_target = sporelings_final_ammount * bulb_per_sporeling
            shroom_target = sporelings_final_ammount * shroom_per_sporeling
            water_target = sporelings_final_ammount * water_per_sporeling
            fertilizer_target = sporelings_final_ammount * fertilizer_per_sporeling
            sfeed_target = sporelings_final_ammount * sfeed_per_sporeling
            ichor_target = sporelings_final_ammount * ichor_per_sporeling
            lacking_ichor = ichor_target - ichor
            lacking_bulb = bulb_target - total_bulb
            lacking_shroom = shroom_target - total_shroom
            lacking_glim = glim_target - total_glim
            water_to_craft = water_target - total_water
            fertilizer_to_craft = fertilizer_target - fertilizer
            sfeed_to_craft = sfeed_target - sfeed
            print('''You have enough glim to make {sporeling} sporelings.
You lack {fbulb} sunlight bulbs, {fshroom} mushrooms and {fichor} sticky ichors.
You also need to craft {fsfeed} steed feed seeds,
for which will require {ffertilizer} to be craft,
which will also require {fwater} aditional sponges to be craft'''.format(
                sporeling=sporelings_final_ammount, fbulb=lacking_bulb, fglim=lacking_glim, \
                fshroom=lacking_shroom, fwater=water_to_craft, fsfeed=sfeed_to_craft, ffertilizer=fertilizer_to_craft, fichor = lacking_ichor))

        elif most == weighted_bulb:
            sporelings_final_ammount = bulb // bulb_per_sporeling
            glim_target = sporelings_final_ammount * glim_per_sporeling
            bulb_target = sporelings_final_ammount * bulb_per_sporeling
            shroom_target = sporelings_final_ammount * shroom_per_sporeling
            water_target = sporelings_final_ammount * water_per_sporeling
            fertilizer_target = sporelings_final_ammount * fertilizer_per_sporeling
            sfeed_target = sporelings_final_ammount * sfeed_per_sporeling
            ichor_target = sporelings_final_ammount * ichor_per_sporeling
            lacking_ichor = ichor_target - ichor
            lacking_bulb = bulb_target - total_bulb
            lacking_shroom = shroom_target - total_shroom
            lacking_glim = glim_target - total_glim
            water_to_craft = water_target - total_water
            fertilizer_to_craft = fertilizer_target - fertilizer
            sfeed_to_craft = sfeed_target - sfeed
            print('''You have enough sunlight bulbs to make {sporeling} sporelings.
You lack {fglim} gilm, {fshroom} mushrooms and {fichor} sticky ichors.
You also need to craft {fsfeed} steed feed seeds,
for which will require {ffertilizer} to be craft,
which will also require {fwater} aditional sponges to be craft'''.format(
                sporeling=sporelings_final_ammount, fbulb=lacking_bulb, fglim=lacking_glim, \
                fshroom=lacking_shroom, fwater=water_to_craft, fsfeed=sfeed_to_craft, ffertilizer=fertilizer_to_craft,fichor = lacking_ichor))


        elif most == weighted_shroom:
            sporelings_final_ammount = total_shroom // shroom_per_sporeling
            glim_target = sporelings_final_ammount * glim_per_sporeling
            bulb_target = sporelings_final_ammount * bulb_per_sporeling
            shroom_target = sporelings_final_ammount * shroom_per_sporeling
            water_target = sporelings_final_ammount * water_per_sporeling
            fertilizer_target = sporelings_final_ammount * fertilizer_per_sporeling
            sfeed_target = sporelings_final_ammount * sfeed_per_sporeling
            ichor_target = sporelings_final_ammount * ichor_per_sporeling
            lacking_ichor = ichor_target - ichor
            lacking_bulb = bulb_target - total_bulb
            lacking_shroom = shroom_target - total_shroom
            lacking_glim = glim_target - total_glim
            water_to_craft = water_target - total_water
            fertilizer_to_craft = fertilizer_target - fertilizer
            sfeed_to_craft = sfeed_target - sfeed

            print('''You have enough mushrooms to make {sporeling} sporelings.
You lack {fglim} glim, {fbulb} sunlight bulbs and {fichor} sticky ichors.
You also need to craft {fsfeed} steed feed seeds,
for which will require {ffertilizer} to be craft,
which will also require {fwater} aditional sponges to be craft'''.format(
                sporeling=sporelings_final_ammount, fbulb=lacking_bulb, fglim=lacking_glim, \
                fshroom=lacking_shroom, fwater=water_to_craft, fsfeed=sfeed_to_craft, ffertilizer=fertilizer_to_craft,fichor = lacking_ichor))
        elif most == weighted_fertilizer:
            sporelings_final_ammount = total_fert // shroom_per_sporeling
            glim_target = sporelings_final_ammount * glim_per_sporeling
            bulb_target = sporelings_final_ammount * bulb_per_sporeling
            shroom_target = sporelings_final_ammount * shroom_per_sporeling
            water_target = sporelings_final_ammount * water_per_sporeling
            fertilizer_target = sporelings_final_ammount * fertilizer_per_sporeling
            sfeed_target = sporelings_final_ammount * sfeed_per_sporeling
            ichor_target = sporelings_final_ammount * ichor_per_sporeling
            lacking_ichor = ichor_target - ichor
            lacking_bulb = bulb_target - total_bulb
            lacking_shroom = shroom_target - total_shroom
            lacking_glim = glim_target - total_glim
            water_to_craft = water_target - total_water
            fertilizer_to_craft = fertilizer_target - fertilizer
            sfeed_to_craft = sfeed_target - sfeed

            print('''You have enough fertilizers to make {sporeling} sporelings.
You lack {fbulb} sunlight bulbs,{fichor} sticky ichorsand {fshroom} mushrooms.
You also need to craft {fsfeed} steed feed seeds,'''.format(
                sporeling=sporelings_final_ammount, fbulb=lacking_bulb, fglim=lacking_glim, \
                fshroom=lacking_shroom, fwater=water_to_craft, fsfeed=sfeed_to_craft, ffertilizer=fertilizer_to_craft,fichor = lacking_ichor))
        elif most == weighted_sfeed:
            sporelings_final_ammount = total_shroom // shroom_per_sporeling
            glim_target = sporelings_final_ammount * glim_per_sporeling
            bulb_target = sporelings_final_ammount * bulb_per_sporeling
            shroom_target = sporelings_final_ammount * shroom_per_sporeling
            water_target = sporelings_final_ammount * water_per_sporeling
            fertilizer_target = sporelings_final_ammount * fertilizer_per_sporeling
            sfeed_target = sporelings_final_ammount * sfeed_per_sporeling
            ichor_target = sporelings_final_ammount * ichor_per_sporeling
            lacking_ichor = ichor_target - ichor
            lacking_bulb = bulb_target - total_bulb
            lacking_shroom = shroom_target - total_shroom
            lacking_glim = glim_target - total_glim
            water_to_craft = water_target - total_water
            fertilizer_to_craft = fertilizer_target - fertilizer
            sfeed_to_craft = sfeed_target - sfeed

            print('''You have enough steed feed or steed feed seeds to make {sporeling} sporelings.
You lack {fshroom} mushrooms and {fichor} sticky ichors.'''.format(
                sporeling=sporelings_final_ammount, fbulb=lacking_bulb, fglim=lacking_glim, \
                fshroom=lacking_shroom, fwater=water_to_craft, fsfeed=sfeed_to_craft, ffertilizer=fertilizer_to_craft,fichor = lacking_ichor))
        elif most == weighted_water:
            sporelings_final_ammount = total_shroom // shroom_per_sporeling
            glim_target = sporelings_final_ammount * glim_per_sporeling
            bulb_target = sporelings_final_ammount * bulb_per_sporeling
            shroom_target = sporelings_final_ammount * shroom_per_sporeling
            water_target = sporelings_final_ammount * water_per_sporeling
            fertilizer_target = sporelings_final_ammount * fertilizer_per_sporeling
            sfeed_target = sporelings_final_ammount * sfeed_per_sporeling
            ichor_target = sporelings_final_ammount * ichor_per_sporeling
            lacking_ichor = ichor_target - ichor
            lacking_bulb = bulb_target - total_bulb
            lacking_shroom = shroom_target - total_shroom
            lacking_glim = glim_target - total_glim
            water_to_craft = water_target - total_water
            fertilizer_to_craft = fertilizer_target - fertilizer
            sfeed_to_craft = sfeed_target - sfeed

            print('''You have enough water or sponges to make {sporeling} sporelings.
You lack {fglim} glim, {fbulb} sunlight bulbs,{fichor} sticky ichors and {fshroom} mushrooms.
You also need to craft {fsfeed} steed feed seeds,
for which will require {ffertilizer} to be craft,'''.format(
                sporeling=sporelings_final_ammount, fbulb=lacking_bulb, fglim=lacking_glim, \
                fshroom=lacking_shroom, fwater=water_to_craft, fsfeed=sfeed_to_craft, ffertilizer=fertilizer_to_craft,fichor = lacking_ichor))
        elif most == weighted_ichor:
            sporelings_final_ammount = ichor// shroom_per_sporeling
            glim_target = sporelings_final_ammount * glim_per_sporeling
            bulb_target = sporelings_final_ammount * bulb_per_sporeling
            shroom_target = sporelings_final_ammount * shroom_per_sporeling
            water_target = sporelings_final_ammount * water_per_sporeling
            fertilizer_target = sporelings_final_ammount * fertilizer_per_sporeling
            sfeed_target = sporelings_final_ammount * sfeed_per_sporeling
            ichor_target = sporelings_final_ammount * ichor_per_sporeling
            lacking_ichor = ichor_target - ichor
            lacking_bulb = bulb_target - total_bulb
            lacking_shroom = shroom_target - total_shroom
            lacking_glim = glim_target - total_glim
            water_to_craft = water_target - total_water
            fertilizer_to_craft = fertilizer_target - fertilizer
            sfeed_to_craft = sfeed_target - sfeed

            print('''You have enough sticky ichor to make {sporeling} sporelings.
You lack {fglim} glim, {fbulb} sunlight bulbs and {fshroom} mushrooms.
You also need to craft {fsfeed} steed feed seeds,
for which will require {ffertilizer} to be craft,
which will also require {fwater} aditional sponges to be craft'''.format(
                sporeling=sporelings_final_ammount, fbulb=lacking_bulb, fglim=lacking_glim, \
                fshroom=lacking_shroom, fwater=water_to_craft, fsfeed=sfeed_to_craft, ffertilizer=fertilizer_to_craft,fichor = lacking_ichor))



calculate_sporeling_amounts()




