from django.shortcuts import render
from .forms import UploadFileForm
from .models import Csv_read
from .applications.calc import diversity_calc
import os

def calculator(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        # 過去のファイルの削除
        if form.is_valid():
            if os.path.isfile("/django/project/media/graph.svg"):
                os.remove("/django/project/media/graph.svg")
            else:
                pass
            
            csv_data = form.save()
            pk = csv_data.pk - 1
            if Csv_read.objects.filter(pk=pk).exists():
                Csv_read.objects.get(pk=pk).delete()
            else:
                pass

            # 多様度指数算出関数の呼び出し
            H, graph = diversity_calc(csv_data.file)

            # アップロードされたCSVファイルの形式が正しくなければトップページヘ
            if H == "error":
                form = UploadFileForm()
                return render(request, 'calculator/home.html', {"form": form})
            else:
                return render(request, 'calculator/diversity_result.html', {"form": form, "H": H, "graph": graph})


    else:
        form = UploadFileForm()

    return render(request, 'calculator/home.html', {"form": form})