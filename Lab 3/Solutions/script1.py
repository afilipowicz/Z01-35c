import glob
import sys

args = sys.argv
extension = args[1]
path = args[2]

print(glob.glob(f"{path}/*.{extension}"))
