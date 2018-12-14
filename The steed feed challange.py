bulb = 8
glim = 1
shroom = 5
pflame = 43
ichor = 28
water = (shroom * 2 + glim * 3)
fertilizer = (3 * shroom + 13 * glim + water) / 5
f_pack = (fertilizer * 5)
pedaço_da_formula = (5 * shroom + 16 * glim )
made_shroom = (((5 * shroom + glim * 16) / 5) * 3 + 15 * bulb) / 10
sfeed = (f_pack + 35 * bulb) / 10
bottle = ((fertilizer * 3 + bulb * 35 + pflame * 5) / 10)
chestnut = ((2*fertilizer + 35*bulb)/10)
sporeling = (50*ichor + 500*shroom + 100*sfeed)
print('chestnut =', chestnut)
print('custo estimado de produção de steed feed =', sfeed)
print(shroom, '= shroom', made_shroom, '= made shroom')
print('fertilizer price =', fertilizer, 'fertilizer pack price =', f_pack, 'pedaço da formula = ', pedaço_da_formula )
print('sporeling =', sporeling)
