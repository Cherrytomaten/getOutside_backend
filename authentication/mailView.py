from django.core.mail import send_mail
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import CustomUser
from authentication.serializers import ResetPasswordSerializer
from authentication.token import account_activation_token


class ConfirmEmail(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        activate_link_url = 'https://www.get-outside-app.de/confirm-email'  # TODO: Frontend route zum aktivieren
        email = request.data.get('email')
        print(email)
        if not email:
            return Response({'error': 'email is empty'}, status=400)
        if CustomUser.objects.filter(email=email).exists():
            print('HI')
            user = CustomUser.objects.get(email=email)
            print(user.username)
            print(user.is_active)
            token = account_activation_token.make_token(user),  # token erzeugen
            confirmation_token = token[0]

            print(confirmation_token)
            link = f'{activate_link_url}?user_uuid={user.uuid}&user_mail={email}&confirmation_token={confirmation_token}'  # link erstellen

            subject = "Welcome to GetOutside :)"
            text = f'Hello {user.username} :) please confirm your email using the following link: {link}'  # TODO: email tamplate einbauen, damit die mail schön ausieht
            sent_mail = send_mail(  # email senden
                subject,
                text,
                'get_outside.cherrytomaten@gmail.com',
                [email]
            )
            return Response({'msg': sent_mail}, status=200)
        else:
            return Response({'error': 'user with this email not found!'}, status=400)


class ActivateUser(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        print('Activate account :)')
        confirmation_token = request.GET.get('confirmation_token')
        # token = request.data.get('confirmation_token')
        print(confirmation_token)
        user_id = request.data.get('user_id')
        user_mail = request.GET.get('user_mail')
        # user_id = request.data('user_id')
        print(user_mail)
        try:
            user = CustomUser.objects.get(email=user_mail)
        except CustomUser.DoesNotExist:
            user = None
        if user is not None and account_activation_token.check_token(user, confirmation_token):
            user.is_active = True
            user.save()
            return Response({'msg': 'Thank you for your email confirmation. Now you can login your account.'},
                            status=200)
        else:
            return Response({'msg': 'Activation link is invalid!'}, status=400)


class ResetPassword(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        activate_link_url = 'https://www.get-outside-app.de/reset-password'  # TODO: Frontend route zum aktivieren
        email = request.data.get('email')
        if not email:
            return Response({'error': 'email is empty'}, status=400)
        if CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.get(email=email)
            token = account_activation_token.make_token(user),  # token erzeugen
            confirmation_token = token[0]
            print(confirmation_token)
            link = f'{activate_link_url}?user_id={user.uuid}&user_mail={email}&confirmation_token={confirmation_token}'  # link erstellen

            subject = "Reset Password "
            text = f'Hello {user.username}, use the following link to reset your password: {link}'  # TODO: email tamplate einbauen, damit die mail schön ausieht
            sent_mail = send_mail(  # email senden
                subject,
                text,
                'get_outside.cherrytomaten@gmail.com',
                [email]
            )
            user.is_active = False
            return Response({'msg': sent_mail}, status=200)
        else:
            return Response({'error': 'user with this email not found!'}, status=400)

    def put(self, request):

        token = request.data.get('confirmation_token')
        # token = request.data.get('confirmation_token')
        user_id = request.data.get('user_id')
        user_mail = request.data.get('user_mail')
        # user_id = request.data('user_id')
        try:
            user = CustomUser.objects.get(email=user_mail)
        except CustomUser.DoesNotExist:
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            # password change here in serializer, find old password first
            data = {
                'password':  request.data.get('password'),
                'password2': request.data.get('password2'),
            }
            serializer = ResetPasswordSerializer(data=data)
            if serializer.is_valid():
                user = serializer.save()
                if user:
                    json = serializer.data
                    return Response(json, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            user.is_active = True
            return Response({'msg': 'Reset link is invalid!'}, status=400)
