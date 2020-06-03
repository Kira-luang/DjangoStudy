# Django第三方库的使用

# 1.内存流(运用内存)
'''
StringIO -> 内存中读写str(针对文本)
BytesIO-> 内存中读写Bytes(针对图片/视频)
'''

# 2.验证码图片简单实现过程
'''
需要Pillow,自实现一个从而了解原理
先生成一张画布:canvas = Image.new(mode, size, color)
生成一个画笔:image_draw = ImageDraw.ImageDraw(im=canvas, mode=mode)
画文字:ImageDraw().text() -> 要求坐标和内容
生成缓存空间:buffer = BytesIO() -> 要把图片生成到内存(如果生成在本地,删除会麻烦),可以自然删除
画布存储到缓存空间:canvas.save(buffer)
把缓存空间的图片(本质是字节)拿出来返回:HttpResponse(buffer.getvalue(), content_type='image/png')->一定要声明类型
'''

# 3.加强验证码功能
'''
设置画笔的字体和大小:image_font = ImageFont.truetype(font, size) -> 导入静态文件,在里面放字体文件
mage_draw.text的参数fill就是设置color
image_draw.point(xy, fill) -> xy是横纵坐标(必须设置不一样),fill一样是颜色

Django自带各种第三方验证码库,可以自行查找
'''
