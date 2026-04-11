class SellerRequest(models.Model):
STATUS_CHOICES = [
('pending', 'Pending'),
('approved', 'Approved'),
('rejected', 'Rejected'),
]

```
user = models.OneToOneField(User, on_delete=models.CASCADE)
passport_image = models.ImageField(upload_to='seller/passport/')
face_image = models.ImageField(upload_to='seller/face/')
status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"{self.user.username} - {self.status}"
```

