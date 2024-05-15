import os

os.system("python3 sentence_check.py")
os.system("python3 remove_space.py")
os.system("isc-parser -i txt_files/bh-1 > txt_files/parser-output.txt")
# os.system("python3 dependency_mapper.py") 
os.system("utf8_wx txt_files/bh-1 > txt_files/wx.txt")
os.system("python3 morph_out_generator.py")
os.system("python3 prune_out_generator.py")
