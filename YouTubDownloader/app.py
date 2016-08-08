import web

urls = (
  '/', 'index' ,
  '/mp4' , 'mp4' ,
  '/mp3' , 'mp3'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class index:
    def GET(self):
        greeting = "Hello World"
        return render.index()

class mp4:
    def POST(self):
        print "Downloading MP4"
        form = web.input(name = "anything")
        url = form.mp4
        print url
        self.downloadMP4(url)
        return render.index()

    def downloadMP4(self , url):
        import pafy
        video = pafy.new(url)
        best = video.getbest()
        best.download(quiet=False)
        return True

class mp3:
    def POST(self):
        print "Downloading MP3"
        form = web.input(name = "anything")
        url = form.mp3
        print url
        self.downloadMP3(url)
        return render.index()

    def downloadMP3(self , url):
        import pafy
        video = pafy.new(url)
        bestaudio = video.getbestaudio()
        bestaudio.download()
        return True


if __name__ == "__main__":
    app.run()