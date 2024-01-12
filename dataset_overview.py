import os

# Set your dataset root directory and output filename here
root_dir = "./"
output_filename = "overview.txt"


def collect_datasets(root):
    return []


def count_jpg_images(dataset_dir):
    counts = {'train-val': {}, 'test': {}}

    # Traverse through 'train-val' and 'test' directories
    for split in ['train-val', 'test']:
        split_path = os.path.join(dataset_dir, split)
        if not os.path.exists(split_path):
            print(f"Directory '{split_path}' does not exist.")
            continue

        # Traverse through each class directory
        for class_name in os.listdir(split_path):
            class_path = os.path.join(split_path, class_name)
            if os.path.isdir(class_path):
                jpg_count = sum(1 for file in os.listdir(class_path) if file.lower().endswith('.jpg'))
                counts[split][class_name] = jpg_count

    return counts


def save_counts_to_file(counts, output_file):
    with open(output_file, 'w') as f:
        for split, classes in counts.items():
            f.write(f"Dataset Split: {split}\n")
            for class_name, count in classes.items():
                f.write(f"Class '{class_name}': {count} images\n")
            f.write("\n")


# Collect datasets
datasets = collect_datasets(root_dir)

# Count images within each dataset
dataset_dirs = [os.path.join(root_dir, dataset) for dataset in datasets]
image_counts = [count_jpg_images(dataset_dir) for dataset_dir in dataset_dirs]

# Save results to a text file
[save_counts_to_file(image_count, output_filename) for image_count in image_counts]

print(f"Image counts saved to {output_filename}")
