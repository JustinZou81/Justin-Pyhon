import os
data_dir = "./datas/many_texts"

contents = []
for file in os.listdir(data_dir):
    file_path = f"{data_dir}/{file}"
    if os.path.isfile(file_path) and file.endswith(".txt"):
        with open(file_path, encoding="utf-8") as fin:
            contents.append(fin.read())

final_content = "\n".join(contents)
print(final_content)
with open("./datas/many_texts.txt", "w", encoding='utf-8', ) as fout:
    fout.write(final_content)
