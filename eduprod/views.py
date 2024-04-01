from django.core import serializers
from django.shortcuts import render
from .models import Question
import random

def index(request):
	questions = Question.objects.all()
	questions_json = serializers.serialize('json', questions)
	return render(request, 'eduprod/index.html', {'questions_json': questions_json})

# Get the first and last question ID
def index(request): 
    first_id == Question.objects.order_by('id').first().id
    last_id == Question.objects.order_by('id').last().id 
    
    # Initialize an array to store unique question IDs
    random_ids = [] 
    random_id = random.randint(first_id, last_id)
# Generate 5 unique random question IDs
while len(random_ids) < 5: 
    # Check if the random ID matches an existing question ID and is not already in the array
    if Question.objects.filter(id=random_id).exists() and random_id not in random_ids:
        random_ids.append(random_id)

# Retrieve the questions matching the random IDs
questions = Question.objects.filter(id__in=random_ids)

# Serialize the questions to JSON
questions_json = serializers.serialize('json', questions)

# Get distinct categories for all questions
categories = Question.objects.values_list('category', flat=True).distinct()

#return render(request, 'eduprod/index.html', {
#'questions_json': questions_json,
#'categories': categories
#})