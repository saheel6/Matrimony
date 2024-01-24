from django.shortcuts import render,redirect
from django.views.generic import CreateView,View
from .forms import CustomUserForm,signinform,userprofileeditform,PreferenceForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import CustomUser,Like,Chat,Subscription,Preference
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from datetime import datetime,timedelta



# Create your views here.


def home(request):
    return render(request,"home.html")



class signupview(CreateView):
    
  template_name="signup.html"
  form_class=CustomUserForm
  success_url=reverse_lazy('signinu')
    
    
  def form_valid(self, form):
          # Handle image upload
     form_data = form.cleaned_data

     photo = form_data['photo'] 
    # Save photo 

     user = form.save(commit=False)
     user.photo = photo
     user.save()
 
     return super().form_valid(form)



class signinview(LoginView):
    template_name = 'signin.html'  # Replace 'your_template_name.html' with your actual template name
    form_class = signinform

    def get_success_url(self):
        return reverse_lazy('profilefilter')  # Replace 'your_success_url' with your actual success URL name
    
    
       
       
def userprofileview(request):

  if not request.user.is_authenticated:
    return redirect('login')

  context = {
    'user': request.user
  }

  return render(request, 'profile.html', context)


class profileeditview(View):
    
   def get(self,request):
       
       updateform=userprofileeditform()
       return render(request,'useredit.html',{'update':updateform})
   
   def post(self,request):

        user=request.user
  
        updateform=userprofileeditform(request.POST,request.FILES,instance=user)

        if updateform.is_valid():
      
          form_data = updateform.cleaned_data

          photo = form_data['photo']

          user = updateform.save(commit=False)
          user.photo = photo 
          user.save()

          return redirect('upro')

        else:
          messages.error(request,'invalid credentials')
          return redirect('useredit')
      
      
class preferenceview(View):
    
    def get(self,request):
        
        form=PreferenceForm()
        
        return render(request,'preference.html',{'form':form})
    
    
    def post(self,request):
      preference = Preference.objects.filter(user=request.user).first()
    
      if not preference:
        preference = Preference(user=request.user)
  
      form = PreferenceForm(request.POST, instance=preference)
  
      if form.is_valid():
        preference = form.save(commit=False)  
        preference.user = request.user
        preference.save()
        return redirect('profilefilter')

      else:
        messages.error(request,'invalid input')
        return redirect('preference')

def preferenceshowview(request):

    if request.method=='GET':
        
        user_pref = Preference.objects.get(user=request.user)

        # Get specific fields
        preferred_gender = user_pref.preferred_gender
        preferred_religion = user_pref.preferred_religion
        preferred_community = user_pref.preferred_community
        preferred_maritalstatus = user_pref.preferred_maritalstatus
        min_height = user_pref.min_height 
        max_height = user_pref.max_height
        min_age = user_pref.min_age
        max_age = user_pref.max_age

def preferenceshowview(request):

    if request.method=='GET':
        
        user_pref = Preference.objects.get(user=request.user)

        # Get specific fields
        gender = user_pref.preferred_gender
        religion = user_pref.preferred_religion
        community = user_pref.preferred_community
        maritalstatus = user_pref.preferred_maritalstatus
        min_height = user_pref.min_height 
        max_height = user_pref.max_height
        age_min = user_pref.min_age
        age_max = user_pref.max_age

        users = CustomUser.objects.all()
        
        if age_min:
            users = users.filter(age__gte=age_min)
            
        if age_max:
            users = users.filter(age__lte=age_max)
            
        if gender:
            users = users.filter(gender__gender=gender)
            
        if religion:
            users = users.filter(religion__religion=religion)
            
        if community:
            users = users.filter(community__community=community)
            
        if maritalstatus:
            users = users.filter(maritalstatus=maritalstatus)
        
        ages = range(18, 100)
        gen = CustomUser.objects.values_list('gender', flat=True).distinct()
        rel = CustomUser.objects.values_list('religion', flat=True).distinct()
        com = CustomUser.objects.values_list('community', flat=True).distinct()
        
        context = {'profiles': users}
        
        return render(request, 'filter.html', context)
        

    
    

class profilefilterview(View):
    
    def get(self,request):
      
        if request.method == 'GET':

            age_minn = request.GET.get('age_min')
            age_maxx = request.GET.get('age_max')
            
            if age_minn and age_maxx:
                users = CustomUser.objects.filter(age__gte=age_minn, age__lte=age_maxx)
            else:
                users = CustomUser.objects.all()
        
        cuser=CustomUser.objects.all()
        gen=CustomUser.objects.values_list("gender__gender",flat=True).distinct()
        rel=CustomUser.objects.values_list("religion__religion",flat=True).distinct()
        com=CustomUser.objects.values_list("community__community",flat=True).distinct()
              
        
        ages = range(18, 100)
        try:
                user_pref = Preference.objects.get(user=request.user)

        # Get specific fields
                gender = user_pref.preferred_gender
                religion = user_pref.preferred_religion
                community = user_pref.preferred_community
                maritalstatus = user_pref.preferred_maritalstatus
                min_height = user_pref.min_height 
                max_height = user_pref.max_height
                age_min = user_pref.min_age
                age_max = user_pref.max_age

                users = CustomUser.objects.all()
                
                if age_min:
                    users = users.filter(age__gte=age_min)
                    
                if age_max:
                    users = users.filter(age__lte=age_max)
                    
                if gender:
                    users = users.filter(gender__gender=gender)
                    
                if religion:
                    users = users.filter(religion__religion=religion)
                    
                if community:
                    users = users.filter(community__community=community)
                    
                if maritalstatus:
                    users = users.filter(maritalstatus=maritalstatus)

                
                context = {
                    'profiles': users,
                    'users': users,
                    'gen':gen,
                    'rel':rel,
                    'com':com,
                    'ages': ages
                }

                return render(request,"filter.html", context)
            
        except:
            context = {
                    
                    'users': users,
                    'gen':gen,
                    'rel':rel,
                    'com':com,
                    'ages': ages
                }

            return render(request,"filter.html", context)
    
    
  

class filtershow(View):

    def get(self, request):
        
        age_min = request.GET.get('age_min')
        age_max = request.GET.get('age_max')
        gender = request.GET.get('gender')
        religion = request.GET.get('religion')
        community = request.GET.get('community')
        
        users = CustomUser.objects.all()
        
        if age_min:
            users = users.filter(age__gte=age_min)
            
        if age_max:
            users = users.filter(age__lte=age_max)
            
        if gender:
            users = users.filter(gender__gender=gender)
            
        if religion:
            users = users.filter(religion__religion=religion)
            
        if community:
            users = users.filter(community__community=community)
        
        ages = range(18, 100)
        gen = CustomUser.objects.values_list('gender', flat=True).distinct()
        rel = CustomUser.objects.values_list('religion', flat=True).distinct()
        com = CustomUser.objects.values_list('community', flat=True).distinct()
             
        context = {
            'users': users,
            'ages': ages,
            'gen': gen,
            'rel': rel,
            'com': com
        }
        
        return render(request, 'fres.html', context)       
    
    

        
def profiledetails(request, id):
  user = CustomUser.objects.get(id=id)
  context = {'user': user}
  return render(request, 'user_details.html', context)

    
def add_like(request, id):
    user = request.user
    liked_user = get_object_or_404(CustomUser, id=id)

    # Check if a like already exists
    existing_like = Like.objects.filter(user=user, liked_user=liked_user).exists()

    if not existing_like:
        # If no existing like, create a new one
        Like.objects.create(user=user, liked_user=liked_user)
        return redirect('fushow')
    else:
        # If like already exists, you can redirect to home or any other desired page
        messages.error(request,'you already liked this candidate')
        return redirect('fushow')  # Adjust 'home' to the appropriate URL name

 
   
def showlikedview(request):
    user_likes = Like.objects.filter(user=request.user)
    context = {
        'likes': user_likes,
        't':'hi hows it going'
        }
    return render(request, 'likedlist.html', context)









def view_chat(request, recipient_id):

    if request.method == 'GET':

            recipient = get_object_or_404(CustomUser, id=recipient_id)

            if not recipient.is_subscribed:
                messages.error(request, 'Recipient is not subscribed to chat')
                return redirect('fushow')

            if not request.user.is_subscribed:
                messages.error(request, 'You need to subscribe to chat')
                return redirect('fushow')
            
            sender = request.user
            recipient = get_object_or_404(User, id=recipient_id)

            chats = Chat.objects.filter(
            sender=sender, 
            recipient=recipient
                   ).order_by('created_at')  | Chat.objects.filter(
             sender=recipient, 
             recipient=sender
              ).order_by('created_at') 

            context = {
              'sender': sender,
              'recipient': recipient,
              'chats': chats
              }

            return render(request, 'chat.html', context)

       
  
    if request.method == 'POST':
        # Logic to send a new chat message
        sender = request.user
        recipient = get_object_or_404(User, id=recipient_id)
        
        message = request.POST.get('message')
        
        new_chat = Chat.objects.create(
            sender=sender,
            recipient=recipient, 
            message=message
        )
        
        return redirect('view_chat',recipient_id=recipient.id)

class subscribe(View):
    
    def get(self,request):
        
        return render(request,'subscription.html')
    
    def post(self,request):
           
        if request.user.is_subscribed==False:
            user = request.user
            card_no=request.POST.get('cardnumber')
            sub = Subscription.objects.create(
             user=user,
             subscription_type='basic', 
             card_number=card_no,
              end_date=datetime.now() + timedelta(days=30)
              )
            user.is_subscribed = True
            user.save()
  
            return redirect('fushow')
        
        else:
            messages.success(request,'already subscribed')
            return redirect('home')



class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('signinu')  

# def unsubscribe(request):
#   user = request.user
#   unsub=Subscription.objects.filter(user=user)
#   unsub.delete()
#   user.is_subscribed = False
#   user.save()

#   return redirect('home')


