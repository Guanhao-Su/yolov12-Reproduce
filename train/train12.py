from ultralytics import YOLO


from ultralytics import YOLO
import torch

#相关参数部分
def get_train_yolov12n_args():
    return {
        'task': 'detect',
        'mode': 'train',
        'model': 'yolo12n.yaml',
        'data': 'coco.yaml',
        'epochs': 600,
        'time': None,
        'patience': 100,
        'batch': 32,
        'imgsz': 640,
        'save': True,
        'save_period': -1,
        'cache': 'disk',
        'device': 7,
        'workers': 8,
        'project': 'YOLO12-HBB',
        'name': 'nano',
        'exist_ok': True,
        'pretrained': True,
        'optimizer': 'auto',
        'verbose': True,
        'seed': 0,
        'deterministic': True,
        'single_cls': False,
        'rect': False,
        'cos_lr': False,
        'close_mosaic': 10,
        'resume': False,
        'amp': True,
        'fraction': 1.0,
        'profile': False,
        'freeze': None,
        'multi_scale': False,
        'overlap_mask': True,
        'mask_ratio': 4,
        'dropout': 0.0,
        'val': True,
        'split': 'val',
        'save_json': False,
        'save_hybrid': False,
        'iou': 0.7,
        'max_det': 300,
        'half': False,
        'dnn': False,
        'plots': True,
        'vid_stride': 1,
        'stream_buffer': False,
        'visualize': False,
        'augment': False,
        'agnostic_nms': False,
        'classes': None,
        'retina_masks': False,
        'embed': None,
        'show': False,
        'save_frames': False,
        'save_txt': False,
        'save_conf': False,
        'save_crop': False,
        'show_labels': True,
        'show_conf': True,
        'show_boxes': True,
        'line_width': None,
        'lr0': 0.01,
        'lrf': 0.0001,
        'momentum': 0.937,
        'weight_decay': 0.0005,
        'warmup_epochs': 3.0,
        'warmup_momentum': 0.8,
        'warmup_bias_lr': 0.0,
        'box': 7.5,
        'cls': 0.5,
        'dfl': 1.5,
        'pose': 12.0,
        'kobj': 1.0,
        'label_smoothing': 0.0,
        'nbs': 64,
        'hsv_h': 0.015,
        'hsv_s': 0.7,
        'hsv_v': 0.4,
        'degrees': 0.0,
        'translate': 0.1,
        'scale': 0.5,
        'shear': 0.0,
        'perspective': 0.0,
        'flipud': 0.0,
        'fliplr': 0.5,
        'bgr': 0.0,
        'mosaic': 1.0,
        'mixup': 0.0,
        'copy_paste': 0.1,
        'copy_paste_mode': 'flip',
        'auto_augment': 'randaugment',
        'erasing': 0.4,
        'crop_fraction': 1.0,
        'cfg': None,
        'tracker': 'botsort.yaml',
        'verbose': True
    }



if __name__ == "__main__":
    args = get_train_yolov12n_args()
    model = YOLO(args['model'])
    model.train(**args)

# 评估模型在验证集上的性能
metrics = model.val(
    val= True, # (bool) validate/test during training
    split= "val", # (str) dataset split to use for validation, i.e. 'val', 'test' or 'train'
    save_json= False, # (bool) save results to JSON file
    iou= 0.7, # (float) intersection over union (IoU) threshold for NMS
    max_det= 300, # (int) maximum number of detections per image
    half= False, # (bool) use half precision (FP16)
    dnn= False, # (bool) use OpenCV DNN for ONNX inference
    plots= True # (bool) save plots and images during train/val
)
# 对图像执行目标检测
# model.args["batch"] = 64
# model.args["device"] = 0
# results = model("path/to/image.jpg")  # 对图像进行预测
# results[0].show()  # 显示结果

# 将模型导出为 ONNX 格式以进行部署
path = model.export(format="onnx")  # 返回导出模型的路径