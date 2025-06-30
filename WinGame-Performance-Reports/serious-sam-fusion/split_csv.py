import pandas as pd
import os

#config
input_file = r"D:\GAME TESTING\WinGame-Performance-Reports\serious-sam-fusion\ssf_test_medium.csv"
output_folder = r"D:\GAME TESTING\WinGame-Performance-Reports\serious-sam-fusion"
chunk_rows = 100000  # Adjust this down if needed

#split
i = 1
for chunk in pd.read_csv(input_file, chunksize=chunk_rows):
    output_path = os.path.join(output_folder, f"ssf_test_medium_part{i}.csv")
    chunk.to_csv(output_path, index=False)
    print(f"✅ Saved: {output_path}")
    i += 1

print(f"\n🎉 Done! Split into {i - 1} part(s).")
