#File Reading Safeguard

from pathlib import Path

while True:
    script_dir = Path(__file__).parent
    file_name = str(input("Enter the filename "))

    file_path = script_dir/file_name


    try:
        file = open(file_path,"r")
            
    except:
        FileNotFoundError
        print("No such file dumbass, open an existing file.")

    else:
        print(file.read())
        file.close()
        exit()
    finally:
        pass
