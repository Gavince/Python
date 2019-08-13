class MusicPlayer(object):

    instance = None

    #记录初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):

        #1 判断类属性是否为空对象
        if cls.instance is None:
            #2 调用父类的方法 为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3 返回引用
        return cls.instance

    def __init__(self): #可以实现一次初始化实例对象

        # 1 判断是否已经初始化
        if MusicPlayer.init_flag:
            return

        print("初始化播放器！")
        # 2 修改播放器初始化的信号值
        MusicPlayer.init_flag = True


Player1 = MusicPlayer()
print(Player1)

Player2 = MusicPlayer()
print(Player2)