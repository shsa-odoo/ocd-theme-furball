{
    'name': 'Theme Furball',
    'description': 'A custom theme for Dog Lovers',
    'version': '1.0',
    'author': 'Sanjay Sharma',
    'category': 'Theme/Creative',
    'depends': ['website'],
    'data': [
        "views/images_library.xml",

        #  Snippets
        'views/snippets/s_sidegrid.xml',
        "views/snippets/s_banner.xml",
        "views/snippets/s_cards_grid.xml",
        "views/snippets/s_image_text.xml",
        'views/footer.xml',
        'views/header.xml',
    ],

    'images': [
        'static/description/theme_furball.jpg',
        # 'static/description/pexels-pixabay-433989.jpg', # any screenshot of website so created can act as a preview
    ],
    'images_preview_theme': {
        # List of images changed in the theme: urls of the images
    },
    'configurator_snippets': {
        'homepage': ['s_sidegrid', 's_banner', 's_cards_grid', 's_image_text'],
    },
    'assets': {
        'web._assets_primary_variables': [
            'theme_furball/static/src/scss/primary_variables.scss',
        ],
        'web.assets_frontend': [
            'theme_furball/static/fonts/*',
            'theme_furball/static/src/scss/font.scss',
        ],
    },
    'license': 'LGPL-3',
}
