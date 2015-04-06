require("Rfacebook")
require("rPython")
require("rJava")
#fb_oauth <- fbOAuth(app_id="1533303760283003", app_secret="e5a1e4e08ca81130b0a7e296b285c33c",extended_permissions = TRUE)
load("FBOuth")
my_likes  <- getLikes(user= "me", n = 50, token = fb_oauth)

newsFeed <- getNewsfeed(token=fb_oauth,50)

#cleanFeed <- newsFeed


fromId <- c(newsFeed$from_id)
fromName <- c(newsFeed$from_id)
postMessage <- list(newsFeed$message)
postType <- c(newsFeed$type)
postLink <- c(newsFeed$link)
fileConn<-file("postLink.txt")
writeLines(postLink,fileConn)
close(fileConn)
python.load("crawler.py")


