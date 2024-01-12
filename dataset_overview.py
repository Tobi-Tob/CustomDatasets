import os, csv

# Settings
root_dir = "./"
datasets = ["Common_Objects", "Road_Signs"]
sub_dirs = ["test", "train-val"]


def get_info(dataset_path, dataset_name):
    classes = {f'{dataset_name}': [0, 0]}

    def count_jpg(split_name):
        if split_name == "train-val":
            split_dir = os.path.join(dataset_path, split_name)
            split = 0
        elif split_name == "test":
            split_dir = os.path.join(dataset_path, split_name)
            split = 1
        else:
            raise AttributeError(f"split is not train-val or test, but: {split_name}")

        for class_name in os.listdir(split_dir):
            path = os.path.join(split_dir, class_name)
            if os.path.isdir(path):
                if class_name not in classes.keys():
                    classes[class_name] = [0, 0]
                jpg_count = sum(1 for file in os.listdir(path) if file.lower().endswith('.jpg'))
                classes[class_name][split] = jpg_count
                classes[f'{dataset_name}'][split] += jpg_count  # add count of class to total of dataset

    count_jpg("train-val")
    count_jpg("test")
    return classes


def write_info(filename, d):
    # Open the file in write mode
    with open(filename, 'w', newline='') as file:
        # Create a writer object specifying the fieldnames
        fieldnames = ['dataset/class', 'train-val', 'test']
        writer = csv.writer(file)
        writer.writerow(fieldnames)

        for key, values in data.items():
            row = [key, str(values[0]), str(values[1])]
            writer.writerow(row)

    print(f"Data written to {filename}")


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


if __name__ == "__main__":
    for dataset in datasets:
        data = get_info(os.path.join(root_dir, dataset), dataset)
        write_info(f"{dataset}_info.csv", data)
        print(data)
