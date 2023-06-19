
import csv
import math
import floss_table

FILE = 'his_way_home_stitch_count.csv'
OUTPUT = 'his_way_home_skein_count.csv'
STRANDS_OF_FLOSS = 2
FABRIC_COUNT = 16
BUFFER = 1.75 # Percentage

def main():
    stitch_counts = None
    with open(FILE) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        stitch_counts = list(csv_reader)

    skein_counts = []

    stitches_per_skein = floss_table.stitches_per_skein_chart[(FABRIC_COUNT, STRANDS_OF_FLOSS)]

    for colour in stitch_counts:
        skeins_required = ((int(colour['count']) / stitches_per_skein) * BUFFER)
        skein = {
            "colour": colour['thread'],
            "skeins": "{:.2f}".format(skeins_required),
            "skeins_round_up": math.ceil(skeins_required),
            "stitches": colour['count']
        }
        skein_counts.append(skein)

    with open(OUTPUT, "w", newline='') as out_file:
        fieldnames = ['colour', 'skeins', 'skeins_round_up', 'stitches']
        writer = csv.DictWriter(out_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(skein_counts)
        
main()