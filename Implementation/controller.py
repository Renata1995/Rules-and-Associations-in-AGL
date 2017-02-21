import cherrypy
import time

class WebApp(object):
    """
    This webapp manages a list of posts. The client could read current posts and create new posts
    """

    def __init__(self):
        """
        Init the app
        """

    @cherrypy.expose
    def index(self):
        """
        Show all conditions of the experiment. The experimenter selects a condition for the participant
        """
        ifile = open("view/condition.html")
        content = ifile.readlines()
        return self.get_head() + content

    @cherrypy.expose
    def new(self):
        """
        Render the "new post" page
        """
        return "HW"

    @cherrypy.expose
    def save(self, newTitle, newContent):
        return "HW"

    def get_head(self, headfile="view/head.html"):
        hfile = open(headfile)
        head_content = hfile.readlines()
        return head_content

# run the webapp
if __name__ == '__main__':
    cherrypy.quickstart(WebApp())

