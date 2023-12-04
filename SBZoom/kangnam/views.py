from django.shortcuts import render

# Create your views here.
import pandas as pd
# 파이썬 시각화 패키지 불러오기
import os
from .models import GuModel
from django.db.models import Q



# Create your views here.
from django.http import HttpResponse

gulist = ['종로구','용산구','성동구','광진구','동대문구','중구',
              '중랑구','성북구','강북구','도봉구','노원구','은평구','구로구',
              '서대문구','마포구','강서구','양천구','금천구','영등포구',
              '동작구','관악구','서초구','강남구','송파구','강동구'             
              ]
gulist1 = ['jongno','yongsan','seongdong','kwangjin','dongdaemoon','joonggu',
              'joonrang','seongbuk','kangbuk','dobong','nowon','eunpyung','guro',
              'seodaemoon','mapo','kangseo','yangcheon','keumcheon','yeundungpo',
              'dongjak','gwanwak','seocho','kangnam','songpa','kangdong'             
              ]
guzip = list(zip(gulist1,gulist))


def index(request):
    return render(request, 'kangnam/index.html', {'guzip':guzip})

def eatOut(request):
    q=GuModel.objects.filter(Q(guName="KANGNAM") & Q(code="KE"))
    
    qlist =[str(a.quarter) for a in q ]
    ilban =[int(a.ilban) for a in q]
    franchise =[int(a.franchise) for a in q]
    total=[int(a.total) for a in q]
    sales=[int(a.sales) for a in q]
    
    #print(qlist)
    #print(ilban)

    title=['강남구 외식업 상권 현황','일반 점포','프렌차이즈','전체','매출액(억)']
     
    ana_zip = list(zip(qlist,ilban,franchise,total,sales))  

    
    return render(request, 'kangnam/eatOut.html', {'guzip':guzip,'title':title, 'qlist':qlist, 'ilban':ilban,'franchise':franchise,'total':total,'sales':sales,'ana_zip':ana_zip})
    
    
def service(request):
    return render(request, 'kangnam/service.html', {'guzip':guzip})

def retail(request):
    return render(request, 'kangnam/retail.html', {'guzip':guzip})


def total(request):
    return render(request, 'kangnam/total.html', {'guzip':guzip})
    
    
def ilban(request):
    return render(request, 'kangnam/ilban.html', {'guzip':guzip})

def franchise(request):
    return render(request, 'kangnam/franchise.html', {'guzip':guzip})

def totalStores(request):
    return render(request, 'kangnam/totalStores.html', {'guzip':guzip})

def totalSales(request):
    return render(request, 'kangnam/totalSales.html', {'guzip':guzip})
