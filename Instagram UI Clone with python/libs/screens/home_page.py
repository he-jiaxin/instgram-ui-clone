import json
from kivymd.uix.screen import MDScreen
from libs.components.circular_avatar_image import CircularAvatarImage
from libs.components.post_card import PostCard

class HomePage(MDScreen):
    """Home Page"""
    profile_picture = '/Users/jiaxinhe/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/PD Projects/Instagram UI Clone with python/libs/photo-1623065691913-e9a650810efd.jpeg'

    def on_enter(self):
        self.list_stories()
        self.list_post()

    def list_stories(self):
        with open("/Users/jiaxinhe/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/PD "
                  "Projects/Instagram UI Clone with python/libs/assets/data/stories.json") as f_obj:
            data = json.load(f_obj)
            for name in data:
                self.ids.stories.add_widget(CircularAvatarImage(
                    avatar=data[name]['avatar'],
                    name=name
                ))

    def list_post(self):
        with open("/Users/jiaxinhe/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/PD "
                  "Projects/Instagram UI Clone with python/libs/assets/data/post.json") as f_obj:
            data = json.load(f_obj)
            for username in data:
                self.ids.timeline.add_widget(PostCard(
                    username=username,
                    avatar=data[username]['avatar'],
                    profile_pic=self.profile_picture,
                    post=data[username]['post'],
                    caption=data[username]['caption'],
                    likes=data[username]['likes'],
                    comments=data[username]['comments'],
                    posted_ago=data[username]['posted_ago'],
                ))
