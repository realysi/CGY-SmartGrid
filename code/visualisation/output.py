from PIL import Image
# Data outputs
"""
Om de data te visualizeren, zal wat data worden gegenereerd in output.txt. 
Elke keer wanneer data.py zal worden gerund, zal data.txt worden overgeschreven.
"""

def output_file(houses, batteries):
    with open('output.json', 'w') as data:
        total_output = 0
        for i in houses:
            total_output += houses[i].max_output
        data.write(f"district:")
        data.write(f"Sum max_outputs:\t {total_output} \n\n")
        data.write(f"costs-shared:")
        data.write(f"________________________Batteries__________________________\n")
        for i in batteries:
            data.write(f"ID:{i} \t {batteries[i]} \n")
        data.write(f"________________________Houses_____________________________\n")
        for i in houses:
            data.write(f"ID:{i} \t {houses[i]} \n")
    return "Output generated"

    