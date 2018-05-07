class Settings():
    """存储游戏设置"""
    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        self.ship_speed_factor = 2.5 # 飞船的移动速度
