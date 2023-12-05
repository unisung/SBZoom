from django.shortcuts import render
from django.db.models import Sum

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


def home(request):
    return render(request, 'kangnam/home.html', {'guzip':guzip})

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
    q=GuModel.objects.filter(Q(guName="KANGNAM") & Q(code="KS"))

    qlist =[str(a.quarter) for a in q ]
    ilban =[int(a.ilban) for a in q]
    franchise =[int(a.franchise) for a in q]
    total=[int(a.total) for a in q]
    sales=[int(a.sales) for a in q]
    
    #print(qlist)
    #print(ilban)

    title=['강남구 서비스업 상권 현황','일반 점포','프렌차이즈','전체','매출액(억)']
     
    ana_zip = list(zip(qlist,ilban,franchise,total,sales))  

    context={}
    context['guzip'] = guzip
    context['title'] = title
    context['qlist'] = qlist
    context['ilban'] = ilban
    context['franchise'] = franchise
    context['total'] = total
    context['sales'] =  sales
    context['ana_zip'] = ana_zip

    return render(request, 'kangnam/service.html',context)

def retail(request):
    q=GuModel.objects.filter(Q(guName="KANGNAM") & Q(code="KR")) # 구명이 강남 이고 code가 KR(소매업)인 데이타

    qlist =[str(a.quarter) for a in q ]
    ilban =[int(a.ilban) for a in q]
    franchise =[int(a.franchise) for a in q]
    total=[int(a.total) for a in q]
    sales=[int(a.sales) for a in q]


    title=['강남구 소매업 상권 현황','일반 점포','프렌차이즈','전체','매출액(억)']
     
    ana_zip = list(zip(qlist,ilban,franchise,total,sales))  

    context={}
    context['guzip'] = guzip
    context['title'] = title
    context['qlist'] = qlist
    context['ilban'] = ilban
    context['franchise'] = franchise
    context['total'] = total
    context['sales'] =  sales
    context['ana_zip'] = ana_zip

    return render(request, 'kangnam/retail.html', context)


def total(request):
    q=GuModel.objects.filter(Q(guName="KANGNAM") & Q(code="KW")) # 구명이 강남 이고 code가 KW(전체)인 데이타

    qlist =[str(a.quarter) for a in q ]
    ilban =[int(a.ilban) for a in q]
    franchise =[int(a.franchise) for a in q]
    total=[int(a.total) for a in q]
    sales=[int(a.sales) for a in q]


    title=['강남구 전체 상권 현황','일반 점포','프렌차이즈','전체','매출액(억)']
     
    ana_zip = list(zip(qlist,ilban,franchise,total,sales))  

    context={}
    context['guzip'] = guzip
    context['title'] = title
    context['qlist'] = qlist
    context['ilban'] = ilban
    context['franchise'] = franchise
    context['total'] = total
    context['sales'] =  sales
    context['ana_zip'] = ana_zip

    return render(request, 'kangnam/total.html', context)
    
    
#----------------------------------------------------------------#    
    
def ilban(request):
    q1=GuModel.objects.filter(Q(guName="KANGNAM") & Q(code="KE")) # 구명이 강남 이고 code가 KE(외식업)인 데이타
    q2=GuModel.objects.filter(Q(guName="KANGNAM") & Q(code="KS")) # 구명이 강남 이고 code가 KS(서비스업)인 데이타
    q3=GuModel.objects.filter(Q(guName="KANGNAM") & Q(code="KR")) # 구명이 강남 이고 code가 KR(소매업)인 데이타   
    q4=GuModel.objects.filter(Q(guName="KANGNAM") & Q(code="KW")) # 구명이 강남 이고 code가 KW(외식+서비스+소매)인 데이타
    

    qlist =[str(a.quarter) for a in q1 ]
    eatOut =[int(a.ilban) for a in q1]   #외식업 일반 매출
    service =[int(a.ilban) for a in q2]  #서비스업 일반
    retail=[int(a.ilban) for a in q3]    #소매업 일반
    total=[int(a.sales) for a in q4]     #전체 일반


    title=['강남구 일반점포 현황','외식업','서비스업','소매업','전체일반점포']
     
    ana_zip = list(zip(qlist,eatOut,service,retail,total))  

    context={}
    context['guzip'] = guzip
    context['title'] = title
    context['qlist'] = qlist

    context['eatOut'] = eatOut
    context['service'] = service
    context['retail'] = retail
    context['total'] =  total

    context['ana_zip'] = ana_zip

    return render(request, 'kangnam/ilban.html', context)


def franchise(request):
    q1=GuModel.objects.filter(Q(guName="KANGNAM") & Q(code="KE")) # 구명이 강남 이고 code가 KE(외식업)인 데이타
    q2=GuModel.objects.filter(Q(guName="KANGNAM") & Q(code="KS")) # 구명이 강남 이고 code가 KS(서비스업)인 데이타
    q3=GuModel.objects.filter(Q(guName="KANGNAM") & Q(code="KR")) # 구명이 강남 이고 code가 KR(소매업)인 데이타   
    q4=GuModel.objects.filter(Q(guName="KANGNAM") & Q(code="KW")) # 구명이 강남 이고 code가 KW(외식+서비스+소매)인 데이타
    

    qlist =[str(a.quarter) for a in q1 ]
    eatOut =[int(a.franchise) for a in q1]   #외식업 프렌차이즈 매출
    service =[int(a.franchise) for a in q2]  #서비스업 프렌차이즈
    retail=[int(a.franchise) for a in q3]    #소매업 프렌차이즈
    total=[int(a.sales) for a in q4]     #전체 일반


    title=['강남구 프렌차이즈 현황','외식업','서비스업','소매업','전체일반점포']
     
    ana_zip = list(zip(qlist,eatOut,service,retail,total))  

    context={}
    context['guzip'] = guzip
    context['title'] = title
    context['qlist'] = qlist

    context['eatOut'] = eatOut
    context['service'] = service
    context['retail'] = retail
    context['total'] =  total

    context['ana_zip'] = ana_zip

    return render(request, 'kangnam/franchise.html', context)


def totalStores(request):
    q1=GuModel.objects.filter(Q(guName="KANGNAM") & Q(code="KE")) # 구명이 강남 이고 code가 KE(외식업)인 데이타
    q2=GuModel.objects.filter(Q(guName="KANGNAM") & Q(code="KS")) # 구명이 강남 이고 code가 KS(서비스업)인 데이타
    q3=GuModel.objects.filter(Q(guName="KANGNAM") & Q(code="KR")) # 구명이 강남 이고 code가 KR(소매업)인 데이타   
    q4=GuModel.objects.filter(Q(guName="KANGNAM") & Q(code="KW")) # 구명이 강남 이고 code가 KW(외식+서비스+소매)인 데이타
    

    qlist =[str(a.quarter) for a in q1 ]
    eatOut =[int(a.total) for a in q1]   #외식업 전체 매출
    service =[int(a.total) for a in q2]  #서비스업 전체
    retail=[int(a.total) for a in q3]    #소매업 전체
    total=[int(a.total) for a in q4]     #전체 


    title=['강남구 전체 점포 현황','외식업','서비스업','소매업','전체일반']
     
    ana_zip = list(zip(qlist,eatOut,service,retail,total))  

    context={}
    context['guzip'] = guzip
    context['title'] = title
    context['qlist'] = qlist

    context['eatOut'] = eatOut
    context['service'] = service
    context['retail'] = retail
    context['total'] =  total

    context['ana_zip'] = ana_zip

    return render(request, 'kangnam/totalStores.html', context)


def totalSales(request):
    q1=GuModel.objects.filter(Q(guName="KANGNAM") & Q(code="KE")) # 구명이 강남 이고 code가 KE(외식업)인 데이타
    q2=GuModel.objects.filter(Q(guName="KANGNAM") & Q(code="KS")) # 구명이 강남 이고 code가 KS(서비스업)인 데이타
    q3=GuModel.objects.filter(Q(guName="KANGNAM") & Q(code="KR")) # 구명이 강남 이고 code가 KR(소매업)인 데이타   
    q4=GuModel.objects.filter(Q(guName="KANGNAM") & Q(code="KW")) # 구명이 강남 이고 code가 KW(외식+서비스+소매)인 데이타
    

    qlist =[str(a.quarter) for a in q1 ]
    eatOut =[int(a.sales) for a in q1]   #외식업 전체 매출
    service =[int(a.sales) for a in q2]  #서비스업 전체
    retail=[int(a.sales) for a in q3]    #소매업 전체
    total=[int(a.sales) for a in q4]     #전체 


    title=['강남구 전체 점포 현황','외식업 매출액(억)','서비스업 매출액(억)','소매업 매출액(억)','전체 매출액(억)']
     
    ana_zip = list(zip(qlist,eatOut,service,retail,total))  

    context={}
    context['guzip'] = guzip
    context['title'] = title
    context['qlist'] = qlist

    context['eatOut'] = eatOut
    context['service'] = service
    context['retail'] = retail
    context['total'] =  total

    context['ana_zip'] = ana_zip

    return render(request, 'kangnam/totalSales.html', context)

