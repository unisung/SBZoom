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

gulist = ['강남구','강동구','강북구','강서구','관악구','광진구','구로구','금천구',
          '노원구','도봉구','동대문구','동작구','마포구','서대문구','서초구','성동구',
          '성북구','송파구','양천구','영등포','용산구','은평구','종로구','중구','중랑구'
          ]
gulist1 = ['kangnam','gangdong','gangbuk','gangseo','gwanak','gwangjin','guro','geumcheon',
	   'nowon','dobong','dongdaemun','dongjak','mapo','seodaemun','seocho','seongdong',
	   'seongbuk','songpa','yangcheon','yeongdeungpo','yongsan','eunpyeong','jongro','junggu','jungnang'            
           ]
guzip = list(zip(gulist1,gulist))

menuNames=["외식업","서비스업","소매업","전체","일반","프렌차이즈","점포전체","전체매출"]
menus=["eatOut","service","retail","total","ilban","franchise","totalStores","totalSales"]
menuzip=list(zip(menuNames,menus))

# /SBZoom/songpa/
def index(request):
    context={}
    context['guzip'] = guzip
    context['menuzip'] = menuzip

    return render(request, 'songpa/index.html', context)

# /SBZoom/songpa/eatOut
def eatOut(request):
    q=GuModel.objects.filter(Q(code="E")) # songpa_gumodel 에서 code가 E(외식업)인 데이타
    
    qlist =[str(a.quarter) for a in q ]
    ilban =[int(a.ilban) for a in q]
    franchise =[int(a.franchise) for a in q]
    total=[int(a.total) for a in q]
    sales=[int(a.sales) for a in q]

    title=['송파구 외식업 상권 현황','일반 점포','프렌차이즈','전체','매출액(억)']
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
    context['menuzip'] = menuzip

    return render(request, 'songpa/eatOut.html', context)
    
# /SBZoom/songpa/service    
def service(request):
    q=GuModel.objects.filter(Q(code="S")) # songpa_gumodel 에서 code가 S(서비스업)인 데이타

    qlist =[str(a.quarter) for a in q ]
    ilban =[int(a.ilban) for a in q]
    franchise =[int(a.franchise) for a in q]
    total=[int(a.total) for a in q]
    sales=[int(a.sales) for a in q]
    
    #print(qlist)
    #print(ilban)

    title=['송파구 서비스업 상권 현황','일반 점포','프렌차이즈','전체','매출액(억)']
     
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
    context['menuzip'] = menuzip

    return render(request, 'songpa/service.html',context)

# /SBZoom/songpa/retail
def retail(request):
    q=GuModel.objects.filter(Q(code="R")) # songpa_gumodel에서 code가 R(소매업)인 데이타

    qlist =[str(a.quarter) for a in q ]
    ilban =[int(a.ilban) for a in q]
    franchise =[int(a.franchise) for a in q]
    total=[int(a.total) for a in q]
    sales=[int(a.sales) for a in q]


    title=['송파구 소매업 상권 현황','일반 점포','프렌차이즈','전체','매출액(억)']
     
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
    context['menuzip'] = menuzip

    return render(request, 'songpa/retail.html', context)

# /SBZoom/songpa/total
def total(request):
    q=GuModel.objects.filter( Q(code="W")) # songpa_gumodel에서 code가 W(전체)인 데이타

    qlist =[str(a.quarter) for a in q ]
    ilban =[int(a.ilban) for a in q]
    franchise =[int(a.franchise) for a in q]
    total=[int(a.total) for a in q]
    sales=[int(a.sales) for a in q]


    title=['송파구 전체 상권 현황','일반 점포','프렌차이즈','전체','매출액(억)']
     
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
    context['menuzip'] = menuzip

    return render(request, 'songpa/total.html', context)
    
    
#----------------------------------------------------------------#    
 
# /SBZoom/songpa/ilban  
def ilban(request):
    q1=GuModel.objects.filter(Q(code="E")) # songpa_gumodel에서 code가  E(외식업)인 데이타
    q2=GuModel.objects.filter(Q(code="S")) # songpa_gumodel에서 code가  S(서비스업)인 데이타
    q3=GuModel.objects.filter(Q(code="R")) # songpa_gumodel에서 code가  R(소매업)인 데이타   
    q4=GuModel.objects.filter(Q(code="W")) # songpa_gumodel에서 code가  W(외식+서비스+소매)인 데이타
    

    qlist =[str(a.quarter) for a in q1 ]
    eatOut =[int(a.ilban) for a in q1]   #외식업 일반 매출
    service =[int(a.ilban) for a in q2]  #서비스업 일반
    retail=[int(a.ilban) for a in q3]    #소매업 일반
    total=[int(a.sales) for a in q4]     #전체 일반


    title=['송파구 일반점포 현황','외식업','서비스업','소매업','전체일반점포']
     
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
    context['menuzip'] = menuzip

    return render(request, 'songpa/ilban.html', context)

# /SBZoom/songpa/franchise
def franchise(request):
    q1=GuModel.objects.filter(Q(code="E")) # songpa_gumodel에서 code가 E(외식업)인 데이타
    q2=GuModel.objects.filter(Q(code="S")) # songpa_gumodel에서 code가 S(서비스업)인 데이타
    q3=GuModel.objects.filter(Q(code="R")) # songpa_gumodel에서 code가 R(소매업)인 데이타   
    q4=GuModel.objects.filter(Q(code="W")) # songpa_gumodel에서 code가 W(외식+서비스+소매)인 데이타
    

    qlist =[str(a.quarter) for a in q1 ]
    eatOut =[int(a.franchise) for a in q1]   #외식업 프렌차이즈 매출
    service =[int(a.franchise) for a in q2]  #서비스업 프렌차이즈
    retail=[int(a.franchise) for a in q3]    #소매업 프렌차이즈
    total=[int(a.sales) for a in q4]     #전체 일반


    title=['송파구 프렌차이즈 현황','외식업','서비스업','소매업','전체일반점포']
     
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
    context['menuzip'] = menuzip

    return render(request, 'songpa/franchise.html', context)

# /SBZoom/songpa/totalStores
def totalStores(request):
    q1=GuModel.objects.filter(Q(code="E")) # songpa_gumodel에서 code가 E(외식업)인 데이타
    q2=GuModel.objects.filter(Q(code="S")) # songpa_gumodel에서 code가 S(서비스업)인 데이타
    q3=GuModel.objects.filter(Q(code="R")) # songpa_gumodel에서 code가 R(소매업)인 데이타   
    q4=GuModel.objects.filter(Q(code="W")) # songpa_gumodel에서 code가 W(외식+서비스+소매)인 데이타
    

    qlist =[str(a.quarter) for a in q1 ]
    eatOut =[int(a.total) for a in q1]   #외식업 전체 매출
    service =[int(a.total) for a in q2]  #서비스업 전체
    retail=[int(a.total) for a in q3]    #소매업 전체
    total=[int(a.total) for a in q4]     #전체 


    title=['송파구 전체 점포 현황','외식업','서비스업','소매업','전체일반']
     
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
    context['menuzip'] = menuzip

    return render(request, 'songpa/totalStores.html', context)

# /SBZoom/songpa/totalSales
def totalSales(request):
    q1=GuModel.objects.filter(Q(code="E")) # songpa_gumodel에서 code가 E(외식업)인 데이타
    q2=GuModel.objects.filter(Q(code="S")) # songpa_gumodel에서 code가 S(서비스업)인 데이타
    q3=GuModel.objects.filter(Q(code="R")) # songpa_gumodel에서 code가 R(소매업)인 데이타   
    q4=GuModel.objects.filter(Q(code="W")) # songpa_gumodel에서 code가 W(외식+서비스+소매)인 데이타
    

    qlist =[str(a.quarter) for a in q1 ]
    eatOut =[int(a.sales) for a in q1]   #외식업 전체 매출
    service =[int(a.sales) for a in q2]  #서비스업 전체
    retail=[int(a.sales) for a in q3]    #소매업 전체
    total=[int(a.sales) for a in q4]     #전체 


    title=['송파구 전체 점포 현황','외식업 매출액(억)','서비스업 매출액(억)','소매업 매출액(억)','전체 매출액(억)']
     
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
    context['menuzip'] = menuzip

    return render(request, 'songpa/totalSales.html', context)

