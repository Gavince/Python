class MusicPlay():
    """

    """
    def __new__(cls, *args, **kwargs):

        #1.创建对象，自动调用
        print("new方法")

        #2.为对象分配空间
        instance = super().__new__(cls)

        #3.放回对象的引用
        return instance

    def __init__(self):
        print("播放器的使用")


music = MusicPlay()
mp4 = MusicPlay()
print(id(music))
print(id(mp4))
