import os
import json

input_folder = './DATA/SD-saliency-900/Source_Images'  # 替换为你的文件夹路径
output_file = './DATA/SD-saliency-900/caption.json'  # 输出的 JSON 文件名

file_names = os.listdir(input_folder)

data = []


for file_name in file_names:
    file_dict = {}
    if os.path.isfile(os.path.join(input_folder, file_name)):
        file_name_sub = file_name.split('.')[0]
        last_underscore_index = file_name_sub.rfind("_")
        file_name_sub = file_name_sub[:last_underscore_index]
        if file_name_sub == "In":
            file_dict[file_name] = f"A photo of inclusion"
        elif file_name_sub == "Pa":
            file_dict[file_name] = f"A photo of patches"
        elif file_name_sub == "Sc":
            file_dict[file_name] = f"A photo of scratches"
        data.append(file_dict)

with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("Create JSON successfully!")
