import zirkia

test = zirkia.Application("DemoZirkiaPY", "Demo ZirkiaPy", "Aubertin Emmanuel")
zirkia.Post_Request('https://httpbin.org/status/500', "")
print (test.AppName)
