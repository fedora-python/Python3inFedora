import subprocess
import json

from svg_wheel import generate_svg_wheel
from utils import (
    annotate_wheels,
    get_top_packages,
    remove_irrelevant_packages,
    save_to_file,
)


TO_CHART = 360


#def main():
#    packages = remove_irrelevant_packages(get_top_packages(), TO_CHART)
#    annotate_wheels(packages)
#    save_to_file(packages, 'results.json')
#    generate_svg_wheel(packages, TO_CHART)

def main():
    subprocess.call(["/usr/bin/python3", "dnf-livecd-python.py", "--actual"])
    with open('python3.json', 'r') as f:
        packages = json.load(f)
        generate_svg_wheel(packages['data'], len(packages['data']))

if __name__ == '__main__':
    main()
