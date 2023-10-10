redirection using reverse function. So in flask, if we want to redirect to any of the url by using function name, it would
be easy. But django doesn't have direct function to url call. but it has name to url call. So if we want to redirect in django,
we have to use HttpResponseRedirect() and inside of it, we use the url. But we won't always remember those urls and it would be
complex to type big url. So we do is we use reverse() function and inside of it, we take a name variable, the same we use when
we set urls in urls.py file. we save it in a variable. the reverse function will go to urls.py and search for that name, then
it will take the url and return it there. Thus in reverse() way we get the name to url and redirect there.