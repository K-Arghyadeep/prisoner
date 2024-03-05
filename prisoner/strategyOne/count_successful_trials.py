import subprocess

# Specify the path to script2.py
script_path = './main.py'

# Run script2.py using subprocess
subprocess.run(['python', script_path])

def count_successful_simulations(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            success_count = 0
            fail_count = 0
            for line in lines:
                if "Simulation Successful" in line:
                    success_count += 1
                if "Simulation Failed" in line:
                    fail_count += 1
            print(f'Success count: {success_count}')
            print(f'Failure count: {fail_count}')
        return None
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return None


file_path = 'SimulationResult.txt'
successful_count = count_successful_simulations('SimulationResult.txt') #####projects\prisoner\strategyOne\