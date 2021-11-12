from rest_framework import serializers

from applications.question.models import Category, Question, Answer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = (
            'id',
            'question',
            'solution',
        )

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author_id'] = request.user.id
        answer = Answer.objects.create(**validated_data)
        return answer

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['question'] = instance.question.title
        representation['author'] = instance.author.email
        return representation


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'category', 'title', 'image', 'problem')


    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author_id'] = request.user.id
        question = Question.objects.create(**validated_data)
        return question

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = instance.category.title
        representation['author'] = instance.author.email
        representation['solutions'] = AnswerSerializer(Answer.objects.filter(question=instance.id), many=True).data
        return representation