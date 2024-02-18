import pandas as pd
from audio import download_audio

# Data Load
df = pd.read_csv(
    filepath_or_buffer=r'data/marco_batalha.csv'
)

# Donwload audio
# for i in list(df["link"]):
#     download_audio(i, output_path="audio/")
