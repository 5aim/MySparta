from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import login, logout, authenticate # 로그인, 로그아웃 기능 구현 위한 임포트


class UserView(APIView): # CBV 방식
    # permission_classes = [permissions.AllowAny] # 누구나 view 조회 가능
    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능

    def get(self, request):
        # 사용자 정보 조회
        return Response({'message': 'get method!!'})
        
    def post(self, request):
        # 회원가입
        return Response({'message': 'post method!!'})

    def put(self, request):
        # 회원 정보 수정
        return Response({'message': 'put method!!'})

    def delete(self, request):
        # 회원 탈퇴
        return Response({'message': 'delete method!!'})

class UserApiView(APIView):
    permission_classes = [permissions.AllowAny] # 누구나 view 조회 가능 설정을 안했을 경우 allow any.

    # 로그인
    def post(self, request):
        username = request.data.get('username', '') # 어떤 값이 담기는지 보기 위해 직관적으로 작성하고
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password) # auth를 돌려서

        if not user: # auth user가 아니면
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."})

        # else: 필요 없는 else. 앞에서 return을 해주기 때문에
        login(request, user) # auth user가 맞다면

        return Response({"message": "로그인 성공!!"})

    # 로그아웃
    def delete(self, request):
        logout(request)
        return Response({"message": "logout success"})

