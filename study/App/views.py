from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Customer, Goods


def add_goods(request, userid, goodid):
    customer = Customer.objects.get(id=userid)
    good = Goods.objects.get(id=goodid)
    customer.goods_set.add(good)
    return HttpResponse('成功添加商品{}'.format(good.name))


def add_customer(request, userid, goodid):
    customer = Customer.objects.get(id=userid)
    good = Goods.objects.get(id=goodid)
    good.customer_id.add(customer)
    return HttpResponse('成功添加消费者{}'.format(customer.name))


def remove_good(request, userid, goodid):
    customer = Customer.objects.get(id=userid)
    good = Goods.objects.get(id=goodid)
    customer.goods_set.remove(good)
    return HttpResponse('成功删除商品{}'.format(good.name))
