import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import os

def analyze_file(file_path, label):
    df = pd.read_csv(file_path)

    if 'MsBetweenPresents' not in df.columns:
        print(f"Missing 'MsBetweenPresents' in: {file_path}")
        return

    df['FPS'] = 1000 / df['MsBetweenPresents']

    avg_fps = df['FPS'].mean()
    fps_1_low = np.percentile(df['FPS'], 1)
    fps_0_1_low = np.percentile(df['FPS'], 0.1)
    total_frames = len(df)
    total_time_sec = df['MsBetweenPresents'].sum() / 1000

    print(f"\nFile: {label}")
    print(f"Total Frames : {total_frames}")
    print(f"Duration     : {total_time_sec:.2f} seconds")
    print(f"Avg FPS      : {avg_fps:.2f}")
    print(f"1% Low       : {fps_1_low:.2f}")
    print(f"0.1% Low     : {fps_0_1_low:.2f}")

    # Generate FPS plot
    plt.figure(figsize=(12, 5))
    plt.plot(df['FPS'], label=label, linewidth=0.8)
    plt.axhline(avg_fps, color='orange', linestyle='--', label=f'{label} Avg: {avg_fps:.1f}')
    plt.title(f'FPS Over Time: {label}')
    plt.xlabel('Frame Number')
    plt.ylabel('FPS')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Save plot
    safe_label = label.lower().replace(" ", "_")
    output_path = f"{safe_label}_fps_plot.png"
    plt.savefig(output_path)
    plt.close()
    print(f"Graph saved as: {output_path}")

    # Markdown table row
    print(f"| {label:<18} | {avg_fps:>7.2f} | {fps_1_low:>7.2f} | {fps_0_1_low:>7.2f} |")

    return {
        "label": label,
        "avg_fps": round(avg_fps, 2),
        "fps_1_low": round(fps_1_low, 2),
        "fps_0_1_low": round(fps_0_1_low, 2),
        "plot": output_path
    }

if __name__ == "__main__":
    base_path = r"D:\GAME TESTING\WinGame-Performance-Reports\ark-survival-evolved"
    files = {
        "Medium Settings": os.path.join(base_path, "ark_test_medium.csv"),
        "High Settings": os.path.join(base_path, "ark_test_high.csv"),
        "Crash Session": os.path.join(base_path, "ark_test_crash.csv"),
    }

    results = []
    for label, path in files.items():
        if os.path.exists(path):
            result = analyze_file(path, label)
            if result:
                results.append(result)
        else:
            print(f"File not found: {path}")
