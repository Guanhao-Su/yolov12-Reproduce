import os

DOTA_CLASSES = [
    'plane',
    'ship',
    'storage-tank',
    'baseball-diamond',
    'tennis-court',
    'basketball-court',
    'ground-track-field',
    'harbor',
    'bridge',
    'large-vehicle',
    'small-vehicle',
    'helicopter',
    'roundabout',
    'soccer-ball-field',
    'swimming-pool'
]

CLASS2ID = {name: idx for idx, name in enumerate(DOTA_CLASSES)}

def classes_to_id(txt_path, save_path):
    with open(txt_path, 'r') as f:
        lines = f.readlines()

    id_lines = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) < 9:  # 忽略无效行
            continue
        cls_name = parts[8]
        if cls_name not in CLASS2ID:
            continue
        cls_id = CLASS2ID[cls_name]
        id_lines.append(f"{cls_id} {parts[0]} {parts[1]} {parts[2]} {parts[3]} {parts[4]} {parts[5]} {parts[6]} {parts[7]}")

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, 'w') as f:
        f.write("\n".join(id_lines))

label_DOTA_dir_train = "datasets/DOTAv1.0/labels/train"
label_yolo_dir_train = "datasets/DOTAv1.0-pre/labels/train"
label_DOTA_dir_val = "datasets/DOTAv1.0/labels/val"
label_yolo_dir_val = "datasets/DOTAv1.0-pre/labels/val"

if __name__ == "__main__":
    for txt_file in os.listdir(label_DOTA_dir_train):
        if not txt_file.endswith('.txt'):
            continue

        classes_to_id(
            os.path.join(label_DOTA_dir_train, txt_file),
            os.path.join(label_yolo_dir_train, txt_file)
        )

    for txt_file in os.listdir(label_DOTA_dir_val):
        if not txt_file.endswith('.txt'):
            continue

        classes_to_id(
            os.path.join(label_DOTA_dir_val, txt_file),
            os.path.join(label_yolo_dir_val, txt_file)
        )

