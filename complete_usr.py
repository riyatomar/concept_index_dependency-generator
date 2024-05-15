import os


scripts=[
    "main_sent.py",
    "concept_row_mod.py",
    "indexing_module.py",
    "dependency_module.py",
]

def run_script(script_name):
    try:
        command=f"python3 {script_name}"
        os.system(command)
    except Exception as e:
        print(f"Error running script: {e}")

for script in scripts:
    run_script(script)
