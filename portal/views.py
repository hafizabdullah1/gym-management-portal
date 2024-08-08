from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import MembersForm
from .models import Members
from django.db.models import Sum
from dateutil.relativedelta import relativedelta
import datetime


# Create your views here.

# home page where all members show
def home(request):
    members = Members.objects.all()
    context = {'members': members}
    return render(request, 'index.html', context)

# add new member
def add_member(request):
    if request.method == 'POST':
        form = MembersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MembersForm()
    context = {'form': form }
    return render(request, 'member_add.html', context)

# update member data
def update_member(request, id):
    member = get_object_or_404(Members, id=id)
    if request.method == 'POST':
        form = MembersForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MembersForm(instance=member)
    context = {'form': form}
    return render(request, "member_update.html", context)

# delete member from portal
def delete_member(request, id):
    member = Members.objects.get(id=id)
    if request.method == 'POST':
        member.delete()
        return redirect('home')
    context = {'member': member}
    return render(request,"member_delete.html", context)

# search members
def search_members(request):
    query = request.GET.get('query')
    if query:
        members = Members.objects.filter(name__icontains=query)
    else:
        members = Members.objects.all()
    data = []
    for member in members:
        data.append({
            'id': member.id,
            'name': member.name,
            'phone_number': member.phone_number,
            'fee_amount': member.fee_amount,
            # 'fee_date': member.fee_date,
            'fee_date': member.fee_date.strftime('%d'),
            # 'image': member.image,
            'image_url': member.image.url if member.image else '',
            'status': member.status
        })
        
    context = { 'members': data } 
    return JsonResponse(context)

        
# Generate reportfrom django.http import JsonResponse
def generate_report(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        members = Members.objects.filter(fee_date__range=[start_date, end_date])
        total_revenue = members.aggregate(Sum('fee_amount'))['fee_amount__sum'] or 0
        total_members = members.count()
    else:
        members = Members.objects.none()
        total_revenue = 0
        total_members = 0

    context = {
        'members': members,
        'total_revenue': total_revenue,
        'total_members': total_members,
        'start_date': start_date,
        'end_date': end_date
    }
    return render(request, 'reports.html', context)

# Due date passed members
def due_members(request):
    today = datetime.date.today()
    due_members = Members.objects.filter(fee_date__lt = today - datetime.timedelta(days=27))

    context = {'due_members': due_members}    
    return render(request, 'due_members.html', context)
