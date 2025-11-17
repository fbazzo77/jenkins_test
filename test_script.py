# test_script.py
import sys
import os
import sys

INPUT_DIR = sys.argv[1]
OUTPUT_DIR = sys.argv[2]

# Definisci il nome del file di input
INPUT_FILE = INPUT_DIR+"/input_text_file.txt"
OUTPUT_FILE=OUTPUT_DIR+"/results.txt"

print("--- Script Python ---")

try:
    
    if not os.path.exists(INPUT_FILE):
        print(f"ERRORE: file not found")
        sys.exit(1)

    #read
    with open(INPUT_FILE, 'r') as f:
        data = f.read()

    # print
  
    print(data)

    print("\n[Output]")
    # 
    num_righe = len(data.split('\n'))
    with open(OUTPUT_FILE, 'w') as f_out:
        f_out.write(str(num_righe))

except Exception as e:
    print(f"Error")
    sys.exit(1)

print("--- End Script Python ---")
