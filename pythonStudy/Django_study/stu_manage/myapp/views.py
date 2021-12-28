from django.shortcuts import render
from django.http import HttpResponse

from myapp.models import Users


def index(request):
    try:
        list = Users.objects.filter(id__in = [1, 3, 5])
        s = ','.join([vo.name for vo in list])

        # 修改(将id值为5的age值改为30)
        # ob = Users.objects.get(id=5)
        # ob.age = 30
        # ob.save()

        # 删除(删除id为3的信息)
        # ob = Users.objects.get(id=3)
        # ob.delete()

        return HttpResponse(s)
    except:
        return HttpResponse("没有找到对应的信息！")


# 浏览用户信息
def indexUsers(request):
    # 执行数据查询，并放置到模板中
    list = Users.objects.all()
    context = {"stulist": list}
    return render(request, "myapp/users/index.html", context)


# 加载添加信息表单
def addUsers(request):
    return render(request, "myapp/users/add.html")


# 执行信息添加操作
def insertUsers(request):
    try:
        ob = Users()
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.phone = request.POST['phone']
        ob.save()
        context = {'info': '添加成功！'}
    except:
        context = {'info': '添加失败！'}
    return render(request, "myapp/users/info.html", context)

# # 执行信息添加操作
# def inserttext(request):
#     ob = Users()
#     ob.name = '丽丽'
#     ob.age = 19
#     ob.phone = 12134643
#     ob.save()
#     ob = Users()
#     ob.name = '潇潇'
#     ob.age = 28
#     ob.phone = 66699988
#     ob.save()
#     ob = Users()
#     ob.name = '乐乐'
#     ob.age = 26
#     ob.phone = 45488858
#     ob.save()
#     ob = Users()
#     ob.name = '洋洋'
#     ob.age = 24
#     ob.phone = 411516546156
#     ob.save()
#     return HttpResponse('添加成功')


# 执行信息删除操作
def delUsers(request, uid):
    try:
        ob = Users.objects.get(id = uid)
        ob.delete()
        context = {'info': '删除成功！'}
    except:
        context = {'info': '删除失败！'}
    return render(request, "myapp/users/info.html", context)


# 加载信息编辑表单
def editUsers(request, uid):
    try:
        ob = Users.objects.get(id = uid)
        context = {'user': ob}
        return render(request, "myapp/users/edit.html", context)
    except:
        context = {'info': '没有找到要修改的信息！'}
        return render(request, "myapp/users/info.html", context)


# 执行信息编辑操作
def updateUsers(request):
    try:
        ob = Users.objects.get(id = request.POST['id'])
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.phone = request.POST['phone']
        # ob.addtime = datetime.now
        ob.save()
        context = {'info': '修改成功！'}
    except:
        context = {'info': '修改失败！'}
    return render(request, "myapp/users/info.html", context)
