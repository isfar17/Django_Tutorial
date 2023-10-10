actual template connection is a bit complex. We want to have seperate template folder for each app. thats easier to work with.
so we will create templates folder inside of the app, but the files will be in a subdirectory of templates. why? because imagine there
are 3 apps. each have templates directory. WHile calling the template folder, django will choose the first tempaltes folder it has
 found. to avoid this we make a subdirectory same name as the app name, that way it is easy to access. then we import them. LASTLy we
 must connect the actual (app instead of templates directory) in settings.py file. This we are good to go.

