# 图片上传存储与查询
'''
以用户名和头像为例:
第一步,设置本地储存位置 -> Media_Root
第二步,与数据库映射关系的models -> 需要install Pillow
第三步,利用models创建用户名与头像路劲关系 -> 创造实例存储
第四部,通过用户名来查询其头像 -> 通过名字查找路劲,然后再调用服务器路劲
'''
