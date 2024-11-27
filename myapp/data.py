# data.py
from django.utils.text import slugify

ARTICLES = [
    {
        "title": "What is Climate Change?",
        "image": "images/articles/climate-change.png",
        "slug": slugify("What is Climate Change?"),
        "content": (
            "<div class='text-center font-semibold text-primary-green text-xl lg:text-2xl mb-2'>"
            "What is Climate Change?</div>"
            "<p>Climate change describes a change in the average conditions — such as temperature and rainfall — in a region over a long period of time. "
            "For example, 20,000 years ago, much of the United States was covered in glaciers. In the United States today, we have a warmer climate and fewer glaciers.</p><br>"
            "<p><strong class='text-primary-green'>Global climate change</strong> refers to the average long-term changes over the entire Earth. These include warming temperatures and changes in precipitation, "
            "as well as the effects of Earth’s warming, such as:</p>"
            "<ul class='list-disc ml-8 mt-2 mb-4'>"
            "<li>Rising sea levels</li>"
            "<li>Shrinking mountain glaciers</li>"
            "<li>Ice melting at a faster rate than usual in Greenland, Antarctica and the Arctic</li>"
            "<li>Changes in flower and plant blooming times</li>"
            "</ul>"
            "<p>Earth’s climate has constantly been changing — even long before humans came into the picture. However, scientists have observed unusual changes recently. "
            "For example, Earth’s average temperature has been increasing much more quickly than they would expect over the past 150 years.</p>"
        ),
        "banner": "images/articles/climate-change-body-image.png"
    },
    {
    "title": "What is Coral Bleaching?",
    "image": "images/articles/coral-bleaching.png",
    "slug": slugify("What is Coral Bleaching?"),
    "content": (
        "<div class='text-center font-semibold text-primary-green text-xl lg:text-2xl mb-2'>"
        "Coral bleaching? What's that?!</div>"
        "<p>A reef is a big group of rocks on the ocean floor, but did you know that a coral reef is actually alive and covered "
        "with very small animals called corals? These animals glue their tiny skeletons to rocks, so they end up staying in "
        "the same place their entire lives!</p><br>"
        "<p>Coral reefs are very sensitive to light and temperature. If the water they live in gets too hot, they might not survive. "
        "They also don't like it when the ocean has too much pollution. Sometimes, storms can even upset coral depending on how "
        "often they happen and how severe they are. If coral reefs are under too much stress, like in these conditions, they can eject "
        "the algae living on them and turn completely white. This is known as <strong class='text-primary-green'>coral bleaching</strong>. This does not necessarily mean the coral is dead - "
        "corals can survive bleaching! They do become more vulnerable to death however, especially if the stress continues for a long period of time.</p><br>"
        "<p>NASA recently developed some very sensitive instruments to study coral reefs from an airplane flying above the ocean. The "
        "COral Reef Airborne Laboratory (CORAL) uses an instrument called the Portable Remote Imaging Spectrometer (PRISM) to see the condition of reefs. "
        "Scientists will now be able to monitor these reefs and their health. They will be able to measure the amounts of coral, algae, and sand on the ocean floor.</p>"
    ),
    "banner": "images/articles/coral-bleaching-body-image.png"
    },
    {
        "title": "What is Green House Effect?",
        "link": "",
        "image": "images/articles/green-house-effect.png",
        "slug": slugify("What is Green House Effect?"),
        "content": (
            "<div class='text-center font-semibold text-primary-green text-xl lg:text-2xl mb-2'>"
            "How does the greenhouse effect work?</div>"
            "<p>As you might expect from the name, the greenhouse effect works … like a greenhouse! A greenhouse is a building with glass walls and a glass roof. "
            "Greenhouses are used to grow plants, such as tomatoes and tropical flowers.</p><br>"
            "<p>A greenhouse stays warm inside, even during the winter. In the daytime, sunlight shines into the greenhouse and warms the plants and air inside. "
            "At nighttime, it's colder outside, but the greenhouse stays pretty warm inside. That's because the glass walls of the greenhouse trap the Sun's heat.</p><br>"
            "<p>The greenhouse effect works much the same way on Earth. Gases in the atmosphere, such as carbon dioxide, trap heat similar to the glass roof of a greenhouse. "
            "These heat-trapping gases are called <strong class='text-primary-green'>greenhouse gases</strong>.</p><br>"
            "<p>During the day, the Sun shines through the atmosphere. Earth's surface warms up in the sunlight. At night, Earth's surface cools, releasing heat back into the air. "
            "But some of the heat is trapped by the greenhouse gases in the atmosphere. That's what keeps our Earth a warm and cozy 58 degrees Fahrenheit (14 degrees Celsius), on average.</p>"
        ),
        "banner": "images/articles/green-house-effect-body-image.png"
    },
    {
        "title": "Weather vs Climate",
        "image": "images/articles/weather-vs-climate.png",
        "slug": slugify("Weather vs Climate"),
        "content": (
            "<div class='text-center font-semibold text-primary-green text-xl lg:text-2xl mb-2'>"
            "Weather vs. Climate</div>"
            "<p>Weather describes the conditions outside right now in a specific place. For example, if you see that it’s raining outside right now, "
            "that’s a way to describe today’s weather. Rain, snow, wind, hurricanes, tornadoes — these are all weather events.</p><br>"
            "<p><strong class='text-primary-green'>Climate</strong>, on the other hand, is more than just one or two rainy days. Climate describes the weather conditions that are expected in a region "
            "at a particular time of year.</p><br>"
            "<p>Is it usually rainy or usually dry? Is it typically hot or typically cold? A region’s climate is determined by observing its weather over a period of many years—generally 30 years or more.</p><br>"
            "<p>So, for example, one or two weeks of rainy weather wouldn’t change the fact that Phoenix typically has a dry, desert climate. Even though it’s rainy right now, "
            "we still expect Phoenix to be dry because that's what is usually the case.</p><br>"
            "<p class='mt-4'>Want to know more about the difference between weather and climate? Take a look at this video! <a href='https://youtu.be/vH298zSCQzY' target='_blank' class='text-primary-green underline'>Watch the video</a></p>"
        ),
        "banner": "images/articles/weather-vs-climate-body-image.png"
    },
]



multimedia = [
        {
            "src": 'https://www.youtube.com/embed/G9t__9Tmwv4?si=Fnj-xldJB7Z66PYd',
            "tag": "video"
        },
        {
            "src": 'https://www.youtube.com/embed/QlQ-MEZgRGY?si=yIqRHSELyKKoRNZv',
            "tag": "video"
        },
        {
            "src": 'https://www.youtube.com/embed/myZAvqqp9Jc?si=OcEsBG1galCHTUTN',
            "tag": "video"
        },
        {
            "src": 'https://www.youtube.com/embed/SN5-DnOHQmE?si=qC_Sa7V-mjmISHPy',
            "tag": "video"
        },
    ]

games = [
    {
        "title": "Dash for Trash",
        "thumbnail": "images/thumbnails/dash-for-trash.png", 
        "link": "https://html-classic.itch.zone/html/10196267/final_dash4trash/index.html?embed=1"
    },
    {
        "title": "Sailors",
        "thumbnail": "images/thumbnails/sailors.png", 
        "link": "https://html-classic.itch.zone/html/10153436/webglpractice/index.html?embed=1"
    },
    {
        "title": "The Clean Sea Crew",
        "thumbnail": "images/thumbnails/clean-sea-crew.png", 
        "link": "https://html-classic.itch.zone/html/10104557/Build%202.0/index.html?embed=1"
    },
    {
        "title": "OceanSmart Games For Change",
        "thumbnail": "images/thumbnails/oceansmart.png", 

        "link": "https://html-classic.itch.zone/html/10195549/index.html?embed=1"
    },
    {
        "title": "The Sustainable Society Club!",
        "thumbnail": "images/thumbnails/society-club.png", 
        "link": "https://html-classic.itch.zone/html/11347764/WebGL/index.html?embed=1"
    }

]
