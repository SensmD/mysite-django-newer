from django.shortcuts import render,HttpResponse
import requests

# Create your views here.

def index(request):

    return HttpResponse("welcome")

def user_list(request):

    return render(request, 'vue第四天-2.html')

def tpl(request):
    name="sensmd"
    roles = ["ceo"]
    user_info = {"name": "sensmd", "salary": 100000, "role": "CTO"}

    return render(request, 'tpl.html', {"n1": name, "n2": roles, "n3": user_info})

def comments(req):
    for i in range(1):  # for循环遍历，批量爬取评论信息
        # 构造url，通过在网页不断点击下一页发现，url中只有page后数字随页数变化，批量遍历就是根据这个
        # url去掉了callback部分，因为这部分内没有有用数据，并且不去掉后面转换为json格式会有问题
        url = 'https://club.jd.com/comment/productPageComments.action?productId=3487483&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&rid=0&fold=1' % i
        # 构造headers
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'referer': 'https://item.jd.com/3487483.html',
        }
        response = requests.get(url, headers=headers).json()  # 字符串转换为json数据
        data = response["comments"]
        print(data)
    return render(req, 'comments.html', {"comments": data})

def something(request):
    # request是一个对象，封装了用户发送过来的所有请求相关数据
    return HttpResponse("welcome")
