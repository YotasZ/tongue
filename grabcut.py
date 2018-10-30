import numpy as np
import cv2

#点击1退出图像显示
class picture_dealing:
    # 对图像的处理，包括基本数据元素：图片
    # 基本成员函数：对图片的压缩，对图片的切割，对图片色泽及颜色的判断
    # 实现对图片的处理效果：
    # 判断图片的大小，如果图片太大，调用图片的压缩函数实现图片的压缩
    # 选定图片的前景，可以自行输入，也可以在图片上进行点点标记自动得到图片的坐标
    # 切割图片
    # 对切割后图片的部分色泽进行分析
    def __init__(self, picName):
        self.img = cv2.imread(picName)

    def get_info(self):#获取前景的x,y,w,h
        self.loc=[]
        self.xloc=[]
        self.yloc=[]
        def get_loc(event,x,y,flags,param):
            if event==cv2.EVENT_LBUTTONDOWN:
                self.loc.append((x,y))
        cv2.namedWindow('image')
        cv2.setMouseCallback('image',get_loc)
        while(1):
            cv2.imshow('image',self.img)
            k=cv2.waitKey(10)
            if k==ord('1'):
                break
        cv2.destroyAllWindows()
        for i in self.loc:
            self.xloc.append(i[0])
            self.yloc.append(i[1])
        self.x_max=max(self.xloc)
        self.x_min=min(self.xloc)
        self.y_max=max(self.yloc)
        self.y_min=min(self.yloc)
        self.width=self.x_max-self.x_min
        self.height=self.y_max-self.y_min
        return




    def grabcut(self):
        rect = (self.x_min, self.y_min, self.width, self.height)
        mask = np.zeros(self.img.shape[:2], np.uint8)
        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)
        cv2.grabCut(self.img, mask, rect, bgdModel, fgdModel, 10, cv2.GC_INIT_WITH_RECT)
        mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
        self.cutted_pic = self.img * mask2[:, :, np.newaxis]

    def show(self):
        while (1):
            cv2.imshow('image', self.cutted_pic)
            k = cv2.waitKey(10)
            if k == ord('1'):
                break
        cv2.destroyAllWindows()

    def save(self,filename):
        cv2.imwrite(filename,self.cutted_pic)

pic=picture_dealing('1.jpg')
pic.get_info()
pic.grabcut()
pic.show()

