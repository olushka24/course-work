import pymorphy3, nltk, string, operator
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from models import Area, Format, Categorie, Course, Client, CompletedCourse

courses = CompletedCourse.objects.raw('''SELECT *
FROM backend_completedcourse
JOIN backend_client bc on bc.id = backend_completedcourse.client_id
JOIN backend_course b on backend_completedcourse.course_id = b.id
WHERE client_id = 3''')

print(courses)
