import os

file_name=open("sentences_for_USR","r",encoding="UTF-8")
file_to_paste=open("txt_files/bh-1","r+",encoding="UTF-8")
file_to_paste_temp=open("txt_files/bh-2","r+",encoding="UTF-8") 

for sentence in file_name:
    sentence=sentence.strip()
    print(sentence)
    try:
        file_to_paste=open("txt_files/bh-1","r+",encoding="UTF-8")
        s_id=sentence.split("  ")[0]
        orig_sent=sentence.split("  ")[1].strip()
        orig_sent_copy=sentence.split("  ")[1]

        file_to_paste.seek(0)
        file_to_paste.write(orig_sent)
        file_to_paste.truncate()
        file_to_paste.close()
        file_to_paste_temp.seek(0)
        file_to_paste_temp.write(orig_sent)
        file_to_paste_temp.truncate()
       
        os.system("python3 run_script_dep_mapper.py")
        os.system("python3 complete_usr.py>dependency_mapper_usr/"+s_id)

    except Exception as e:
        print(e)