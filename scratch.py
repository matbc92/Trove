glim_per_sporeling=1
bulb_per_sporeling=1
shroom_per_sporeling=1
water_per_sporeling=1
fertilizer_per_sporeling=1
sfeed_per_sporeling=1
def lacking_calculation(sporelings_target):
    sporelings_final_ammount=sporelings_target 
    global glim_per_sporeling
    global bulb_per_sporeling
    global shroom_per_sporeling
    global water_per_sporeling
    global fertilizer_per_sporeling
    global sfeed_per_sporeling
    glim_target = sporelings_final_ammount*glim_per_sporeling
    bulb_target = sporelings_final_ammount * bulb_per_sporeling
    shroom_target = sporelings_final_ammount * shroom_per_sporeling
    water_target = sporelings_final_ammount * water_per_sporeling
    fertilizer_target = sporelings_final_ammount * fertilizer_per_sporeling
    sfeed_target = sporelings_final_ammount * sfeed_per_sporeling
    global lacking_bulb 
    lacking_bulb = bulb_target - total_bulb
    global lacking_shroom 
    lacking_shroom = shroom_target - total_shroom
    global lacking_glim 
    lacking_glim = glim_target - total_glim
    global water_to_craft 
    water_to_craft = water_target - total_water
    global fertilizer_to_craft 
lacking_calculation(100)
print(lacking_glim)
