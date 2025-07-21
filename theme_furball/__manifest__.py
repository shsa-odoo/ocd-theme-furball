{
    "name": "Theme Furball",
    "description": "A custom theme for Dog Lovers",
    "version": "1.0",
    "author": "Sanjay Sharma",
    "category": "Theme/Creative",
    "depends": ["website"],
    "data": [
        "views/images_library.xml",

        #  Snippets
        "views/snippets/s_sidegrid.xml",
        "views/snippets/s_banner.xml",
        "views/snippets/s_cards_grid.xml",
        "views/snippets/s_image_text.xml",

        #custom header footer
        "views/footer.xml",
        "views/header.xml",
    ],

    "images": [
        "static/description/furball_screenshot.jpg",
        "static/description/furball_description.jpg",
    ],
    "images_preview_theme": {
        "website.s_default_banner_image": "/theme_furball/static/src/img/snippets/s_banner.jpg",
        "website.library_image_03": "/theme_furball/static/src/img/snippets/library_image_03.jpg",
        "website.library_image_10": "/theme_furball/static/src/img/snippets/library_image_10.jpg",
        "website.library_image_05": "/theme_furball/static/src/img/snippets/library_image_05.jpg",
        "website.library_image_14": "/theme_furball/static/src/img/snippets/library_image_14.jpg",
        "website.library_image_16": "/theme_furball/static/src/img/snippets/library_image_16.jpg",
        "webiste.s_key_images_default_image_1": "/theme_furball/static/src/img/snippets/grid_1.jpg",
        "webiste.s_key_images_default_image_2": "/theme_furball/static/src/img/snippets/grid_2.jpg",
        "webiste.s_key_images_default_image_3": "/theme_furball/static/src/img/snippets/grid_3.jpg",
        "webiste.s_key_images_default_image_4": "/theme_furball/static/src/img/snippets/grid_4.jpg",
    },
    "configurator_snippets": {
        "homepage": ["s_banner", "s_image_gallery", "s_cards_grid"],
    },
    "assets": {
        "web._assets_primary_variables": [
            "theme_furball/static/src/scss/primary_variables.scss",
        ],
        "web.assets_frontend": [
            "theme_furball/static/fonts/*",
            "theme_furball/static/src/scss/font.scss",
        ],
    },
    "license": "LGPL-3",
}
