from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .models import News , MainNews
from api.serializers import NewsSerializer, MainNewsSerializer
from .data import GetData

# Create your views here.

@api_view(['GET'])
def api(request):
    list_of_urls ={
        "api/" : "GET list of all the APIs Routes. ",
        "api/:type_of_news": "GET Returns the news with the specified category e.g Bussines",
        "Derrick(NOT A ROUTE)" : "Please be awre that the data is scrapped, the API might be slow at times."
    }
    
    return Response(
        an.getContent()['image_caption']
    )

@api_view(['GET'])
def main_news(request, category):
    all_categories = ['africa', 'south-africa','world','business','politics','sci-tech']
    if category not in all_categories:
        return Response({"Error": "Category not available",
                        "Here are All categories ": "'africa', 'south-africa','world','business','politics','sci-tech'"})
    main_content = GetData(category)
    MainNews.objects.all().delete()
    try:
        caption = main_content.getContent()['image_caption']
    except:
        caption = "The is no Caption here."


    main_data = MainNews(
        title = main_content.getContent()['title'],
        lead_content = main_content.getContent()['lead_content'],
        image_caption = caption,
        img = main_content.getContent()['image']

    )
    try:
        main_data.save()
    except:
        print("Couldn't save the data.")

    news = MainNews.objects.all().order_by('id')
    print(news)
    serialized = MainNewsSerializer(news,context={'request': request},many=True)
    return Response(serialized.data)


@api_view(['GET'])
def body_news(request, category):
    all_categories = ['africa', 'south-africa','world','business','politics','sci-tech']
    if category not in all_categories:
        return Response({"Error": "Category not available",
                        "Here are All categories ": "'africa', 'south-africa','world','business','politics','sci-tech'"})
    body_content = GetData(category)
    News.objects.all().delete()
    
    image_array = body_content.getImages()
    links_array = body_content.links()
    title_array = body_content.getBodyTitle()
    summary_array = body_content.summary()
    
    for body in range(len(image_array)):
        body_data = News(
        them_images = image_array[body],
        body_title = title_array[body],
        summary = summary_array[body],
        links = links_array[body]
        )
        body_data.save()
    
    news = News.objects.all().order_by('id')
    serialized = NewsSerializer(news,context={'request': request},many=True)

    return Response(serialized.data)





