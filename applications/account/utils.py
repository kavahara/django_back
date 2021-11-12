from django.core.mail import send_mail

def send_activation_email(email, activation_code):
    activation_url = f'http://localhost:8000/account/activate/{activation_code}/'
    message = f'''thank you for registration, pls activate ur account, Activation Link: {activation_url}'''


    send_mail(
        'Activate your account',
        message,
        'test@stackoverflow.kg',
        [email, ],
        fail_silently=False,
    )