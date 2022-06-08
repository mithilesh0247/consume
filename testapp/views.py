from django.shortcuts import render

# Create your views here.
import requests
def get_geographic_info(request):
    ip=request.META.get('HTTP_X_FORWARDED_FOR',"") or request.META.get("REMOTE_ADDR")
    #url='http://api.ipstack.com/'+str(ip)+"?access_key=874738426ce71068a985faabd6641d3f"
    url='http://api.ipstack.com/'+str(ip)+"?access_key=7818eae677e0cc79fb1ef0d882baabcb"
    response=requests.get(url)
    data=response.json()
    print(data)
    return render(request,'info.html',{'data':data})
    