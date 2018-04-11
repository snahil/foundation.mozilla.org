# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-04 23:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
	('news', '0011_auto_20171012_1326'),
	('highlights', '0006_auto_20180208_2205'),
	('wagtailcore', '0040_page_draft_title'),
	('wagtailimages', '0019_delete_filter'),
	('wagtailpages', '0006_auto_20180403_1640'),
    ]

    operations = [
	migrations.CreateModel(
	    name='Homepage',
	    fields=[
		('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
		('hero_headline', models.CharField(blank=True, help_text='Hero story headline', max_length=140)),
		('hero_story_description', wagtail.core.fields.RichTextField()),
		('hero_button_text', models.CharField(blank=True, max_length=50)),
		('hero_button_url', models.URLField(blank=True)),
		('hero_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hero_image', to='wagtailimages.Image')),
	    ],
	    options={
		'abstract': False,
	    },
	    bases=('wagtailcore.page',),
	),
	migrations.CreateModel(
	    name='HomepageFeaturedHighlights',
	    fields=[
		('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
		('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
		('highlight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='highlights.Highlight')),
		('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_highlights', to='wagtailpages.Homepage')),
	    ],
	    options={
		'verbose_name': 'highlight',
		'verbose_name_plural': 'highlights',
	    },
	),
	migrations.CreateModel(
	    name='HomepageFeaturedNews',
	    fields=[
		('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
		('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
		('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='news.News')),
		('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_news', to='wagtailpages.Homepage')),
	    ],
	    options={
		'verbose_name': 'news',
		'verbose_name_plural': 'news',
	    },
	),
	migrations.AlterField(
	    model_name='modularpage',
	    name='body',
	    field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'h2', 'h3', 'h4', 'h5', 'ol', 'ul', 'link', 'image', 'hr'])), ('image_text', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'])), ('image', wagtail.images.blocks.ImageChooserBlock()), ('ordering', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Image on the left'), ('right', 'Image on the right')]))))), ('image', wagtail.images.blocks.ImageChooserBlock()), ('figure', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(help_text='Please remember to properly attribute any images we use.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this figure should link out to.', required=False))))), ('figuregrid', wagtail.core.blocks.StructBlock((('grid_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(help_text='Please remember to properly attribute any images we use.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this figure should link out to.', required=False)))))),))), ('video', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.CharBlock(help_text='Please make sure this is a proper embed URL, or your video will not show up on the page.')), ('height', wagtail.core.blocks.IntegerBlock(default=450))))), ('iframe', wagtail.core.blocks.StructBlock((('url', wagtail.core.blocks.CharBlock(help_text='Please note that only URLs from white-listed domains will work.')), ('height', wagtail.core.blocks.IntegerBlock(default=450))))), ('linkbutton', wagtail.core.blocks.StructBlock((('label', wagtail.core.blocks.CharBlock()), ('URL', wagtail.core.blocks.CharBlock()), ('styling', wagtail.core.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary button'), ('btn-secondary', 'Secondary button'), ('btn-success', 'Success button'), ('btn-info', 'Info button'), ('btn-warning', 'Warning button'), ('btn-error', 'Error button'), ('btn-ghost', 'Ghost button')])), ('outline', wagtail.core.blocks.BooleanBlock(default=False, required=False))))), ('spacer', wagtail.core.blocks.StructBlock((('size', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'quarter spacing'), ('2', 'half spacing'), ('3', 'single spacing'), ('4', 'one and a half spacing'), ('5', 'triple spacing')])),))))),
	),
    ]