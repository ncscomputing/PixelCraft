# #By @KariLawler (Twitter)
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
O = 1 # Orange
S = 6 # Pink / Skin
G = 5 # Green
W = 0 # White
R = 14 # Red
SB = 9# Sky blue / cyan
B = 12# Brown
DG = 13 # DARK GREEN
BL = 15 # Black 
# No Block = -1, White = 0, Orange = 1, Magenta = 2, Light Blue = 3,
# Yellow = 4, Lime = 5, Pink = 6, Grey = 7, Light Grey = 8,
# Cyan = 9, Purple = 10, Blue = 11, Brown = 12, Green = 13, Red = 14, Black = 15


Creeper = [
[DG, DG, DG, DG, DG, DG, DG, DG],
[DG, BL, BL, DG, DG, BL, BL, DG],
[DG, BL, BL, DG, DG, BL, BL, DG],
[DG, DG, DG, BL, BL, DG, DG, DG],
[DG, DG, BL, BL, BL, BL, DG, DG],
[DG, DG, BL, BL, BL, BL, DG, DG],
[DG, DG, BL, DG, DG, BL, DG, DG],
[DG, DG, DG, DG, DG, DG, DG, DG],
]


 
block = 35 # wool
x, y, z = mc.player.getPos()
pixel_y = y + len(Creeper) - 1
pixel_z = z - 6
for row in Creeper:
    pixel_x = x
    for pixel in row:
        if pixel > -1:
            mc.setBlock(pixel_x, pixel_y, pixel_z, block, pixel)
        pixel_x += 1
    pixel_y -= 1
