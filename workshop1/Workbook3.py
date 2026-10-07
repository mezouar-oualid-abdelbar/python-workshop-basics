

rgb = ["R", "G", "B"]
rgb_copy = rgb  # a copy of rgb list!
rgb_copy.append("A")
rgb_copy
# ??? ["R", "G", "B" ,"A"]

rgb
# ??? ["R", "G", "B" ,"A"]

id(rgb) == id(rgb_copy) # they reference the same object
# ??? true

rgb = ["R", "G", "B"]
correct_rgb_copy = rgb[:]
correct_rgb_copy.append("A")
correct_rgb_copy
# ???  ["R", "G", "B" ,"A"]

rgb
# ??? ["R", "G", "B"]

id(rgb) == id(correct_rgb_copy)
# ??? false

