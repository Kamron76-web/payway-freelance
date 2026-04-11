from .models import Job, Bid, FreelancerProfile, Product, SellerRequest
from .forms import ProductForm, SellerRequestForm

@login_required
def seller_apply(request):
profile = get_object_or_404(FreelancerProfile, user=request.user)

```
if profile.is_seller:
    return redirect('home')

existing_request = SellerRequest.objects.filter(user=request.user).first()

if request.method == 'POST':
    form = SellerRequestForm(request.POST, request.FILES, instance=existing_request)
    if form.is_valid():
        seller_request = form.save(commit=False)
        seller_request.user = request.user
        seller_request.status = 'pending'
        seller_request.save()
        return redirect('home')
else:
    form = SellerRequestForm(instance=existing_request)

return render(request, 'seller_apply.html', {'form': form, 'existing_request': existing_request})
```
