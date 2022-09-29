import os, re

"""
Youtube playlist downloaded, filenames are like:
Audio Signal Processing for Machine Learning - 001 - Extracting Spectral Centroid and Bandwidth with Python and Librosa.mp4
The order numbers are '001' to '023', and need to be reversed.
"""
filenames = os.listdir(os.getcwd())

for filename in filenames:
    match = re.search(r'[0-9]{3}', filename)
    number = int(match.group())
    num = str(24 - number).zfill(3)
    new_filename = re.sub(r'[0-9]{3}', num, filename, 1)
    os.rename(filename, new_filename)
