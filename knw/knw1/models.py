from django.db import models

# Create your models here.
class Question(models.Model):
    # 自动生成了名为id的列，作为primary_key，
    # id从1开始自增
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    
    # 生成的foreginKey为question_id，自动加上了_id，
    # 使用.get(qeustion_id=1)通过foreginKey查询时，要输入完整的列名，加上id
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text