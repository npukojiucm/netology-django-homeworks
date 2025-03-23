from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class TagInlineFormset(BaseInlineFormSet):

    def clean(self):

        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main') is True:
                count += 1

            if count > 1:
                raise ValidationError('Выбрано более 1 основного раздела')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = TagInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at']

    inlines = [ScopeInline, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
