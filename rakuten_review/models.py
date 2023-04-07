from django.db import models

# Create your models here.


class WeeklyRanking(models.Model):

    # ランキングの 2023年3月29日(水)更新 の部分を記録する
    update_date = models.DateField(verbose_name="ランキング更新日")

    # 254バイトの文字数制限
    # 無制限のTextFieldを使う選択肢もある。(制限がないだけDBのパフォーマンスが悪い)
    name        = models.CharField(verbose_name="商品名",max_length=254)
    price       = models.IntegerField(verbose_name="価格")
    average     = models.FloatField(verbose_name="レビュー平均点")
    volume      = models.IntegerField(verbose_name="レビュー件数")
    rank        = models.IntegerField(verbose_name="順位")

    # 要検証:50文字で足りる？
    shop_code   = models.CharField(verbose_name="ショップコード",max_length=50)
    item_url    = models.URLField(verbose_name="商品URL")

