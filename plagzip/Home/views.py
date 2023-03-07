from django.shortcuts import render,HttpResponse
import os,subprocess
from django.conf import settings

# Create your views here.
def Index(request):
    return render(request,'Index.html')

def upload_file(request):
    if request.method == 'POST':
        # retreiving zip file name 
        try:
            uploaded_file = request.FILES['file']
            filen_name = uploaded_file.name
        except:
            filen_name = 'Download'
        if not request.FILES:
            subprocess.call(f'"window.exe"') 
            with open('report.txt','w') as f:
                f.write("Files not there...")
                f.close()
            return render(request, 'index.html',context)
        else:
            my_text = "Please Wait while File uploading..."
            context = {'message': my_text}
            uploaded_file = request.FILES['file']
            ##########################################
            with open('report.txt','w') as f:
                f.write("Files are uploadng...")
                f.close()
            ##########################################

            #  Moving File in raw path of plagfiles
            if len(os.listdir(r'D:\Plag\Raw')) > 0:
                pass
            else:
                with open(f'D:\Plag\Raw\{filen_name.replace(".zip","")}.zip', 'wb+') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)
            subprocess.Popen('window.exe')
            return render(request, 'index.html',context)
    else:
        return render(request, 'index.html')
        
def download_file(request):
    filen_name = 'Download'
    filename = f'D:\Plag\Download\{filen_name}.zip'
    # Determine the full path to the file
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    if file_path:
        # Open the file for reading as binary data
        with open(file_path, 'rb') as f:
            # Create a response object with the file contents
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            # Set the content-disposition header to force a file download
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
    else:
        return render(request, 'index.html')

def update_text(request):
    with open('report.txt','r') as f:
        my_text = f.read()
    f.close()
    return HttpResponse(my_text)