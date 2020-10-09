from django.contrib.auth import login, logout,authenticate
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from .forms import JobseekerForm,JobcreatorForm
from django.views.generic import CreateView 

import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

def register(request):
    return render(request, "register.html")
    
class registerUser(CreateView):
    model = User
    form_class= JobseekerForm
    template_name= '../templates/registerUser.html'
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("login")

    

class registerEmp(CreateView):
    model=User
    form_class= JobcreatorForm
    template_name= '../templates/registerEmp.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("login")

def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_jobseeker:
                    login(request,user)
                    return redirect('userProfile')
                else:
                    login(request,user)
                    return redirect('empProfile')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")

    return render(request, '../templates/login.html',
    context={'form': AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')

def userProfile(request):
    df_joblist = pd.read_csv('df_joblist.csv')
    tfidf_vectorizer = pickle.load(open('tfidfvec.pkl','rb'))
    tfidf_jobid = pickle.load(open('tfidfjob.pkl','rb'))
    
    current_user = request.user
    u_id = current_user.id
    u_list = Jobseeker.objects.get(pk=u_id)
    u_skills = u_list.skills
  

    data = {
        'id':u_id,
        'Key_word':u_skills
    }
    user_q=pd.DataFrame(data,columns=['id','Key_word'],index=['0'])
    z=user_q.id[0]

   



    
    user_tfidf = tfidf_vectorizer.transform(user_q['Key_word'])
    

    cos_similarity_tfidf = map(lambda x: cosine_similarity(user_tfidf, x),tfidf_jobid)
   
    output2 = list(cos_similarity_tfidf)
    

    def get_recommendation(top, df_joblist, scores):
        recommendation = pd.DataFrame(columns = ['index', 'jobid',  'jobtitle', 'score'])
        count = 0
        for i in top:
            recommendation.at[count, 'index'] = z
            recommendation.at[count, 'jobid'] = df_joblist['jobid'][i]
            recommendation.at[count, 'jobtitle'] = df_joblist['jobtitle'][i]
            recommendation.at[count, 'score'] =  scores[count]
            count += 1
        return recommendation
    top = sorted(range(len(output2)), key=lambda i: output2[i], reverse=True)[:20] #sorted(iterable,key=func,reverse)
    #print(len(output2))
    #print(top)
    list_scores = [output2[i][0][0] for i in top]
    #print(list_scores)
    op=get_recommendation(top,df_joblist, list_scores)

    for i in range(len(op)):
        index = op['index'].values[i]
        jobid = op['jobid'].values[i]
        jobtitle = op['jobtitle'].values[i]
        score = op['score'].values[i]

        rec_info = jobrec(index=index,jobid=jobid,jobtitle=jobtitle,score=score)
        rec_info.save()


        current_user = request.user
        u_id = current_user.id
        #u_list = Jobseeker.objects.get(pk=u_id)
        recm = jobrec.objects.filter(index=u_id)

    
    context = {'recm':recm}
    

    return render(request, "userProfile.html",context)   

def empProfile(request):
    return render(request, "empProfile.html")  


