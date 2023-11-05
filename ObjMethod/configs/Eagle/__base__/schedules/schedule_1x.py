max_epochs = 40

optimizer=dict(
        type='AdamW',
        lr=0.0025,
        weight_decay=0.0001,
        betas=(0.9, 0.999)
)

optimizer_config = dict(  # optimizer hook 的配置文件
    grad_clip=dict(
        max_norm=35,
        norm_type=2))

lr_config = dict(  # 学习率调整配置，用于注册 LrUpdater hook
    policy='CosineAnnealing',  # 调度流程(scheduler)的策略
    warmup='linear',  # 预热(warmup)策略，也支持 `exp` 和 `constant`
    warmup_iters=1000,  # 预热的迭代次数
    warmup_ratio=0.3333333333333333,  # 用于预热的起始学习率的比率
    min_lr_ratio=1e-5,
)  # 衰减学习率的起止回合数

evaluation = dict(  # evaluation hook 的配置
    interval=max_epochs-1,  # 验证的间隔
    metric='mAP')  # 验证期间使用的指标

runner = dict(
    type='EpochBasedRunner',  # 将使用的 runner 的类别 (例如 IterBasedRunner 或 EpochBasedRunner)
    max_epochs=max_epochs) # runner 总回合(epoch)数， 对于 IterBasedRunner 使用 `max_iters`

checkpoint_config = dict(  # checkpoint hook 的配置文件
    interval=1)  # 保存的间隔是 1