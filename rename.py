import os
from tqdm import tqdm
dataDir = os.path.join(__file__, '..', 'data')

files = [file for file in os.listdir(dataDir) if file.endswith('.WAV')]

for file in tqdm(files):
    os.rename(
        os.path.join(dataDir, file),
        os.path.join(dataDir, os.path.splitext(file)[0] + '.wav')
    )