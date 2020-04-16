import os

visualization_list = os.listdir("resource/pic")


visualization_already_output_list = []
for line in open("resource/visualization.txt"):
    visualization_already_output_list.append(line.strip() + ".png")

visualization_not_output_list = [ item for item in visualization_list if item not in visualization_already_output_list ]

print(visualization_not_output_list)
