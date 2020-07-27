import os

# from auditor import MiddleWare

from witch import witch as app
# from witch.middleware_callback import callback

home_directory = os.environ['HOME']
configuration_file_name = f'{home_directory}/.config/dolphin.yml'

app.configure()  # filename=configuration_file_name)
app.initialize_orm()
# app = MiddleWare(app, callback)
