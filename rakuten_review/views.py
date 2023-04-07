from django.shortcuts import render,redirect
from django.views import View

# 1回のリクエストでまとめてデータを送信する
# https://noauto-nolife.com/post/django-multi-send/


from .models import WeeklyRanking
from .forms import WeeklyRankingForm


class IndexView(View):
    def get(self, request, *args, **kwargs):





        return render(request, "rakuten_review/index.html")
    def post(self, request, *args, **kwargs):

        update_dates    = request.POST.getlist("update_date")
        names           = request.POST.getlist("name")
        prices          = request.POST.getlist("price")
        averages        = request.POST.getlist("average")
        volumes         = request.POST.getlist("volume")
        ranks           = request.POST.getlist("rank")
        shop_codes      = request.POST.getlist("shop_code")
        item_urls       = request.POST.getlist("item_url")

        for update_date,name,price,average,volume,rank,shop_code,item_url in zip(update_dates,names,prices,averages,volumes,ranks,shop_codes,item_urls):

            dic                 = {}
            dic["update_date"]  = update_date
            dic["name"]         = name 
            dic["price"]        = price
            dic["average"]      = average   
            dic["volume"]       = volume
            dic["rank"]         = rank
            dic["shop_code"]    = shop_code
            dic["item_url"]     = item_url


            form    = WeeklyRankingForm(dic)

            if form.is_valid():
                print("保存します。")
                form.save()

        return redirect("rakuten_review:index")

index   = IndexView.as_view()


