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

    # Output file path (same directory as the CSV)
    directory = os.path.dirname(file_path)
    safe_label = label.lower().replace(" ", "_")
    output_plot_path = os.path.join(directory, f"{safe_label}_fps_plot.png")

    # Generate and save plot
    plt.figure(figsize=(12, 5))
    plt.plot(df['FPS'], label=label, linewidth=0.8)
    plt.axhline(avg_fps, color='orange', linestyle='--', label=f'{label} Avg: {avg_fps:.1f}')
    plt.title(f'FPS Over Time: {label}')
    plt.xlabel('Frame Number')
    plt.ylabel('FPS')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_plot_path)
    plt.close()
    print(f"Graph saved as: {output_plot_path}")

    return {
        "label": label,
        "avg_fps": round(avg_fps, 2),
        "fps_1_low": round(fps_1_low, 2),
        "fps_0_1_low": round(fps_0_1_low, 2),
        "plot": os.path.basename(output_plot_path)
    }

if __name__ == "__main__":
    base_path = r"D:\GAME TESTING\WinGame-Performance-Reports\just-cause-3"
    files = {
        "Low Settings": os.path.join(base_path, "justcause3_test_low.csv"),
        "Medium Settings": os.path.join(base_path, "justcause3_test_medium.csv"),
        "High Settings": os.path.join(base_path, "justcause3_test_high.csv"),
        "Very High Settings": os.path.join(base_path, "justcause3_test_veryhigh.csv"),
    }

    results = []
    for label, path in files.items():
        if os.path.exists(path):
            result = analyze_file(path, label)
            if result:
                results.append(result)
        else:
            print(f"File not found: {path}")

    # Write performance.md in base_path
    if results:
        md_path = os.path.join(base_path, "performance.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write("Performance Report: Just Cause 3\n\n")
            f.write("| Setting           | Avg FPS | 1% Low | 0.1% Low |\n")
            f.write("|-------------------|---------|--------|----------|\n")
            for r in results:
                f.write(f"| {r['label']:<18} | {r['avg_fps']:>7.2f} | {r['fps_1_low']:>6.2f} | {r['fps_0_1_low']:>8.2f} |\n")
            f.write("\n")

            f.write("### Graphs\n")
            for r in results:
                f.write(f"- {r['label']}: ![{r['label']}]({r['plot']})\n")

        print(f"\nMarkdown report written to: {md_path}")
