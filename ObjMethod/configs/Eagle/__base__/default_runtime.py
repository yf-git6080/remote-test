work_dir='work_dirs'

log_config = dict(  # register logger hook 的配置文件
    interval=50,  # 打印日志的间隔
    hooks=[
        dict(type='TextLoggerHook'),
        dict(type='TensorboardLoggerHook')
    ])  # 用于记录训练过程的记录器(logger)

dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
resume_from  = False
workflow = [('train', 1)]
opencv_num_threads = 0
mp_start_method = 'fork'
device='cuda'
