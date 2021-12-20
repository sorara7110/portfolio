from django.shortcuts import render
from .forms import UploadFileForm
from .models import Csv_read
from .applications.calc import diversity_calc
import os

def calculator(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        # リクエストがポストだった場合の処理
        # 過去のファイルの削除
        if form.is_valid():

            # 過去のグラフが残っていれば削除
            if os.path.isfile("/django/project/media/graph.svg"):
                os.remove("/django/project/media/graph.svg")

            # 過去の表が残っていれば削除
            if os.path.isfile("/django/project/media/table.svg"):
                os.remove("/django/project/media/table.svg")

            # 過去のcsvファイルが残っていれば削除
            csv_data = form.save()
            pk = csv_data.pk - 1
            if Csv_read.objects.filter(pk=pk).exists():
                Csv_read.objects.get(pk=pk).delete()

            # 多様度指数算出関数の呼び出し
            graph, table = diversity_calc(csv_data.file)

            # アップロードされたcsvファイルの形式が正しくなければトップページヘ
            if graph != "error":
                return render(request, 'calculator/diversity_result.html', {"form": form, "graph": graph, "table": table})
    
    form = UploadFileForm()
    return render(request, 'calculator/home.html', {"form": form})