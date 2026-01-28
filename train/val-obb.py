from ultralytics import YOLO

model = YOLO("YOLO12-OBB/nano/weights/best.pt")

results = model.val(
                        data="DOTAv1.0.yaml",
                        split="test",
                        save_json = True,
                        imgsz = 1024,
                        batch = 1,
                        device = 6,
                        verbose = True,
                        exist_ok=True,
                        multi_scale=True,
                    )

