__author__ = 'Kuba'


from PIL import Image, ImageDraw
from threading import Thread
import math

class Maintrin(Thread):
    def __init__(self, image, depth, max_depth, x, y, angle, length, width,
                 subtrin_length, subtrin_resize,
                 subtrin_width, subtrin_width_loss, ):
        super(Maintrin, self).__init__()
        self.image = image
        self.max_depth = max_depth
        self.depth = depth
        self.x = x
        self.y = y
        self.angle = angle
        self.length = length
        self.width = width
        self.subtrin_length = subtrin_length
        self.subtrin_resize = subtrin_resize
        self.subtrin_width = subtrin_width
        self.subtrin_width_loss = subtrin_width_loss
        self.rad = math.pi / 180

    def run(self):
        angle = 120
        next_x = self.x + math.cos(self.angle * self.rad) * self.length
        next_y = self.y + math.sin(self.angle * self.rad) * self.length
        self.image.line((self.x, self.y, next_x, next_y), fill=0, width=self.width)
        next2_x = next_x + math.cos((self.angle-angle) * self.rad) * self.length
        next2_y = next_y + math.sin((self.angle-angle) * self.rad) * self.length
        self.image.line((next_x, next_y, next2_x, next2_y), fill=0, width=self.width)
        self.image.line((next2_x, next2_y, self.x, self.y), fill=0, width=self.width)

        if ++self.depth is not self.max_depth:

            trin1 = Maintrin(self.image, self.depth + 1, self.max_depth, next_x, next_y,
                               self.angle-angle, self.subtrin_length, self.subtrin_width,
                               self.subtrin_length * self.subtrin_resize,
                               self.subtrin_resize,
                               self.subtrin_width - self.subtrin_width_loss,
                               self.subtrin_width_loss )

            trin2 = Maintrin(self.image, self.depth + 1, self.max_depth, next2_x, next2_y,
                               self.angle-angle*2, self.subtrin_length, self.subtrin_width,
                               self.subtrin_length * self.subtrin_resize,
                               self.subtrin_resize,
                               self.subtrin_width - self.subtrin_width_loss,
                               self.subtrin_width_loss )

            trin3 = Maintrin(self.image, self.depth + 1, self.max_depth, self.x, self.y,
                               self.angle, self.subtrin_length, self.subtrin_width,
                               self.subtrin_length * self.subtrin_resize,
                               self.subtrin_resize,
                               self.subtrin_width - self.subtrin_width_loss,
                               self.subtrin_width_loss )

            trin1.start()
            trin1.join()
            trin2.start()
            trin2.join()
            trin3.start()
            trin3.join()


im = Image.new('RGB', (2000, 2000), (255, 255, 255, 255))
draw = ImageDraw.Draw(im)
s = Maintrin(draw,         #image
          0,            #current depth
          12,           #max depth
          0,            #position x
          2000,         #position y
          0,            #angle
          2000,          #length
          12,           #width
          1000,          #subtrin length
          0.5,          #subtrin resize
          12,           #subtrin width
          1)            #subtrin width loss

s.start()
s.join()

im.save("result.ppm", "ppm")