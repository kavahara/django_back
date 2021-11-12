from rest_framework.decorators import api_view

from rest_framework import viewsets
from django.db.models import Q

# 1. с помощью функций
from applications.question.models import Category, Question, Answer
from applications.question.permissions import IsQuestionAuthor
from applications.question.serializers import CategorySerializer, QuestionSerializer, AnswerSerializer
from rest_framework.response import Response

#
# @api_view(['GET'])
# def category_list(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)


# 2.  с помощью APIView
from rest_framework.views import APIView
from rest_framework import status
#
# class CategoryView(APIView):
#     def get(self, request):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# 3. с помощью generics
from rest_framework import generics


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


#CRUD for questions

class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        search = self.request.GET.get('q')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(problem__icontains=search)
            )
        if category is not None:
            queryset = queryset.filter(category__title__icontains=category)
        print(category)
        return queryset


from rest_framework.permissions import IsAuthenticated


class QuestionCreateView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, ]


class QuestionUpdateView(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsQuestionAuthor]


class QuestionDeleteView(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsQuestionAuthor]


# CRUD for answers


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, ]